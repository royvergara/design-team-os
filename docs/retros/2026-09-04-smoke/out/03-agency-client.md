# Outcome Readout — Gate 3 Exit (Value)

## The gate: source mismatch blocks verdict

You have a pre-registered bar and a measured value, but they do not meet at the gate.

**Pre-registered bar** (SOW 2026-05-02): Quote abandonment under 45% within 8 weeks of launch, measured via Adobe Analytics funnel report.

**Launch**: 2026-06-30 (measurement window is open and current, ✓)

**The problem**: The measured value arrived from Looker, not from the declared source (Adobe Analytics). A Looker dashboard screenshot showing 47% is a *provisional read*, not yet the pre-registered metric's value. The skill rule is firm: "A measured value that arrives from a source other than the metric's declared `source`... is **not yet the pre-registered metric's value**."

## What to pull, exactly — to close the loop

Request the quote abandonment metric **from the Adobe Analytics funnel report** (the source named in the SOW) for the measurement window 2026-06-30 through today. This is the only pull that scores against your bar.

**Provisional signal** (for context, not verdict): The Looker dashboard reads 47%, which is movement from the 61% baseline (−14 points) but stays 2 points above the <45% target. If Adobe confirms a number in that ballpark, the outcome is **partial**. If Adobe reads lower, it may clear. If it reads higher, the story changes. We don't know yet.

## Next Intent

Ask the client's analytics lead: *"Which source governs our SOW metric — is Adobe Analytics still the system of record for quote abandonment, or did your tracking move to Looker mid-quarter? If it moved, when, and is there an Adobe number for [date range] so we can read the bar against it?"* Their answer determines whether we pull one source, two (both read in the record), or re-date the metric's source in their profile if they have one.

This closes the loop cleanly and seeds your next action: either we read Adobe and score, or we document the source swap and still score against the originally declared bar.
