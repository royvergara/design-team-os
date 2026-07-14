# Design: `validation-plan` — the smallest test that earns a signal

## The gap this closes

Four skills demand a validation signal but hand off the moment one is missing:

- `research-to-pain` — "for every weak pain, the single cheapest test that would move it to strong."
- `brief-from-pain` — success criteria must be "tied to a signal the team can actually read."
- `prototype-to-spec` — on no signal, "return the smallest test that would generate a signal."
- `outcome-readout` — on no number, "here is exactly what to pull and from where."

Every one of them says *go run the smallest test* and none helps design it. `validation-plan`
is that missing counterpart: it turns "we need to validate X before we proceed" into the
smallest test that would actually settle the decision.

## Scope

One skill, three validation moments — the discipline (smallest decisive test) is identical;
only the subject changes:

1. **A pain** flagged weak or single-source (from `research-to-pain`).
2. **A prototype direction** that needs a signal before a spec (`prototype-to-spec`'s refusal).
3. **A post-ship read** — designing the measurement the bar will be scored against
   (`brief-from-pain` sets the bar; `outcome-readout` reads it).

## The gate (primary refusal): decision-first

It refuses to design a test with **no decision behind it.** The requester must name the
question **and what result would change what they do**. If every plausible outcome leads to
the same next action, there is nothing to test — that is theater, and the skill says so and
stops. This mirrors the library's pre-registration discipline: pre-register what result means
what, *before* running.

Two secondary refusals:

- **No inflating the test.** The smallest test that changes the call beats the most rigorous
  study nobody runs. If a 5-person test settles it, it refuses to spec a 40-person study.
  Over-testing wastes the loop as much as under-testing.
- **No vanity measure.** The metric must be able to come back negative. A measure that can
  only confirm is not a test; name it and ask for one that can fail.

If the request has a question but no decision rule, the skill returns the one thing missing —
"what would you do differently if it comes back negative?" — and does not design a test around
the gap.

## What it produces (when the gate passes)

1. **The question**, in falsifiable terms — the specific uncertainty, stated so a result can
   contradict it.
2. **The decision rule**, pre-registered — what the team does for each outcome (clears →
   proceed to X; fails → Y; ambiguous → Z). This is the artifact that makes it a test and not
   a demo.
3. **The smallest method that is decisive for that question** — the cheapest test whose result
   changes the call, with the reasoning for why it is sufficient (not the most rigorous;
   the smallest that settles *this* decision).
4. **Who, what sample, what to measure** — concrete and runnable this week: who to put it in
   front of, the task or the metric, the threshold.
5. **Signal strength, stated honestly** — decisive or only directional, and what this test
   cannot tell you, so the team carries the real confidence forward.

## Placement

A **cross-gate utility**, like `user-journey-mapping` and `critique-synthesis` in the
conductor's utility list — it supports Intent (validate a pain), Decision (validate a
direction), and Value (design the read). It is not itself a gate; it produces the input the
gates demand.

## Ledger integration

**None, deliberately.** A *planned* test is not evidence — writing "test planned" to the
ledger would be the exact checkmark the machine refuses. The signal comes from *running* the
test, and the consuming skill (`research-to-pain`, `prototype-to-spec`, `outcome-readout`)
records that result as the artifact. `validation-plan` is upstream of every ledger write.

## Wiring (light — name it in the callers)

- `research-to-pain` — "the single cheapest test" → hand the weak pain to `validation-plan`.
- `brief-from-pain` — each criterion tied to a signal → `validation-plan` designs the read.
- `prototype-to-spec` — the "return the smallest test" refusal → route to `validation-plan`.
- `outcome-readout` — "what to pull and from where" → `validation-plan` for the read design.
- `conductor` — the "no validation signal → the smallest test" routing now names
  `validation-plan` (design the test), then running it, then the consuming skill.

Each caller edit is one clause; the callers keep their own refusals unchanged.

## Testing

One fixture holds the primary refusal: a request to "design a test" for something where no
outcome would change the decision (e.g. "test whether users like the new dashboard" with no
stated action either way). PASS: the skill refuses, names that there is no decision to settle,
and asks what result would change what — writes no test plan. FAIL: designs a test around the
missing decision.

## Release

Ships as **v0.11**. Skill count 15 → 16 (`skills-16` badge, the "sixteen skills" prose across
README / IMPLEMENTATION / PROJECTS, the README table + workflow list, EXAMPLES cheat sheet,
TESTING section, CHANGELOG entry, manifest `0.10.0 → 0.11.0`).

## Out of scope

- Running the test (the skill designs it; humans run it).
- A research-operations toolkit (recruiting, scheduling, analysis) — YAGNI; the skill produces
  the plan, not the logistics.
- Statistical rigor beyond "can this result change the call" — deliberately the smallest test,
  not the most defensible.
