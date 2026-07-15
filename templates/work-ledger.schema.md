# The work ledger

A **work ledger** is one file per piece of work that carries the state of that work across
sessions, people, and weeks: which gates have been proven, with the evidence itself embedded.
The [project profile](project-profile.schema.md) answers the *stable* questions once; the
ledger answers the *per-work* question — where are we — without relying on anyone's chat
memory.

File location: **`design-os.work/<work-slug>.yaml`**, one file per work item, in **your
product repo** — a sibling of `design-os.profile.yaml`. This library ships only the schema
(this file) and an example ([`work-ledger.example.yaml`](work-ledger.example.yaml)).

## The one rule: artifacts, never checkmarks

**A ledger entry is the artifact itself — the evidence, the pre-registered number, the
verdict with its reasoning — never a status flag.** There is no `status:`, `passed:`, or
`done:` field in this schema, deliberately. A line that says a gate passed without carrying
what passed it is a laundered gate, and every skill in this library treats it as an open
gate.

Two consequences:

- **Skills re-judge what they read.** A ledger carries the validated pain's evidence
  downstream so `brief-from-pain` doesn't re-ask for it — but the skill still judges that
  evidence against its own gate, exactly as if it were pasted into chat. The ledger is a
  courier, not an authority.
- **A missing key is an open gate.** The ledger is a state *set*, not a checklist: entries
  appear in any order, get overwritten when work cycles (a triage FAIL becomes a PASS by
  replacement — history lives in git), and can be deleted when evidence is retracted.

## Shape

Every field is optional; presence means the artifact exists, absence means the gate is open.

```yaml
work: activation-checklist        # slug; matches the filename
updated: 2026-07-06               # date of the last entry written

intent:
  pain: >                         # what breaks, for whom, in their terms
    New workspaces stall at the second setup step and never reach first value.
  evidence:                       # the actual signals, named and counted — never "validated: true"
    - "PostHog funnel: 38% of new workspaces never complete setup step 2, stable 3 months"
    - "Support: 140 tickets tagged integration-setup this quarter, silent OAuth failure theme"
    - "Interviews: 6 of 8 new admins named the integrations step as where they gave up"
  goal: "Lift activation (setup complete within 7 days) — company OKR 2.3"
  class: exploration        # core | exploration | obligation — the work's intent type,
                            # declared at intake. Optional; absent reads as unclassified.
                            # Distinct from the owned bet: class describes what kind of
                            # bet the work IS; a bet is a gate exception carried without
                            # evidence. An obligation-class effort can still run every
                            # gate with full evidence.

decision:
  brief: briefs/activation-checklist.md
  bar:                            # pre-registered success criteria, verbatim, set BEFORE generation
    criteria:
      - "Activation rate 38% -> 55% within 6 weeks of ship"
    confidence: 70          # optional, 0-100: the team's stated confidence, recorded
                            # when the bar is ratified, before any build. Absent → the
                            # call is UNRATED: excluded from any calibration population
                            # and labeled as such. Never backfilled after a read.
  triage:                         # latest triage of the latest prototype
    verdict: PASS
    prototype: v0.dev/xyz123      # what was triaged
    criteria: "6 of 6 MET"        # the honest distance gauge — a fraction of binary rows, never a score
    attempt: 2                     # how many triages this work has taken (trajectory; history lives in git)
  reviews:
    design_system: "2 BLOCKERs fixed, re-audit clean (2026-06-30)"
    critique: "decision: ship with persistent skip; dissent recorded"
  kills:                    # one entry per direction dead at a DECISION POINT only:
    - direction: "Checklist-first onboarding"
      died_at: triage-final          # triage-final | critique-not-selected | readout-stop
      why: "2/6 brief criteria; completion theater, no invite path"   # the evidence, never bare
      cost: "$0.7k"                  # estimate is fine; say so if estimated
      date: 2026-05-14
                            # Sketch-stage divergent exploration is deliberately NOT
                            # recorded here — kills are decisions, not discards.
  craft:                    # written by design-system-enforcement when it audits
    violations: 3           # count at the audit date
    detail: "design-os.reviews/onboarding-craft-2026-05.md"   # pointer to the violation list
    date: 2026-05-20

value:
  validation:
    signal: "usability 2026-07-01: 5 of 6 completed setup < 90s, baseline 2 of 6"
    record: specs/activation-checklist.md#validation-record
  outcome:                        # written by outcome-readout after ship + measurement window
    measured: "49% at 6 weeks (PostHog, activation-v2 dashboard)"
    verdict: partial              # solved | partial | didn't — with the bar it was judged against
    next_intent: "drop-off moved to the integration step — new Gate 1 input"
```

## The owned bet — the one legitimate exception

Real organizations sometimes proceed without the artifact on purpose: a contract commitment,
a compliance deadline, a strategic bet on a new market. A system with no way to record that
doesn't get followed under pressure — it gets abandoned silently, which is worse than a
logged exception. So a gate can carry an **owned bet** instead of its artifact:

```yaml
intent:
  bet:                            # a conscious decision to proceed WITHOUT the artifact
    owner: "Dana K, VP Product"   # a named human with the authority to own it
    reason: "Northwind contract commits this for Q3; pain is assumed, not validated"
    declared: 2026-07-10
    review_by: "4 weeks post-ship: funnel + support themes decide if the bet held"
```

What separates a bet from a laundered gate: **a bet declares the evidence is absent and
names who owns proceeding anyway; laundering claims the evidence exists.** Four fields, all
required — `owner` (a person, not a team), `reason`, `declared`, `review_by` (the evidence
and date that will judge the bet). A bet missing any of them reads as a checkmark, and every
skill treats it as one.

A bet never closes a gate. The gate stays **open — bet on file**: the `conductor` reports it
as exactly that (never as proven), downstream skills proceed but say plainly they are
building on an unproven gate, and `outcome-readout` scores the bet at `review_by` like any
other bar. Enthusiasm is not a bet — "the VP loved it" claims merit; a bet says "we know we
have no evidence, and here is who owns that."

## Who writes it, who reads it

Skills append their own artifact when they complete (`research-to-pain` writes `intent`,
`brief-from-pain` writes `decision.bar`, `prototype-triage` writes `decision.triage`, and so
on). The `conductor` skill reads the whole file to report which gates are proven, which are
open, and what is runnable now. Humans read it in review — a ledger diff in a PR is the
work's state changing, visible to the whole team.

## In a Claude Project (chat)

No filesystem, so the ledger degrades to the same YAML kept as a pinned block in the
Project's knowledge: paste it in when you resume, paste the updated block back when a skill
adds an artifact. Same structure, same rule — the block carries evidence, never checkmarks.
