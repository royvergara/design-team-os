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

Read [templates/scorecard.html](../../templates/scorecard.html) and fill it from the reconciled inputs. If a `design-os.profile.yaml` is present, default `{{OWNER}}` from `people.scorecard_owner`, `{{FOLIO_CLASSIFICATION}}` from `reporting.classification`, and `{{FOLIO_PERIOD}}` from `calendar.current_period` — presentation defaults only; no profile field ever supplies a verdict or a number.

**Prefer the deterministic filler over filling token-by-token.** Your job is producing the _data_ — the tokens, repeat items, state flags, and DATA_JSON values the guide below defines; the mechanical fill is a templating job, not a judgment job. Write those values as one JSON file (shape in the header of `${CLAUDE_PLUGIN_ROOT}/scripts/render.mjs`: `tokens`, `repeats`, `states`, `dataJson`) and run `node ${CLAUDE_PLUGIN_ROOT}/scripts/render.mjs ${CLAUDE_PLUGIN_ROOT}/templates/scorecard.html <data.json> <out.html>` — the script and template live in the plugin, your data and output live in the product repo, so use `${CLAUDE_PLUGIN_ROOT}` for the first two and a repo path for the last two (a bare `scripts/`/`templates/` resolves to nothing outside this library). It fills every marker, strips the guide comments, and **fails loudly on any missing token** instead of leaving a silent blank. Fill by hand only when Node isn't available, following the token guide below either way; every rule in it (what each token means, what the gate forbids) governs the data you write, not just a hand-fill.

- Replace every text token: folio `{{FOLIO_CLASSIFICATION}}` / `{{FOLIO_PERIOD}}` (both optional — default "Internal" and the known period), `{{EFFORT_NAME}}` `{{OWNER}}` `{{GENERATED_DATE}}`, `{{CLASS_CHIP}}` from the ledger's intent class ("Unclassified" if absent), `{{HEADLINE_MAIN}}` and `{{HEADLINE_MISS_PHRASE}}` (the featured headline flows and wraps on its own — no manual `<br>` needed), `{{DECK}}`, `{{HERO_LABEL}}` (the hero metric's short name, e.g. "Day-7 activation") `{{HERO_VALUE}}` `{{HERO_CAPTION_1}}` `{{HERO_CAPTION_2}}`, `{{LEAD_1}}` `{{LEAD_2}}` `{{LEAD_3}}` (one-line standfirsts under the three gate-section titles — the section's main takeaway), `{{PAIN}}` (the pain), `{{GOAL}}` (the metric — what is measured), `{{BAR_LINE}}` (the bar as a short from→to, e.g. "34% → 50%") and `{{BAR_STAMP}}` (the registration stamp — the lock-date + a "pre-build" note, e.g. "Locked 2026-04-02 · pre-build"; stated confidence renders from the DATA_JSON `confidence` value, "unrated" when null), `{{PROSE_NEXT_READ}}`, the four serif verdict lines `{{VERDICT_1}}` `{{VERDICT_2}}` `{{VERDICT_3}}` `{{VERDICT_5}}` (section 04 has none — it's the bets table), and `{{SOURCE_FILENAME}}` (fills the footer's data-source attribute).
- For each `<!-- repeat:NAME -->` block, duplicate the inner element per item and fill its tokens; drop the block if it has no items: **glance** (`{{G_LABEL}}` `{{G_VALUE}}` `{{G_VALUE_CLASS}}` `{{G_FROM}}` `{{G_DELTA}}` `{{G_DELTA_CLASS}}`, classes "met" / "miss" / "leverage-only"; `{{G_DELTA}}` is a short status chip — the verdict alone, e.g. "Below bar" / "7× faster", not "Outcome · …", since the card's color key and the value's color already say outcome vs leverage), **kill** (`{{K_DIRECTION}}` `{{K_DIED_AT}}` `{{K_COST}}` `{{K_WHY}}`, from the ledger's kill entries), **beat** (`{{B_WHEN}}` `{{B_TEXT}}` `{{B_STATE}}` "met" / "miss" / "next", optional `{{B_WAFFLE_FILLED}}` / `{{B_WAFFLE_TOTAL}}` — a dated read APPENDS a new beat, it never overwrites one), **bet** (`{{BET_WORK}}` `{{BET_OWNER}}` `{{BET_REVIEW_BY}}` `{{BET_FINDING}}` `{{BET_OVERDUE_CLASS}}` = "is-overdue" when the review date has passed with an empty finding, else empty).
- Keep the `<!-- state:bets -->` guard only if at least one owned bet exists; otherwise delete it and its block. The outcome pill reads its state from `outcome.state` in the data below, one of the same three the gate defines: "met", "miss", "leverage-only" (a measured miss is an honest result, never a green win).
- String-replace `{{DATA_JSON}}` with a pure JSON literal — never a quoted string, never a function — shaped as `outcome` {baseline, current, bar, state, baselineLabel, currentLabel, finalLabel, unreadNote[2], gridTicks[]}, `confidence` (a number, or null when unrated), `leverage[]` ({label, serves, was, now, target, wasLabel, nowLabel, targetLabel}), `price` ({avoided, spent, avoidedLabel, spentLabel}, or null). The runtime turns these numbers into pixel geometry — you never compute a chart's coordinates, percentages, or geometry.
- Write the headline distilled: two sentences max, restating only numbers already in the deck, and it must state the miss whenever the pill is a miss. The verbatim pre-registered sentence lives in the deck, not the headline. Each verdict line is generated testimony written from numbers already on the page — never commentary, never softening a miss.
- Remove every `<!-- ... -->` guide comment from the final file.

Write the result to a file beside the source markdown, same basename, `.md` → `.html` (`ai-outcomes-scorecard.md` → `ai-outcomes-scorecard.html`). The file must stay self-contained — never add an external URL, font, or script.

**Register.** The template renders in the light _document_ register by default — a formal report on warm mist, built to be read, printed, forwarded, and pasted into a deck. That is the right default for any artifact that leaves the room. The dark _instrument_ register (the brand's turquoise-on-teal machine voice) is an opt-in presentation skin: add `data-theme="dark"` to the `<html>` tag. The rule for every rendered output in this system: **if it gets forwarded, printed, or embedded, it defaults to light; the dark skin is for surfaces you frame yourself.** Print is always light, either way.

Then offer to publish it as a shareable Artifact and return the link. The file is the durable, owned thing; the link is a convenience.

## Quality bar

The page never says something the gate forbids. If it shows a proven outcome, a measured number and its source stand behind it. A leverage-only page says so on its face. An overdue bet reads as unjudged, never as a win. If you rendered a result you could not point a number at, you faked the gate — the same failure `outcome-readout` refuses one feature at a time.
