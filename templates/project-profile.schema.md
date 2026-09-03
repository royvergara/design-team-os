# The project profile

A **project profile** is one file at the root of your product repo that answers, once, the
stable questions a skill would otherwise re-ask every run — the repo's facts (where your
design system lives, what your analytics events are called, where specs get written) and
the team's declarations (this period's goals, what your metrics mean, who ratifies bars,
when the period closes). A skill reads it instead of interrogating you. Constant context
is also the machine's cheapest reliability win: the same declared inputs produce far
steadier outputs than context re-typed slightly differently every run.

**What it is, named:** the profile is this machine's **judgment context layer** — what the
skills judge *from*. It is the same object the analytics world calls a semantic layer, at the
design-work layer instead: metric definitions that settle what a number means before a bar is
registered against it, the source of truth each number is read from, the goals work is checked
against, and who holds which decision right. Declared once, versioned in git, read by every
skill — and never a judge itself. No profile field has ever supplied a verdict; it supplies
the context a verdict is reached in. See [docs/ai-governance.md](../docs/ai-governance.md)
for how a declaration here becomes binding.

File name: **`design-os.profile.yaml`**, in **your product repo** — not in this library.
This library ships only the schema (this file) and an example
([`project-profile.example.yaml`](project-profile.example.yaml)).

## Why it exists

Dogfooding the skills into a real app surfaced one adoption tax: stable context
(design-system reference, event names, spec path) got re-supplied on every run. The profile
removes that — supply it once, in data.

## What it never does

**A profile supplies context; it never satisfies a gate.** The gates take *per-instance
judgment* — a validation signal, a named pain with evidence, success criteria set before
building. None of those live in a profile. `prototype-to-spec` still demands the validation
signal even when a profile is present. Keep stable config in the profile; keep the gate
inputs where they belong — with a human, per piece of work.

The team blocks extend the same rule two ways. **People fields are decision *rights*, never
performed *acts*:** `people.bar_ratifiers` says who *may* ratify a bar; it never means a bar
*was* ratified — the ratification still has to happen, per piece of work. And **a goal in
the profile never substitutes for an artifact stating its own:** `prd-to-ia` still requires
the PRD to state its goal; the profile's `goals:` list is what the stated goal gets checked
*against*, not a stand-in for it.

**Never put a secret in the profile.** `tools:` names the products; credentials and
connections live in your own tooling (MCP config, env), never in a committed YAML file.

## Two surfaces, opposite capabilities

A skill is consumed two ways, and the profile works in both:

| | Claude Code (CLI) | Claude Project (chat) |
| --- | --- | --- |
| Filesystem + product repo present | yes | no |
| How a skill gets the profile | reads & verifies the file | the values are pasted in |

This is why the schema keeps **explicit values** (a chat agent can grep nothing) **and**
`source:` pointers (a CLI skill can re-derive and verify them).

## Fields skills can draw on

Every field is optional. Most gate skills read the profile now — each names its fields in
one sentence in its own SKILL.md; anything not listed there is convention a fork can adopt.

### Repo facts (derivable — `verified_against_commit` is their freshness signal)

| Field | What it is |
| --- | --- |
| `verified_against_commit` | Product-repo SHA the values were checked at. A CLI skill warns if HEAD is ahead. |
| `design_system.reference` | Where the DS rules live (the source of truth). Read by `design-system-enforcement`, `brief-to-prompt`, `prototype-to-spec`. |
| `design_system.component_catalog` | Where reusable components / utility classes live. |
| `design_system.enforcement` | Guard tests / lint rules that enforce the system, if any. Read by `design-system-enforcement`. |
| `analytics.tool`, `analytics.events` | The analytics product and the real event names. |
| `analytics.source` | Where event names are defined (e.g. `posthog.capture()` sites), for CLI re-derivation. Read by `outcome-readout` to locate the measured number. |
| `spec_output` | Path pattern for written specs. (`artifacts.specs` is the newer general form; this stays as an alias.) |
| `evidence_sources` | Where validation signal comes from. Read by `research-to-pain` as where to look. |
| `constraints` | Stack-specific gotchas that change a skill's output. |

