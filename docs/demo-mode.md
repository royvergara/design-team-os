# Demo mode — fabricate freely, label everything

A user evaluating this system legitimately wants to drive the whole pipeline end-to-end
before any real work exists — "this is a demo, infer the inputs" is a fair request, and the
gates must not make the machine undemoable. This page is the one convention that makes a
demo safe. It binds every skill; none needs its own copy.

## The rule

**When the user declares a demo, test, or dry run: fabricate freely, and mark every
fabricated value as synthetic in every artifact it touches.** Not once in the chat — in the
artifacts. A `⚠️ synthetic` (or equivalent) marker travels with the value into the ledger
entry, the brief, the plan's result section, the rendered page. Chat scrolls away; artifacts
are what the next session reads.

Three consequences:

1. **A labeled fake is honest; a silent fake is the exact failure the gates exist to catch.**
   The system's whole defense is that artifacts carry evidence. An unlabeled fabricated
   value _is_ gate-laundering, whoever typed it.
2. **Synthetic evidence never counts as proven.** The `conductor` reads a labeled-synthetic
   artifact as an **open** gate (the demo walked through it; nothing earned it), and the
   render templates give synthetic values their own marked state — hatched, dashed, never
   the proven green. A demo that ends with an all-green board taught the user the wrong
   lesson about what green means.
3. **The demo ends with the reset named.** When the walkthrough closes, say which artifacts
   carry synthetic blocks and offer the reset: strip them so the ledger reflects only what
   was really earned. A demo skeleton left unlabeled in a repo becomes next quarter's
   "wait, did we validate this?"

## What demo mode never relaxes

The gates still fire — a demo _shows_ the refusal instead of skipping it. If the user asks
"what if validation passed?", the answer is the hypothetical routing plus the refusal to
write it as state, exactly as in real work; then, if they want to proceed as a demo, the
fabricated signal goes in **labeled**. The demo teaches the discipline by exercising it,
never by suspending it.

## Marking conventions

- YAML ledger entries: a `# ⚠️ SYNTHETIC DEMO` comment on the block, plus `⚠️ synthetic`
  inside any prose value.
- Markdown artifacts: a blockquote banner at the top of the synthetic section — what is
  fabricated, and that it must be re-run for real before any decision.
- Rendered pages: the template's synthetic state (see templates/conductor.html) or an
  explicit demo label in the folio line (see the scorecard's classification token).
