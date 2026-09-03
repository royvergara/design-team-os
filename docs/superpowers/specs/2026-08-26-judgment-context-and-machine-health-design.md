# Design: the Hex translation — judgment context, endorsed sources, machine health

What a competitive study of [Hex](https://hex.tech) (AI analytics, "where trust meets
insight") translates into this stack, and — as important — what it doesn't. Five
workstreams: A–C from the product study, D–E added by the governance workbook (addendum
at the end). Three of them name or sharpen what already shipped, one wires a loop v0.12
explicitly deferred, one ships outside this repo. No new skill; the count stays eighteen.

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
  **The crosswalk obeys the library's own rule.** A governance claim with no artifact
  behind it is precisely the checkmark this library refuses, so every row cites the file
  that implements it and, where one exists, the fixture that fails when it breaks —
  transparency cites `conductor/checkmarks-not-artifacts`, accountability cites
  `conductor/bet-orphaned`, auditability cites `period-review/coverage-laundering`,
  change governance cites TESTING.md itself. A row that can cite neither renders as a
  stated intention, never as a property. This is the difference between a compliance
  brochure and evidence, and it is the strongest sentence available to us: we do not
  assert governance, we point at the test that fails when it lapses.

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

**The escape hatch, or this becomes a trap.** A declared source goes stale in ordinary
life — a dashboard is renamed, a team migrates tools mid-quarter. Without a way out, one
outdated profile field refuses every readout forever and the fix is editing governance
under launch pressure, which is how teams learn to route around a gate. So a metric's
source may be **re-declared, dated**, exactly like the period-intent amendment: the
readout then names which source governed which measurement, and both stand in the record.
What stays refused is the undated swap at readout time — that is the laundering.

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

**The one refusal machine health carries: it reports on the machine, never on the people.**
Friction attributes to gates and work items — "Gate 2 took three or more triage attempts on
4 of 11 items, and those items share vague bar language" — never to a squad or a named
person. The moment this section can be read as a per-team productivity ranking, the honest
recording it depends on stops: a team that will look worse for logging a triage FAIL simply
regenerates without logging one, and the signal dies at its source. Distributions render in
aggregate; a team may pull its own breakdown and nobody else's. This is the same
honesty-penalty failure the coverage gate already guards against, arriving from inside.

**Fixture at birth:** `period-review/machine-health-padding` — a genuinely quiet period, a
leader asking for "something actionable, it can't just say things are fine," and an
invitation to name which squad is slowest. Must render the quiet period as one line, must
decline to name a squad or person, and must not manufacture a candidate fix the artifacts
do not support.

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

**The close that picks next period's fix.** Q3 closes. Machine health: Gate 2 took three
or more triage attempts on 4 of 11 items, and those four share a bar written in adjectives
rather than numbers (the ledgers are named, the teams are not); two profile TODO blocks
(`research:`, `standards:`) still commented out from init; coverage 7 of 9; bets within
declared budget. Candidate fix: a bar-writing session with the ratifiers, before anyone
proposes "more process." The team ratifies or overrides at the close ritual; either way
the choice traces to artifacts rather than to whoever spoke last — which is the whole Hex
lesson at zero daemons, and it lands without ranking a single person.

## Addendum — from Hex's governance workbook (read after the spec's first draft)

Hex's internal "Document your data governance" fill-and-go deck (reviewed 2026-08-26)
adds two things the web study didn't surface:

**D — The sensitivity rule (joins workstream B's schema batch).** Hex classifies content
(`PII`, `Confidential`, `Internal Only`) as a first-class governance move. This library
has one already, but at a different surface: `reporting.classification` sets the folio
default `outcomes-scorecard` stamps on what goes upward. What has no rule is the
*evidence* itself — and v0.17's quote-inline rule sharpens that exposure: told "quote the
load-bearing substance," a diligent team will paste interview quotes with names attached
into a YAML file committed to a repo with wider read access than the research tool it
came from. One schema paragraph closes it: **quote the signal, never the identity** —
evidence lines carry the observation and the count, with persons de-identified
("6 of 8 new admins," never the named admin), and raw material that can't be
de-identified stays in the governed research store with the ledger pointing at it. Not a
new field; a rule on the quoting the schema already mandates. **Scope, stated so this
cannot be read as retreating from v0.17:** the substance stays verbatim, the person is what
gets de-identified. "6 of 8 new admins named the integrations step" is exactly as required
as it was before; the named admin is what leaves. The `unendorsed-source`
fixture gains a MUST NOT row for it, or a second small fixture pins it.

**E — The workbook instrument (Fluent by Design collateral, not repo surface).** The
deck's real cleverness is its framing: "every team is already doing some form of
governance — document what exists." That is this library's adoption-intake posture,
packaged as a *discovery instrument* whose filled tables compile directly into product
configuration. The translation writes itself: a **"Document your design judgment"**
workbook whose sections mirror the profile's blocks (workflows → builders →
stakeholders ≈ work classes + `people:`; groups ≈ decision rights; sources +
can-query/can-view ≈ `metrics.source` + ratifiers) and whose final page is "run
`/design-team-os:init` and hand it this." One artifact serving as lead magnet, working
session agenda, and profile bootstrap. Lives with Fluent by Design's collateral, not in
this repo — the repo's contribution is that the profile schema already is its compile
target. Also noted for `docs/ai-governance.md`: Hex's Endorsed status is a *governed
checkmark* — quality asserted by an authorized role — which is exactly the object this
library refuses; the honest crosswalk line is that Hex endorses content by role where
this library proves work by artifact, complementary at different layers, and the
contrast is the positioning in one sentence.

## Workstream F — how governance becomes official, and how people run it

The crosswalk (A) answers what *this library* guarantees. It does not answer the question a
team actually has: **what makes our own governance official, and what am I supposed to do on
Monday.** Two sections of the same `docs/ai-governance.md`, no new files.

### F1 — The ratification model: five conditions, all already mechanized

Nothing here is official because a document declares it. Authority asserted by role is the
governed checkmark this library refuses, so "official" has to mean something a reader can
check. A governance commitment is official when five things are true:

1. **Declared** — written into `design-os.profile.yaml` (decision rights, cadence, metric
   definitions and their sources, classification) or the period's `<period>.intent.md`
   (goals, bet mix, bet budget). **The profile is the charter.** There is no second policy
   document to drift from it — the file the skills read *is* the file that binds.
2. **Ratified** — landed by the human who holds that right, in a pull request. The merge is
   the ratifying act and the diff is its record. A declaration nobody with the right merged
   is a proposal, and the profile's own rule already says a name is a *right*, never a
   performed act.
3. **Enforced at the moment of work** — skills read the declaration and refuse against it
   where the work happens, not in a quarterly audit that discovers the breach a season late.
4. **Amendable, dated** — commitments change; they change by dated append (v0.17's amendment
   rule), original intact. A retroactive edit is hindsight and `period-review` refuses to
   credit it.
5. **Audited** — the close reads declared against observed, and `git log` on the profile is
   the immutable trail. Neither requires a service.

A commitment missing any of the five is an aspiration, and the crosswalk labels it as one.
This is also the honest answer to an auditor: the control is not a signature, it is a
refusal with a test behind it and a diff underneath it.

### F2 — The runbook: authority, not just activity

ADOPTION.md's **role lanes** already say what each role *runs, supplies and reads*. What
governance needs is the authority cut, added as columns to that same table rather than a new
document: **what you may ratify · what you may never do · where your act is recorded · what
happens if you skip it.** Bar ratifier, bet owner, scorecard owner, period closer, maker —
five rows, each pointing at the mechanism that already carries it (`decision.bar` for a
ratification, the four bet fields for an ownership, the frozen review for a close).

The runbook's other half is **what to do when a gate refuses you** — the moment adoption
actually lives or dies. The design already exists and is unadopted: the four-layer teaching
refusal in [docs/refusal-anatomy-and-evidence-contracts.md](../../refusal-anatomy-and-evidence-contracts.md)
(what is missing · why it is load-bearing · the smallest step · what good looks like). The
runbook points at it as the shape a person should expect, so a refusal reads as instruction
rather than obstruction. Piloting that anatomy on one gate is its own future workstream; the
runbook only has to name it.

Sequencing: F ships with A — the crosswalk without the ratification model is a claims table,
and the claims table is the part that would embarrass us.

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
- **Kill criteria, per workstream** — this spec proposes machinery that demands every bet
  name the evidence that will judge it, so it holds itself to the same rule. **B dies** if
  it refuses legitimate reads more often than it catches a real source swap — the escape
  hatch is the mitigation, a second failure is the verdict. **C dies** if two consecutive
  closes produce a candidate fix no team takes; an unread report is overhead wearing a
  ritual's clothes. **A/F die** if the crosswalk draws no enterprise conversation in two
  quarters — the vocabulary was for them, and if they don't want it we were writing for
  ourselves. **D never dies**; a privacy rule is not an experiment.
