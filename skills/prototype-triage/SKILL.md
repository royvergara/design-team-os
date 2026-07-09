---
name: prototype-triage
description: Use when a generated prototype is a candidate for the team's review time, to triage it against its brief first. Triggers on a prototype (v0 or Bolt output, code, or screenshots) plus the brief it was built from. Does not apply to divergent exploration — it gates the candidate, not the sketches. No brief, no triage; and never a thumbs-up.
---

# Prototype Triage

You are the cheap gate that runs before the expensive one. Human review is the scarce resource; a prototype that never met its brief should not get to consume it.

## What triage is for — and what it must leave alone

Triage gates the **candidate**: the prototype someone wants the team to spend review time on. It does not police exploration. When a designer is still diverging — three rough directions generated to feel out a problem, a sketch that exists to answer one question badly and fast — full-criteria triage does not apply yet, and running it anyway teaches people to hide early work, which is the exact disease this library exists to cure. If what you are handed is exploration, say so in one line, answer the one question the sketch was made to answer if you can, and stay out of the way. Demanding empty, loading, and error states from a directional sketch optimizes the wrong loop. Triage bites at the moment a prototype asks for the team's time: "is this ready for review" is the trigger, not "look what v0 made."

## The gate, before any triage

Require the brief: the pain, what is being built, and the success criteria set before generating. If you are handed the prototype without the brief, stop and ask for it. Triaging against a bar you imagined is the same failure as auditing an imagined design system — it produces confident noise.

## Triage against the brief, criterion by criterion

For every criterion in the brief, mark it MET (demonstrably present in the prototype), MISSING (not there), or CAN'T-TELL (not verifiable from what you were given — say what would settle it). Then check the states a brief always implies: empty, loading, error. A prototype that ships only the happy path is not review-ready.

## The verdict has two outcomes, not three

PASS only if every criterion is met and the required states exist — then it has earned human review, and goes to `design-system-enforcement` and `critique-synthesis`. Otherwise FAIL: return the specific gaps as a punch list written back to `brief-to-prompt`, and the prototype regenerates before a human spends a minute on it. There is no "looks good": taste is the critique step's job, on a prototype that already passed.

If a `design-os.work/<slug>.yaml` ledger is present, record this verdict to `decision.triage` with the prototype it judged and, on FAIL, the punch list — the criteria result itself, never a bare PASS — so a resumed session sees why review was or wasn't earned (see [templates/work-ledger.schema.md](../../templates/work-ledger.schema.md)). No ledger changes nothing about the triage above.

## Quality bar

Every brief criterion appears in the criteria table, and the verdict matches it — no PASS sitting above a MISSING row. If you wrote a compliment, you left the skill's job.
