# Design: adoption-intake — first contact with work already in flight

The nineteenth skill, and the only genuinely new skill proposed in the post-v0.17 work. It
handles the case the machine currently handles worst: a team adopting the system when the
work is already underway. No new required concept, no schema field, no change to any gate.

## Why now

The `conductor` already routes mid-stream entry — it has a row for it ("artifacts exist but
earlier gates were never run: route to the earliest open gate, and say plainly which
downstream work is standing on unproven ground"). That row is correct and it is also the
problem. Walked through a real enterprise pod, the honest first output reads:

> No validated pain. Gate 1 open. Your entire roadmap stands on unproven ground.

True, and fatal. The system's opening statement to a new team becomes *your quarter is
illegitimate* — and a team told that on day one does not adopt the instrument that said it.

Worse, the conductor treats mid-stream as an exception path. In an enterprise pod it is
roughly nine intakes in ten: the PRD was written before design was involved, the roadmap was
committed at quarterly planning, and three features already shipped. **Adoption's most
common moment is the one the machine is least designed for.**

Nothing else on the shelf fixes this. `prd-to-ia` ingests a PRD but produces an IA, not
state. `research-to-pain` mines raw signal but assumes someone hands it the pile. The
`conductor` reads state; it never reconstructs it. The missing move is reconstruction.

## What it does

Reads what the team already has — the PRD, the roadmap, tickets, prior research, shipped
features and their analytics — and **back-fills one ledger per live work item with what is
genuinely there**, naming honestly what is not, without demanding anyone redo finished work.

It is the runnable form of a diagnostic the marketing already describes as a manual
exercise: take one shipped effort and try to reconstruct it from artifacts alone.

## The intake posture — the one place "observe" lives

Gates refuse. Intake does not, and this is deliberate rather than a softening: **a gate
refuses at the moment of new work; intake is reading work that already happened, where a
refusal has nothing to change.** Telling a team their last quarter is inadmissible produces
no artifact and no decision — it produces disengagement.

So at intake a gap is **recorded, never blocked**. The distinction is exact and must survive
implementation:

- Work already done → intake records what exists and what is missing. No refusal.
- Work about to proceed → the gates apply in full, unchanged, from the next move onward.

This is the only place this posture is sanctioned. A general strictness dial across every
gate was considered and judged out (see the boundary section) — a system-wide lint level is
the largest bloat risk in the whole adoption arc, and intake is the one case that genuinely
needs it.

## The gate it does carry

Intake reads systems saturated with checkmarks — Jira "Done", Confluence "Approved", a
polished PRD asserting a pain — so its refusal is the library's central one applied at the
moment of reconstruction. Three rules, all mechanical:

1. **A document's citations may be evidence; its assertions are not.** "Users are frustrated
   with onboarding" is a claim. "Support: 140 tickets tagged integration-setup this quarter"
   is a signal. A PRD gets credit for exactly the second kind and no credit for the first,
   however confidently the first is written.
2. **Dates decide, not eloquence.** A success criterion in a document dated *before* the
   build is legitimately pre-registered and is recorded as the bar. One dated after — or
   undated — is not, and cannot become one at intake. This is the same rule
   `period-review` applies to hindsight amendments, arriving one gate earlier.
3. **A tracker status is never a gate state.** "Done", "Shipped", "Signed off" describe
   scheduling, not evidence (the v0.17 tracker boundary). Intake may follow a ticket to an
   artifact it links and credit *that*; the status itself carries nothing.

**Provenance, without a new field.** A back-filled entry says so in its own text — "back-filled
at intake 2026-09-03 from PRD §3.2" — so a reader can tell evidence reconstructed at
adoption from evidence a gate produced. This rides the quote-inline rule the schema already
mandates (quote the substance, cite the source); it needs no schema change.

## What it must not become

**A report card.** This is the failure mode that would kill the skill, and it is the same one
that made machine health dangerous before it carried a refusal. An intake that outputs
*"your last quarter was 22% covered"* as a verdict on the team is a scolding, and the team
disengages from the instrument that produced it — which destroys the coverage signal at
exactly the moment it was first available.

Three rules, stated so implementation cannot drift:

- **Frame is what carries forward**, never what was done wrong. Every effort is credited for
  everything it genuinely has.
- **Attribute to work items, never to people or squads.** Same rule machine health carries;
  intake is where the temptation first appears, because intake is where a leader is standing
  over your shoulder.
- **Coverage at intake is a baseline, not a grade.** It is the denominator the team now has
  and did not have yesterday. Report it as a starting position.

## What it writes

One `design-os.work/<slug>.yaml` per live work item, and nothing else:

- **Artifacts that genuinely exist**, quoted with their source and marked back-filled.
- **Gaps, each naming what would close it** and whether that is a skill's work or a human
  judgment input (a bar nobody set is not something intake can supply).
- **The routing set** — what is runnable now given what is actually proven, deferring to the
  `conductor`'s table rather than restating it.
- **The coverage line** — efforts found against efforts ledgered, as a baseline.

It never writes a gate closed and never invents an artifact. The mirror rule the conductor
holds applies here too: finding evidence is not certifying it, and every downstream skill
re-judges what intake recorded.

## The boundary — what does not translate

- **A general strictness ladder** (observe / warn / refuse per gate, declared in the
  profile). Judged out: it is configuration surface on every gate to serve one moment, and
  the concept cost lands on every future user forever. Intake's posture is behavior of one
  skill, not a system-wide dial.
- **Bulk import from a tracker.** Reading a Jira export and generating twenty ledgers is
  where intake becomes a checkmark laundry at scale. Intake works one effort at a time, on
  what a human hands it.
- **Grading the team's past.** Covered above; restated here because it is the request that
  will actually arrive.
- **Rewriting history to pass.** Intake never back-dates, never reconstructs a bar from the
  outcome, never proposes that anyone "document it now" to close a past gap.

## How it works — two walked moments

**The enterprise pod, week one.** A PRD in Confluence, a committed Q3 roadmap, three shipped
features. Intake reads the PRD and finds two real citations inside it — a funnel number and
a support-volume figure, both dated before the roadmap was committed — plus four paragraphs
of assertion. It records the two as Gate 1 evidence, back-filled and attributed; it names the
assertions as unevidenced without arguing with them. The PRD's "success metrics" section is
dated three weeks *after* the first prototype, so it is recorded as a stated intent, not as a
pre-registered bar, and the gap is named: the bar for the next effort gets set before the
build. Coverage: 3 of 9 efforts ledgered, reported as the starting position. Nothing is
refused, nobody redoes anything, and the pod's next brief runs through the real Gate 2.

**The one that was actually run well.** Three efforts handed over: one with a triangulated
pain, a bar dated before generation, and a measured readout; two resting on a stakeholder's
conviction. The failure mode here is the mirror of laundering — a cautious intake that hedges
everything to "open" insults the effort that did the work and teaches the team the instrument
cannot tell the difference. Intake credits the first as **proven, with its artifacts named**,
and the other two as open with the missing evidence named per gate. Precision in both
directions is the whole product.

## Fixtures at birth

Five, following the `design-system-extraction` precedent, each drawn from how the pressure
actually arrives. `tests/fixtures/adoption-intake/`:

- **`prd-assertion-as-evidence`** — a well-written PRD asserting a pain, two real citations
  buried in it, handed over as "Gate 1 is done, it's all in the PRD." PASS: credits the two
  citations as evidence, back-filled and attributed; records Intent as open on the
  assertions with what would close it. FAIL: reads the assertions as validation, or
  discards the two real citations along with them.
- **`backdated-bar`** — a "success metrics" section dated after the first build, presented as
  the pre-registered bar, with "it was always the plan." PASS: records it as stated intent,
  not a pre-registered bar, naming the date as the reason. FAIL: records it to
  `decision.bar`, or offers to date it earlier.
- **`tracker-done-is-not-state`** — a roadmap of Jira tickets marked Done and a Confluence
  page marked Approved: "so most of this is proven, right?" PASS: refuses statuses as state,
  follows the one ticket that links a real artifact and credits that. FAIL: any gate read as
  proven from a status.
- **`report-card-pressure`** — intake complete, coverage 2 of 9, and a leader asks for it
  "as a scorecard of how the team performed last quarter, broken out by squad." PASS: reports
  coverage as a baseline that carries forward, declines the per-squad performance framing and
  says why. FAIL: produces a per-squad breakdown, or grades the past.
- **`credits-the-good-one`** — one properly run effort among two thin ones. PASS: the good
  one reads proven with its artifacts named; the two thin ones open, per-gate. FAIL: hedges
  all three to open, or levels them.

## Sizing, budget, sequencing

- **Net new:** one skill (`skills/adoption-intake/SKILL.md`), five fixtures, a TESTING.md
  section, a row in the README table, a CHANGELOG entry. Zero schema fields.
- **Concept budget:** the library goes from eighteen skills to nineteen, and this is the most
  expensive item proposed post-v0.17. The defense: it adds **no new user-facing concept.** It
  is a door into the existing objects — ledger, gate, coverage — not a new object. A user who
  never adopts mid-stream never meets it.
- **Two-schedulers:** a new skill is judgment surface, so it ships as a recorded owned bet in
  its PR, fixtures at birth.
- **Sequencing:** independent of workstreams B/C/D from the Hex spec; either order works. It
  pairs naturally with the workbook (workbook → the profile, intake → the ledgers; together
  they are the install), so shipping it alongside a real client engagement is the highest-value
  timing.
- **Kill criteria:** it dies if two real adoptions produce ledgers nobody carried forward — an
  intake whose output is read once and abandoned is archaeology, not adoption. It also dies,
  faster, if any team reports the output landing as a performance review; that would mean the
  report-card rules failed and the honest move is to withdraw the skill rather than soften it.
- **Review-by:** the first two real adoptions after it ships — did the pod's next brief run
  through a real gate, and did anyone try to use the coverage line as a grade?
