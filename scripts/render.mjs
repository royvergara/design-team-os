#!/usr/bin/env node
// render.mjs — deterministic template filler for Design Team OS render templates
// (templates/scorecard.html, templates/conductor.html, and any future template
// that uses the same three markers).
//
// Why this exists: filling a 600-line HTML template is a templating job, not a
// judgment job. An LLM doing it token-by-token is slow and can mis-fill; this
// script either renders correctly or fails loudly. The skill's job shrinks to
// producing the small data JSON — the judgment — and the render becomes free.
//
// Usage:
//   node scripts/render.mjs <template.html> <data.json> <out.html>
//
// Data shape (every key optional):
//   {
//     "tokens":  { "WORK_SLUG": "relive-the-night", ... },   // {{TOKEN}} → value
//     "repeats": { "gate": [ { "G_NAME": "INTENT", ... } ] }, // one object per item
//     "states":  { "synthetic": true, "bets": false },        // keep or drop guarded blocks
//     "dataJson": { ... }                                     // becomes {{DATA_JSON}}, a pure JSON literal
//   }
//
// Marker syntax (shared by all templates):
//   {{TOKEN}}                                — replaced with tokens.TOKEN, verbatim (HTML allowed;
//                                              tokens ending in _HTML are fragments by convention)
//   <!-- repeat:name --> ... <!-- /repeat:name -->
//                                            — inner block duplicated once per repeats.name item,
//                                              item keys fill the block's {{TOKENS}}
//   <!-- state:name --> ... <!-- /state:name -->
//                                            — block kept when states.name is truthy, else removed
//
// Order: states → repeats → tokens → strip HTML guide comments → strict check.
// A leftover {{TOKEN}} after filling is an error (exit 1), never a silent blank.

import { readFileSync, writeFileSync } from "node:fs";

const [templatePath, dataPath, outPath] = process.argv.slice(2);
if (!templatePath || !dataPath || !outPath) {
  console.error(
    "usage: node scripts/render.mjs <template.html> <data.json> <out.html>",
  );
  process.exit(2);
}

const die = (msg) => {
  console.error(`render.mjs: ${msg}`);
  process.exit(1);
};

let html;
let data;
try {
  html = readFileSync(templatePath, "utf8");
} catch (e) {
  die(`cannot read template: ${e.message}`);
}
try {
  data = JSON.parse(readFileSync(dataPath, "utf8"));
} catch (e) {
  die(`cannot parse data JSON: ${e.message}`);
}

const tokens = { ...(data.tokens ?? {}) };
const repeats = data.repeats ?? {};
const states = data.states ?? {};
const warnings = [];

// {{DATA_JSON}} is a token like any other, but its value must be a pure JSON
// literal — never a quoted string. Serialize it here so the data file carries
// real JSON, not JSON-in-a-string.
if (data.dataJson !== undefined)
  tokens.DATA_JSON = JSON.stringify(data.dataJson);

const fillTokens = (str, map, context) => {
  const used = new Set();
  const out = str.replace(/\{\{([A-Z0-9_]+)\}\}/g, (whole, name) => {
    if (Object.prototype.hasOwnProperty.call(map, name)) {
      used.add(name);
      return String(map[name]);
    }
    return whole; // left for the global pass / strict check
  });
  for (const key of Object.keys(map)) {
    if (!used.has(key))
      warnings.push(
        `${context}: key "${key}" matched no {{${key}}} in its block`,
      );
  }
  return out;
};

// 1. State guards — kept when truthy, removed (with their contents, including
//    any repeat blocks inside) when false or missing. Missing gets a warning:
//    an undeclared state silently disappearing is how a section gets lost.
html = html.replace(
  /[ \t]*<!--\s*state:([\w-]+)\s*-->([\s\S]*?)<!--\s*\/state:\1\s*-->[ \t]*\n?/g,
  (_, name, inner) => {
    if (!(name in states))
      warnings.push(
        `state "${name}" not declared in data.states — block removed`,
      );
    return states[name] ? inner : "";
  },
);

// 2. Repeat blocks — the inner element duplicated per item. An empty or missing
//    list removes the block (matching the skills' "drop the block if it has no
//    items" instruction), with a warning when it was never declared at all.
html = html.replace(
  /[ \t]*<!--\s*repeat:([\w-]+)\s*-->\n?([\s\S]*?)[ \t]*<!--\s*\/repeat:\1\s*-->[ \t]*\n?/g,
  (_, name, inner) => {
    const items = repeats[name];
    if (items === undefined) {
      warnings.push(
        `repeat "${name}" not declared in data.repeats — block removed`,
      );
      return "";
    }
    if (!Array.isArray(items)) die(`repeats.${name} must be an array`);
    return items
      .map((item, i) => fillTokens(inner, item, `repeat ${name}[${i}]`))
      .join("");
  },
);

// 3. Global tokens.
html = fillTokens(html, tokens, "tokens");

// 4. Strip HTML guide comments (never JS comments inside <script>).
html = html.replace(/[ \t]*<!--[\s\S]*?-->[ \t]*\n?/g, "");

// 5. Strict check — a leftover token means the data was incomplete. Fail loudly;
//    a silently blank cell on a scorecard is a lie of omission.
const leftover = [...new Set(html.match(/\{\{[A-Z0-9_]+\}\}/g) ?? [])];
if (leftover.length)
  die(`unfilled tokens after render: ${leftover.join(", ")}`);

writeFileSync(outPath, html);
for (const w of warnings) console.warn(`render.mjs: warning — ${w}`);
console.log(`render.mjs: wrote ${outPath} (${Buffer.byteLength(html)} bytes)`);
