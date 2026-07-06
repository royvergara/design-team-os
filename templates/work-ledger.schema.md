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

decision:
  brief: briefs/activation-checklist.md
  bar:                            # pre-registered success criteria, verbatim, set BEFORE generation
    - "Activation rate 38% -> 55% within 6 weeks of ship"
  triage:                         # latest triage of the latest prototype
    verdict: PASS
    prototype: v0.dev/xyz123      # what was triaged
  reviews:
    design_system: "2 BLOCKERs fixed, re-audit clean (2026-06-30)"
    critique: "decision: ship with persistent skip; dissent recorded"

value:
  validation:
    signal: "usability 2026-07-01: 5 of 6 completed setup < 90s, baseline 2 of 6"
    record: specs/activation-checklist.md#validation-record
  outcome:                        # written by outcome-readout after ship + measurement window
    measured: "49% at 6 weeks (PostHog, activation-v2 dashboard)"
    verdict: partial              # solved | partial | didn't — with the bar it was judged against
    next_intent: "drop-off moved to the integration step — new Gate 1 input"
```

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
