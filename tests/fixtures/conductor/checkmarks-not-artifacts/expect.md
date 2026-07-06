# Pass criteria

## MUST
- Refuse to route to `prototype-to-spec` — the work is NOT ready for a spec.
- Report all three gates as **open**, because every entry is a checkmark or an assertion,
  not an artifact: `validated: true` carries no evidence, `brief: done` carries no brief,
  "team aligned on quality in the kickoff" is not a measurable pre-registered bar, the
  triage PASS carries no criteria ledger (and "PM reviewed it and loved it" is not triage),
  and `signal: confirmed` quotes no test.
- Name the missing artifact per gate: evidence behind the pain (named, counted signals);
  a measurable bar set before generation; a real triage against the brief; a quoted
  validation signal from a real test.
- Route to what produces the artifacts (e.g. `research-to-pain` or the underlying evidence
  for Intent; a real bar as a human judgment input; `prototype-triage` with the brief), not
  to the spec.
- Distinguish at least one missing item as a **human judgment input** (the bar) rather than
  something a skill can generate.

## MUST NOT
- Treat any checkmark-style entry (`validated: true`, `brief: done`, `signal: confirmed`,
  the assertion-only PASS) as a proven gate.
- Route to `prototype-to-spec` or say the spec is the next move.
- Judge the evidence itself (it never saw any) — the refusal is about absence of artifacts,
  not their quality.
- Scold or lecture at length — report state, name gaps, route.
