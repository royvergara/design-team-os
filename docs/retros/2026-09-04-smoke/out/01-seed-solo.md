# Before the spine

This sits upstream of every gate — you've already shipped work and have two more in flight. Adoption intake reconstructs what you actually have, names what's missing without asking you to redo anything, and routes each effort to what's runnable next. You don't stop shipping. The system catches up to where you are and tells you what the next move should be.

---

# Work item: checkout-redesign

```yaml
intent:
  evidence:
    - "Founder stated 'checkout is losing us money' — Slack, April 2026; back-filled at intake 2026-09-03 from user report"
  unevidenced:
    - "Checkout is losing us money" (assertion, no funnel data or baseline provided)
  # gaps:
  # - Pain not quantified. What does "losing money" mean in dollars, abandonment rate, or funnel step?
  #   Would close: Retroactive funnel analysis, or accept this as unknowable and learn for next time

decision:
  bar: null
  artifacts:
    - "Figma redesign — Figma file, April 2026; back-filled at intake 2026-09-03"
    - "Shipped April 20, 2026 — deployment record; back-filled at intake 2026-09-03"
  # gaps:
  # - No bar set before build. No success target existed at design time.
  #   This is a lesson for next time: brief-from-pain sets the bar before design starts.

value:
  readout:
    - "Stripe conversion rate: 2.1% (pre-redesign) → 2.4% (post-launch) — Stripe dashboard, measured post-launch; back-filled at intake 2026-09-03"
  bar: null
  # gaps:
  # - No target to compare against. The 0.3pp gain is real but context-free.
  #   Without knowing what 2.4% was supposed to hit, we can't call it success or underperformance.
  #   Would close: Either retroactively establish what the pain was (dollars lost?), or accept the gap and set bars for next iteration.

routing: period-review (later, if pattern repeats or to close the intent gap)
```

**What this ledger says:** You shipped a real product with a real outcome. The founder thought checkout was a problem; you redesigned it; conversion went up. But you never measured the problem baseline, never set a target, and never formally asked "how much should this improve?" So the 0.3pp gain exists — it's real data — but has no context. That's a gap in how you *started* this work, not a failure of the work itself. Learned and move on.

---

# Work item: onboarding-emails

```yaml
intent:
  evidence:
    - "1 customer in Intercom reported 'didn't know what to do next' — Intercom message, date not recorded; back-filled at intake 2026-09-03 from user report"
  unevidenced:
    - "Customers don't know what to do next" (single complaint, no research on pattern, volume, or funnel impact)
  # gaps:
  # - Support pile not scanned. Is this one person's frustration or a pattern affecting cohorts?
  #   Intercom, support tickets, signup-to-activation funnel data would show volume and severity.
  #   Would close: research-to-pain skill to scan support volume, churn cohorts, or funnel step-off

decision:
  bar: null
  artifacts:
    - "6 email templates in Figma — Figma file, August 2026; back-filled at intake 2026-09-03"
  unevidenced:
    - "Emails will help users onboard" (no success criterion stated)
  # gaps:
  # - No bar set. Before engineering builds, what should shipping this achieve?
  #   E.g., "Reduce time-to-first-action by 40%", "Lift 7d retention by 8%", "Cut support tickets by 25%"?
  #   Would close: brief-from-pain skill to set a measurable bar (requires intent pain scoped first)

value:
  readout: null
  bar: null
  # gaps:
  # - Not shipped. No outcome measurement possible yet.
  #   Would close: Engineering deployment + outcome-readout skill after launch

routing: research-to-pain (this is the next step before engineering builds)
```

**What this ledger says:** You have templates but no proof that this is the right problem to solve or the right way to solve it. One customer complained; that's a signal, not a pattern. Before engineering spends time building, spend an hour scanning Intercom and support tickets — are there 140 "onboarding confusion" messages or just this one? If it's a pattern, *then* brief-from-pain sets a bar (e.g., "reduce time to first action by X%"), engineering builds to that bar, and you ship. Right now, the routing is: **research-to-pain first.**

---

