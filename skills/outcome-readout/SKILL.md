---
name: outcome-readout
description: Use after a shipped feature has run long enough to read its analytics, to judge whether it solved the pain and produce the next thing worth working on. Triggers on a launched feature plus its spec/Validation Record and live numbers, or a request for a "did it work" readout, post-launch review, or outcome scorecard.
---

# Outcome Readout

*Closes the Value loop back to strategy. Draft v0.1 — working starting point, expect to refine.*

## Purpose

Read what shipped against what was promised, render an honest verdict, and hand strategy the
next problem worth starting. `prototype-to-spec` bakes the success metric and instrumentation
into the build so the Value gate is *answerable* — this skill is what finally answers it.
Without it, the spine generates and ships forever and never learns whether any of it mattered.
This is the loop-back the whole library is built around.

## When to use / not use

**Use it** once a feature has shipped and enough time has passed to read its pre-registered
metric, and you have the spec's Validation Record plus the live numbers.

**Do not use it** before there is real post-launch data (too early — wait, or say how long),
or as a substitute for the spec's own pre-registration (if no metric was set before launch,
this skill cannot manufacture one after the fact — see the gate).

## Project profile (read before asking for context)

Look for a project profile named `design-os.profile.yaml`:

- **If you can read files:** read it from the repo root; verify any value you rely on against
  its `source` (e.g. confirm an event name is real before reading it). Warn if
  `verified_against_commit` is behind HEAD.
- **If you cannot read files (chat / Project):** use the profile if pasted; otherwise ask
  once for the specific field you need, not a full questionnaire.
- **No profile present:** fall back to *Inputs needed* and flag the gap in *Decisions you
  should check*.

From the profile this skill pulls: `analytics.tool` and `analytics.events` (to confirm the
metric's events exist and were emitted) and `evidence_sources`. The profile names the
*vocabulary*; it does not supply the verdict or the numbers — those are measured, and the
gate below holds out for them.

## The gate question

Value asks: *did it solve the pain and move the needle?* This skill makes it answerable:
*what was the pre-registered metric, what did it actually measure post-launch, and does that
clear the bar the team set before building?*

## The gate (this skill refuses)

Do not render a success (or failure) verdict unless you have **both**:

1. **The pre-registered metric and bar** — the success criterion set *before* launch (from
   the spec's Validation Record / the brief). If none was pre-registered, you cannot score
   the launch; say so, and the fix is upstream (`brief-from-pain`), not a number invented now.
2. **The measured post-launch value** — the actual number the metric reads now. No verdict on
   a metric you haven't measured.

**No success claim without the number.** "Engagement looks up," "users seem to love it," "the
team is happy" are not verdicts — they are vibes. If you don't have the measured value, the
output is "not yet measurable, here's exactly what to pull," not a verdict.

**Never score against a criterion invented after launch.** You may only judge the launch
against the bar that was set before it. Moving the goalposts to a metric that happens to look
good is how teams launder a miss into a win — refuse it. If the pre-registered metric turns
out to be the wrong one, that is itself a finding for the next Intent round, not license to
swap in a flattering number.

## Process

1. **Restate the pre-registered bar** — the metric and the target, from the Validation
   Record / brief. If it's absent, stop and flag (gate failure 1).
2. **Pull the measured value** — the metric's actual post-launch number. Confirm the events
   it depends on are real (against the profile) and were emitted. If you can't get the
   number, say precisely what to pull and from where (gate failure 2).
3. **Compare to the bar** — met, partially met, or not met. Use the number, not impression.
4. **Render the verdict** — solved / partial / didn't, tied explicitly to the bar and the
   value.
5. **Diagnose** — briefly, why: did it solve the pain, miss the pain, or solve a different
   thing? Pull on `evidence_sources` if behavior contradicts the headline number.
6. **Produce the next Intent input** — the next problem worth starting (a fresh pain to take
   to `prd-to-ia` / `user-journey-mapping`), or an explicit "stop investing here."

## Output format

Produce a single markdown readout:

- **Pre-registered bar** — the metric and target set before launch.
- **Measured value** — the actual post-launch number, with where it came from.
- **Verdict** — solved / partial / didn't, against the bar. One line, no hedging.
- **Why** — short diagnosis: did it address the pain, and what the number does and doesn't say.
- **Next Intent input** — the next problem worth starting, framed as a Gate-1 prompt, OR an
  explicit "stop investing here, because…". This is the loop-back; it is never empty.
- **Decisions you should check** — assumptions made, and any gap between what was measured and
  what the bar actually needed.

## Quality bar (self-check)

Before handing off, confirm:

- The verdict cites a pre-registered bar and a measured number — not one without the other.
- You did not score against any criterion invented after launch.
- "Not yet measurable" is used honestly when the number isn't in hand — no verdict faked from
  vibes.
- The events the metric relies on were verified as real and emitted, not assumed.
- The next Intent input is concrete enough to actually start (or stop) on — the loop closes.

## Handoff → next gate

This readout closes the spine and reopens it. Its verdict is the Value gate's real answer, and
its **next Intent input loops back to `prd-to-ia` / `user-journey-mapping`** — the next pain
worth starting, or a decision to stop. Intent → Decision → Value → Intent: the loop the README
promises, finally made real.
