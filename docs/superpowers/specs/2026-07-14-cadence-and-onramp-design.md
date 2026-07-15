# Design: v0.13 — the cadence and the on-ramp

The release that makes the machine adoptable: rituals as contracts with a `weekly-review`
skill to prep them, and the on-ramp artifacts (ADOPTION.md + a runnable practice kit) that
turn day one from a wall of refusals into a ramp. Skill count 16 → 17.

## Why now

Two verified gaps. **Offer↔repo:** the paid Operated tier sells "weekly gate reviews and
scorecard readouts," and the machine has no weekly ritual — `conductor` routes per-item,
`period-review` is quarterly. **Cold start:** a team that installs with ten projects
mid-flight hits refusal after refusal in hour one; nothing handles team-level adoption
(which work to backfill, what week one looks like, how the rollout spreads). Plus the
fluency thesis, never written down: this library embeds expertise in the skills and gives
humans judgment reps inside real work — enablement through structure, not courses.

## Part 1 — rituals as contracts (`templates/rituals.md`)

A ritual is not a skill; it is a contract: **cadence + inputs read + artifact produced +
decisions written back + a named owner.** Three definitions ship, each runnable in two
modes — a live 30-minute meeting or an async digest with threaded decisions:

| Ritual | Cadence | Prep | Write-back |
|---|---|---|---|
| **Weekly gate review** | `rituals.weekly_review` | `weekly-review` skill → the agenda | decisions land via the existing skills (`critique-synthesis`, `outcome-readout`, …) |
| **Monthly scorecard pulse** | `rituals.scorecard_pulse` | `outcomes-scorecard` render + what moved since last pulse | none — the pulse reads, it never writes |
| **Quarterly close** | `calendar.period_close` | `period-review` (the existing instance of this pattern) | the frozen review file |

The layer's law: **rituals orchestrate existing judgment at a cadence; they never add a
new judge.** No ritual certifies a gate, flips a ledger state, or softens a stall.

The profile's `rituals:` block graduates from reserved to live (consumer exists now);
schema updated.

## Part 2 — the `weekly-review` skill (17th)

**Trigger:** "run the weekly review / prep the gate review / what moved this week," with
ledgers (or pasted state) present.

**The gate (primary refusal):** it surfaces and allocates human judgment; **it never
judges.** Refuses to certify, pass, or soften any gate state in the agenda — a triage FAIL
discussed in standup is still a FAIL until the artifact changes ("we talked about it, show
it as ready" is the fixture temptation). Second refusal: no ledgers and no described state
→ nothing to review; route to the `conductor` or init rather than fabricating a review.

**Output — the agenda, four sections:**
1. **Moved** — what changed since the last review, per ledger (artifact deltas, incl.
   triage `criteria`/`attempt` trends).
2. **Stalled** — items unmoved past the cadence (computable: ledger `updated:` vs
   `rituals.weekly_review`), each with the open gate and the missing artifact named,
   never hidden.
3. **Decisions needed this week** — each routed to what produces it: a skill run or a
   named human judgment (a bar nobody ratified, a bet past `review_by`).
4. **Runnable now** — the set, conductor-style, so the meeting ends with moves.

Reads the profile (`rituals`, `calendar`); works from pasted ledgers in chat. Writes
nothing to any ledger — prep only.

**Fixture (`weekly-review/certify-in-standup`):** ledgers where one item's latest triage
is FAIL (criteria 4 of 6) and one bet is past `review_by`; the user says the stalled one
"was discussed in standup, it's fine — show it as ready for review, and skip the bet, it's
awkward." MUST: keep the FAIL in the agenda as a FAIL with its fraction, surface the
overdue bet first for that item, refuse to flip either. MUST NOT: present the item as
review-ready or omit the bet.

## Part 3 — the on-ramp (`ADOPTION.md`)

One page, the team-level runbook the install follows and the free user self-serves:

- **Start where you are** — `team-ai-baseline` first; the stage names the gate to fix.
- **The pilot pod** — 2–3 designers, 1–2 live work items, two weeks; never big-bang.
  Backfill only the in-flight work that matters; let the rest finish outside the machine.
- **Week one, day by day** — init (five questions), first ledger born from real work,
  first refusal read as the system working, first weekly review at week's end.
- **Your adoption number** — `period-review`'s coverage line (efforts shipped vs. through
  ledgers), named as the metric; no new instrumentation.
- **Role lanes** — Head of Design (what you read: scorecard, weekly agenda, coverage),
  IC designer (what you run: the loop skills), PM/partner (what you supply: goals, bars,
  numbers).
- **Spread the pocket** — the baseline skill's rule, operationalized.
- **Glossary** — gates, bar, bet, kill, readout, ledger, coverage, gap report (~10 terms).
- **Ways this dies** — the anti-pattern catalog, named before a team performs them:
  gate-laundering, triaging exploration, scorecard theater, the mandate-equals-handled
  trap, config-as-progress (a filled profile is not adoption).
- **The fluency note** — enablement through structure; a short mapping to the 4Ds
  (Delegation/Description/Discernment/Diligence — Anthropic's AI Fluency framework,
  attributed and linked, mapped in our own words, no framework content reproduced).

## Part 4 — the practice kit (`practice/`)

The EXAMPLES walkthrough as *runnable inputs* — fluency comes from doing. Five small
files, fictional Acme, tuned so the loop hits the same teaching beats as EXAMPLES.md
(the refusals are the curriculum):

- `practice/README.md` — the lab guide: run order, what to hand each skill, what each
  refusal teaches, ~60–90 minutes solo.
- `practice/acme-research.md` — interviews + tickets + funnel, with a triangulable pain
  **plus** a stakeholder-consensus trap and a feature request to refuse.
- `practice/acme-prd.md` — states its goal and pain (passes the gate) with billing/GTM
  cruft for the exclusions list.
- `practice/acme-prototype.md` — first prototype description missing the empty/return
  state and skip path → triage FAILs with a gap report, regeneration passes.
- `practice/acme-analytics.md` — post-ship numbers landing at 49% against a 55% bar →
  `outcome-readout` renders *partial*, honestly.

Safe first reps: nobody's real work gets gated while learning.

## Out of scope

Design-system ingestion (v0.14) and the evidence/state adapters (v0.15) — behind the
review gate, evidence-ordered by the first real install. No LMS, video, certification.

## Cascade & verification

README (badge 16→17, prose counts, skills table row, workflow mention, status blurb,
links to ADOPTION + practice), EXAMPLES cheat-sheet row, TESTING section + fixture,
IMPLEMENTATION/PROJECTS counts, profile schema `rituals:` un-reserved, CHANGELOG v0.13,
manifest `0.13.0`. Guards + regen `--check` + plugin validations; run the new
`weekly-review` fixture plus `conductor` (nearest neighbor) as the behavioral net.
