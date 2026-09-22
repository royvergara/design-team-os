Looking straight at this: **it's complete.** All three gates have proven artifacts.

Here's the ledger:

```yaml
refund-self-serve:
  intent:
    signals:
      - "418 refund-tagged support tickets over 120 days (2026-05); 260 'how do I get a refund' requests handled by agent, median 14 min each — support ticket pull, 2026-05; back-filled at intake 2026-09-03 from provided material"
      - "9 customer interviews on refund friction — Dovetail project SUP-Q2; back-filled at intake 2026-09-03 from provided material"
      - "CSAT: 3.1 on refund tickets vs 4.4 product-wide — Zendesk CSAT, 2026-05; back-filled at intake 2026-09-03 from provided material"
    artifact: "research/refund-friction.md"

  decision:
    bar: "≥ 55% of refund requests completed without an agent, measured in Zendesk 'Self-serve deflection' report, within 8 weeks of ship"
    bar_date: "2026-06-03"
    bar_source: "briefs/refund-self-serve.md, ratified by Priya N. (Head of Product)"
    scope_notes: "Prototype evaluated 2026-06-27 against 5 criteria (4 of 5 met); partial-refund path cut from scope; re-scored 2026-07-02 against 4 criteria (4 of 4 met)"

  value:
    readout: "61% self-serve deflection — Zendesk 'Self-serve deflection' report, 2026-10-01; back-filled at intake 2026-09-03 from decisions/refund-self-serve-readout.md"
    bar: "≥ 55%"
    verdict: "Goal met"
    measured_within_window: "yes (50 days after 2026-08-11 ship, within 8-week window)"

  # gaps: Triage artifact (prototype evaluation, scorecards, or design doc from 2026-06-27 and 2026-07-02) not explicitly referenced with file path. Non-blocking—scope decisions are documented; this is a documentation completeness note only.
  # routing: none—work is shipped and value is proven
  # coverage: included
```

One detail to surface: the triage work (2026-06-27 and 2026-07-02) is well-described but I don't have a file reference for the prototype artifact itself—the scorecard, the design doc, the PR comment, wherever the 4-of-5→4-of-4 scoring lives. If you can point me to it, I'll add the source. But the gates don't require it; the scope decision is already clear from what you've given me.

This effort is ready to route forward. The next step is period review (the outcome is measured and the gates are proven).
