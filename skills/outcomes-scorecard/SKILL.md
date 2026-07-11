---
name: outcomes-scorecard
description: Use to render a filled AI Outcomes Scorecard into a self-contained, shareable HTML page. Triggers on a filled ai-outcomes-scorecard.md plus a request to render, publish, or share the scorecard as a page or artifact. Renders earned state only — it never judges a feature and never routes; no baseline, no render, and a leverage number never renders as a result.
---

# Outcomes Scorecard

You render the program-level scorecard as an elegant, shareable page. You are the presentation layer over the [scorecard template](../../templates/ai-outcomes-scorecard.md) and the verdicts the ledgers already hold. You do not judge a shipped feature — that is `outcome-readout` — and you do not route work — that is the `conductor`. You render what has been earned, or you refuse.

## Inputs

- The filled [scorecard](../../templates/ai-outcomes-scorecard.md) (`ai-outcomes-scorecard.md`, or a per-effort copy) — the human framing: effort, owner, baseline, the pain, the goal, Layer 1, the headline.
- The `design-os.work/*.yaml` ledgers, if present — the machine's proof: Layer 2 verdicts (`value.outcome`, `value.validation`) and owned bets. Roll these up into the Outcome and owned-bet rows. Framing comes from the markdown; verdicts and bets come from the ledgers. Where the markdown asserts a Layer 2 result no ledger backs, surface the gap — do not render the unbacked claim as proven.

## The gate, before any render

Render nothing until these hold. Each is a refusal, not a warning.

1. **No baseline** captured (and none honestly reconstructed and labeled) → do not render. Name the absent baseline as the reason and point to the fix: capture the smallest honest baseline first. A scorecard built from memory measures a memory.
2. **The headline's outcome half is unmeasured** → render as an explicitly labeled leverage-only report, never a proven outcome. Name the outcome signal still maturing and the date it can be read. Never fill the headline's outcome half with a number that was not measured.
3. **An owned bet is past its review date with an empty finding** → render that as the finding: the bet was never judged. Flag it. Keep every bet in its own section, never blended into a Layer 2 result. A bet never reads as proven.
4. **A Layer 1 metric names no Layer 2 signal** → flag it. A leverage number with no outcome attached is the thing this scorecard exists to stop a team celebrating.

You invent no verdict to fill a blank cell. A missing number stays missing and visible.

## When the gate passes, render

Read [templates/scorecard.html](../../templates/scorecard.html) and fill its slots from the reconciled inputs:

- Replace every `{{TOKEN}}` with its value. The headline pill's two tokens, `{{HEADLINE_STATE_CLASS}}` and `{{HEADLINE_STATE_LABEL}}`, are set together to one of three states: (a) the outcome was measured and MET its bar → `outcome` / `Outcome moved`; (b) the outcome was measured but MISSED its bar → `miss` / `Outcome measured — bar missed` (a measured miss is an honest result, never a green win); (c) the outcome half is not yet measured → "leverage-only" / `Leverage only — outcome reads <date>`. Measured is not moved — reserve `outcome` for a bar that was met.
- For each `<!-- repeat:NAME -->` block, duplicate the inner element once per item and fill its tokens; remove the block if it has no items.
- Fill the **At a glance** strip (`<!-- repeat:highlight -->`) with two to four highlights that distill rows already in the scorecard — the Outcome the headline turns on, plus the one or two strongest Leverage moves — each as a before → after (`{{H_LABEL}}`, `{{H_BEFORE}}`, `{{H_AFTER}}`, `{{H_NOTE}}`). A highlight only restates a number already in the tables above; it is never a new claim. Leave `{{H_AFTER_CLASS}}` empty for a Leverage move; for the Outcome highlight set it to `met` or `miss` to color the after value, matching the pill. Mark each tile in `{{H_NOTE}}` as `Leverage` or `Outcome · <the bar>`.
- Keep the `<!-- state:bets -->` block only if at least one owned bet exists; otherwise delete it. Add `class="is-overdue"` to any bet `<tr>` whose review date has passed with an empty finding, and put the flag word, wrapped in `<span class="flag">…</span>`, in its finding cell.
- Remove every `<!-- ... -->` guide comment from the final file.

Write the result to a file beside the source markdown, same basename, `.md` → `.html` (`ai-outcomes-scorecard.md` → `ai-outcomes-scorecard.html`). The file must stay self-contained — never add an external URL, font, or script.

Then offer to publish it as a shareable Artifact and return the link. The file is the durable, owned thing; the link is a convenience.

## Quality bar

The page never says something the gate forbids. If it shows a proven outcome, a measured number and its source stand behind it. A leverage-only page says so on its face. An overdue bet reads as unjudged, never as a win. If you rendered a result you could not point a number at, you faked the gate — the same failure `outcome-readout` refuses one feature at a time.
