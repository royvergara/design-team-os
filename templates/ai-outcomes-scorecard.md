# AI Outcomes Scorecard

One scorecard per AI assisted design effort. This is the program level companion to the [`outcome-readout`](../skills/outcome-readout/SKILL.md) skill: the skill reads a single shipped feature against its pre registered bar, this scorecard rolls the whole effort up. Fill the baseline before the work starts. Update at prototype, at ship, and at the quarter.

Picture the meeting where nobody argues the work failed. Someone just asks what it returned. This document exists so that room never goes quiet.

The whole thing earns one sentence: the work got faster, and the speed moved a real outcome. Everything below exists so you can write that sentence with numbers in it.

Copy this file into your product repo, next to `design-os.profile.yaml`, and keep it under version control. The per feature evidence lives in the [work ledgers](work-ledger.schema.md); this is where the ledgers roll up.

## Before you fill anything: the gate

Two prerequisites. No exceptions.

1. **A baseline.** What the loop looked like before the change.
2. **A goal.** The business outcome this effort exists to move, named as a customer pain and a number.

If you cannot reconstruct a baseline, stop. A scorecard built after the fact measures a memory, not a change. Write the smallest honest baseline the team can still reconstruct in the note below, start capturing today, and score the next cycle instead.

## The effort

| Field | Entry |
|---|---|
| Effort or program name | |
| Owner | |
| Date baseline captured | |
| The pain (whose pain, in their words) | |
| The goal (the number this should move) | |

## The baseline

| Question | Before |
|---|---|
| Time from brief to a validated prototype | |
| Directions explored per brief | |
| Cost per validated learning | |
| How decisions got made (opinion, signal, or seniority) | |

Smallest honest baseline note, if reconstructing:

## Layer 1, Leverage: is the work faster and cheaper?

Leverage is activity, not a result. Label it that way out loud. Every row must name the Layer 2 signal it serves. A leverage number with no outcome attached is the exact thing this scorecard exists to stop a team from celebrating.

| Metric | Baseline | Current | Target | Serves which Layer 2 signal |
|---|---|---|---|---|
| Brief to validated prototype | | | | |
| Directions explored per brief | | | | |
| Cost per validated learning | | | | |
| Workflow adoption, share of projects | | | | |
| Decisions backed by a real user signal | | | | |

## Layer 2, Outcome: did the speed produce value?

Three signals, each readable at a different moment. The move that makes this scorecard work: pull the first two forward to the prototype stage, before production code exists, so weak bets die while being wrong is still cheap.

| Signal | When read | What it answers | How measured | Result |
|---|---|---|---|---|
| Attitudinal (leading) | Discovery and prototype | Will they want it, can they use it | | |
| Behavioral (proxy) | Prototype and early build | Do they actually do it | | |
| Performance (lagging) | After ship | Adoption, retention, conversion, revenue | | |

## Work carried by an owned bet

Some of the work rolled up here proceeded without evidence on purpose, on the record: an [owned bet](work-ledger.schema.md), with a named owner, a declared absence of evidence, a reason, and a review date. Bets belong on the scorecard, and they belong in their own section, never blended into a Layer 2 result.

| Work | Gate carrying the bet | Owner | Reason | Review by | What the review found |
|---|---|---|---|---|---|
| | | | | | |

A bet never reads as proven. If its review date has passed and the row is still empty, that is the finding: the bet was never judged. Say so out loud in the headline rather than letting it age quietly into a claim.

## The headline

The only result worth reporting up is the line between the layers. Fill it as one sentence:

> We compressed time to validated learning from ______ to ______, and the accelerated work moved ______ by ______.

If you can only fill the first half, you have a leverage report. Say so, name the outcome signal still maturing and the date it can be read, and do not present activity as the result.

## Quality bar, before this leaves the team

- [ ] Baseline captured before the start, or honestly reconstructed and labeled as such
- [ ] The pain and the number named at the top
- [ ] Every Layer 1 metric points at a Layer 2 signal
- [ ] At least one attitudinal or behavioral signal read at the prototype stage
- [ ] Every owned bet listed in its own section, with its review date and what the review found
- [ ] The headline sentence filled, or explicitly marked leverage only with a read date
- [ ] Per feature readouts run through [`outcome-readout`](../skills/outcome-readout/SKILL.md) before any feature is called a win
