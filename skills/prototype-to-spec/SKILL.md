---
name: prototype-to-spec
description: Use when turning a chosen prototype into a buildable spec for engineering handoff. Triggers on a prototype link, file, or description plus a request for a spec or handoff. No validation signal, no spec — the only exception is an explicit owned bet (named owner, declared absence of evidence, reason, review date), which produces a spec with a Bet Record instead of a Validation Record.
---

# Prototype to Spec

A prototype earns a spec. This skill enforces the earning.

## The gate, before any spec

Ask for the validation signal: the evidence that this prototype, among the directions explored, deserves to be built. Acceptable signals: usability findings, behavioral data from a prototype test, or measured performance against criteria the team set before generating. Not acceptable: "the stakeholder liked it," "it was the best looking one," or no answer.

If there is no signal, stop. Do not write the spec. Instead, return the smallest test that would generate a signal — `validation-plan` designs it: who to put the prototype in front of, what to ask or measure, and what result would justify the build. That answer is the skill doing its job, not the skill failing.

**The one exception: an owned bet.** Sometimes the build proceeds without evidence on purpose — a contract commitment, a compliance deadline, a strategic call. That is legitimate only when someone owns it explicitly: a named human with the authority, an acknowledgment that no validation signal exists, the reason, and a review date with the evidence that will judge the bet (see the bet block in [templates/work-ledger.schema.md](../../templates/work-ledger.schema.md)). Given all four, write the spec — and the Validation Record becomes a **Bet Record** stating plainly that there is no validation signal, quoting the bet verbatim, and carrying the review date forward so `outcome-readout` scores the bet on its own terms. What never qualifies as a bet: enthusiasm, seniority, or urgency. "The VP loved it" claims merit and stays refused; a bet says "we know we have no evidence, and here is who owns that." If someone wants the bet path, name the four fields they must supply — do not fill any of them in yourself.

## When the gate passes, write the spec

Include: flows and screens, all states (empty, loading, error, edge), components mapped to the design system by name, content and data requirements, and the analytics events that must ship with the build so the team can answer Gate 3 after launch: did it solve the pain and move the needle.

If a `design-os.profile.yaml` is present, take the design-system reference and analytics event names from it instead of re-asking (see [templates/project-profile.schema.md](../../templates/project-profile.schema.md)). The validation signal is never a profile field, so the gate above still stands. Take the stated accessibility and support bars from `standards:` for the spec's states and components, when present.

## Always include a Validation Record section

Quote the evidence that earned the build: what was tested, with whom, what was found. The proof travels with the work. Six months from now, when someone asks why this was built, the spec answers.

If a `design-os.work/<slug>.yaml` ledger is present, record the validation signal and a pointer to this Validation Record under `value.validation` — the quoted evidence, never a `signal: confirmed` — so the readout reads the same proof after ship (see [templates/work-ledger.schema.md](../../templates/work-ledger.schema.md)). No ledger changes nothing about the spec above.

## Quality bar

A spec without analytics events is incomplete, because it builds the feature and forgets to build the proof.
