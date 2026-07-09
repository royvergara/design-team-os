# Changelog

All notable changes to Design Team OS. Each `v0.x` release extends the machine or
sharpens a capability it already has; the plugin manifest
(`.claude-plugin/plugin.json`) carries the matching version.

The format is loosely [Keep a Changelog](https://keepachangelog.com/). Every skill
listed enforces a gate — it refuses when its inputs aren't earned — and every one
is covered by a runnable fixture in [TESTING.md](TESTING.md).

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
  proceed *without* evidence: named human owner, declared acknowledgment the evidence
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
