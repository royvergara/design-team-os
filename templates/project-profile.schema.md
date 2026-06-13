# The project profile

A **project profile** is one file at the root of your product repo that answers, once, the
stable questions a skill would otherwise re-ask every run: where your design system lives,
what your analytics events are called, where specs get written. A skill reads it instead of
interrogating you.

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

## Two surfaces, opposite capabilities

A skill is consumed two ways, and the profile works in both:

| | Claude Code (CLI) | Claude Project (chat) |
| --- | --- | --- |
| Filesystem + product repo present | yes | no |
| How a skill gets the profile | reads & verifies the file | the values are pasted in |

This is why the schema keeps **explicit values** (a chat agent can grep nothing) **and**
`source:` pointers (a CLI skill can re-derive and verify them).

## Fields skills can draw on

Every field is optional. Only `prototype-to-spec` reads the profile in this library today
(reference implementation); the rest are conventions any skill or fork can adopt.

| Field | What it is |
| --- | --- |
| `verified_against_commit` | Product-repo SHA the values were checked at. A CLI skill warns if HEAD is ahead. |
| `design_system.reference` | Where the DS rules live (the source of truth). |
| `design_system.component_catalog` | Where reusable components / utility classes live. |
| `analytics.tool`, `analytics.events` | The analytics product and the real event names. |
| `analytics.source` | Where event names are defined (e.g. `posthog.capture()` sites), for CLI re-derivation. |
| `spec_output` | Path pattern for written specs. |
| `evidence_sources` | Where validation signal comes from. |
| `constraints` | Stack-specific gotchas that change a skill's output. |

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
