# Design: v0.9 — the judgment foundation, the period review, and the scorecard as an instrument

**Date:** 2026-07-14
**Status:** Approved for planning (pressure-tested across five rounds; design imported from Claude Design and reconciled)
**Author:** Roy Vergara (with Claude)

## The one-sentence version

v0.9 teaches the machine to record judgment (bet class, stated confidence, kills), adds a
frozen quarterly **period review** that turns those records into trends, and rebuilds the
scorecard render as a narrative instrument — the Claude Design composition on the
established palette, charts driven by data, honesty rules enforced by the runtime.

## Motivation

The system measures production (leverage) and results (outcomes) but not **selection** —
whether the team chooses well. As AI makes production cheap, selection quality is the
scarce skill and the brand's entire thesis ("judgment got expensive"), yet no number in
the machine measures it. Three gaps, one release:

1. **Judgment is unrecorded.** Kills, stated confidence, and bet intent vanish; only
   survivors get scored — survivorship bias built into the instrument.
2. **There is no time dimension.** The scorecard is a snapshot; calibration, kill
   economics, and mix only exist as trends (n>1). Every quarter without the fields is
   trend history that can never be honestly reconstructed.
3. **The render fell short as a deliverable.** Iterated through five design rounds to a
   final direction (Claude Design import, reconciled below): a narrative, chapter-based,
   data-visualized document that is elegant enough to carry upward.

## Part 1 — The foundation: what the ledger learns to record

Three additions to `templates/work-ledger.schema.md`. All optional; all written by
skills as a side effect of the work, never hand-filled.

- **`intent.class`** — `core | exploration | obligation`, declared at intake.
  *Core*: move a known KPI. *Exploration*: buy learning. *Obligation*: compliance,
  contract, strategic call. **Distinct from the owned bet** (class = the work's intent
  type; bet = a gate exception carried without evidence) — the spec keeps these as
  separate fields and says so, because blurring them erodes the bet's v0.6 meaning.
- **`decision.bar.confidence`** — the team's stated confidence that the work clears its
  pre-registered bar, recorded beside the bar when `brief-from-pain` ratifies it (one
  optional question). **Absent → the call is *unrated***: excluded from the calibration
  population and visibly labeled, never guessed. Bend-don't-break: no gate refuses over
  a missing confidence.
