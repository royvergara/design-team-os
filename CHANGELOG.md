# Changelog

All notable changes to Design Team OS. Versions follow the repo's `v0.x` drops;
the plugin manifest (`.claude-plugin/plugin.json`) carries the matching version.

The format is loosely [Keep a Changelog](https://keepachangelog.com/). Every skill
listed enforces a gate — it refuses when its inputs aren't earned — and every one
is covered by a runnable fixture in [TESTING.md](TESTING.md).

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
