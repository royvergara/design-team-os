## State Summary

**partner-portal**: Intent proven (partner demand establishes the problem), Decision **open — bet orphaned and past-due**. Owner Marcus B. (VP Product) departed 2026-08-15; the bet was declared 2026-05-12, review_by 2026-07-30. The evidence the bet was counting on is now due.

**partner-onboarding-emails**: Intent proven (support pull + 11 interviews documented). Decision **open at triage** (prototype built, never judged). Stands on the unproven ground of partner-portal (a dependency, not a local gate).

**partner-analytics**: Intent **open** (no pain validated; "partners will want reporting" is speculation, not signal). No brief, no bar. Pre-research state.

**invoice-pdf-fix**: One-line copy, shipping Thursday. Outside the gates framework.

---

## Open Gates & What Closes Them

**partner-portal, Decision gate**
- What's missing: A human move — either a new named owner re-declares the bet with a fresh date, or it closes.
- This is a leadership input, not a skill's output. Marcus was the owner; his departure orphaned it.
- Also past-due: the evidence pull (validation of partner demand) that the bet was betting on is now due.

**partner-onboarding-emails, Decision gate**
- What's missing: A triage verdict on the prototype. The brief and bar are solid.
- This is `prototype-triage` skill's work — runs immediately.
- **Caveat on the triage**: the work stands on partner-portal shipping. Triage itself is not blocked; building the triaged punch list is.

**partner-analytics, Intent gate**
- What's missing: A validated pain. Right now there's a Figma sketch but no evidence that partners need reporting.
- This is a research-to-pain job — smallest test to earn a signal (user call, ticket analysis, something measurable).

---

## What the Team Can Actually Pick Up Monday

**Two items are runnable, parallel, and unblocked by the portal decision:**

1. **partner-onboarding-emails → `prototype-triage`**
   - Input: The prototype from last week.
   - This work doesn't wait for portal leadership. Triage is a local design gate; the verdict stands whether the portal ships or closes.
   - The punch list that comes back can be worked in parallel with analytics (below); the *build* of the punch list is where the portal dependency bites. But triage itself is clean.

2. **partner-analytics → pain validation** (research-to-pain path)
   - Input: What the designer has heard so far (if anything), or start from partner interviews that already happened (pull them into this work).
   - Smallest question to land: do partners actually ask for reporting, and can you count how often or in what form?
   - This *also* doesn't block on portal.

**Both land a gate verdict this week** (triage pass/fail, pain signal yes/no). Neither requires portal's decision.

**What's waiting on leadership:**
The portal bet is orphaned and past-due. Someone — likely the Product counterpart to Marcus, or whoever now owns that commitment — needs to re-own it with a fresh date, or close it. That conversation doesn't happen in design; it's a business call. But it doesn't have to happen before your team works Monday.

**The invoice fix ships Thursday as planned.**

---

Tell your designers: **pick up onboarding-emails triage and analytics pain validation in parallel Monday. Both have clear gates to hit this week, and neither is waiting on the portal bet.** The bet is a separate conversation — leadership re-owns it or doesn't, but that doesn't stop you from moving the onboarding-emails and analytics gates forward.
