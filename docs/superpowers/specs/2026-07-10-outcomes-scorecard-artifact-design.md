# Design: `outcomes-scorecard` — the shareable scorecard artifact

**Date:** 2026-07-10
**Status:** Approved for planning
**Author:** Roy Vergara (with Claude)

## The one-sentence version

A new gate skill that renders a team's filled AI Outcomes Scorecard into a
self-contained, elegant, shareable HTML page — uniquely theirs, version-controlled
next to its source, and unable to be styled into a lie.

## Motivation

The scorecard exists today as `templates/ai-outcomes-scorecard.md`: a markdown
template with empty tables a team fills in. It is the artifact a Head of Design
"takes upward" (README line 74), but in its raw form it is a grid of tables — not
something you drop into a board deck or share with a stakeholder and have it *land*.

The ask: turn the filled scorecard into an output someone can **view and share** —
uniquely populated with their data, formatted elegantly, consumable at a glance.
Crucially, this is not a one-off render. It is a **reusable capability in the OS**:
anyone running Design Team OS can render their own scorecard, and every render looks
like one system.

## Alignment with the engine (why this fits, and where it is new)

**What keeps it in-family:**

- **It is a gate, not a decoration.** Every one of the current fourteen skills
  refuses when its inputs are not earned. This one refuses to render a scorecard
  that has no baseline, and refuses to let a leverage-only result present itself as
  an outcome. The elegance is the surface; the refusal is the skill.
- **It reads ledgers, never writes them.** Like every skill, it ends where the
  ledger's "artifacts, never checkmarks" invariant is untouched. It renders
  `value.outcome`, `value.validation`, and owned bets that the ledgers *already*
  hold. It sets no checkmark and closes no gate.
- **It is the proof layer, not a spine gate.** It sits beside `outcome-readout`,
  outside the 11-step spine, as the presentation of the rollup.

**What is genuinely new — and the line it forces us to hold:**

Every existing skill is text-in → prose-judgment-out. **None produce a file.** This
is the engine's first *producer* skill. That is acceptable only if it holds a hard
line: **it renders what is already earned, and refuses otherwise. It never judges.**

- Judging one shipped feature is `outcome-readout`'s job.
- Routing / "what's next" is the `conductor`'s job.
- This skill invents nothing. If it ever fabricated a verdict to fill a blank cell,
  it would be laundering — the exact failure the whole system is built to stop.

## The skill contract

**Name:** `outcomes-scorecard` (noun-noun, pairs with `outcome-readout`).

**Trigger:** a filled `ai-outcomes-scorecard.md` (or a request to render/publish the
scorecard as a shareable artifact/page). No filled scorecard, no render.

**Inputs:**

1. The filled `ai-outcomes-scorecard.md` — the human-authored framing: effort,
   owner, baseline, the pain, the goal, Layer 1 metrics, the headline sentence.
2. The `design-os.work/*.yaml` ledgers, if present — the machine-written proof:
   Layer 2 verdicts (`value.outcome`, `value.validation`) and owned bets. These are
   *rolled up* into the Layer 2 and owned-bet sections.

