# Rituals

A ritual is how the machine gets a heartbeat. It is **not a skill** — it is a contract
with five fields, and skills only do the prep and the recording; humans do the judging in
between:

| Field | What it declares |
| --- | --- |
| **Cadence** | When it runs (declared once, in the profile's `rituals:` / `calendar:` blocks) |
| **Inputs read** | The state it opens with — ledgers, the last frozen review, the scorecard |
| **Artifact produced** | What the prep step generates (an agenda, a render, a frozen file) |
| **Decisions written back** | Where the humans' calls land — always via the existing skills, always as artifacts |
| **Owner** | The named human who runs it (`rituals.*.owner`) |

**The law of the layer: rituals orchestrate existing judgment at a cadence; they never add
a new judge.** No ritual certifies a gate, flips a ledger state, or softens a stall. A
triage FAIL discussed warmly in a meeting is still a FAIL until the artifact changes.

**Two execution modes, same contract.** Every ritual runs as a live meeting (30 minutes,
the agenda is the prep artifact) **or** async (the prep artifact posted as a digest,
decisions made in threads, recorded the same way). Teams that won't add a meeting lose
nothing; the contract cares about the write-back, not the room.

## The three rituals

### Weekly gate review

- **Cadence:** `rituals.weekly_review` (day + owner).
- **Inputs:** every open ledger in `design-os.work/` (or pasted state in chat).
- **Prep:** the [`weekly-review`](../skills/weekly-review/SKILL.md) skill → the agenda:
  what moved, what stalled, decisions needed, runnable now.
- **Written back:** each decision through its own skill — a critique decision via
  `critique-synthesis`, a verdict via `outcome-readout`, a kill recorded to the ledger's
  `decision.kills[]`, a ratified bar to `decision.bar`. The review itself writes nothing.
- **Owner:** `rituals.weekly_review.owner`.

The meeting ends when every "decision needed" has an owner and every runnable move has a
name on it. Thirty minutes is enough because the agenda arrives pre-read.

### Monthly scorecard pulse

- **Cadence:** `rituals.scorecard_pulse` (monthly by default).
- **Inputs:** the ledgers + the last rendered scorecard.
- **Prep:** `outcomes-scorecard` re-render, plus one paragraph: what moved since the last
  pulse, in the ledgers' own numbers.
- **Written back:** nothing — **the pulse reads, it never writes.** It exists so the
  scorecard's story stays continuous instead of being reconstructed at quarter close.
- **Owner:** `people.scorecard_owner`.

### Quarterly close

- **Cadence:** `calendar.period_close`.
- **Inputs:** the period's closed ledgers and prior frozen reviews.
- **Prep and artifact:** [`period-review`](../skills/period-review/SKILL.md) — the
  existing instance of this pattern — renders the frozen `design-os.reviews/<period>.html`.
- **Written back:** the frozen file itself; a prior period's file is never edited.
- **Owner:** `people.scorecard_owner`.

Closing the period also re-opens the profile: `goals:` and `calendar.current_period` get
re-declared for the new period (a re-run of `/design-team-os:init` prompts exactly this).

## Staleness — what the cadence buys the machine

Declaring a cadence makes "stalled" computable instead of vibes: a ledger whose `updated:`
date predates the last two weekly reviews is stalled by definition, and the weekly agenda
says so with the open gate and the missing artifact named. Without a declared cadence the
machine can still route (the `conductor` never needed a calendar) — it just can't tell you
what's been sitting.
