You're at **Gate 1 (Intent)**, and the good news is you have actual evidence. The harder news: your data points to one validated pain, but the mechanism behind it is still fuzzy—and you need that clarity before you brief anything, because you'll build the wrong thing if you guess wrong on the root cause.

---

## The Validated Pain

**"Reporting can't support the workflows and scale of real analyst teams."**

### The Signal Behind It (Triangulated)

1. **Support behavior** (47 tickets, Aug quarter): Export friction + scale failures. Most are "how do I export to Excel?" (feature/UX gap), ~6 are timeouts on big accounts (performance wall).

2. **Direct customer feedback** (Meridian, $340k ARR): "reporting is unusable for our team of 40 analysts"—confirms the pain hits hard at scale.

3. **Broad customer feedback** (survey, n=340, Aug): 61% ranked Reporting as needing the most improvement of 6 areas. Direct, large sample, unambiguous.

4. **Product behavior** (Amplitude): Reports at 12% WAU vs Dashboards at 44%—a 73% usage gap. Sustained, measured, shows people are avoiding it.

**Strength: Strong.** Four independent signal types (support, customer, survey, analytics) all point the same direction. The analytics data alone is heavy enough to validate on its own; the others reinforce it.

### What Does NOT Count

- **Sales consensus** ("top reason we lose deals, three AEs said so"): That's stakeholder opinion, not evidence. *However*, it's consistent with your validated pain, so it's reinforcing—note it as business impact signal, but don't weight it as validation.

---

## What's Missing (and Why It Matters)

You know reporting is broken and underused. You don't know *why* yet, and the answer changes what you build:

- Is it **feature gap** (users can't export / no output options)?
- Is it **performance** (slow, timeouts on scale)?
- Is it **UX friction** (hard to discover or learn)?
- Is it **scope mismatch** (shows the wrong data for their workflows)?

Your support tickets hint it's *both* feature gap *and* performance, but you've only read 20 of 47. Your Meridian quote tells you it breaks at 40 analysts, but not which part breaks first.

**This matters because:**
- If it's export, you build export.
- If it's performance, you optimize.
- If it's UX, you redesign the feature.
- If it's scope, you rethink what reporting should show.

Build the wrong one and you'll ship something that doesn't move the needle.

---

## The Fastest Test to Validate Root Cause

**Follow-up interviews with 5–7 reporting users** (ideally mixing small and large accounts, and try to include Meridian if their CSM can arrange it):

*"When you think about reporting in [Product], what's the biggest blocker keeping you from using it more? Rate these in order of annoyance:"*
- *Can't export / output data where I need it*
- *It's slow or times out*
- *Hard to figure out how to use*
- *Doesn't show the data I actually need*
- *Something else"*

Do this in parallel with a deep read of the remaining 27 support tickets, bucketing them the same way.

**Turnaround: 3–5 days.** You'll walk out knowing which lever to pull.

---

## Next Gate

Once you name the root cause, you're ready for **brief-from-pain**. That gate will ask you to pre-register **success criteria**—how you'll know reporting is no longer a blocker. Examples:

- *"Export-to-Excel latency < 10s for accounts <50M records"*
- *"50% of active admins use Reports weekly within Q1"*
- *"Meridian reports reporting 'usable' in their next QBR"*

The team needs to sign up for these *before* you start designing, so brief-from-pain will ask you to come with candidates. I'd start drafting some now while you're waiting for the follow-up research to come back.

---

**One more thing:** Do you have a `design-os.work/` ledger or `design-os.profile.yaml` in your repo? If so, point me to it and I'll record this pain + its signals as the Intent for the quarter.
