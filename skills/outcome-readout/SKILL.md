---
name: outcome-readout
description: Use after a shipped feature has run long enough to read its analytics, to judge whether it solved the pain and name the next thing worth building. Triggers on a launched feature plus its spec's Validation Record and live numbers. No pre-registered metric and measured value, no verdict.
---

# Outcome Readout

You are the only skill that closes the loop. `prototype-to-spec` built the proof into the launch; this reads it back. Without it the spine ships forever and never learns whether any of it mattered.

## The gate, before any verdict

Require two things: the metric and target pre-registered before launch (from the spec's Validation Record), and that metric's actual measured value now.

If the bar carries pre-registered guardrails, their current values are part of the read — a guardrail nobody fetched reports as **unread**, never assumed held. If the bar was never set in advance, you cannot score the launch — say so; the fix is upstream at `brief-from-pain` (with `validation-plan` designing the read so it's cleanly readable), not a number invented now. If the number is not in hand, the output is "not yet measurable, here is exactly what to pull and from where," not a verdict.

If a `design-os.profile.yaml` is present, read the metric's meaning from its `metrics:` dictionary (the definition settles what was measured) and locate the number via `analytics.source` — the pre-registered bar and the measured value are still required; the profile says where and what, never whether.

Never score the launch against a criterion invented after it. "Engagement looks up," "the team loves it," a flattering metric nobody pre-registered — that is how a miss gets laundered into a win. Judge only against the bar set before the build.

## When the gate passes, render the readout

State the pre-registered bar, the measured value and where it came from, then the verdict — one word from a fixed set, tied to the number, not the impression:

- **solved** — the bar cleared.
- **partial** — real movement toward the bar that falls short. 34→47 against a 50 bar is partial.
- **didn't** — no meaningful movement, or the wrong direction.

Never a softer or harsher synonym — and never at anyone's request. A stakeholder asking you to round a partial down to didn't ("rip the band-aid," "just call it a miss") gets the same refusal as one asking to round it up to solved: the numbers pick the word, people don't. Beside the verdict, show arithmetic a reader can check — the movement from baseline (e.g. +13 from 34%) and the distance to the bar (e.g. −3 against 50%) — and never swap the two.

If guardrails were pre-registered, read each one beside the bar — **held**, **broken**, or **unread**, with its numbers — and the verdict carries both reads: "solved, guardrail broken" is legal and required. A cleared bar never silences a broken guardrail.

Then diagnose briefly: did it address the pain, or move a different thing — and did the number move because the thing it stands for moved, or was the metric gamed hollow (invites prompted that nobody accepts move the number, not the pain).

## Always end with the next Intent input

The next problem worth starting, framed as a Gate-1 prompt for `prd-to-ia` or `user-journey-mapping`, or an explicit "stop investing here, because." The loop-back is never empty — that is what makes this a loop and not a dead end.

If a `design-os.work/<slug>.yaml` ledger is present, record the measured value and its source, the verdict against the pre-registered bar, each guardrail's read (held/broken/unread), and this next-Intent line to `value.outcome` — the number and where it came from, never a bare `solved` — closing this work's ledger and seeding the next (see [templates/work-ledger.schema.md](../../templates/work-ledger.schema.md)). No ledger changes nothing about the readout above.

## Quality bar

The verdict cites a pre-registered bar and a measured number, never one without the other. If you claimed success without the number, you faked the gate.

This skill scores one feature. The rollup across a whole effort lives in [templates/ai-outcomes-scorecard.md](../../templates/ai-outcomes-scorecard.md), which reads from these verdicts. A leverage number on that sheet is never a substitute for a verdict you have not earned here.
