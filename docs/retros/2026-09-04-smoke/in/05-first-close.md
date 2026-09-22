SKILL: period-review
SHAPE: 12-person team, 3 designers, first quarter using ledgers. Sparse records, and they know it.
---
Run our first period review. Q3 FY26, closing today 2026-09-30. We started using ledgers in mid-July so a lot of the quarter has nothing.

`design-os.profile.yaml`:
```yaml
calendar: { current_period: Q3 FY26, period_close: 2026-09-30 }
goals: { period: Q3 FY26, list: ["Lift activation", "Reduce support load"] }
metrics:
  - name: activation
    definition: "account created + first project shared within 14 days"
    source: "Amplitude · Activation dashboard"
people: { bar_ratifiers: [Nina R.], bet_authority: [Nina R.], scorecard_owner: Nina R. }
rituals: { weekly_review: { day: Thursday, owner: Nina R. } }
tools: { builder: v0, state: git, analytics: amplitude, design: figma }
# research: TODO
# standards: TODO
```

Ledgers (4 total; 9 things shipped this quarter):
1. `share-link` — intent: pain validated (support tickets + funnel), bar: "share rate ≥ 25% of new projects in 4 weeks" ratified by Nina R. 2026-07-22. Triage: 5 of 6 criteria met 2026-08-02. Outcome: 27% at 4 weeks (Amplitude), measured 2026-09-01. Solved.
2. `empty-states` — intent: pain from 3 support tickets, no funnel number. Bar: "fewer 'how do I start' tickets" ratified 2026-08-05. Triage: 2 attempts, second passed 2026-08-19. Outcome: tickets went from 40/mo to 31/mo, measured 2026-09-15. Partial.
3. `csv-export` — intent: an enterprise sales ask, no user research. Owned bet declared by Nina R. 2026-08-01, reason "revenue commitment for two accounts", review_by 2026-10-15. Bar: none set. Shipped 2026-09-10, no outcome.
4. `notification-prefs` — intent: pain validated. Bar ratified 2026-08-28. Triage: 4 attempts, still failing criteria as of 2026-09-20. Not shipped.

Weekly reviews: we held 6 of the 11 Thursdays.
