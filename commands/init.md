---
description: Scaffold Design Team OS state files in this repo — the project profile (stable context) and the work-ledger directory (per-feature gate state). Non-destructive; never overwrites existing files.
---

Set up Design Team OS in the current repository. This is safe to run more than once — it only creates what is missing and never overwrites existing state.

## 1. The project profile — `design-os.profile.yaml` at the repo root

Check whether `design-os.profile.yaml` already exists at the repo root.

- **If it exists:** do not touch it. Report that it is already present and move on.
- **If it does not exist:** create it from the template at `${CLAUDE_PLUGIN_ROOT}/templates/project-profile.example.yaml`, then improve it by deriving this repo's real values in place — do not leave placeholders:
  - Find where the design system / tokens live and set `design_system.reference` (and `component_catalog` if there is a separate component library).
  - Find the analytics tool and real event names (e.g. grep for `posthog.capture(`, `analytics.track(`, or the equivalent) and fill `analytics.tool`, `analytics.events`, and `analytics.source`.
  - Set `spec_output` to wherever specs are written, if there is a convention.
  - Set `verified_against_commit` to the current HEAD SHA.
  - For anything you genuinely cannot determine from the repo, leave the field out and tell the user which ones need a human value. Do not invent paths or event names — a stale pointer is worse than a missing one (see the profile schema at `${CLAUDE_PLUGIN_ROOT}/templates/project-profile.schema.md`).

## 2. The work-ledger directory — `design-os.work/`

Check whether a `design-os.work/` directory exists at the repo root.

- **If it exists:** leave every file in it untouched — those are live work ledgers.
- **If it does not exist:** create it, and add a `design-os.work/README.md` that explains: one `<slug>.yaml` per piece of work, written by the skills as gates pass and read by the `conductor`; the one rule is **artifacts, never checkmarks** (an entry is the evidence itself, or the gate is open); full schema at `${CLAUDE_PLUGIN_ROOT}/templates/work-ledger.schema.md`. Do not create any actual work ledger — those are born when real work starts.

## 3. Report

Summarize what you created versus what already existed, list any profile fields that still need a human value, and state the next move plainly: start a piece of work by handing research or a PRD to the relevant skill (it will begin writing a ledger), or ask the `conductor` "where are we?" once a ledger exists. Remind the user that neither file ever satisfies a gate — the profile supplies context, the ledger carries evidence, and the skills still judge.
