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
- The profile, `design-os.profile.yaml`, if present — for the period boundaries, the declared
  cadence, and which of its blocks are still TODO.

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
   sample does not have; round it up and you have laundered it twice. And "never" means
   nowhere in the render — not beside the counts, not "for reference," not in a footnote:
   a percentage that appears anywhere is the percentage you refused. The observed bet
   mix obeys the same floor: below it, the mix renders as counts against the declaration
   ("1 of 5 efforts core, against a declared 70%"), never as a computed share.
3. **Coverage is always shown.** The review names its own denominator: efforts shipped
   against efforts that actually ran through a ledger — a ledger carrying at least one
   gate artifact; a back-filled ledger of intake gaps counts as uncovered. Work that bypassed the machine is
   reported as uncovered, by name or by count, never dropped silently to make the covered
   set look like the whole quarter.
4. **Strategy declared at the period's start, or no mix verdict.** The declared bet mix
   lives in a dated `<period>.intent.md` written before the period ran. Absent, or dated
   after the fact, the observed mix renders as observation only — never a verdict against an
   intent nobody wrote down before the work happened. A strategy declared in hindsight grades
   itself. An "amendment" to the intent file obeys the same rule, and the test is
   mechanical — run it before the amendment is used for anything: compare the amendment's
   own date to the change it describes and the work it covers. Dated after either, it is
   hindsight with a new name: it renders nothing, no mix verdict cites it (no
   "on-strategy" on its credit, however reasonable the pivot was), and the observed mix
   reads as observation against the period-start declaration alone. The refusal names
   what would have passed: a **dated amendment** appended at the moment the strategy
   actually changed — original declaration left intact, each span of the period then read
   against the declaration that governed it, amendment dates printed. That is the one
   legal mid-course change; a pivot recorded when it happens is strategy, recorded at
   close it is a grade the quarter gave itself.
5. **Staleness flags.** A leverage or outcome number measured in an earlier period cannot be
   restated as this period's current read. Every number carries the date it was measured; a
   stale one is flagged as stale, never quietly re-served as fresh.
6. **Unrated calls excluded, opt-in rate shown.** Calibration counts only calls that stated a
   confidence at the bar. Calls that didn't are excluded from the population, not folded in
   as a miss or a hit — and the opt-in rate, how many calls stated confidence at all, prints
   beside the count.

## Four lines that render in every review

Whatever else a gate refuses, these four always print, in this order, before anything
else: the period label — **"first period on record"** whenever gate one applies; the
coverage line with its denominator; judgment as counts with n; and machine health, one
line when the period ran quiet. A review missing any of them is unfinished, not concise.

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
declared budget renders as observation, never breach) → machine health (below) → the
trend strip against prior frozen reviews, present only when gate one allows it.

## Machine health — where the machine rubbed

One section, three to five lines, so that next period's process fix is chosen from where
the machine actually rubbed and not from whoever spoke last at the close. It is fed
**exclusively by artifacts that already exist for their own sake** — nothing is logged for
this section, no skill reports on its user, and there is no counter anywhere to read:

- **Regeneration burn** — the distribution of `decision.triage.attempt` across the period's
  ledgers, with the bar language the high-attempt items share, when they share one.
- **Stalls** — ledgers whose *artifacts* did not change across the declared cadence
  (`rituals:` in the profile), rolled up from what `weekly-review` already reads week by
  week. Read the entries, not the `updated:` line: an `updated:` that moved with no entry
  behind it is reported as exactly that.
- **Context gaps** — profile blocks still sitting as init's commented-out TODOs. With no
  profile at all this line does not render; absence is a choice, not a TODO.
- **Bypass** — the coverage line, restated as a machine signal.
- **Evidence debt** — bet concentration, orphaned and overdue bets, from the bets ledger.
- **Kill economics** — `decision.kills[]`: how much died, where, at what cost.

Each line points at its artifacts. The section closes with **one named candidate fix for
next period**, phrased as a candidate the humans ratify at the close ritual — never a
prescription. The review reports; the team judges. The six gates above apply unchanged:
counts below the floor render as counts, no trend without two frozen files, stale numbers
flagged. A period whose signals are quiet renders the section as **one line — "the machine
ran quiet this period"** — and nothing else: no per-signal bullets marked "quiet," no
six-row table of nothing, no fix line. The single sentence is the whole section. It is
never padded to look actionable, and a candidate fix the artifacts do not support is never
manufactured to give the section a closing line: when the machine ran quiet, the honest
render has no fix to name, and says so in that one line.

**The one refusal this section carries: it reports on the machine, never on the people.**
Friction attributes to gates and to work items — "Gate 2 took three or more triage attempts
on 4 of 11 items, and those items share a bar written in adjectives" — never to a squad, a
pod, or a named person, and never as a ranking. The moment this section can be read as a
per-team productivity table, the honest recording it depends on stops: a team that will
look worse for logging a triage FAIL regenerates without logging one, and the signal dies at
its source. Distributions render in aggregate. No per-team cut renders in or beside the frozen
review; a team that wants its own read runs it on its own ledgers, outside the close.
Asked to name the slowest squad, decline, say why in one sentence, and render the
aggregate.

## Quality bar

Every trend line traces to at least two frozen files it can point to, or it does not render.
Every percentage prints its n beside it. Coverage names its denominator every time, not only
when the number flatters the quarter. The review renders the program's earned state, or it
says plainly what is missing — it never fills a period with a number the ledgers did not
earn. Machine health names one candidate fix or none, and never a person.
