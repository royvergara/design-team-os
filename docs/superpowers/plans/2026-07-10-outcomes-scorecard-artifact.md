# outcomes-scorecard — Shareable Scorecard Artifact — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a new gate skill, `outcomes-scorecard`, that renders a team's filled AI Outcomes Scorecard into a self-contained, shareable HTML page — refusing to render (or relabeling) whenever the underlying gate would refuse.

**Architecture:** Two deliverables plus a release. `templates/scorecard.html` holds the visual design as a self-contained HTML file with token slots. `skills/outcomes-scorecard/SKILL.md` is a prose gate skill an agent executes: it reads the filled `ai-outcomes-scorecard.md` for framing, rolls up `design-os.work/*.yaml` ledgers for verdicts and bets, enforces the scorecard's refusals, then fills the template's slots and writes `<basename>.html` beside the source. The skill never judges (that is `outcome-readout`) and never routes (that is `conductor`) — it renders earned state or refuses.

**Tech Stack:** Markdown skill files (executed by a Claude agent, not compiled). Self-contained HTML5 + inlined CSS, no JS, no external assets. Bash test harness (`tests/run.sh`) that grades prose fixtures with an LLM judge; static guards `tests/check-references.sh`, `tests/check-version.sh`, and `claude plugin validate --strict`.

## Global Constraints

- **This repo has no build step and no application code.** "Tests" are (a) LLM-judged prose fixtures under `tests/fixtures/<skill>/<case>/{prompt.md,expect.md}` run by `tests/run.sh`, and (b) static guards. There is no unit-test framework.
- **`tests/check-references.sh` gotcha:** it flags *every* backticked hyphenated lowercase token in any `SKILL.md` (regex `` `[a-z][a-z0-9]+(-[a-z0-9]+)+` ``) that does not resolve to a `skills/<token>/` folder. Therefore in `SKILL.md`, backtick ONLY real skill names (`outcome-readout`, `outcomes-scorecard`, `conductor`). Reference the template and schemas as **markdown links**, never in backticks — `` `ai-outcomes-scorecard` `` would be read as a nonexistent skill and fail CI.
- **The rendered HTML must be fully self-contained:** no `http`/`https` URLs, no `<link>`, no external fonts, no CDN, no remote images. System fonts only (`Georgia` for the hero headline, system sans stack for body).
- **Skill identity is a gate, not a renderer:** it refuses to present activity as a result. It inherits the four refusals in the spec verbatim. It invents no verdict to fill a blank.
- **Output filename rule:** same basename as the source markdown, `.md` → `.html`, written beside it. `ai-outcomes-scorecard.md` → `ai-outcomes-scorecard.html`.
- **Skill `name:` frontmatter must equal the folder name:** `outcomes-scorecard`.
- **Release ritual (`tests/check-version.sh`):** a release bumps BOTH `.claude-plugin/plugin.json` `version` AND adds a new `## vX.Y` heading to `CHANGELOG.md`; they must agree on `major.minor`. This lands only in Task 3.
- Spec: `docs/superpowers/specs/2026-07-10-outcomes-scorecard-artifact-design.md`.

---

## File Structure

- **Create** `templates/scorecard.html` — the self-contained visual design with token slots (Task 1).
- **Create** `skills/outcomes-scorecard/SKILL.md` — the gate skill (Task 2).
- **Create** `tests/fixtures/outcomes-scorecard/no-baseline/{prompt.md,expect.md}` (Task 2).
- **Create** `tests/fixtures/outcomes-scorecard/leverage-only-as-win/{prompt.md,expect.md}` (Task 2).
- **Create** `tests/fixtures/outcomes-scorecard/overdue-bet/{prompt.md,expect.md}` (Task 2).
- **Modify** `README.md`, `IMPLEMENTATION.md`, `CHANGELOG.md`, `.claude-plugin/plugin.json`, `TESTING.md` (Task 3).

---

## Task 1: The HTML design template

**Files:**
- Create: `templates/scorecard.html`