**Reconciliation rule:** framing comes from the markdown; verdicts and bets come from
the ledgers. Where the markdown asserts a Layer 2 result that no ledger backs, the
skill surfaces the gap rather than rendering the unbacked claim as proven. (The
markdown is the human's framing; the ledger is the evidence of record.)

## The gate (the refusals it inherits)

The rendered page can never say something the markdown gate forbids. Enforced at
render time:

- **No baseline captured** → refuse to render. A scorecard built from memory measures
  a memory, not a change. Output: what is missing and where to start, not a page.
- **Headline only half-filled** (leverage moved, outcome not yet read) → render as a
  clearly **labeled leverage report**, naming the outcome signal still maturing and
  the date it can be read. Never dress activity as a result.
- **An owned bet past its review date with an empty finding** → render *that* as the
  finding, flagged, not hidden. A bet never reads as proven.
- **A Layer 1 metric that names no Layer 2 signal** → flag it. A leverage number with
  no outcome attached is the thing the scorecard exists to stop a team celebrating.

## Output

- **File:** written **beside its source markdown, same basename, `.md` → `.html`**.
  So `ai-outcomes-scorecard.md` → `ai-outcomes-scorecard.html`, and a per-effort
  `onboarding-scorecard.md` → `onboarding-scorecard.html`. No new directory, no
  `init` change; multiple efforts self-handle by their distinct source filenames.
- **Self-contained:** inlined CSS, no CDN, no build step, no external fonts or images.
  Opens anywhere; survives being dropped into Notion, emailed, or committed.
- **Theme-aware:** light/dark via `prefers-color-scheme`.
- **Print/PDF-clean:** it will end up in a board deck. Print styles are a requirement,
  not a nice-to-have.
- **Optional share link:** after writing the file, the skill offers to publish it as a
  claude.ai Artifact and return a shareable URL. The file is the durable, owned thing;
  the Artifact is the convenience link.

## Visual language

Editorial and prose-forward, matching the repo's voice, with the two-layer logic made
legible:

- **The headline sentence is the hero** — the first and largest thing on the page, the
  line carried upward.
- **Outcome (Layer 2) sits visually above Leverage (Layer 1).** Leverage is styled as
  supporting activity, deliberately subordinate — the layout itself refuses to let a
  fast-number steal the spotlight.
- **Honesty is encoded in the design, not just the copy:**
  - a leverage-only headline gets a distinct "not yet a result" treatment;
  - owned bets live in a visibly quarantined block, never blended into an outcome;
  - a past-due unjudged bet is flagged (e.g. a warning accent).
- Responsive; single column on narrow screens.

**YAGNI:** no chart library, no JS framework, no live data, no interactivity beyond an
optional theme toggle. One page, one effort, self-contained.

## Components

1. **`skills/outcomes-scorecard/SKILL.md`** — the gate: trigger, inputs, reconciliation,
   the refusals, and the render/publish behavior. Cross-references `outcome-readout`,
   `ai-outcomes-scorecard.md`, and `work-ledger.schema.md`. Valid frontmatter
   (`claude plugin validate --strict`), resolvable cross-refs
   (`check-references.sh`).
2. **`templates/scorecard.html`** — the design, versioned. A self-contained HTML file
   with clearly-marked token slots the skill fills. This is where the visual language
   lives, so every render looks like one system and the design can evolve in one place.

**Token contract (template ↔ skill):** the template defines named slots for every
scorecard field (effort meta, baseline rows, Layer 1 rows with their served signal,
Layer 2 signals with when-read/result, owned-bet rows, the headline, and per-section
state flags like `leverage-only` / `bet-overdue`). The skill's job is to fill those
slots from the reconciled inputs. The exact token syntax is an implementation-plan
detail; the contract is that the skill never emits raw HTML structure — it only fills
the template's slots.

## Testing

- **Gate fixture** under `tests/fixtures/outcomes-scorecard/…`, wired into
  `tests/run.sh`. It tests the *gate*, not the aesthetics: feed it a
  laundering-tempting scorecard (a leverage number and a flattering headline, no
  Layer 2 verdict) and assert the skill refuses to render it as a result — it either
  declines or renders an explicitly labeled leverage-only page. A second case: a
  scorecard with no baseline → assert refusal.
- **Static CI** already covers frontmatter validity and cross-reference resolution;
  the new SKILL.md must pass both.

## Doc reconciliation (same-PR, non-negotiable)

This repo has a documented history of counts going stale on release (v0.6.1 was a
release solely to fix this). Adding a fifteenth skill requires, in the same PR:

- `IMPLEMENTATION.md` — "all fourteen skills" → fifteen.
- `README.md` — "all fourteen skills" → fifteen (line ~116).
- `CHANGELOG.md` — a v0.8 entry describing the skill + template.
- `.claude-plugin/plugin.json` — version bump; `tests/check-version.sh` must stay green.
- `TESTING.md` — a section documenting the new fixture, matching the existing pattern.

## Out of scope (explicit YAGNI)

- Rendering the per-feature `outcome-readout` as its own artifact. This ships the
  program-level scorecard only. If the render language proves out, a per-feature
  variant is a later, separate effort.
- A ledger-digest / dashboard across many efforts.
- Any charting, animation, or interactivity beyond a theme toggle.
- A hosted, always-live dashboard. The output is a static, owned file plus an optional
  share link — not a service.

## Open questions

None blocking. Token syntax and the exact HTML structure are deferred to the
implementation plan.
