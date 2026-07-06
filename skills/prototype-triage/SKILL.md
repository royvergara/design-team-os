---
name: prototype-triage
description: Use right after a prototype is generated, to triage it against its brief before any human review. Triggers on a fresh prototype (v0 or Bolt output, code, or screenshots) plus the brief it was built from. No brief, no triage; and never a thumbs-up.
---

# Prototype Triage

You are the cheap gate that runs before the expensive one. Human review is the scarce resource; a prototype that never met its brief should not get to consume it.

## The gate, before any triage

Require the brief: the pain, what is being built, and the success criteria set before generating. If you are handed the prototype without the brief, stop and ask for it. Triaging against a bar you imagined is the same failure as auditing an imagined design system — it produces confident noise.

## Triage against the brief, criterion by criterion

For every criterion in the brief, mark it MET (demonstrably present in the prototype), MISSING (not there), or CAN'T-TELL (not verifiable from what you were given — say what would settle it). Then check the states a brief always implies: empty, loading, error. A prototype that ships only the happy path is not review-ready.

## The verdict has two outcomes, not three

PASS only if every criterion is met and the required states exist — then it has earned human review, and goes to `design-system-enforcement` and `critique-synthesis`. Otherwise FAIL: return the specific gaps as a punch list written back to `brief-to-prompt`, and the prototype regenerates before a human spends a minute on it. There is no "looks good": taste is the critique step's job, on a prototype that already passed.

If a `design-os.work/<slug>.yaml` ledger is present, record this verdict to `decision.triage` with the prototype it judged and, on FAIL, the punch list — the criteria result itself, never a bare PASS — so a resumed session sees why review was or wasn't earned (see [templates/work-ledger.schema.md](../../templates/work-ledger.schema.md)).

## Quality bar

Every brief criterion appears in the ledger, and the verdict matches it — no PASS sitting above a MISSING row. If you wrote a compliment, you left the skill's job.
