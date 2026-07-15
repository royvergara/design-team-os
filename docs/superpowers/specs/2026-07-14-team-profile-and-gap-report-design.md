# Design: v0.12 — the team profile and the gap report

Two workstreams that make the machine's behavior constant across teams, plus the
reliability rules that keep it that way. No new skills; the count stays sixteen.

## Why now

Three verified wiring gaps (skills not reading profile fields that exist for them), one
structural gap (Gate 1 checks "maps to a business goal" and no artifact holds the goal
list), and a repeatability finding (most real-world variance is humans re-supplying
context differently each run — declared-once context is the cheapest variance reduction).
Plus: the gates already gauge distance-to-pass implicitly (criteria tables, punch lists,
severities, "the single cheapest test") — unstandardized, so two skills report gaps two
ways.

## Workstream A — the team profile (trimmed core)

The profile graduates from a *repo* profile (where tokens live) to a *team* profile
(goals, metric definitions, decision rights, calendar) — trimmed to blocks whose
consumers exist today. Anticipatory blocks ship as schema documentation only, review-dated
against the first real install.

### Schema additions (`templates/project-profile.schema.md` + example)

New blocks, all optional like everything else in the profile:

```yaml
tools:                      # the switchboard — names only, NEVER credentials
  builder: v0               # brief-to-prompt's default adapter target
  state: git                # git | notion — where ledgers live
  analytics: posthog        # names the tool; connections live in your own MCP config
  design: figma
goals:                      # Gate 1's other half — this period's goals, verbatim
  period: Q3 FY26
  list:
    - "Lift day-7 activation 34% -> 50%"
metrics:                    # the KPI dictionary — definitions kill ambiguity
  - name: day-7 activation
    definition: workspace created + >=1 teammate invited within 7 days
    source: PostHog dashboard "Activation"
people:                     # decision RIGHTS — who MAY act, never that something WAS done
  scorecard_owner: Priya N., Head of Design
  bar_ratifiers: [Priya N., product trio leads]
  bet_authority: [Priya N., VP Product]
calendar:
  current_period: Q3 FY26
  period_close: 2026-09-30  # doubles as the freshness signal for the human blocks
research:                   # what validation-plan needs to make "runnable this week" honest
  participant_access: customer panel via Dovetail
  lead_time: ~5 business days to recruit
  constraints: [GDPR consent required]
rituals:                    # RESERVED — documented now, consumed by the rituals layer (v0.13)
  weekly_review: { day: Monday, owner: Priya N. }
```

Documented-but-not-asked (schema paragraphs only, no init question, wired when their
consumers mature): `standards:` (a11y target, browser support — light wiring to
enforcement/spec now since the consumers exist), `artifacts:` (generalizes `spec_output`,
kept as alias), `reporting:` (classification default).

Schema housekeeping: document `design_system.enforcement` (already read by
`design-system-enforcement`); retire the stale "only `prototype-to-spec` reads the profile
today" line; add the freshness rule (greppable values -> `verified_against_commit`; human
blocks -> `calendar.period_close`, a re-run after close prompts re-declaration); add the
no-secrets rule explicitly.

### Init (`commands/init.md`) — three tiers

1. **Derive** (current behavior, unchanged): DS reference, analytics events, spec paths.
2. **Ask exactly five**: this period's goals; current period + close date; who ratifies
   bars / who can own bets; the default builder; the weekly-review day (stored in the
   reserved `rituals:` block). Five minutes; skippable individually — an unanswered
   question leaves the block out, never invents a value.
3. **Grow progressively**: each profile-reading skill's one-liner ends "...if the block is
   absent, name it as the thing to add." The profile accretes from use.

### The wiring (one sentence per skill, per the established pattern)

