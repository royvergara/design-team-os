# Changelog

All notable changes to Design Team OS. Each `v0.x` release extends the machine or
sharpens a capability it already has; the plugin manifest
(`.claude-plugin/plugin.json`) carries the matching version.

The format is loosely [Keep a Changelog](https://keepachangelog.com/). Every skill
listed enforces a gate — it refuses when its inputs aren't earned — and every one
is covered by a runnable fixture in [TESTING.md](TESTING.md).

## v0.15 — 2026-07-16

The dogfood release: everything a real end-to-end run (Live Music Memoirs, 2026-07-15 —
see docs/retros/) said was missing around the judgment layer. No gate changed; the chrome did.

### Added

- **The conductor renders.** templates/conductor.html — the readout as a shareable page:
  gate cards each carrying their artifact pointer, an **artifact manifest** (the one
  consolidated view of every path a ledger points to), the runnable set with caveats on the
  cards, and marked states for synthetic / bet-carried values (hatched, dashed — never
  proven green). Opt-in via a new render section in the `conductor` skill; the render is a
  derived view, never state.
- **Deterministic template filling.** scripts/render.mjs fills any render template's
  tokens, repeat blocks, state guards, and DATA_JSON from one data file, strips guide
  comments, and fails loudly on a missing token. The dogfood's scorecard fill took an LLM
  subagent ~5 minutes and ~107k tokens and required catching a mis-fill by eye; the script
  does it in milliseconds or refuses. `outcomes-scorecard` and the conductor's render
  section now prefer it, with hand-fill as the no-Node fallback.
- **Orientation blocks in the seven gate skills** (research-to-pain, brief-from-pain,
  brief-to-prompt, prototype-triage, validation-plan, prototype-to-spec, outcome-readout):
  one line in — where this gate sits on the spine — and one line out — what the _next_
  gate will demand of the work. The dogfood's sharpest usability finding was working lost:
  no sense of position, or of what passing here costs at the next gate.
- **Init orients.** The init command's report now ends with the spine map and the doors in
  (what's in hand → which skill), instead of stranding a first-time user in front of twenty
  skill names; skipped profile questions are written into the profile as commented TODO
  blocks so gaps stay visible instead of tripping a skill weeks later.
- **The execution bridge for validation.** templates/interview-capture.md — one file per
  session, quotes before reads, tallies mapped verbatim onto the plan's pre-registered
  decision rules. The dogfood repo's real validation arc died between plan and run: scripts
  existed, zero interviews happened. `validation-plan` now points at the capture template.
- **Demo mode, as law.** docs/demo-mode.md — fabricate freely when the user declares a
  demo, mark every fabricated value synthetic _in the artifacts_, synthetic never counts as
  proven, gates fire as demonstrations rather than being suspended, and the demo ends with
  the reset named. The dogfood improvised exactly this; now it's the convention.
- **The client test drive.** commands/demo.md (`/design-team-os:demo`) — run a client's
  _real_ artifacts through the gates for real judgment (refusals included — they're the
  most convincing thirty seconds), continue past their evidence on flagged inference to a
  final readout and scorecard, and clean up by deleting one gitignored `design-os.demo/`
  sandbox. The **evidence boundary** — where their artifacts stop carrying the work — is
  recorded in the ledger and visible on the renders: real gates solid, inferred hatched,
  plus a fixed demo ribbon both templates now carry behind a `state:demo` guard.

## v0.14 — 2026-07-15

The balancing loop, in the machine's own idiom.

### Added

- **Guardrails.** A bar may now name what must _not_ degrade while its criteria are
  chased — pre-registered and ratified _with_ the bar, at the same moment, under the same
  discipline (`decision.bar.guardrails`; absent is legal, never invented later).
  `outcome-readout` reads each guardrail beside the bar with a closed verdict set —
  **held / broken / unread** (a guardrail nobody fetched is _unread_, never assumed held) —
  and the verdict carries both reads: **"solved, guardrail broken" is a legal, required
  compound.** A cleared bar never silences a broken guardrail. The diagnosis also asks the
  proxy question: did the number move because the thing it stands for moved, or was the
  metric gamed hollow?
- **The win-laundering fixture** (`outcome-readout/guardrail-broken`): bar cleared,
  guardrail broken, a user pushing to lead with the win and exile the guardrail to next
  quarter — the mirror of every miss-laundering refusal the library already holds.
- Riders: two ways-this-dies rows in ADOPTION.md (_the symptomatic fix_, _the metric that
  ate the product_), and the practice kit's week-8 numbers now carry a broken guardrail so
  the lab teaches the compound verdict.

### Fixed (0.14.1) — reliability-envelope pins from the wringer

A full-suite run plus four novel adversarial simulations put v0.14 through the wringer:
30/34 on the suite (every failure a previously-passing borderline — the envelope, not
regressions) and 4/4 on the novel attacks, including a post-hoc guardrail refused with no
fixture teaching it. The four borderline cases were diagnosed and pinned at their roots:

- **`conductor`** — both failures shared one mode: the caveat stated in the summary but
  dropped from the routing. Pinned: the unproven ground a move stands on (the bet, the open
  gate) travels _with_ the runnable move; preserved work is plainly "downstream on unproven
  ground." 3/3.
- **`outcome-readout`** — the partial/didn't boundary oscillated under "rip the band-aid"
  pressure. Pinned mechanical: cleared → solved; short of bar but meaningfully above
  baseline → partial; at baseline or wrong way → didn't. Once the numbers are placed, no
  judgment call remains. 3/3.
- **`team-ai-baseline`** — the "one question" was genuinely ambiguous (probe the boundary
  the placement rested on, or the next stage's gate?). Pinned: the question probes the
  placement's own uncertain boundary; the named gap already covers the next gate. 1/1.

Judged down from a seven-item systems-thinking package: the other candidates were either
behaviors the skills already exhibit unprompted (observed in simulation), or need history
no team has yet — each parked with a named trigger in the spec
(docs/superpowers/specs/2026-07-15-guardrail-design.md).

## v0.13 — 2026-07-14

The machine gets a heartbeat and a ramp.

### Added

- **Rituals as contracts** ([templates/rituals.md](templates/rituals.md)) — a ritual is
  cadence + inputs read + artifact produced + decisions written back + a named owner,
  runnable as a live meeting or an async digest. Three ship: the weekly gate review, the
  monthly scorecard pulse (reads, never writes), and the quarterly close (`period-review`,
  the pattern's existing instance). The layer's law: rituals orchestrate existing judgment
  at a cadence; they never add a new judge.
- **`weekly-review`** (seventeenth skill) — preps the weekly agenda from the open ledgers:
  what moved (artifact deltas, triage fractions trending), what stalled (computable
  against the declared cadence, never euphemized; an overdue bet leads its line), the
  decisions needed (each routed to the skill or human that produces it), and what's
  runnable now. Its gate: it surfaces and routes, it never judges — a triage FAIL
  discussed warmly in standup is still a FAIL until the artifact changes, and with no
  state to read it refuses to fabricate a review. Fixture-tested against exactly that
  temptation.
- **The on-ramp.** [ADOPTION.md](ADOPTION.md) — the team-level runbook: start at
  `team-ai-baseline`, pilot pod over big-bang, week one day by day, role lanes,
  `period-review`'s coverage line named as the adoption number, a glossary, and the
  ways-this-dies catalog (gate-laundering, triaging exploration, scorecard theater,
  config-as-progress, the review that judges). Plus the fluency thesis, finally written
  down: enablement through structure — the expertise lives in the skills, humans get
  judgment reps inside real work — with a short, attributed mapping to the 4Ds.
- **The practice kit** ([practice/](practice/)) — the EXAMPLES walkthrough as runnable
  inputs: Acme research (with the consensus trap and the feature request to refuse), a
  PRD that passes with cruft for the exclusions list, a first prototype that FAILs triage
  into a gap report, and week-8 numbers that read _partial_ against the bar. The refusals
  are the curriculum; every gate bites where it costs nothing.
- The profile's `rituals:` block graduates from reserved to live.

### Fixed (0.13.1)

Two boundary pins from the first full-suite smoke + practice-kit simulation:

- **`prd-to-ia`** — the new profile-goals-no-pain fixture failed twice (a finding, not a
  flake): the skill stopped correctly but quoted the _profile's_ goals on the stop block's
  `Stated goal:` line. Pinned — in the stop-block template itself, where the model writes,
  not just the wiring prose: `Stated goal:` quotes the PRD and only the PRD; a goal that
  lives in the profile but not the document is still `missing`, with profile goals allowed
  only on a separate for-mapping line below the block.
- **`outcome-readout`** — simulation showed verdict-label wobble on the borderline (a
  49% read against a 55% bar headlined "Did Not" while the diagnosis said "partial win").
  Pinned the closed set's boundary: _solved_ clears the bar; _partial_ is real movement
  short of it; _didn't_ is no meaningful movement or the wrong direction — the word from
  the set, once, never a softer or harsher synonym. New borderline fixture
  (`partial-boundary`) holds it from the round-down side.

## v0.12 — 2026-07-14

The machine learns the team, and distance-to-pass becomes a standard.

### Added

- **The team profile.** `design-os.profile.yaml` graduates from repo facts to team
  declarations: `goals:` (the period's business goals — Gate 1 finally has the list a
  stated goal gets checked against), `metrics:` (the KPI dictionary; definitions settle
  what a number means before a bar is registered against it), `people:` (decision _rights_
  — who may ratify a bar or own a bet; never that they did), `calendar:` (the period and
  its close date, which doubles as the freshness signal for every team block), `tools:`
  (the stack switchboard — names only, never credentials), and `research:` (recruiting
  reality, so `validation-plan`'s "runnable this week" is honest). `standards:`,
  `artifacts:`, and `reporting:` ship documented; `rituals:` is reserved for the rituals
  layer.
- **Three-tier init.** `/design-team-os:init` derives the repo facts (unchanged), asks
  exactly five human questions (goals; period + close; ratifiers/bet authority; default
  builder; weekly-review day), and leaves the rest to grow by use — each profile-reading
  skill names its block when it first needs it. Re-running after `period_close` prompts
  re-declaring goals.
- **Eleven skills wired to the profile**, one sentence each — including three fixes for
  fields that already existed unread (`brief-to-prompt` ← builder + design system,
  `research-to-pain` ← evidence sources, `outcome-readout` ← metric definition + number
  source).
- **The gap report contract** (CONTRIBUTING): a failed gate never softens its verdict and
  never emits a readiness score — it reports distance the way a compiler does: the closed-
  set verdict, the criteria fraction ("4 of 6 MET"), the one gap to close first, the punch
  list ranked by cost, and the smallest action that would change the verdict.
  `prototype-triage` is the reference implementation, and the ledger's `decision.triage`
  gains `criteria` + `attempt` (replace-semantics preserved — history lives in git).
- **The reliability rules, written down**: the determinism boundary (what must be identical
  lives in code/schema/templates; prompts hold judgment; verdicts are closed sets) and the
  model re-baseline ritual (a model change re-runs the full suite before being trusted).

### The honesty rule this release must not break

A richer profile invites gate-laundering by config, so two fixtures guard it: a profile
`goals:` block never substitutes for a PRD stating its own goal (`prd-to-ia` still stops),
and a `bar_ratifiers` listing is a right, never a ratification performed (`brief-from-pain`
still refuses). The profile got bigger; the gates didn't get smaller.

## v0.11 — 2026-07-14

The loop gets the step it kept pointing at.

### Added

- **`validation-plan`** (sixteenth skill) — designs the smallest test that would settle a
  decision, the counterpart to the four skills that demand a signal but hand off when one is
  missing. Its gate refuses to design a test with no decision behind it: name what result
  would change what you'd do, or there is nothing to test (a vanity metric that can only
  confirm is the same failure). It holds to the smallest test that changes the call over the
  most rigorous study nobody runs, and it designs the test rather than re-litigating the
  caller's gate. No ledger write — a planned test isn't evidence; the signal comes from
  running it, recorded by the consuming skill.
- **Wired into the four callers** (`research-to-pain`, `brief-from-pain`, `prototype-to-spec`,
  `outcome-readout`) and the `conductor` routing, each with a single clause — "the smallest
  test" now hands to `validation-plan`.
- **Sixteen skills** are live; the new skill's decision-first refusal is fixture-tested.

Second phase of the skills-audit follow-up (v0.10 consolidated the tool-specific prompt
skills; this adds the validation step the loop kept deferring).

## v0.10 — 2026-07-14

The prototype-prompt skills become tool-agnostic.

### Changed

- **`brief-to-prompt-v0` + `brief-to-prompt-bolt` → one `brief-to-prompt`.** A single skill
  now writes the gated prompt for any AI builder — v0, Bolt.new, Lovable, Replit, Claude
  Artifacts, Framer — with thin per-tool adapters instead of a skill per vendor. The gate
  (won't write a prompt until the brief defines what good looks like), the prompt structure,
  and the Discernment checklist are unchanged and vendor-neutral; the target only tunes a few
  lines — a screen generator scopes to one surface; a full-app builder adds mock-data
  instructions and a scope guard, and refuses until the data question is answered.
- **`conductor` routing** now names `brief-to-prompt` with a variant note, not two skills.
- **Fifteen skills** are live (was sixteen); every one's primary refusal stays fixture-tested,
  including the merged skill's quality-bar and full-app data gates.

First step of a skills-audit follow-up: the library is now honestly agnostic — judgment is
vendor-neutral, and only the output boundary adapts (see the "On tools" note in the README).

## v0.9.1 — 2026-07-14

Polish pass on the scorecard's presentation layer — same data, same gates, a more
legible instrument.

### Changed

- **An editorial lead.** The opening is now a featured, framed "The verdict" block: a
  full-bleed headline that flows and wraps on its own, the deck and the big outcome figure
  (now labeled) in a split row, and the baseline graph and status grouped inside one
  elevated frame. The byline became a document-metadata header (Prepared by / Rendered /
  Class). New `{{HERO_LABEL}}` token; the headline no longer needs manual line breaks.
- **The margin rail is gone.** Chapter numbers moved out of the gutter into the column as
  circular badges, and every section — masthead, standfirsts, closing prose — now spans the
  full container width instead of an indented measure. Each gate section opens with a
  one-line standfirst of its main takeaway (`{{LEAD_1}}` / `{{LEAD_2}}` / `{{LEAD_3}}`).
- **One card system.** The glance band, the bet ticket, the kills table, the trajectory
  chart, and the owned-bet table now share a single elevated card token (soft border,
  radius, lift shadow) instead of four slightly different surfaces. Collapsed a latent
  double-card around the trajectory chart.
- **The registered bet reads as a ticket.** Section 01's pain / metric / bar sit in a
  framed card with a gold "Locked … · pre-build" stamp and a perforation rule — the
  pre-registration that makes the scorecard honest now looks the part. New `{{BAR_STAMP}}`
  token; `{{GOAL}}` is the metric and `{{BAR_LINE}}` the numeric bar.
- **At-a-glance is a proper card** — a header with an Outcome/Leverage color key, three
  evenly-split columns, and each metric's verdict as a status chip ("Below bar",
  "7× faster"). `{{G_DELTA}}` drops the "Outcome ·"/"Leverage ·" prefix the key now carries.
- **Leverage sliders** move to a full-width, two-lane layout — values ride above the
  track, the target below, with edge-anchored labels — so a value and its target never
  collide even when their marks nearly coincide.
- **Tables** gain gate chips on "Died at", right-aligned tabular cost, and a quiet row hover.
- **Harmonized palette** — the electric teal and cool greys warm toward the marketing
  site's register; misses stay honestly clay. Ported through the template's CSS custom
  properties, so the dark presentation skin re-colors from the same tokens.

The reference render at [`templates/ai-outcomes-scorecard.example.html`](templates/ai-outcomes-scorecard.example.html)
is regenerated from the updated template.

## v0.9 — 2026-07-14

The machine learns to measure judgment, and the proof layer becomes an instrument.

### Added

- **Judgment fields in the work ledger** — intent class (core / exploration / obligation),
  stated confidence beside the pre-registered bar (absent = unrated, never guessed), and
  kill records carrying evidence and cost for directions dead at a decision point.
  `brief-from-pain` asks for confidence; `critique-synthesis` and
  `design-system-enforcement` gain the ledger lines the other skills already carry.
- **`period-review`** (sixteenth skill) — rolls a period's closed ledgers into a frozen
  review page: outcomes, calibration, kill economics, bet mix, coverage. Six refusals,
  fixture-tested: no trend from a single period, counts below n=10, the coverage
  denominator always shown, strategy declared at period start or the mix is observation
  only, stale reads flagged, unrated calls excluded and disclosed.
- **The scorecard as an instrument** — `templates/scorecard.html` rebuilt on the
  reconciled Claude Design composition (folio, margin-rail chapters, the verdict figure,
  serif judgment lines) in the established palette (terracotta miss, both registers),
  charts drawn by an embedded runtime from a data block the skill fills — geometry is
  never computed by the model, and no projection is ever drawn. Reference render
  committed as templates/ai-outcomes-scorecard.example.html.

### Changed

- `outcomes-scorecard` fills the new contract (class chip, confidence, kills, dated
  appended reads, five data-written judgment lines); its gate is unchanged.
- `/design-team-os:init` also scaffolds `design-os.reviews/`.

## v0.8.3 — 2026-07-13

The scorecard renders as a document, not a screen.

### Changed

- **`templates/scorecard.html`** now defaults to a light "document" register — a formal
  report on warm mist with deep-teal ink and scarce turquoise — built to be read, printed,
  forwarded, and pasted into a deck. The dark "instrument" skin (turquoise-on-teal, glows)
  is preserved as an opt-in presentation register via `<html data-theme="dark">`; print is
  always light. Same palette family, Gloock serif, and status logic — only the ground flips.
- **`outcomes-scorecard` SKILL.md** records the two-register rule: one visual system, two
  grounds, chosen by the artifact's job — anything that leaves the room defaults to light;
  the dark skin is for surfaces you frame yourself. Guidance for every future rendered output.
- README scorecard showcase swapped to the light render (a deliberate mist band inside the
  dark page, and honest to the actual default output).

## v0.8.2 — 2026-07-12

Pixel-exact type parity for the scorecard render.

### Changed

- **`templates/scorecard.html`** now embeds the Gloock display face as a base64 woff2
  data-URI (~17.5KB, latin subset, OFL) rather than relying on the Georgia fallback, so a
  rendered scorecard's headline matches the marketing site's didone serif exactly. The
  file stays fully self-contained — the font is inline, no external fetch — and Georgia
  remains the per-glyph fallback. No behavior or contract change.

## v0.8.1 — 2026-07-12

The scorecard render adopts the house visual system. Cohesion pass, no behavior change.

### Changed

- **`templates/scorecard.html`** re-themed to the Fluent by Design expressive system
  (deep-teal instrument palette, scarce turquoise as the machine glow, mist-white ink,
  hairline dividers, the Gloock→Georgia didone display stack) so a rendered scorecard
  matches the marketing site and the baseline pages. The reserved status set (met /
  measured-miss / leverage-only) rides the brand's two-voice tension — turquoise for the
  machine's good glow, warm coral and amber for the honest miss and the pending state —
  and stays confined to the Outcome; Leverage numbers remain neutral ink. Single dark
  theme like the live site; print inverts to a mist band for board decks. The token
  contract and the skill's gate are unchanged.

## v0.8 — 2026-07-10

The proof layer becomes shareable. v0.7 gave the scorecard its template; this makes it
a page a Head of Design can view, print, and send.

### Added

- **`outcomes-scorecard` skill** (`skills/outcomes-scorecard/`) — renders a filled AI
  Outcomes Scorecard into a self-contained, theme-aware, print-clean HTML page written
  beside its source (`ai-outcomes-scorecard.md` → `ai-outcomes-scorecard.html`), then
  offers to publish it as a shareable Artifact link. The engine's first producer skill,
  and still a gate: it renders earned state only. No baseline, no render; a leverage-only
  headline renders labeled as such with its read date; an owned bet past its review date
  with an empty finding renders as the finding, never as a win. It never judges a feature
  (`outcome-readout`) and never routes (`conductor`). Three adversarial fixtures cover the
  refusals.
- **`templates/scorecard.html`** — the self-contained render template (inlined CSS, no
  JS, no external assets) that carries the visual language, versioned so every render
  looks like one system.

## v0.7 — 2026-07-10

The proof layer gets its artifact. The machine already produced per feature verdicts;
this is the sheet they roll up into, and the one a Head of Design carries upward.

### Added

- **AI Outcomes Scorecard** (`templates/ai-outcomes-scorecard.md`) — the program level
  companion to `outcome-readout`. Two layers, Leverage (is the work faster and cheaper)
  and Outcome (did the speed produce value), a baseline gate that refuses a scorecard
  built from memory, and a headline sentence that only fills in when both halves are
  real. Every Layer 1 metric must name the Layer 2 signal it serves, so activity cannot
  be reported as a result. Owned bets get their own section with the review date that
  will judge them, never blended into an outcome.
- **Templates section in the README**, listing the three files under `templates/`: the
  work ledger, the project profile, and the scorecard.

### Changed

- `outcome-readout` now names the scorecard as its program level rollup, and states that
  a leverage number never substitutes for a verdict the skill has not earned.

## v0.6.1 — 2026-07-09

Post-v0.6 reconciliation sweep: three stale spots the release left behind.

### Fixed

- `/design-team-os:init` — the scaffolded `design-os.work/README.md` now explains the
  owned bet alongside the artifacts-never-checkmarks rule, so a team using bets finds
  them documented in their own ledger directory.
- TESTING.md intro — the gate litany now matches its own v0.6 T-cases: triage's
  exploration carve-out and the spec's Bet Record exception.
- IMPLEMENTATION.md — the fork-header example pinned "upstream v0.5" (its second
  staleness this month); the version is now a fill-in placeholder so it cannot rot
  again.

## v0.6 — 2026-07-09

The release where the gates learn to bend without breaking. Driven by fresh-persona
review (an uncontaminated Head of Design, IC designer, and client-exec read of the
repo) plus paste-path testing of skills inside adversarial Claude Projects.

### Added

- **The owned bet** — the one sanctioned exception to a gate. A recorded decision to
  proceed _without_ evidence: named human owner, declared acknowledgment the evidence
  is absent, reason, and a `review_by` naming what will judge the bet. Schema block in
  `templates/work-ledger.schema.md`; honored by `brief-from-pain` (unvalidated pain →
  brief that opens by declaring the bet) and `prototype-to-spec` (no signal → spec
  with a Bet Record instead of a Validation Record); reported by the `conductor` as
  "open, bet on file" — never as proven — with due bets surfaced first. A bet missing
  any field reads as a checkmark. Rationale: a system with no override doesn't get
  followed under pressure, it gets abandoned silently.
- **PROJECTS.md** — the browser door made first-class: run any skill in a Claude
  Project with no install, per-gate bundle suggestions, chat-degraded state, and the
  honest limits. Backed by tests: gates held pasted into Projects whose own
  instructions push for compliance, including three skills bundled in one Project.
- Five new gate fixtures: `prototype-to-spec/owned-bet`, `conductor/owned-bet`,
  `prototype-triage/exploration-sketches`, `critique-synthesis/constraint-not-opinion`,
  `research-to-pain/heavy-single-signal`.

### Changed

- **`prototype-triage`** — exploration carve-out: triage gates the candidate for team
  review, not divergent sketches. Full-criteria triage on three directional
  generations teaches people to hide early work; the skill now says so and stays out
  of the way.
- **`research-to-pain`** — weighs signals, not just kinds: one behavioral signal of
  overwhelming scale and stability can validate single-source-but-heavy (with the
  confirming signal named), and two thin agreeing anecdotes never sum to strong. A
  stakeholder relaying named customers verbatim counts as a lead with names attached,
  not opinion.
- **`critique-synthesis`** — constraints (legal, platform, committed patterns) are
  pulled out and verified before any weighing; they bound the decision rather than
  compete with signals. User evidence is weighed by quality (n, task realism,
  fidelity artifacts) and trumps only on questions user behavior can answer. Equal
  signals in genuine conflict resolve to a precisely-specified deciding test — still
  a decision, never a summary.
- **`team-ai-baseline`** — dropped the embedded uncited statistics; the skill now
  refuses to quote figures without a supplied source.
- **README** — two-door install (browser first for non-terminal designers, Claude
  Code for the machine), an IC-inclusive line in "Who this is for", EXAMPLES.md
  promoted above the fold, the gate-tested claim aligned with actual fixture
  coverage, and the open-layer section rewritten to say plainly what is free and
  what is for sale.

## v0.5.2 — 2026-07-09

Fix a non-portable reference in the `/design-team-os:init` scaffold.

### Fixed

- `/design-team-os:init` wrote the work-ledger schema pointer into the generated
  `design-os.work/README.md` as `${CLAUDE_PLUGIN_ROOT}/templates/work-ledger.schema.md`,
  which the harness expands to an absolute plugin-install path (e.g.
  `/…/design-team-os/templates/work-ledger.schema.md`). That file is committed to the
  user's product repo, so the path was a dead link for any teammate who never installed
  the plugin — the exact stale-pointer failure IMPLEMENTATION.md warns against. The
  command now writes the canonical GitHub URL for the schema instead. Caught by an
  end-to-end smoke test of the real installed command.

## v0.5.1 — 2026-07-09

Coherence pass: one story across every doc, no behavior changes to any gate.

### Changed

- `skills/README.md` rewritten — it still described the eight-skill v0.1 drop; now
  points at the 14-skill table, leads with the plugin install, and states the
  standalone rule (ledger, profile, and `conductor` are optional, never prerequisites).
- README sweep: v0.1-era scope ("from a PRD to a code ready prototype") updated to
  the full loop ("raw research to a shipped, measured outcome"), conductor no longer
  double-counted next to "all fourteen skills," Quickstart now installs the plugin
  rather than a single skill, and the Friday-cadence claim softened to match the
  actual release history.
- TESTING.md: prose test definitions added for `brief-from-pain`, `prototype-triage`,
  and `outcome-readout` (their fixtures existed but were undocumented); intro now
  names every skill's gate and leads with the runnable harness; new "In CI" section
  documents `gates.yml`, the `run-gates` label, and the static checks.
- EXAMPLES.md: `research-to-pain` added to the trigger cheat sheet (it was the one
  missing skill).
- CONTRIBUTING.md / `gates.yml` comments: the two `claude plugin validate` commands
  are now correctly attributed — only the `plugin.json` invocation parses skill
  frontmatter.
- Spine-skill ledger paragraphs made consistent: all five now carry the explicit
  "No ledger changes nothing" sentence; `brief-from-pain` records the brief path to
  `decision.brief` (not `decision.bar`) per the schema; `outcome-readout`'s
  forbidden bare verdict now matches the schema vocabulary (`solved`);
  `prototype-triage`'s per-criterion output is a "criteria table" everywhere,
  ending the collision with the work-ledger sense of "ledger."

## v0.5 — 2026-07-06

The release where the "OS" in the name becomes literal: the machine that routes the
loop, plus one-command install.

### Added

- **`conductor`** skill — reads a work ledger (or whatever artifacts are in hand) and
  reports which gates are proven, which are open, and what can run now. Routes, never
  judges; refuses to treat a checkmark as a passed gate.
- **Work-ledger schema** (`templates/work-ledger.schema.md` + example) — one
  `design-os.work/<slug>.yaml` per feature, carrying gate state across sessions and
  people. One rule: artifacts, never checkmarks.
- **Ledger write-path** wired into the five spine skills (`research-to-pain`,
  `brief-from-pain`, `prototype-triage`, `prototype-to-spec`, `outcome-readout`), so
  the skills write the artifacts the conductor reads. A no-op when no ledger is present.
- **Claude Code plugin packaging** — `.claude-plugin/plugin.json` + `marketplace.json`
  (the repo is its own `fluent-by-design` marketplace), and a `/design-team-os:init`
  command that scaffolds the profile and ledger directory, non-destructively.

### Fixed

- `conductor` frontmatter failed to parse (a colon-space in the description read as a
  nested YAML map), which silently dropped its description at load time. Surfaced by
  `claude plugin validate --strict`.

## v0.4 — 2026-07-04

### Added

- **`team-ai-baseline`** skill — places a design team on a four-stage AI maturity curve
  (Experimenting, Scattered, Operating, Compounding) and names the one gate holding it
  back. Refuses to count tools bought or a stated mandate as adoption.

## v0.3 — 2026-06-21

### Added

- **`research-to-pain`** skill — turns raw research into a small set of ranked,
  evidence-backed customer pains. Refuses to crown a pain as validated on stakeholder
  opinion, a feature request, or a single untriangulated source. Sits one step above the
  rest of Gate 1, producing the validated pain everything downstream assumes.

## v0.2 — 2026-06-12

### Added

- Three loop-closing skills that wire the gates into a full Intent → Decision → Value →
  Intent loop: **`brief-from-pain`** (a pain becomes a brief with a pre-registered bar),
  **`prototype-triage`** (the cheap gate before human review), **`outcome-readout`**
  (reads the shipped result against the bar and hands strategy the next problem).
- The project-profile mechanism (`templates/project-profile.schema.md`) — supply stable
  context once instead of re-answering it every run.
- The runnable smoke-test harness (`tests/run.sh` + fixtures, [TESTING.md](TESTING.md)).

## v0.1 — 2026-06-12

### Added

- The eight starter skills: `prd-to-ia`, `design-system-enforcement`,
  `critique-synthesis`, `user-journey-mapping`, `prototype-to-spec`,
  `brief-to-prompt-v0`, `brief-to-prompt-bolt`, `figma-plugin-orchestration`.
