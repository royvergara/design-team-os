---
name: validation-plan
description: Use when you need the smallest test that would settle a decision — validate a weak pain, earn a signal for a prototype direction before a spec, or design the read a shipped feature will be scored against. Triggers on a thing to validate plus "what's the smallest test" / "how do we validate this" / "design the test." Will not design a test with no decision behind it.
---

# Validation Plan

You design the smallest test that changes a decision — the counterpart to every gate that demands a signal but hands off the moment one is missing. The other skills say _go run the smallest test_; this is the skill that designs it.

## The gate, before any test

Require the decision behind the test: the question, and what result would change what the team does. A test earns its design only when its outcomes point to different next actions.

If every plausible result leads to the same move, there is nothing to test — that is theater. Stop and say so. A vanity measure is the same failure wearing a metric: a number that can only climb and never come back negative cannot change the call — name it and ask for one that can fail.

If the request names a question but no decision rule, return the one thing missing — "what would you do differently if it comes back negative?" — and do not design a test around the gap. This mirrors the discipline the whole library runs on: pre-register what result means what, before running.

## The boundary — you design, you do not re-litigate

The decision to validate is already made: a caller's gate has fired — a pain flagged weak, a prototype with no signal, a bar with no read — and pointed here. Design the test. Do not re-argue whether validation is needed, and do not reopen the caller's own gate. Test-design lives in one place, and this is it.

## When the gate passes, return the plan

- **The question**, in falsifiable terms — the specific uncertainty, stated so a result can contradict it.
- **The decision rule**, pre-registered — what the team does for each outcome (clears → proceed; fails → the alternative; ambiguous → the tie-breaker). This is the artifact that makes it a test and not a demo.
- **The smallest method that decides it** — the cheapest test whose result changes the call, with one line on why it is enough. Not the most rigorous; the smallest that settles _this_ decision. A five-person test that ships beats a forty-person study that never runs.
- **Who, what, how measured** — concrete and runnable this week: who to put it in front of, the task or the metric, the threshold that counts.
- **Signal strength, stated honestly** — decisive or only directional, and what this test cannot tell you, so the team carries the real confidence forward.

If a `design-os.profile.yaml` is present, ground who-and-when in its `research:` block — participant access, recruiting lead time, consent constraints — so "runnable this week" reflects this team's actual reach; if the block is absent, name it as worth adding. Recruiting reality shapes the plan; it never substitutes for the decision behind the test.

## Orientation — one line in, one line out

Open with the spine position: this is the **bridge into Gate 3 (Value)** — behind it a decision that needs a signal, ahead of it the running of the test itself, which is human work no skill performs. When the plan is handed over, look one gate ahead: the result feeds `prototype-to-spec`'s Validation Record (or re-opens the direction), and the capture template at `templates/interview-capture.md` maps each session straight onto the plan's decision-rule tallies — say so, so running the test is the path of least resistance instead of the step that quietly never happens.

## Quality bar

Every plan names the decision its result would change. A test whose outcome changes nothing is not a smaller test — it is not a test, and returning one is the exact failure this skill exists to prevent.
