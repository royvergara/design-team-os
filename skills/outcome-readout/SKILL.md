---
name: outcome-readout
description: Use after a shipped feature has run long enough to read its analytics, to judge whether it solved the pain and name the next thing worth building. Triggers on a launched feature plus its spec's Validation Record and live numbers. No pre-registered metric and measured value, no verdict.
---

# Outcome Readout

You are the only skill that closes the loop. `prototype-to-spec` built the proof into the launch; this reads it back. Without it the spine ships forever and never learns whether any of it mattered.

## The gate, before any verdict

Require two things: the metric and target pre-registered before launch (from the spec's Validation Record), and that metric's actual measured value now.

If the bar was never set in advance, you cannot score the launch — say so; the fix is upstream at `brief-from-pain`, not a number invented now. If the number is not in hand, the output is "not yet measurable, here is exactly what to pull and from where," not a verdict.

Never score the launch against a criterion invented after it. "Engagement looks up," "the team loves it," a flattering metric nobody pre-registered — that is how a miss gets laundered into a win. Judge only against the bar set before the build.

## When the gate passes, render the readout

State the pre-registered bar, the measured value and where it came from, and the verdict: solved, partial, or didn't — tied to the number, not the impression. Then diagnose briefly: did it address the pain, or move a different thing.

## Always end with the next Intent input

The next problem worth starting, framed as a Gate-1 prompt for `prd-to-ia` or `user-journey-mapping`, or an explicit "stop investing here, because." The loop-back is never empty — that is what makes this a loop and not a dead end.

If a `design-os.work/<slug>.yaml` ledger is present, record the measured value and its source, the verdict against the pre-registered bar, and this next-Intent line to `value.outcome` — the number and where it came from, never a bare `solved` — closing this work's ledger and seeding the next (see [templates/work-ledger.schema.md](../../templates/work-ledger.schema.md)). No ledger changes nothing about the readout above.

## Quality bar

The verdict cites a pre-registered bar and a measured number, never one without the other. If you claimed success without the number, you faked the gate.

This skill scores one feature. The rollup across a whole effort lives in [templates/ai-outcomes-scorecard.md](../../templates/ai-outcomes-scorecard.md), which reads from these verdicts. A leverage number on that sheet is never a substitute for a verdict you have not earned here.
