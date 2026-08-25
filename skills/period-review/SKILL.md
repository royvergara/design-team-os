---
name: period-review
description: Use to close out a period — a quarter by default — and render the program's judgment record across every closed ledger in design-os.work/. Triggers on a request to run the period review, close out the quarter, or show leadership the trend, with closed ledgers present. A first period with no prior frozen review renders as the baseline, never a trend; judgment below n=10 calls renders as counts, never a percentage; and coverage — how many efforts shipped against how many ran through a ledger — always prints, even when the gap is unflattering.
---

# period-review

You render the program's earned state across a period. You do not judge one feature — that
is `outcome-readout`. You do not place the team on a maturity curve — that is
`team-ai-baseline`, though you may cite its latest read. You do not route work — that is the
`conductor`. Your subject is time: what a whole period's ledgers actually earned, set beside
what prior periods earned, with nothing borrowed from hope or from a single good quarter.

## Inputs

- The period's closed ledgers in `design-os.work/`.
- The period's dated strategy declaration, if one exists: `design-os.reviews/<period>.intent.md`,
  written at the period's start, naming the bet mix the team meant to run.
- Prior frozen reviews in `design-os.reviews/` — the only source a trend may ever cite.

A period is a quarter by default (`2026-Q3`); any cadence works, as long as it is
consistent, declared, and dated. You do not choose the cadence — you read whatever the team
has already been declaring.

## The six gates, before any render

Each of these is a refusal, not a caveat you note and proceed past.

1. **No prior frozen review, no trend.** With no earlier `design-os.reviews/` file to stand
   beside, this period renders labeled "first period on record" — never a trajectory, never
   a "trending up" or "getting better" headline. One point has no slope; do not draw one to
   satisfy a leadership deck.
2. **Small-n floor.** Below n=10 calls in the trailing window (default four periods, and the
   n is always printed beside the number), judgment renders as counts — "3 of 4 calls hit" —
   never a percentage. A percentage built on a handful of calls launders a precision the
   sample does not have; round it up and you have laundered it twice.
3. **Coverage is always shown.** The review names its own denominator: efforts shipped
   against efforts that actually ran through a ledger. Work that bypassed the machine is
   reported as uncovered, by name or by count, never dropped silently to make the covered
   set look like the whole quarter.
4. **Strategy declared at the period's start, or no mix verdict.** The declared bet mix
   lives in a dated `<period>.intent.md` written before the period ran. Absent, or dated
   after the fact, the observed mix renders as observation only — never a verdict against an
   intent nobody wrote down before the work happened. A strategy declared in hindsight grades
   itself. The one legal mid-course change is a **dated amendment**: appended to the same
   file at the moment the strategy actually changed — a pivot, a redirected quarter — with
   the original declaration left intact. The review then reads each span of the period
   against the declaration that governed it, amendment dates printed. An "amendment" dated
   after the work it blesses is hindsight with a new name, and gets the same refusal.
5. **Staleness flags.** A leverage or outcome number measured in an earlier period cannot be
   restated as this period's current read. Every number carries the date it was measured; a
   stale one is flagged as stale, never quietly re-served as fresh.
6. **Unrated calls excluded, opt-in rate shown.** Calibration counts only calls that stated a
   confidence at the bar. Calls that didn't are excluded from the population, not folded in
   as a miss or a hit — and the opt-in rate, how many calls stated confidence at all, prints
   beside the count.

## When the gates pass, render

Render `design-os.reviews/<period>.html` in the scorecard's visual system — the same
registers, the same honesty runtime rules, no projection geometry ever drawn into a trend.
Read [templates/scorecard.html](../../templates/scorecard.html) for the design language; a
dedicated review template is future work, so borrow its palette and registers rather than
invent a new visual system for one page. If a `design-os.profile.yaml` is present, take the period label and boundaries from its `calendar:` block — the period definition only; every number still comes from the frozen ledgers.

**Frozen: a prior period's file is never edited.** The trend is the sequence of frozen
files, not a running total — a new period adds a new file; it never rewrites the one before
it. Git is the event log here; there is no dashboard and no service holding state you could
silently correct.

Content, top to bottom: masthead (the period, the declared strategy, and its declaration
date) → the period's one-sentence headline → the coverage line → outcomes rollup (effort ·
class · bar · verdict) → judgment (calibration, kill economics, observed mix against
declared) → bets ledger (open / reviewed / overdue / orphaned, plus the concentration
read: open bets against active ledgers, printed beside the declared mix — and beside the
declared bet budget, when the period's intent file names one; a concentration with no
declared budget renders as observation, never breach) → the trend strip against prior
frozen reviews, present only when gate one allows it.

## Quality bar

Every trend line traces to at least two frozen files it can point to, or it does not render.
Every percentage prints its n beside it. Coverage names its denominator every time, not only
when the number flatters the quarter. The review renders the program's earned state, or it
says plainly what is missing — it never fills a period with a number the ledgers did not
earn.
