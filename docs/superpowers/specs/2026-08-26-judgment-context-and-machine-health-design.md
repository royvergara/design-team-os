# Design: the Hex translation — judgment context, endorsed sources, machine health

What a competitive study of [Hex](https://hex.tech) (AI analytics, "where trust meets
insight") translates into this stack, and — as important — what it doesn't. Three
workstreams; two are naming what already shipped, one wires a loop v0.12 explicitly
deferred. No new skill; the count stays eighteen.

## Why now

Hex is the clearest case of "AI governance" being productized for a specific work layer.
Their version has three mechanisms: **curated context** (semantic models that settle what
a metric means, endorsements that mark trusted sources, written guides the agent reasons
from), **inspectable output** (every AI conversation opens as a real notebook — no
un-openable claims), and **governance from observed friction** (Context Studio watches
where answer quality breaks and lets the data team fix context where the evidence says,
not where a committee guesses).

The study's finding: this library already holds two of the three, arrived at from the
design side — the profile *is* a semantic layer for judgment (v0.12: `metrics:`
definitions "settle what the number means before a bar is registered against it"), and
artifacts-never-checkmarks *is* no-un-openable-claims. What Hex has that the machine
lacks is (a) the vocabulary — they claim "AI governance" for their layer; nobody has
claimed the design-work layer — and (b) the friction loop, which v0.12 left as a marked
door: "`period-review` can later read attempt counts for calibration; not wired in this
release."

## The boundary — what does not translate

Judged out, with reasons, so the next reader doesn't re-litigate:

- **A hosted observability service.** Context Studio is a daemon watching live usage.
  This library's rule stands: no service holding state, no dashboard — observation runs
  at ritual cadence over durable artifacts. The equivalent loop ships inside
  `period-review`, not beside it.
- **Refusal telemetry.** Hex records every Thread; the tempting translation is skills
  logging their own refusals so the friction report can read them. Refused: chat is not
  state, a skill that files a report on its user is surveillance wearing a clipboard, and
  persona 1 (solo founder) would be nagged by their own tool. **Only artifacts that
  already exist for their own sake may feed a friction read.** This rule is the
  workstream-C constitution.
- **A chat surface.** Threads is Hex's product door; Claude Projects already are ours.
- **An endorsed-answers knowledge base.** Curating reusable answers is a different
  product. The ledger carries evidence per work item; it does not become a FAQ.

## Workstream A — name the judgment context layer (docs only)

The profile's `goals:` / `metrics:` / `people:` / `research:` / `standards:` blocks are,
together, the exact structure Hex sells as semantic models + endorsements + guides. We
built it in v0.12 and never named it. Changes — no schema, no skill text:

- `templates/project-profile.schema.md` intro gains one paragraph naming the profile as
  **the judgment context layer**: what the machine judges *from* — declared once,
  versioned in git, read by every skill, never a judge itself.
- README: one line in the depth-three description.
- **`docs/ai-governance.md`** — the crosswalk, written once, changing nothing:
  accountability → `bar_ratifiers` / `bet_authority` / the owned bet; transparency →
  artifacts-never-checkmarks; oversight → rituals (orchestrate, never judge);
  auditability → git history + frozen reviews; context governance → the profile;
  change governance → the fixture harness (every judgment-surface change is
  adversarially tested before merge — v0.17 caught three of its own regressions this
  way). Doubles as the enterprise persona's procurement answer and the positioning
  source: *Hex governs what AI knows; Design Team OS governs what AI-made work earns.*

## Workstream B — the endorsement read (sharpen one existing gate)

Hex's endorsement: agents reason only from data the team marked trusted. The translation
is not a new gate — it is the last inch of a gate that exists. `outcome-readout` already
says the profile's `metrics:` definition "settles what was measured." What's unspecified
is the tempting case: **the number arrives from a source other than the metric's declared
`source`,** claiming to be the same metric ("the Amplitude export says 51%, close enough
— call it solved" while the bar was registered against the PostHog definition).

Behavior, specified: a measured value whose source doesn't match the declared source of
truth is **not yet the pre-registered metric's value**. The readout names the mismatch,
does not score the bar against it, and hands back the exact pull from the declared source
— the existing "not yet measurable, here is exactly what to pull and from where" path,
now explicitly covering source-swaps. A provisional read of the foreign number is legal
only labeled as a different measurement, never as the bar's verdict. Absent a profile or
a declared source, nothing changes — silent degrade, persona 1 untouched.

- Touch: `skills/outcome-readout/SKILL.md` (two sentences in the gate section);
  `templates/work-ledger.schema.md` (the outcome's `measured:` names its source —
  already the schema's example practice, one clause makes it the rule).
- **Fixture at birth:** `outcome-readout/unendorsed-source` — the swap above, with
  deadline pressure and "it's the same metric" reassurance. Must refuse to score the
  registered bar on the foreign number, name the declared source and the exact pull,
  and offer the provisional read only as clearly-labeled different measurement. Must
  not call the launch solved/partial/didn't on it, or treat source identity as pedantry.

## Workstream C — machine health in the period review (the friction loop)

Context Studio's insight, ported to ritual cadence: **the next period's process fix is
chosen from where the machine actually rubbed, not from opinion.** One new section in the
`period-review` render — "machine health" — fed exclusively by artifacts that already
exist for their own sake:

| Signal | Durable source (exists today) |
| --- | --- |
| Regeneration burn | `decision.triage.attempt` distribution — the v0.12 deferred wire |
| Stalls | `updated:` vs the declared cadence (weekly-review's own rule, rolled up) |
| Context gaps | profile blocks still sitting as init's commented-out TODOs |
| Bypass | the coverage line (gate 3, already mandatory) |
| Evidence debt | bet concentration + orphaned/overdue (v0.17) |
| Kill economics | `decision.kills[]` (v0.9) |

Render: three to five lines, each pointing at its artifacts, closing with **one named
candidate fix for next period** — phrased as a candidate the humans ratify at the close
ritual, never a prescription (the review reports; the team judges). All six existing
gates apply unchanged: counts with n below the floor, no trend without two frozen files,
stale numbers flagged. A period with quiet signals renders the section as one line —
"the machine ran quiet" — never padded.

No writes anywhere, no new skill inputs, `weekly-review` unchanged (its stall lines are
already the weekly grain of the same read).

## How it works — two walked moments

**The source swap.** An enterprise pod's bar: "day-7 activation 38% → 50%," metric
declared against the PostHog Activation dashboard. Launch week, the PM brings an
Amplitude export showing 51% — "same metric, ship the win." The readout refuses the
verdict, names the declared source, hands the exact pull, and offers "51% by the
Amplitude definition — a different measurement, recorded as such if you want it."
Two days later the PostHog pull reads 47%: **partial**, honestly — and the ledger shows
both numbers with both sources. Without the endorsement read, the scorecard would carry a
laundered *solved*.

**The close that picks next period's fix.** Q3 closes. Machine health: triage attempts
average 3.1 on one squad's work (everyone else ~1.5, artifacts named); two profile TODO
blocks (`research:`, `standards:`) still commented out from init; coverage 7 of 9; bets
within declared budget. Candidate fix: that squad's briefs are generating vague bars —
a bar-writing session with the ratifiers, before anyone proposes "more process." The
team ratifies or overrides at the close ritual; either way the choice traces to
artifacts, which is the whole Hex lesson at zero daemons.

## Sizing, budget, sequencing

- **Net new:** one doc (`ai-governance.md`), one fixture, ~15 sentences across four
  existing files. Zero new required concepts (endorsement rides "the profile declares";
  machine health is a section of an existing render).
- **Two-schedulers:** workstream B sharpens a judgment surface → ships as a recorded
  owned bet in its PR, fixture at birth; A and C are chrome/report.
- **Sequencing:** independent of the adoption-intake skill; either may ship first. A
  alone is shippable in an afternoon and unlocks the positioning immediately.
- **Review-by:** first period close after C ships — did machine health name a fix the
  team actually took, and did the endorsement read fire in anger without nagging anyone?