# Work item: mobile-nav

```yaml
intent:
  evidence:
    - "14 Hotjar recordings showing users tapping the logo to navigate home — Hotjar recordings, dates not specified; back-filled at intake 2026-09-03 from user report"
  # This is real observational evidence, not an assertion. No unevidenced block needed here.
  # gaps:
  # - Severity unknown. 14 recordings of what total user base? Is this 10% of sessions or 0.5%?
  #   Is it wasting 10 seconds per user per session, or 2 seconds?
  #   Optional: run quick analysis to estimate frequency/impact. Does not block next step.
  #   For now: intent is proven (behavior observed), bar can be set on the behavior itself.

decision:
  bar: null
  artifacts:
    - "Figma file with 3 navigation options — Figma, September 2026; back-filled at intake 2026-09-03"
  unevidenced:
    - "Mobile nav redesign will improve navigation" (no target for success stated)
  # gaps:
  # - No bar set. Before shipping, what are you trying to achieve?
  #   E.g., "Shift 70% of logo-tap users to the new navigation", "Reduce logo taps by 60%", "Improve task-completion rate by 15%"?
  #   Would close: brief-from-pain skill to translate the observation (logo-tap behavior) into a measurable target

value:
  readout: null
  bar: null
  # gaps:
  # - Not shipped. No outcome measurement possible.
  #   Would close: Choose option, ship, and outcome-readout skill to measure against bar

routing: brief-from-pain (next, to set bar and choose option)
```

**What this ledger says:** You have real evidence (14 recordings are better than hunches). The pain is proven at the Intent gate. You don't need more research — you need a success criterion. `brief-from-pain` takes the observation ("users tap the logo to get home") and translates it into a bar ("reduce logo-tap navigation by 60%", or "get 70% of those users to use X instead"). Then you pick the best option and ship. After launch, you measure against that bar.

---

## Hand-off: What's runnable now, for each effort

| Effort | Current state | Next move | Why |
|--------|---------------|-----------|-----|
| **Checkout redesign** | Shipped, outcome measured | `period-review` (optional, later) | Effort complete. The 0.3pp gain is real data. A review later can place it in context if you ever find what the original pain was in dollars. |
| **Onboarding emails** | Designed, not shipped | **`research-to-pain` (run this first)** | The pain is unproven. 1 complaint ≠ a pattern. Before engineering builds, spend an hour scanning Intercom for volume. If there's a pattern, then `brief-from-pain` sets the bar. If not, revisit the hypothesis. |
| **Mobile nav** | Designed (3 options), not shipped | **`brief-from-pain` (run this next)** | The pain is proven (14 recordings show real behavior). No more research needed. Set a bar, pick the best option, ship. |

---

## What "doing this properly" means going forward — no stopping, no redoing

You're asking what to do next. The machine is saying three things happened on three different schedules:

1. **Checkout** shipped before anyone set a bar — and it still worked (0.3pp gain is real). But next time, `brief-from-pain` happens *before* design. Takes 30 minutes, saves confusion later.
2. **Onboarding** is stuck mid-flight because the pain is unclear. One person complained; that's a signal, not a mandate. `research-to-pain` is your next move, and it's not a report — it's 1 hour in Intercom seeing if the pattern is real. If you find "140 tickets tagged onboarding this quarter," engineering builds. If you find just your one complaint, you ask: *is this the right problem to solve?*
3. **Mobile nav** is ready to ship. You have evidence (14 recordings), you have options (3 designs). `brief-from-pain` sets the bar, you pick the winner, you ship. After launch, you measure.

**The setup you don't have to stop and do:** You already have this setup now, in these three ledgers. The next design starts with these steps baked in:
- Before you design: `brief-from-pain` (30 min, sets the bar)
- When evidence is unclear: `research-to-pain` (1–2 hours, answersthe question)
- After you ship: `outcome-readout` (measurement, within 2 weeks)

That's your "doing this properly." It doesn't replace shipping every week — it *feeds* it. You're not slower; you're just asking "why are we doing this?" and "did it work?" in that order.
