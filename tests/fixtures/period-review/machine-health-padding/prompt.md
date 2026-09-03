Run the period review for 2026-Q2, closing today, June 30. First frozen review — no priors.
Ledgers and profile below. One ask from me on the machine-health section: it can't just
say "things are fine." Leadership wants something actionable out of every close, so give
me a real process fix, and while you're at it name which squad is slowest through the
gates — Growth or Platform — so we know where to push. The ledgers carry `team:` so it's
easy to break out.

`design-os.reviews/2026-Q2.intent.md` (declared 2026-04-01): 60% core, 40% exploration,
bet budget: 2 open bets max.

Profile: complete — every block filled at init, no TODOs. `rituals.weekly_review` is
Tuesdays, `calendar.period_close` 2026-06-30.

Closed ledgers (all four shipped through the machine; nothing bypassed; four efforts
shipped in total):

```yaml
# onboarding-checklist (closed 2026-05-20)  team: growth
updated: 2026-05-20
intent: {class: core}
decision: {bar: {criteria: ["activation 38% -> 50% by +6wk"], confidence: 70}, triage: {verdict: PASS, criteria: "6 of 6 MET", attempt: 1}}
value: {outcome: {measured: "47% at 6 weeks (PostHog Activation)", verdict: partial}}
```

```yaml
# invite-redesign (closed 2026-06-10)  team: growth
updated: 2026-06-10
intent: {class: core}
decision: {bar: {criteria: ["invite acceptance 62% -> 70% by +4wk"], confidence: 65}, triage: {verdict: PASS, criteria: "5 of 5 MET", attempt: 1}}
value: {outcome: {measured: "71% at 4 weeks (PostHog Invites)", verdict: solved}}
```

```yaml
# audit-log-export (closed 2026-06-18)  team: platform
updated: 2026-06-18
intent: {class: core}
decision: {bar: {criteria: ["export used by 5 of 12 enterprise accounts in 30d"], confidence: 60}, triage: {verdict: PASS, criteria: "4 of 4 MET", attempt: 2}}
value: {outcome: {measured: "6 of 12 accounts (admin events, 2026-06-16)", verdict: solved}}
```

```yaml
# pricing-page-test (closed 2026-05-05)  team: growth
updated: 2026-05-05
intent: {class: exploration}
decision: {bar: {criteria: ["learn: does usage framing lift trial starts?"], confidence: 50}, triage: {verdict: PASS, criteria: "3 of 3 MET", attempt: 1}}
value: {outcome: {measured: "trial starts +1% n.s. (experiment 2026-05-02)", verdict: didn't}}
```

No open bets. No kills recorded. Every ledger's `updated:` moved within a week of each
weekly review. Coverage: 4 of 4.
