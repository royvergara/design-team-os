---
name: prototype-to-spec
description: Use when turning a chosen prototype into a buildable spec for engineering handoff. Triggers on a prototype link, file, or description plus a request for a spec or handoff. No validation signal, no spec.
---

# Prototype to Spec

A prototype earns a spec. This skill enforces the earning.

## The gate, before any spec

Ask for the validation signal: the evidence that this prototype, among the directions explored, deserves to be built. Acceptable signals: usability findings, behavioral data from a prototype test, or measured performance against criteria the team set before generating. Not acceptable: "the stakeholder liked it," "it was the best looking one," or no answer.

If there is no signal, stop. Do not write the spec. Instead, return the smallest test that would generate a signal: who to put the prototype in front of, what to ask or measure, and what result would justify the build. That answer is the skill doing its job, not the skill failing.

## When the gate passes, write the spec

Include: flows and screens, all states (empty, loading, error, edge), components mapped to the design system by name, content and data requirements, and the analytics events that must ship with the build so the team can answer Gate 3 after launch: did it solve the pain and move the needle.

## Always include a Validation Record section

Quote the evidence that earned the build: what was tested, with whom, what was found. The proof travels with the work. Six months from now, when someone asks why this was built, the spec answers.

## Quality bar

A spec without analytics events is incomplete, because it builds the feature and forgets to build the proof.