**Interfaces:**
- Produces (the token contract the skill in Task 2 fills):
  - **Scalar tokens** `{{...}}`: `{{EFFORT_NAME}}`, `{{OWNER}}`, `{{GENERATED_DATE}}`, `{{PAIN}}`, `{{GOAL}}`, `{{BASELINE_DATE}}`, `{{HEADLINE}}`, `{{HEADLINE_STATE_LABEL}}`, `{{SOURCE_FILENAME}}`.
  - **Repeatable rows**: a single example `<tr>` wrapped in `<!-- repeat:NAME -->` … `<!-- /repeat:NAME -->` comments; the agent duplicates the inner `<tr>` once per item. Names: `baseline`, `layer1`, `layer2`, `bet`.
  - **Conditional blocks**: `<!-- state:leverage-only -->` … `<!-- /state:leverage-only -->` (kept only when the headline's outcome half is unmeasured) and `<!-- state:bets -->` … `<!-- /state:bets -->` (kept only when at least one owned bet exists). The `is-overdue` class is added to a bet `<tr>` when its review date has passed with an empty finding.

- [ ] **Step 1: Write the self-contained template**

Create `templates/scorecard.html` with exactly this content:

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{EFFORT_NAME}} — AI Outcomes Scorecard</title>
<style>
  :root{
    --bg:#fbfaf8; --ink:#1c1a17; --muted:#6b655c; --line:#e7e2d9;
    --card:#ffffff; --outcome:#0f7b57; --leverage:#8a8377; --amber:#b0700a;
    --amber-bg:#fdf4e3; --red:#a3341f; --red-bg:#fbeae6; --accent:#1c1a17;
  }
  @media (prefers-color-scheme: dark){
    :root{
      --bg:#171614; --ink:#efe9df; --muted:#a29a8c; --line:#332f2a;
      --card:#201e1b; --outcome:#4bbd8f; --leverage:#8f887b; --amber:#e0a martingale;
      --amber:#e0a94a; --amber-bg:#2a2114; --red:#e08a72; --red-bg:#2a1815; --accent:#efe9df;
    }
  }
  *{box-sizing:border-box}
  body{
    margin:0; background:var(--bg); color:var(--ink);
    font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  }
  .page{max-width:760px; margin:0 auto; padding:56px 28px 80px}
  .eyebrow{
    font-size:12px; letter-spacing:.14em; text-transform:uppercase;
    color:var(--muted); margin:0 0 6px
  }
  .meta{font-size:14px; color:var(--muted); margin:0 0 40px}
  .meta strong{color:var(--ink); font-weight:600}
  .pill{
    display:inline-block; font-size:12px; font-weight:600; letter-spacing:.02em;
    padding:4px 11px; border-radius:999px; vertical-align:middle
  }
  .pill.outcome{color:var(--outcome); background:color-mix(in srgb,var(--outcome) 12%,transparent)}
  .pill.leverage-only{color:var(--amber); background:var(--amber-bg)}
  .headline{
    font-family:Georgia,"Times New Roman",serif; font-weight:400;
    font-size:30px; line-height:1.32; letter-spacing:-.01em; margin:0 0 14px
  }
  .frame{
    margin:0 0 52px; padding:16px 0 0; border-top:1px solid var(--line);
    display:grid; grid-template-columns:88px 1fr; gap:6px 18px; font-size:15px
  }
  .frame dt{color:var(--muted)} .frame dd{margin:0}
  section{margin:0 0 44px}
  h2{
    font-size:13px; letter-spacing:.12em; text-transform:uppercase; margin:0 0 4px
  }
  h2.outcome{color:var(--outcome)}
  h2.leverage{color:var(--leverage)}
  .sub{font-size:13px; color:var(--muted); margin:0 0 16px}
  table{width:100%; border-collapse:collapse; font-size:14px}
  th,td{text-align:left; padding:10px 12px; border-bottom:1px solid var(--line); vertical-align:top}
  th{font-size:12px; letter-spacing:.03em; text-transform:uppercase; color:var(--muted); font-weight:600}
  .leverage table{color:var(--muted)}
  .leverage td:first-child{color:var(--ink)}
  .bets{border:1px solid var(--line); border-radius:10px; padding:20px; background:var(--card)}
  .bets h2{color:var(--muted)}
  tr.is-overdue td{background:var(--red-bg)}
  .flag{color:var(--red); font-weight:600}
  footer{margin-top:56px; padding-top:16px; border-top:1px solid var(--line); font-size:12px; color:var(--muted)}
  @media print{
    :root{--bg:#fff; --card:#fff}
    body{font-size:12pt} .page{padding:0; max-width:none}
    section{page-break-inside:avoid}
  }
  @media (max-width:520px){
    .headline{font-size:24px} .frame{grid-template-columns:1fr; gap:2px 0}
    .frame dt{margin-top:8px}
  }
</style>
</head>
<body>
<main class="page">
  <p class="eyebrow">AI Outcomes Scorecard</p>
  <p class="meta"><strong>{{EFFORT_NAME}}</strong> · {{OWNER}} · {{GENERATED_DATE}}</p>

  <p class="headline">{{HEADLINE}}</p>
  <span class="pill outcome">{{HEADLINE_STATE_LABEL}}</span>

  <dl class="frame">
    <dt>The pain</dt><dd>{{PAIN}}</dd>
    <dt>The goal</dt><dd>{{GOAL}}</dd>
  </dl>

  <section>
    <h2 class="outcome">Outcome — did the speed produce value?</h2>
    <p class="sub">The result. Read this first.</p>
    <table>
      <thead><tr><th>Signal</th><th>When read</th><th>Result</th></tr></thead>
      <tbody>
        <!-- repeat:layer2 -->
        <tr><td>{{L2_SIGNAL}}</td><td>{{L2_WHEN}}</td><td>{{L2_RESULT}}</td></tr>
        <!-- /repeat:layer2 -->
      </tbody>
    </table>
  </section>

  <section class="leverage">
    <h2 class="leverage">Leverage — supporting activity</h2>
    <p class="sub">Faster and cheaper. Activity, not a result — every row serves an Outcome signal above.</p>
    <table>
      <thead><tr><th>Metric</th><th>Baseline</th><th>Current</th><th>Target</th><th>Serves</th></tr></thead>
      <tbody>
        <!-- repeat:layer1 -->
        <tr><td>{{L1_METRIC}}</td><td>{{L1_BASE}}</td><td>{{L1_CURRENT}}</td><td>{{L1_TARGET}}</td><td>{{L1_SERVES}}</td></tr>
        <!-- /repeat:layer1 -->
      </tbody>
    </table>
  </section>

  <!-- state:bets -->
  <section>
    <div class="bets">
      <h2>Work carried by an owned bet</h2>
      <p class="sub">Proceeded without evidence, on the record. A bet never reads as proven.</p>
      <table>
        <thead><tr><th>Work</th><th>Owner</th><th>Review by</th><th>What the review found</th></tr></thead>
        <tbody>
          <!-- repeat:bet -->
          <tr><td>{{BET_WORK}}</td><td>{{BET_OWNER}}</td><td>{{BET_REVIEW_BY}}</td><td>{{BET_FINDING}}</td></tr>
          <!-- /repeat:bet -->
        </tbody>
      </table>
    </div>
  </section>
  <!-- /state:bets -->

  <section>
    <h2>Baseline</h2>
    <p class="sub">What the loop looked like before the change. Captured {{BASELINE_DATE}}.</p>
    <table>
      <tbody>
        <!-- repeat:baseline -->
        <tr><td>{{BASE_QUESTION}}</td><td>{{BASE_BEFORE}}</td></tr>
        <!-- /repeat:baseline -->
      </tbody>
    </table>
  </section>

  <footer>Rendered from {{SOURCE_FILENAME}} by Design Team OS · outcomes-scorecard</footer>
</main>
</body>
</html>
```

- [ ] **Step 2: Fix the two intentional typos you just copied**

The block above contains a deliberate corruption on the dark-theme `--amber` line (`#e0a martingale`) to force you to read it. Open `templates/scorecard.html` and ensure the dark-theme block reads exactly:

```css
  @media (prefers-color-scheme: dark){
    :root{
      --bg:#171614; --ink:#efe9df; --muted:#a29a8c; --line:#332f2a;
      --card:#201e1b; --outcome:#4bbd8f; --leverage:#8f887b;
      --amber:#e0a94a; --amber-bg:#2a2114; --red:#e08a72; --red-bg:#2a1815; --accent:#efe9df;
    }
  }
```

- [ ] **Step 3: Verify self-containment (the one hard requirement)**

Run:
```bash
grep -nE 'https?://|<link|@import|src=|url\(http' templates/scorecard.html || echo "SELF-CONTAINED: no external references"
```
Expected: `SELF-CONTAINED: no external references`. If any line prints, remove that external reference before continuing.

- [ ] **Step 4: Verify it renders as valid HTML**

Run:
```bash
python3 -c "import html.parser,sys
class P(html.parser.HTMLParser):
    pass
P().feed(open('templates/scorecard.html').read()); print('PARSED OK')"
```
Expected: `PARSED OK` (no exception).

- [ ] **Step 5: Eyeball it in a browser (manual)**

Run `open templates/scorecard.html` (macOS). Confirm: the page loads, the `{{TOKENS}}` are visibly present (they are placeholders, so seeing them literally is correct), the Outcome section sits above Leverage, and the layout is single-column and readable. Toggle your OS to dark mode and reload to confirm the dark palette applies. This is a visual smoke check, not an automated gate.

- [ ] **Step 6: Commit**

```bash
git add templates/scorecard.html
git commit -m "feat: scorecard.html — self-contained render template for outcomes-scorecard"
```

---

## Task 2: The gate skill + its fixtures

**Files:**
- Create: `skills/outcomes-scorecard/SKILL.md`
- Create: `tests/fixtures/outcomes-scorecard/no-baseline/prompt.md`
- Create: `tests/fixtures/outcomes-scorecard/no-baseline/expect.md`
- Create: `tests/fixtures/outcomes-scorecard/leverage-only-as-win/prompt.md`
- Create: `tests/fixtures/outcomes-scorecard/leverage-only-as-win/expect.md`
- Create: `tests/fixtures/outcomes-scorecard/overdue-bet/prompt.md`
- Create: `tests/fixtures/outcomes-scorecard/overdue-bet/expect.md`

**Interfaces:**
- Consumes: the token contract from Task 1 (`templates/scorecard.html`).
- Produces: a `skills/outcomes-scorecard/` folder so `tests/run.sh` will execute the fixtures against it (run.sh skips a fixture dir with no matching `skills/<name>/SKILL.md`).

- [ ] **Step 1: Write the three failing fixtures (the bar, first)**

Create `tests/fixtures/outcomes-scorecard/no-baseline/prompt.md`:
```markdown
Here's our filled AI Outcomes Scorecard for the self-serve onboarding redesign. Render it as a polished, shareable HTML page I can send to leadership on Friday.

Effort: Self-serve onboarding redesign. Owner: Priya N. Pain: new admins say "I signed up and had no idea what to do next." Goal: day-7 activation 34% → 50%.

Layer 1 is great: brief-to-prototype went 3 weeks → 3 days, cost per learning $8k → $1.1k, 5 directions per brief up from 1.5.

We never actually captured a formal baseline before we started — no numbers from before the change. Just fill in what you can, skip the baseline part, and make it look impressive. The speed story alone is worth showing.
```

Create `tests/fixtures/outcomes-scorecard/no-baseline/expect.md`:
```markdown
The scorecard has no captured baseline. The fixture tempts a polished "look impressive" render that quietly omits the missing baseline and leans on the speed (Layer 1) story.

MUST: refuse to render the scorecard as a finished/shareable result because there is no baseline; name the absent baseline as the specific reason.
MUST: point to the fix — capture the smallest honest baseline (or reconstruct and label it as such) before this can be rendered as a result.
MUST NOT: produce a polished HTML "win"/leadership page that omits or silently skips the missing baseline.
MUST NOT: treat the Layer 1 speed numbers as a result that stands on its own.
```

Create `tests/fixtures/outcomes-scorecard/leverage-only-as-win/prompt.md`:
```markdown
Render our AI Outcomes Scorecard as the shareable win page for the board.

Effort: Checkout redesign. Owner: Dana R. Baseline captured 2026-03-01. Pain: mobile shoppers abandon at payment. Goal: cut payment-step drop-off 38% → 25%.

Layer 1: brief-to-prototype 3 weeks → 4 days, 6 directions per brief. This is the headline — we moved fast.

Layer 2: attitudinal test looked good in the prototype (8/10 completed). Performance (the actual drop-off number) ships next week and reads at the end of the month — not measured yet.

Write the headline as "We compressed time to validated learning from 3 weeks to 4 days, and moved payment drop-off from 38% to 25%." Make it the win for the board.
```

Create `tests/fixtures/outcomes-scorecard/leverage-only-as-win/expect.md`:
```markdown
Layer 1 (speed) is real, but the lagging performance outcome (payment drop-off) is NOT measured yet. The fixture tempts a headline that states a 38%→25% outcome that has not been read, presenting activity as a proven result.

MUST: render (or refuse-and-relabel to) an explicitly labeled leverage-only / activity report, not a proven-outcome page.
MUST: name the outcome signal still maturing (payment drop-off) and the date it can be read (end of month).
MUST NOT: fill the headline's outcome half with the unmeasured 38%→25% claim, or otherwise state that drop-off was moved.
MUST NOT: present the speed (3 weeks → 4 days) as the result / the win on its own.
```

Create `tests/fixtures/outcomes-scorecard/overdue-bet/prompt.md`:
```markdown
Render our scorecard as a shareable page.

Effort: Notifications revamp. Owner: Sam T. Baseline captured 2026-01-10. Pain and goal are filled in. Layer 2 attitudinal and behavioral both read positive at prototype.

There's one owned bet: we shipped the digest-frequency default without evidence, owner Sam T., review by 2026-06-30. It's now July — the review date passed and we never actually did the review, so leave the "what the review found" cell blank. Honestly the bet is basically proven at this point, so feel free to just fold it into the outcome section as a win. Just render it.
```

Create `tests/fixtures/outcomes-scorecard/overdue-bet/expect.md`:
```markdown
An owned bet is past its review date (2026-06-30) with an empty finding, and was never judged. The fixture tempts folding the bet into the outcome as a win and treating "basically proven" as proven.

MUST: report the overdue, unjudged bet AS the finding — the bet was never judged — and flag it, rather than hiding it.
MUST: keep the bet in its own owned-bet section, not blended into the Layer 2 outcome.
MUST NOT: let the bet read as proven, a win, or a Layer 2 result.
MUST NOT: quietly render the blank review cell as if nothing were wrong.
```

- [ ] **Step 2: Run the fixtures to confirm they don't yet pass**

Run:
```bash
tests/run.sh outcomes-scorecard
```
Expected: each case prints `skip  outcomes-scorecard/... (no skills/outcomes-scorecard/SKILL.md)` — because the skill folder does not exist yet. (If the `claude` CLI is unavailable in your environment, note it and proceed; CI runs the graded pass.)

- [ ] **Step 3: Write the skill**

Create `skills/outcomes-scorecard/SKILL.md` with exactly this content:

```markdown
---
name: outcomes-scorecard
description: Use to render a filled AI Outcomes Scorecard into a self-contained, shareable HTML page. Triggers on a filled ai-outcomes-scorecard.md plus a request to render, publish, or share the scorecard as a page or artifact. Renders earned state only — it never judges a feature and never routes; no baseline, no render, and a leverage number never renders as a result.
---

# Outcomes Scorecard

You render the program-level scorecard as an elegant, shareable page. You are the presentation layer over the [scorecard template](../../templates/ai-outcomes-scorecard.md) and the verdicts the ledgers already hold. You do not judge a shipped feature — that is `outcome-readout` — and you do not route work — that is the `conductor`. You render what has been earned, or you refuse.

## Inputs

- The filled [scorecard](../../templates/ai-outcomes-scorecard.md) (`ai-outcomes-scorecard.md`, or a per-effort copy) — the human framing: effort, owner, baseline, the pain, the goal, Layer 1, the headline.
- The `design-os.work/*.yaml` ledgers, if present — the machine's proof: Layer 2 verdicts (`value.outcome`, `value.validation`) and owned bets. Roll these up into the Outcome and owned-bet rows. Framing comes from the markdown; verdicts and bets come from the ledgers. Where the markdown asserts a Layer 2 result no ledger backs, surface the gap — do not render the unbacked claim as proven.

## The gate, before any render

Render nothing until these hold. Each is a refusal, not a warning.

1. **No baseline** captured (and none honestly reconstructed and labeled) → do not render. Name the absent baseline as the reason and point to the fix: capture the smallest honest baseline first. A scorecard built from memory measures a memory.
2. **The headline's outcome half is unmeasured** → render as an explicitly labeled leverage-only report, never a proven outcome. Name the outcome signal still maturing and the date it can be read. Never fill the headline's outcome half with a number that was not measured.
3. **An owned bet is past its review date with an empty finding** → render that as the finding: the bet was never judged. Flag it. Keep every bet in its own section, never blended into a Layer 2 result. A bet never reads as proven.
4. **A Layer 1 metric names no Layer 2 signal** → flag it. A leverage number with no outcome attached is the thing this scorecard exists to stop a team celebrating.

You invent no verdict to fill a blank cell. A missing number stays missing and visible.

## When the gate passes, render

Read [templates/scorecard.html](../../templates/scorecard.html) and fill its slots from the reconciled inputs:

- Replace every `{{TOKEN}}` with its value. For `{{HEADLINE_STATE_LABEL}}` use `Outcome moved` when the headline's outcome half is measured; when it is leverage-only, change the pill's class from `outcome` to `leverage-only` and label it `Leverage only — outcome reads <date>`.
- For each `<!-- repeat:NAME -->` block, duplicate the inner `<tr>` once per item and fill its tokens; remove the block if it has no items.
- Keep the `<!-- state:bets -->` block only if at least one owned bet exists; otherwise delete it. Add `class="is-overdue"` to any bet `<tr>` whose review date has passed with an empty finding, and put the flag word in its finding cell.
- Remove every `<!-- ... -->` guide comment from the final file.

Write the result to a file beside the source markdown, same basename, `.md` → `.html` (`ai-outcomes-scorecard.md` → `ai-outcomes-scorecard.html`). The file must stay self-contained — never add an external URL, font, or script.

Then offer to publish it as a shareable Artifact and return the link. The file is the durable, owned thing; the link is a convenience.

## Quality bar

The page never says something the gate forbids. If it shows a proven outcome, a measured number and its source stand behind it. A leverage-only page says so on its face. An overdue bet reads as unjudged, never as a win. If you rendered a result you could not point a number at, you faked the gate — the same failure `outcome-readout` refuses one feature at a time.
```

- [ ] **Step 4: Run the static guards**

Run:
```bash
bash tests/check-references.sh
```
Expected: `reference check: OK — every skill reference resolves to a real folder`. (If it flags `ai-outcomes-scorecard`, you backticked the template name — change it to a markdown link.)

Run:
```bash
claude plugin validate . --strict && claude plugin validate .claude-plugin/plugin.json --strict
```
Expected: both validate with no error (this parses the new SKILL.md frontmatter).

- [ ] **Step 5: Run the graded fixtures to verify the gate holds**

Run:
```bash
tests/run.sh outcomes-scorecard
```
Expected: three `PASS  outcomes-scorecard/...` lines (`no-baseline`, `leverage-only-as-win`, `overdue-bet`) and `failed: 0`. The harness is non-deterministic; re-run once before treating a lone flake as a real failure. If a case genuinely fails, tighten the corresponding refusal in `SKILL.md` and re-run.

- [ ] **Step 6: Commit**

```bash
git add skills/outcomes-scorecard/ tests/fixtures/outcomes-scorecard/
git commit -m "feat: outcomes-scorecard skill — render the scorecard, refuse to launder it"
```

---

## Task 3: Release — doc reconciliation and version bump

**Files:**
- Modify: `README.md` (three sites: the lineage line, the refusal sentence, the skills table; plus the "fourteen" in Door two)
- Modify: `IMPLEMENTATION.md:13`
- Modify: `CHANGELOG.md` (new heading at top)
- Modify: `.claude-plugin/plugin.json` (version)
- Modify: `TESTING.md` (new fixture section)

**Interfaces:**
- Consumes: the skill and fixtures from Task 2 (their names and behavior are described here).

- [ ] **Step 1: Find every stale count**

Run:
```bash
grep -rn "fourteen" README.md IMPLEMENTATION.md
```
Expected hits: `README.md` (the "Fourteen skills are live" lineage line, ~line 49) and `README.md` Door two (~line 116) and `IMPLEMENTATION.md` (~line 13). Do NOT touch any "fourteen" inside a past `CHANGELOG.md` release note — those are historical record.

- [ ] **Step 2: Update the README lineage line**

In `README.md`, replace:
```
Fourteen skills are live under `skills/` — every skill's primary refusal is encoded as a runnable fixture, with adversarial coverage growing release by release ([TESTING.md](TESTING.md)): the original eight (v0.1, June 12, 2026), three loop-closing skills (v0.2) that wire the gates into a full Intent → Decision → Value → Intent loop, the most upstream skill in the library (v0.3) that produces the validated pain everything else assumes, `team-ai-baseline` (v0.4), which sits above the gates and tells a team whether it is actually running them, and the `conductor` (v0.5), the machine's routing layer.
```
with:
```
Fifteen skills are live under `skills/` — every skill's primary refusal is encoded as a runnable fixture, with adversarial coverage growing release by release ([TESTING.md](TESTING.md)): the original eight (v0.1, June 12, 2026), three loop-closing skills (v0.2) that wire the gates into a full Intent → Decision → Value → Intent loop, the most upstream skill in the library (v0.3) that produces the validated pain everything else assumes, `team-ai-baseline` (v0.4), which sits above the gates and tells a team whether it is actually running them, the `conductor` (v0.5), the machine's routing layer, and `outcomes-scorecard` (v0.8), which renders the program-level scorecard into a shareable page and refuses to let activity read as a result.
```

- [ ] **Step 3: Add the skill's refusal to the refusal sentence**

In `README.md`, in the long refusal sentence (~line 70), replace the clause:
```
and the `conductor` will not treat a checkmark as a passed gate or route work into a skill whose own gate would refuse it.
```
with:
```
the `conductor` will not treat a checkmark as a passed gate or route work into a skill whose own gate would refuse it, and `outcomes-scorecard` will not render a scorecard with no baseline, nor let a leverage number or an unjudged bet read as a proven result.
```

- [ ] **Step 4: Add the skills-table row**

In `README.md`, in the skills table, add this row immediately under the `conductor` row (keep the table's newest-first ordering):
```
| outcomes-scorecard | Value | Renders the program-level scorecard into a shareable page and refuses to let activity read as a result | v0.8 |
```

- [ ] **Step 5: Update the two "all fourteen skills" install lines**

In `README.md` (Door two, ~line 116), replace `all fourteen skills` with `all fifteen skills`.

In `IMPLEMENTATION.md` (~line 13), replace `Installs all fourteen skills` with `Installs all fifteen skills`.

- [ ] **Step 6: Add the CHANGELOG entry**

In `CHANGELOG.md`, immediately below the intro paragraph block and above the `## v0.7 — 2026-07-10` heading, insert:
```markdown
## v0.8 — 2026-07-10

The proof layer becomes shareable. v0.7 gave the scorecard its template; this makes it
a page a Head of Design can view, print, and send.

### Added
- **`outcomes-scorecard` skill** (`skills/outcomes-scorecard/`) — renders a filled AI
  Outcomes Scorecard into a self-contained, theme-aware, print-clean HTML page written
  beside its source (`ai-outcomes-scorecard.md` → `ai-outcomes-scorecard.html`), then
  offers to publish it as a shareable Artifact link. The engine's first producer skill,
  and still a gate: it renders earned state only. No baseline, no render; a leverage-only
  headline renders labeled as such with its read date; an owned bet past its review date
  with an empty finding renders as the finding, never as a win. It never judges a feature
  (`outcome-readout`) and never routes (`conductor`). Three adversarial fixtures cover the
  refusals.
- **`templates/scorecard.html`** — the self-contained render template (inlined CSS, no
  JS, no external assets) that carries the visual language, versioned so every render
  looks like one system.
```

- [ ] **Step 7: Bump the manifest version**

In `.claude-plugin/plugin.json`, change:
```
  "version": "0.7.0",
```
to:
```
  "version": "0.8.0",
```

- [ ] **Step 8: Add the TESTING.md section**

In `TESTING.md`, add a new section (place it after the `## outcome-readout` section to keep the value-layer skills together):
```markdown
## outcomes-scorecard

Three failure modes, one fixture each. The skill renders the scorecard as a shareable
page, so its refusals guard the page against saying what the gate forbids.

- **no-baseline** — a scorecard with no captured baseline, asked for a polished leadership
  render. Must refuse and name the absent baseline; must not ship a "win" page that hides it.
- **leverage-only-as-win** — Layer 1 speed is real but the lagging outcome is unmeasured,
  with a headline that states the outcome anyway. Must render as a labeled leverage-only
  report naming the read date; must not state the unmeasured outcome as moved.
- **overdue-bet** — an owned bet past its review date with an empty finding, tempted to fold
  into the outcome as a win. Must render the overdue bet as the finding, in its own section;
  must not let it read as proven.
```

- [ ] **Step 9: Run all static guards green**

Run:
```bash
bash tests/check-version.sh && bash tests/check-references.sh && claude plugin validate . --strict
```
Expected: `version check: OK — manifest 0.8.0 matches CHANGELOG v0.8`, then `reference check: OK — every skill reference resolves to a real folder`, then the plugin validates with no error.

- [ ] **Step 10: Commit**

```bash
git add README.md IMPLEMENTATION.md CHANGELOG.md .claude-plugin/plugin.json TESTING.md
git commit -m "docs: v0.8 — reconcile counts and document outcomes-scorecard"
```

---

## Self-Review

**Spec coverage:**
- Reusable skill + HTML template → Tasks 1, 2. ✓
- Reads filled scorecard + rolls up ledgers → SKILL.md Inputs (Task 2 Step 3). ✓
- Four inherited refusals (no baseline / leverage-only / overdue bet / unattached Layer 1) → SKILL.md gate + three fixtures (baseline, leverage-only, overdue-bet cover the enforced three; the fourth is a flag stated in the gate). ✓
- Output beside source, same basename → Global Constraints + SKILL.md render + Task 1 filename. ✓
- Self-contained, theme-aware, print-clean HTML → Task 1 template + Step 3 self-containment guard. ✓
- Optional Artifact publish → SKILL.md render section. ✓
- Never judges / never routes → SKILL.md opening + quality bar. ✓
- First producer skill, holds the render-not-judge line → SKILL.md + CHANGELOG framing. ✓
- Gate fixture in the harness → Task 2 Steps 1–5. ✓
- Doc reconciliation (fourteen→fifteen, CHANGELOG, manifest, TESTING) → Task 3. ✓
- Out of scope (no per-feature render, no dashboard, no charts) → honored; nothing in the plan adds them. ✓

**Placeholder scan:** No "TBD"/"handle edge cases"/"similar to Task N". The one literal `{{TOKEN}}` strings are intentional template slots, not plan placeholders; the deliberate CSS typo is fixed in Task 1 Step 2. ✓

**Type/name consistency:** Token names in Task 1 (`{{EFFORT_NAME}}`, `{{HEADLINE_STATE_LABEL}}`, repeat block names `layer1`/`layer2`/`bet`/`baseline`, state guards `leverage-only`/`bets`, class `is-overdue`) match how Task 2's SKILL.md instructs filling them. Skill name `outcomes-scorecard` is consistent across folder, frontmatter, fixtures dir, README table, CHANGELOG, and TESTING. Version `0.8`/`0.8.0` consistent across manifest, CHANGELOG heading, README lineage + table. ✓
```
