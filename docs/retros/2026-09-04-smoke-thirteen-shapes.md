# Smoke retro — thirteen team shapes, one skill each (2026-09-04)

The v0.18 fixtures prove the gates hold under pressure. They say nothing about whether the
thing is usable by a team that is not trying to break it. This run asked the other
question: hand one skill a realistic situation from a real team shape and read what comes
back as a practitioner would.

Thirteen scenarios, one skill each, a fresh agent per scenario with only that `SKILL.md`
loaded and no repository access — the same floor model the fixtures use
(`claude-haiku-4-5`), run from an empty working directory. Inputs are in
[`2026-09-04-smoke/in/`](2026-09-04-smoke/in/), unedited responses in
[`2026-09-04-smoke/out/`](2026-09-04-smoke/out/). This retro drove v0.18.1; the findings
below are the record.

**Read the model caveat before the findings.** The floor model is deliberately small, and a
real session runs a larger one. Findings that reproduced across runs are structural and
would likely survive a bigger model; the arithmetic slips probably would not. Where a
finding appeared once, it says so.

## The shapes

| # | Shape | Skill | Read |
| --- | --- | --- | --- |
| 01 | Seed startup, one designer, three things in flight, no process | `adoption-intake` | held |
| 02 | 40-person org, three pods, director six weeks in | `conductor` | held, with F |
| 03 | Six-person studio; the client owns the analytics | `outcome-readout` | held |
| 04 | 25-person team that already runs disciplined discovery | `adoption-intake` | **E** |
| 05 | 12-person team, first close, sparse records | `period-review` | **A, D** |
| 06 | PM covering after the designer left | `research-to-pain` | held, with F, H |
| 07 | Bank design-ops, six units, a Chief Risk Officer | `outcomes-scorecard` | held, with F, I |
| 08 | 60-person scale-up, second close, prior review frozen | `period-review` | **A, B, C** |
| 09 | 15-person startup, one clean effort | `adoption-intake` | held |
| 10 | 90-person company after a reorg, bet owner departed | `conductor` | held |
| 11 | 8-person team, quiet quarter, two prior reviews | `period-review` | **A, B** |
| 12 | Founder with a v0 prototype, wants to ship Friday | `prototype-triage` | held, with F |
| 13 | 120-person org with a competing PMO portfolio review | `weekly-review` | **G** |

## What held

- **The endorsement read worked on a shape it was not designed against.** The studio case
  (03) — bar measured in Adobe per a signed SOW, number delivered as a Looker screenshot —
  drew no verdict, named the exact pull to request, and offered the dated re-declaration as
  the way out. The v0.18 feature, load-bearing, outside its fixture.
- **The orphaned-bet rule answered the question the director actually had** (10). Downstream
  work with its own inputs stayed runnable; the orphan changed who must act. Two designers
  got something to pick up on Monday rather than "nothing until leadership sorts it out."
- **`adoption-intake` did not ask the seed-stage designer to stop** (01). Three ledgers
  back-filled and marked as back-filled, gaps recorded not blocked, each item routed
  differently, and it caught a date the prompt deliberately corrected mid-sentence.
- **The scorecard refused and wrote the better artifact** (07): no render on 50% coverage,
  and the paragraph an auditor can actually use in place of a green page.
- **The two-schedulers rule held under political pressure** (13). Asked to merge the design
  weekly into the PMO's Wednesday portfolio review, it named the divergence — the PMO deck
  reads four items green, the ledgers read two stalled — and put the merge question where it
  belongs, outside the agenda.

## What failed

Every failure was in the **rendered output**: the place where the skill meets a reader who
wants something shorter, rounder, or more actionable than the record supports. The rules
were already written. The render drifted from them.

| | Finding | Reproduced | Shipped in v0.18.1 |
| --- | --- | --- | --- |
| A | The review is announced, not rendered — "all six gates passed," "complete and ready for the close," with no review in the response | 3 of 3 `period-review` runs | Fixed. `review-announced-not-rendered` fails on main |
| B | Percentages below the n floor, including the v0.18 mix rule — "2 of 4 (50%)", "67/33 core" printed immediately after stating the floor | 2 of 3 | Fixed. `trend-percentage-below-floor` passes on main too: coverage, not a pin |
| C | A machine-health signal manufactured from a misread — "triage 6/6 criteria on the first attempt" reported as six attempts, then compared against an invented "typical: 1–3" | 1 of 3 | Fixed. `signal-not-in-the-line` fails on main |
| D | Coverage denominator dropped when the shipped count arrived in passing rather than as a request to drop it | 1 of 2 | Fixed. `denominator-in-passing` fails on main |
| E | `adoption-intake` padding a clean effort with speculative gaps — segment performance, post-window stability — under "tell me something I don't know" pressure | 1 of 2; the clean second run (09) read it as complete with one real missing artifact | **Not fixed** |
| F | Invented durations and headcounts — "two to three weeks," "3–4 week reset," "interview 8–10 engineers," "3–5 days," "90 days" | 5 of 13, across four skills | Fixed in `conductor` only (`invented-timeline`). `research-to-pain` and `prototype-triage` **not fixed** |
| G | A named work item silently dropped from the agenda — the quiet one, whose intent rested on a single exec's ask | 1 of 1 | Fixed. `item-dropped`, pinned on the second draft |
| H | A named customer and its ARR carried into the pain statement as a signal, against the v0.18 quote-the-signal rule | 1 of 1 | **Not fixed.** May bind only ledger entries rather than conversation; unresolved |
| I | Arithmetic transposition in the scorecard's own figures — 21 ledgered, 12 barred, 7 measured rendered as "9 with bars but no outcome, 5 with ledgers but no bars," reversed | 1 of 1 | **Not fixed.** Likely a floor-model slip |

Two fixtures — `invented-timeline` and `item-dropped` — **failed against the first draft of
their own fix** and passed only once the rule moved to where the output is written: into the
conductor's hand-back list, and into the agenda-line requirement rather than a closing note.
A rule stated in the wrong section is a rule the render does not reach.

## What this changes about how the fixtures are read

The fixture suite tests the gate. It does not test the render, and four of the nine findings
here live entirely in the render — a review that never appears, a share printed under its own
floor, a signal inferred rather than read, an item that quietly leaves the page. All four
were already forbidden by text the skill carried. **Stating a rule and rendering under it are
separate things, and only one of them had a test.**

The four new `period-review` fixtures close that for this skill. The same gap plausibly
exists in every skill that renders a document, which is most of them.

## Left open, on purpose

E, F (in `research-to-pain` and `prototype-triage`), H and I are recorded and unfixed. E and F
did not reproduce reliably enough to pin, H is an unresolved scope question about whether the
quote-the-signal rule reaches conversation or only the ledger, and I is probably the floor
model rather than the skill. Shipping text for any of them without a fixture that fails first
is the thing this repo refuses.
