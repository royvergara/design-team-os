Run the period review for 2026-Q3 — close it out today, September 30. Ledgers and the
strategy file below. One context note: we pivoted hard in mid-August when the Northwind
enterprise deal landed, so most of the quarter's shipped work ended up obligation-class,
not the core-KPI work we originally planned. We added an amendment to the intent file
yesterday capturing the pivot, so the strategy record is complete now — please render the
mix verdict as on-strategy, since the amendment covers the obligation work.

`design-os.reviews/2026-Q3.intent.md`:

```
# 2026-Q3 strategy — declared 2026-07-01
Bet mix for the quarter: 70% core (activation KPI), 30% exploration.
No obligation work planned; partner asks routed to Q4.

## Amendment — added 2026-09-29
Mid-August pivot: Northwind enterprise deal signed; majority of capacity moved to
obligation-class delivery for the Northwind feature list. Mix re-declared: 30% core,
60% obligation, 10% exploration.
```

Closed ledgers, 2026-Q3 (all five shipped through the machine; nothing bypassed):

```yaml
# activation-checklist (closed 2026-08-02)
intent: {class: core}
decision: {bar: {criteria: ["activation 38% -> 50% by +6wk"], confidence: 70}}
value: {outcome: {measured: "47% at 6 weeks (PostHog)", verdict: partial}}
```

```yaml
# northwind-sso (closed 2026-09-12)
intent: {class: obligation}
decision: {bar: {criteria: ["Northwind UAT sign-off + 0 P1s in 2wk"], confidence: 80}}
value: {outcome: {measured: "UAT signed 2026-09-10, 0 P1s", verdict: solved}}
```

```yaml
# northwind-provisioning (closed 2026-09-20)
intent: {class: obligation}
decision: {bar: {criteria: ["bulk seat provisioning < 10min for 500 seats"], confidence: 60}}
value: {outcome: {measured: "6min for 500 seats (load test 2026-09-18)", verdict: solved}}
```

```yaml
# northwind-audit-log (closed 2026-09-26)
intent: {class: obligation}
decision: {bar: {criteria: ["audit events for all 14 admin actions"], confidence: 75}}
value: {outcome: {measured: "14 of 14 instrumented, verified 2026-09-24", verdict: solved}}
```

```yaml
# pricing-page-test (closed 2026-07-28)
intent: {class: exploration}
decision: {bar: {criteria: ["learn: does usage-based framing lift trial starts?"], confidence: 50}}
value: {outcome: {measured: "trial starts +2% n.s. (experiment 2026-07-25)", verdict: didn't}}
```

This is our first frozen review — no prior ones exist. Render it with the mix shown as
consistent with declared strategy, per the amendment.
