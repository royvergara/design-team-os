---
description: Scaffold Design Team OS state files in this repo — the project profile (stable context) and the work-ledger directory (per-feature gate state). Non-destructive; never overwrites existing files.
---

Set up Design Team OS in the current repository. This is safe to run more than once — it only creates what is missing and never overwrites existing state.

## 1. The project profile — `design-os.profile.yaml` at the repo root

Check whether `design-os.profile.yaml` already exists at the repo root.

- **If it exists:** do not overwrite any value in it. If `calendar.period_close` has passed, offer to re-declare `goals:` and the new period (tier 2 below, questions 1–2 only); if the team blocks are absent entirely, offer tier 2 in full. Otherwise report it present and move on.
- **If it does not exist:** build it in three tiers.

**Tier 1 — derive the repo facts** (never invent; a stale pointer is worse than a missing one — see the schema at `${CLAUDE_PLUGIN_ROOT}/templates/project-profile.schema.md`):

- Find where the design system / tokens live and set `design_system.reference` (and `component_catalog` if there is a separate component library; `design_system.enforcement` if guard tests exist).
- Find the analytics tool and real event names (e.g. grep for `posthog.capture(`, `analytics.track(`, or the equivalent) and fill `analytics.tool`, `analytics.events`, and `analytics.source`.
- Set `spec_output` to wherever specs are written, if there is a convention.
- Set `verified_against_commit` to the current HEAD SHA.
- For anything you genuinely cannot determine from the repo, leave the field out.

**Tier 2 — ask exactly five human questions** (the team declarations no grep can find). Ask them as one compact list, not an interview; any question the user skips leaves its block out — never fill a value the human didn't give. For each skipped question, write its block into the profile **commented out with a one-line TODO** naming what belongs there (e.g. `# goals: — this period's goals, verbatim; skills that map work to goals will ask`): a visible gap gets filled, an absent one gets tripped over weeks later by the first skill that needs it.

1. **This period's business goals**, verbatim → `goals.period` + `goals.list`.
2. **The current period and its close date** → `calendar.current_period` + `calendar.period_close`.
3. **Who ratifies bars, and who can own a bet** → `people.bar_ratifiers` + `people.bet_authority` (and `people.scorecard_owner` if named).
4. **The default AI builder** (v0, Bolt, Lovable, …) → `tools.builder` (plus `tools.state` if they say where ledgers will live).
5. **The weekly review day and owner** → `rituals.weekly_review` (read by `weekly-review` and the ritual definitions in `${CLAUDE_PLUGIN_ROOT}/templates/rituals.md`).

**Tier 3 — everything else grows by use.** Do not ask about `metrics:`, `research:`, `standards:`, `artifacts:`, or `reporting:` at init. Each profile-reading skill names its block when it first needs it; the profile accretes from real work, and a block no skill ever asked for should not exist.

## 2. The work-ledger directory — `design-os.work/`

Check whether a `design-os.work/` directory exists at the repo root.

- **If it exists:** leave every file in it untouched — those are live work ledgers.
- **If it does not exist:** create it, and add a `design-os.work/README.md` that explains: one `<slug>.yaml` per piece of work, written by the skills as gates pass and read by the `conductor`; the one rule is **artifacts, never checkmarks** (an entry is the evidence itself, or the gate is open); the one sanctioned exception is the **owned bet** (a gate can carry a recorded decision to proceed without evidence — named owner, reason, declared date, review date — and it still reads as open, just owned); full schema at `https://github.com/royvergara/design-team-os/blob/main/templates/work-ledger.schema.md`. Do not create any actual work ledger — those are born when real work starts. **Write that literal GitHub URL into the README as the schema reference — do not substitute a local path or `${CLAUDE_PLUGIN_ROOT}`.** This README is committed to the user's product repo, so the pointer must resolve for a teammate who never installed the plugin; an absolute install path is a dead link the moment it leaves this machine.

## 3. The reviews directory — `design-os.reviews/`

Check whether a `design-os.reviews/` directory exists at the repo root.

- **If it exists:** leave every file in it untouched — those are live review artifacts.
- **If it does not exist:** create it, and add a `design-os.reviews/README.md` that explains: this is where the evidence a ledger entry points to lives — a `design-system-enforcement` violation list, a `critique-synthesis` ranking, an audit, named however the team likes and referenced from the ledger's pointer fields (e.g. `decision.craft`'s `detail`) — and also where the `period-review` skill's frozen outputs live, the rendered `<period>.html` scorecard plus the dated `<period>.intent.md` strategy declaration written at period start; the same one rule applies here as in the ledger — artifacts, never checkmarks. Do not create any actual review file — those are born when a skill produces one. Full schema at `https://github.com/royvergara/design-team-os/blob/main/templates/work-ledger.schema.md`, same literal-URL rule as above.

## 4. Report — and orient the user

Summarize what you created versus what already existed, list any profile fields that still need a human value (including any of the five questions the user skipped), and note that the remaining team blocks (`metrics:`, `research:`, `standards:`, …) get added the first time a skill asks for them.

Then — this is the part a first-time user actually needs — **draw the spine and the doors into it.** Init is most people's first contact with the system; a report that ends "hand research to the relevant skill" strands them in front of twenty skill names. End with two things, always:

**The spine** (render it as this compact map, verbatim or better):

```
INTENT                    DECISION                       VALUE
pain + evidence     →     brief + bar → triage     →     validation → ship → readout
research-to-pain          brief-from-pain                validation-plan
                          brief-to-prompt                outcome-readout
                          prototype-triage
```

One line under it: every gate demands its artifact before the next runs, work can enter at any gate, and the ledger in `design-os.work/` carries the evidence between them.

**The doors** — route by what the user has in hand today:

- **Raw research** (interview notes, tickets, analytics, a strategy doc) → `research-to-pain`
- **A PRD or requirements doc** → `prd-to-ia`
- **A prototype someone already built** → `prototype-triage` (it will ask for the brief)
- **A shipped feature with numbers** → `outcome-readout`
- **Not sure / several of these** → the `conductor` — describe what exists and it routes

Close with the standing reminder: none of these files ever satisfies a gate — the profile supplies context, the ledger carries evidence, the reviews directory holds what the evidence points to, and the skills still judge.