- **`decision.kills[]`** — one entry per direction that died **at a decision point**:
  final triage fail, critique non-selection, or a readout "stop investing." Each entry
  carries the direction, where it died, the reason *with its evidence*, a cost estimate,
  and the date — artifacts, never `killed: true`. Sketch-stage divergent exploration is
  deliberately not counted (triage's carve-out stands); counting sketches would inflate
  kill records into noise.

Two skills gain the ledger line the other five already carry (same "if a ledger is
present…" pattern, same "no ledger changes nothing" close):

- **`critique-synthesis`** records the ranked decision it already produces *and* the
  non-selected directions as kills with their reasons.
- **`design-system-enforcement`** records the violations it found (count + pointer),
  feeding a future craft trend.

`/design-team-os:init` additionally scaffolds `design-os.reviews/`.

## Part 2 — The period review: producer skill #2

**Skill: `period-review`** (sixteenth skill; sibling naming: `outcome-readout` judges one
feature → `outcomes-scorecard` renders one effort → `period-review` renders the program
over time). It reads `design-os.work/*.yaml`, rolls the period's closed ledgers up, and
renders `design-os.reviews/<period>.html` in the same visual system as the scorecard.
A period is a quarter by default (`2026-Q3`); any consistent cadence works — what the
gates require is only that periods are declared, dated, and never rewritten.
**Frozen reviews are never edited** — the trend is the sequence of frozen files; git is
the event log; the repo is the database. No dashboard, no service.

Page content, top to bottom: masthead (period, declared strategy and its declaration
date) → the period's one-sentence headline → **coverage line** ("8 efforts shipped;
6 through ledgers") → outcomes rollup (effort · class · bar · verdict) → judgment
(calibration, kill economics, observed mix vs declared) → bets ledger (open / reviewed /
overdue) → trend strip vs prior frozen reviews.

**Its gates — each a refusal, each fixture-tested:**

1. **No prior frozen period → no trend claims.** The first review renders labeled
   "first period on record"; it never fabricates a trajectory.
2. **Small-n floor.** Below n=10 calls in the window, judgment renders as **counts**
   ("3 of 4 calls hit"), never percentages. Calibration computes on a trailing window
   (default 4 quarters), and the n is always printed.
3. **Coverage is always shown.** The review reports its own denominator — efforts that
   bypassed ledgers are named as uncovered, never silently omitted. The instrument is
   honest about what it cannot see.
4. **Strategy declared at period start or no mix verdict.** The declared bet mix lives
   in a dated `design-os.reviews/<period>.intent.md` written at the period's start; if
   absent (or dated late), the observed mix renders as observation only, with no verdict
   against intent — declaring strategy after the fact would let the mix grade itself.
5. **Staleness flags.** A leverage number measured two periods ago cannot be quoted as
   current; reads carry dates and stale ones are flagged.
6. **Unrated calls excluded and shown.** Calibration counts only calls that stated
   confidence; the opt-in rate is printed beside the curve.

Identity: it renders earned state. It never judges a feature (`outcome-readout`), never
places the team on a maturity curve (`team-ai-baseline` — the review may *cite* the
latest baseline read), and never routes (`conductor`).

Machine-side only (needs ledgers), like the conductor — PROJECTS.md says so.

**Fixtures** (`tests/fixtures/period-review/`): **single-period-trend** ("show
leadership our improvement" with one period → refuses the trend, renders first-period-
on-record); **small-n-percentage** ("give them the % hit rate", n=3 → counts, never
percentages); **coverage-laundering** ("skip the two efforts that didn't use ledgers" →
denominator reported anyway).

## Part 3 — The scorecard render: the reconciled design

The template (`templates/scorecard.html`) is rebuilt on the Claude Design import
(project `9354b0f8…`, file `AI Outcomes Scorecard.dc.html`), reconciled by this
precedence: **the design owns composition and personality; the established palette owns
every hue; the honesty gates outrank the design; the D3 `DATA` contract outranks the
design's markup.**

**Composition (from the design, kept):** document folio (doc title left, classification
· period right, double rule); masthead with serif title and class chip; lede; hero as a
two-column verdict — distilled two-sentence headline left, the **giant Gloock verdict
figure** right (~122px, a single monolithic figure — no ghost or paired numeral, which
read as layered clutter or a ragged silhouette in earlier passes; the baseline folds
into the stacked small-caps caption beneath: "+13 pts from 34%" / "below a 50% bar",
right-aligned so the column stays a clean rectangle); full-width progress bar to the bar; pill + legend; number-led glance band
(hairline-divided, no cards); **left margin rail** with Gloock chapter numerals
(01–05); slider rows for leverage; the kills card with number-led avoided/spent bars;
the trajectory card; the dated timeline with waffle dots; serif judgment lines closing
each chapter; colophon (FxD mark, provenance, page number). Entrance animations (rise /
grow / draw) kept, disabled under `prefers-reduced-motion` and print.

**Palette (established theme, translated):** light document register default —
ground `#f4f7f6`, ink `#0e2a29`, muted `#5c6f6e`, accent `#0a8f82`, **miss terracotta
`#ad4a2e`** (the light-register equivalent of the dark register's coral — the magenta in
the design file is re-keyed role-for-role), pending amber `#a86a00`. Dark instrument
register as the opt-in `data-theme="dark"` skin (teal room, `#40e0d0`, coral `#e0906f`),
token-level so charts re-theme live. Print always light.

**Type:** Gloock (display, every numeral on every chart) + **Source Sans 3** (body; the
design specifies it) — both embedded as data-URI woff2 (Gloock latin ~23KB; SS3 variable
+ italic ~45KB). The file stays fully self-contained: no CDN, no external fetch, ever.

**Charts:** the design's charts are rebuilt **data-driven** on an inlined D3 runtime
(~280KB min, the same embed move as the fonts). The skill fills one `const DATA = {…}`
block — values, dates, states — and never computes geometry; the runtime turns data into
the design's exact look. Honesty rules live in the runtime where they cannot be skipped:

- **No projection is ever drawn.** The design file's dashed projection line is removed
  and stays removed; the unread window renders as labeled maturing-space. "Still
  climbing" may live in words (attributed), never in geometry (which reads as data).
- The gap-to-bar always draws when the state is a miss.
- Charts are direct-labeled and survive grayscale printing.
- A `<noscript>` note covers JS-dead contexts; the text and tables carry every number,
  so the document never loses its record.

**Narrative contract (locked from the format rounds):**

- Headline: distilled, two sentences max, restates only numbers present in the deck,
  **must state the miss when the pill is a miss**. The verbatim pre-registered sentence
  lives in the deck, so pre-registration stays on the page word-for-word.
- Serif judgment lines: budget of five, one per chapter, each written from numbers
  already on the page — generated testimony, never commentary. Prose can never
  contradict or soften the pill. A miss is an honest chapter, not a redemption arc.
- Chapters are numbered because the gates are a real sequence: 01 The bet (Intent) ·
  02 The work (Decision) · 03 The reads (Value) · 04 On the record (owned bets —
  **gate-required, always present when bets exist**) · 05 Where it stands.
- New slots beyond v0.8: class chip, confidence, kills block, folio classification +
  period (optional), dated appended reads (never overwrite), hero figure tokens.

**Craft pass (applied to the reference artifact, part of the template):** scroll-
orchestrated reveal — chapters and their bars/line-draws animate on entering the
viewport, not on load — JS-gated so a JS-dead context hides nothing, disabled under
print and `prefers-reduced-motion`; a 2px reading-progress hairline (live only,
print-hidden); the margin-rail numerals are anchors with visible focus states; the
redundancy diet (the hero figure and the trajectory own "47%" — the progress strip is
pure geometry; a key number appears at most four times per page); optical hang on the
headline's em-dash (line-start hangs only — never mid-sentence); `text-wrap: pretty`
on prose; native `<title>` tooltips on chart data points.

The existing three `outcomes-scorecard` fixtures must still pass unchanged; the render
instructions in `skills/outcomes-scorecard/SKILL.md` are updated for the `DATA` block
and the new slots, with the gate section untouched.

## Testing

- Three new `period-review` fixtures (above) wired into `tests/run.sh`; TESTING.md
  section documenting them.
- The three existing `outcomes-scorecard` fixtures re-run and must hold.
- Static guards must stay green: `check-references.sh` (backtick discipline in the new
  SKILL.md — only real skill names in backticks), `check-version.sh`,
  `claude plugin validate --strict`.
- Render smoke check (as in v0.8.3): deterministic fill of the new template → zero
  leftover tokens/guards, parses, self-contained (data: URIs only), both registers
  render, print stylesheet holds.

## Release reconciliation (same-PR, non-negotiable)

Sixteenth skill: README lineage line, skills-table row (`period-review · Program ·
v0.9`), the long refusal sentence gains the review's refusals, both "fifteen skills"
install lines (README Door two, IMPLEMENTATION.md), **PROJECTS.md count and its
browser-door caveat** (period-review is machine-side like the conductor), README Status
paragraph, TESTING.md, CHANGELOG `## v0.9`, manifest `0.9.0`. Case-insensitive sweep:
`grep -rniE "fifteen" README.md IMPLEMENTATION.md PROJECTS.md` must return nothing
current-doc. `work-ledger.schema.md` documents the three new fields and the two new
writer skills.

## Out of scope (explicit, deferred to v0.10)

- Evidence tiers (designed at spec, earned at readout, verb restrictions).
- Finance rungs (profile-held metric links, cited/ratified money). Both are additive
  labeling layers that work retroactively; neither blocks the data clock.
- A per-feature `outcome-readout` render; a multi-effort live dashboard; charting
  beyond the template's runtime.

## Open questions

None blocking. Slider/chart geometry details and the exact `DATA` shape are
implementation-plan material; the `.dc` file and the published artifact
(claude.ai/code/artifact/2281c377…) are the visual reference of record.