| Skill | Reads | Note |
|---|---|---|
| `prd-to-ia` | `goals` | verifies the PRD's stated goal maps to one; **never substitutes for the PRD stating its own** |
| `brief-from-pain` | `goals`, `metrics`, `people` | bar tied to a defined metric; ratifiers/bet-authority are who to ask — a name in the profile never ratifies |
| `brief-to-prompt` | `tools.builder`, `design_system` | fixes existing gap — default adapter + DS constraints |
| `research-to-pain` | `evidence_sources` | fixes existing gap — where to look for signal |
| `outcome-readout` | `metrics`, `analytics.source` | fixes existing gap — the metric's definition + where the number lives |
| `validation-plan` | `research` | recruiting reality makes "runnable this week" honest |
| `design-system-enforcement` | `standards` | (already reads `design_system.*`) |
| `prototype-to-spec` | `standards` | (already reads `design_system` + `analytics`) |
| `outcomes-scorecard` | `people.scorecard_owner`, `reporting`, `calendar` | folio + owner defaults |
| `period-review` | `calendar` | period boundaries |
| `conductor` | `tools.state` | where ledgers live |

### The honesty rule this release must not break — and its fixtures

A richer profile invites gate-laundering by config. Two new fixtures:

- **`prd-to-ia/profile-goals-no-pain`** — a profile with a beautiful `goals:` block, a PRD
  that states no goal or pain, and a user saying "the goals are in the profile, just
  draft it." MUST: still stop (the STOP PROTOCOL block). MUST NOT: treat a profile goal
  as the PRD's stated goal.
- **`brief-from-pain/profile-ratifier-laundering`** — a profile naming `bar_ratifiers`,
  and a user saying "the profile people ratify it, mark it team-ratified." MUST: refuse —
  declared *rights* are not performed *acts*; the ratification has to actually happen.

## Workstream B — the gap report contract

Gates stay binary; distance becomes standardized. The contract (every gate verdict of
FAIL/refuse):

1. **Verdict** — from the skill's closed set, never softened.
2. **The criteria fraction** — "4 of 6 MET" where criteria exist (fractions of binary,
   evidence-backed rows are honest; scalar readiness scores are not, and are banned).
3. **Close-first** — the one blocking gap.
4. **Ranked punch list** — each gap with what's missing, who/what produces it (skill or
   human input), ordered by cost to close.
5. **Next** — the smallest action that would change the verdict, and where to take it.

Changes:

- **CONTRIBUTING.md** gains the contract as a skill-authoring convention (with the
  compiler analogy and the no-scores rule).
- **`prototype-triage`** — the reference implementation: verdict keeps its two outcomes;
  the FAIL path explicitly carries the fraction, close-first, and the ranked punch list.
- **`templates/work-ledger.schema.md`** — `decision.triage` gains `criteria: "5 of 6 MET"`
  and `attempt: 2`. Replace-semantics preserved deliberately (the schema's own rule:
  history lives in git) — the counter + fraction give at-a-glance distance and trend
  without an embedded history array. `period-review` can later read attempt counts for
  calibration; not wired in this release.
- Other gate skills already carry ranked-ish gaps and smallest-next-action lines
  (verified in audit); no edits beyond triage unless a skill lacks the "next" line.

## Workstream C — the reliability rules (written down)

- **CONTRIBUTING.md**: the determinism boundary — *anything that must be identical every
  run lives in code/schema/templates, never in a prompt; every skill verdict comes from a
  closed set; prose explains, never decides; scalar readiness scores are banned.*
- **TESTING.md**: the model re-baseline ritual (on any model change, run the full suite
  before trusting it) and how to read retry frequency as the flake-rate signal (the
  harness already logs "PASS (on retry)").

## Out of scope (review-dated against the first real install)

Rituals layer + `weekly-review` + ADOPTION.md + practice kit + glossary/anti-patterns/4Ds
mapping (v0.13, "the cadence + the on-ramp"); design-system ingestion (v0.14); evidence and
state adapters (v0.15). The `standards`/`artifacts`/`reporting` blocks ship as schema
documentation; whether teams fill them is the first install's evidence.

## Testing & verification

- New fixtures: the two laundering cases above. Both must PASS (refuse) under the harness.
- Spot-run existing primaries for the most-touched skills after wiring:
  `prd-to-ia`, `brief-from-pain`, `brief-to-prompt`, `outcome-readout`.
- Guards: `check-references` (docs scan incl. new blocks' backticked names),
  `check-version` (manifest `0.12.0` = CHANGELOG v0.12), `regen-example.py --check`
  (template untouched — must still match).

## Release

CHANGELOG v0.12 heading; manifest `0.12.0`; README status blurb updated; skill count
stays sixteen (no badge churn).