### Team declarations (human — `calendar.period_close` is their freshness signal)

| Field | What it is |
| --- | --- |
| `tools.builder` | The default AI builder (`v0`, `bolt`, `lovable`, …). `brief-to-prompt`'s default adapter target. |
| `tools.state` | Where ledgers live (`git` \| `notion`). Read by the `conductor`. |
| `tools.analytics` / `tools.support` / `tools.design` | Names of the products in the stack — names only, never credentials. |
| `goals.period`, `goals.list` | This period's business goals, verbatim. Read by `prd-to-ia` (mapping check) and `brief-from-pain`. |
| `metrics[]` | The KPI dictionary — `name`, `definition`, `source` per metric. Definitions kill "two teams compute activation differently." The source is part of the definition: `outcome-readout` scores a bar only on a value read from it, and records a value from anywhere else as a different measurement. A source may change honestly (a dashboard renamed, a tool migrated): **re-declare it dated** — edit `source` to name the new source, the date it took effect, and the source it replaces, at the moment of the change; the git diff is the record. A source edited without a date is an undated swap, and the readout treats it as one. Read by `brief-from-pain` and `outcome-readout`. |
| `people.scorecard_owner` | Who carries the scorecard upward. Read by `outcomes-scorecard`. |
| `people.bar_ratifiers` | Who *may* ratify a bar (a right, never an act). Read by `brief-from-pain`. |
| `people.bet_authority` | Who *may* own a bet (same rule). Read by the bet path. |
| `calendar.current_period`, `calendar.period_close` | The period label and its close date. Read by `period-review` and `outcomes-scorecard`; the close date is the staleness signal for every block in this table. |
| `research.participant_access`, `research.lead_time`, `research.constraints` | Recruiting reality. Read by `validation-plan` so "runnable this week" is honest. |
| `standards.accessibility`, `standards.support` | The stated bar (e.g. WCAG 2.2 AA; browser/device matrix). Read by `design-system-enforcement` and `prototype-to-spec`. |
| `artifacts.*` | Homes for written outputs (`specs`, `briefs`, …). Generalizes `spec_output`. |
| `reporting.classification` | The folio default (e.g. `Confidential`). Read by `outcomes-scorecard`. |
| `rituals.*` | Cadence declarations (e.g. `weekly_review: {day, owner}`). Read by `weekly-review` and the ritual definitions in [templates/rituals.md](rituals.md). |

**Freshness:** repo facts go stale by commit (`verified_against_commit`); team declarations
go stale by calendar. When `calendar.period_close` has passed, a re-run of
`/design-team-os:init` prompts re-declaring `goals:` and the new period — a goals list from
last quarter is a stale pointer like any other.

## How a skill reads it (one line, not a stanza)

These skills are terse on purpose, so the integration is one sentence in the relevant
section, not a preamble. The reference line in `prototype-to-spec`:

> If a `design-os.profile.yaml` is present, take the design-system reference and analytics
> event names from it instead of re-asking — the validation signal is never a profile field,
> so the gate still stands.

In a Claude Project (no filesystem) the user pastes the profile in; with no profile, the
skill falls back to asking, exactly as it does today.

## Bootstrapping (don't hand-transcribe it)

A profile hand-copied from a repo drifts fast — verify it instead of typing it. In Claude
Code, ask:

> Read this repo and write `design-os.profile.yaml`. For `analytics.events`, grep
> `posthog.capture(` (or your tool's capture call) **in app source only — exclude
> `node_modules`**, or a dependency's events leak in. For `design_system`, find the token
> source and any guard tests. Fill `verified_against_commit` with the current short SHA.
> Show me the file before writing it.

Re-run it when the repo moves enough to matter. A chat user takes the generated file and
pastes it into their Project once. This keeps the heavy work on the cold path; the skill
pays one sentence.
