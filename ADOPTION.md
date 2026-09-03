# Adoption — the on-ramp

The gates refuse hard, and a team that installs this with ten projects mid-flight can hit
refusal after refusal in its first hour. That is the system working — but nobody adopts a
system that only says no. This is the ramp: how a real team goes from install to the loop
running, without a big bang and without theater.

**The fluency thesis first, because it shapes everything here:** this library does not try
to train every designer into a prompt expert. The expertise is embedded in the skills —
`brief-to-prompt` writes the prompt, the Discernment checklist tells you what to inspect,
every refusal teaches its principle at the exact moment it's violated. What humans develop
is **judgment**, and the gates give them judgment reps inside real work. Enablement through
structure, not courses. (If you use Anthropic's AI Fluency framework — the 4Ds — the map
is direct: *Delegation* is the HUMAN/DELEGATED split and the prompt's scope lines,
*Description* is the brief structure, *Discernment* is the checklists, triage, and
critique, *Diligence* is the gates, the ledger, and the readout. This library is those
four, operationalized in the workflow.)

## Start where you are

Run [`team-ai-baseline`](skills/team-ai-baseline/SKILL.md) before anything else. The stage
it returns names the one gate to fix — and the honest floor beats the hopeful ceiling,
because every plan built on the ceiling breaks on contact with the team. If the placement
stings, that's the baseline doing its job; it is also your before-picture.

## The pilot pod — never big-bang

Two or three designers, one or two live work items, two weeks. Not the whole team, not a
mandate, not a migration.

- **Backfill only the work that matters.** Of everything in flight, pick the one or two
  items whose outcome leadership will actually ask about. Those get ledgers (the
  `conductor` handles mid-stream entry — artifacts you already have count; gates that were
  never run read as open, and that's fine). Everything else finishes outside the machine.
- **Pick the pocket that's already ahead.** The baseline skill's rule: the fix for an
  uneven team is making one group's practice the whole team's. Your pilot pod is that
  pocket.
- **Practice before real work, if the pod is nervous:** the [practice kit](practice/) runs
  the whole loop on fictional inputs in about an hour — every refusal in a place where it
  costs nothing.

## Week one

- **Day 1:** `/design-team-os:init` — five questions, five minutes. Goals, period,
  ratifiers, builder, review day. (In chat: paste the profile from
  [templates/project-profile.example.yaml](templates/project-profile.example.yaml).)
- **Day 1–2:** the pod runs the practice kit, or goes straight at the backfilled items:
  hand `research-to-pain` the real tickets, hand `prd-to-ia` the real PRD.
- **Day 2–4:** the first ledger is born from real work. Expect the first refusal — a
  missing bar, an unvalidated pain. **Read it as the system working:** the refusal names
  exactly what's missing and the smallest way to get it. That gap existed before the
  install; now it's visible.
- **Day 5:** the first [weekly review](templates/rituals.md). Small agenda, that's fine —
  the ritual exists from week one, so the machine has a heartbeat before it has volume.

## Your adoption number

Don't invent an adoption metric — the machine already carries one. `period-review`'s
**coverage line** — how many efforts shipped vs. how many ran through ledgers — is
adoption, measured the same way everything else here is measured: by artifacts, not by
enthusiasm. It prints even when unflattering. Watch it grow from the pilot pod outward;
a filled profile and installed plugin are config, not adoption.

## Role lanes

| Role | You run | You supply | You read |
| --- | --- | --- | --- |
| **Head of Design** | `team-ai-baseline`, the rituals | goals, the ratifications, bet ownership | the scorecard, the weekly agenda, the coverage line |
| **IC designer** | the loop skills (research → brief → prompt → triage → spec) | the evidence, the work itself | the gap reports — they name your next move |
| **PM / partner** | — | the PRD's stated goal and pain, the numbers after ship | the readout and its next-Intent line |

### The authority cut

The lanes above say what you *do*. This says what you may **decide** — and where the
decision is recorded, because an authority whose exercise leaves no artifact is the
checkmark this library refuses. The five conditions that make any of it official are in
[docs/ai-governance.md](docs/ai-governance.md).

| Role | You may ratify | You may never | Recorded as | If you skip it |
| --- | --- | --- | --- | --- |
| **Bar ratifier** (`people.bar_ratifiers`) | the success criteria, before anything is generated | invent the bar after launch, or ratify one you wrote alone when the profile names others | `decision.bar` — criteria verbatim, plus confidence if stated | the brief does not complete; triage and the readout have nothing to score against |
| **Bet owner** (`people.bet_authority`) | proceeding without the evidence, in your own name | own a bet as a team, or inherit one from someone who left | the four bet fields — owner, reason, declared, review_by | the gate reads open with no bet: downstream work stands on nothing and the conductor says so |
| **Scorecard owner** (`people.scorecard_owner`) | what goes upward, and its classification | let a leverage number stand in for a verdict you have not earned | the rendered scorecard, from ledger verdicts | the folio renders without an owner, and nobody is answerable for the claim |
| **Period closer** | the period's declared strategy, before the period runs; the candidate fix at the close | declare or amend strategy after the work it blesses | `<period>.intent.md`, dated · the frozen `<period>.html` | no mix verdict is possible — the observed mix renders as observation only |
| **Any maker** | nothing — you supply evidence, the gates judge it | carry a checkmark forward, or quote a person's identity where the signal would do | the ledger artifact your skill writes | the gate stays open, by design, until the artifact exists |

## Spreading past the pod

When the pod's first item closes its loop — a readout with a verdict, honest either way —
that artifact is the internal case study. Spread by showing the ledger and the readout,
not by mandating the tooling. The second pod forms around the next work item leadership
cares about; the profile and rituals are already there.

## Glossary

| Term | Meaning |
| --- | --- |
| **Gate** | A decision checkpoint (Intent, Decision, Value) that work must earn its way through |
| **Bar** | The pre-registered, team-ratified success criteria — set before anything is generated |
| **Ledger** | One YAML file per work item carrying the evidence across sessions and people |
| **Artifact** | The evidence itself — the only thing that counts as state (never a checkmark) |
| **Bet** | A recorded decision to proceed *without* evidence: named owner, reason, review date |
| **Kill** | A direction dead at a decision point, recorded with its evidence and cost |
| **Readout** | The post-ship verdict against the pre-registered bar: solved, partial, or didn't |
| **Gap report** | How a failed gate reports distance: criteria fraction, close-first, ranked punch list |
| **Coverage** | Efforts shipped vs. efforts through ledgers — your adoption number |
| **Conductor** | The routing layer: which gates are proven, which are open, what can run now |

## Ways this dies

Named now so you recognize them later — every one of these is a failure the skills
already refuse, appearing in team-sized form:

- **Gate-laundering.** A checkmark travels forward without its artifact — "we aligned on
  that" becomes a passed gate. The conductor refuses to carry it; so should your meetings.
- **Triaging exploration.** Running full criteria against a designer's three rough
  directions teaches people to hide early work. Triage bites at "is this ready for
  review," never at "look what I made."
- **Scorecard theater.** Rendering the scorecard weekly while the ledgers are empty.
  Leverage numbers with no outcome verdicts is the exact activity-without-proof the
  system exists to end.
- **The mandate-equals-handled trap.** Leadership installs the plugin, announces the OS,
  and reads adoption as done. The coverage line is the antidote — it prints the truth.
- **Config-as-progress.** A beautiful profile, zero ledgers. The profile is context;
  the ledgers are the machine running.
- **The review that judges.** The weekly ritual starts "approving" gates in the room.
  Rituals orchestrate judgment; they never become a judge — state changes in artifacts,
  not meetings.
- **The symptomatic fix.** The same complaint gets patched release after release — a
  macro, a banner, a tooltip — while the pain that generates it never gets briefed. If a
  theme keeps re-entering Intent, the fixes are symptomatic; trace it to what breaks.
- **The metric that ate the product.** The bar becomes the target and the target gets
  gamed — activation "hit" by prompting invites nobody accepts — or an adjacent metric
  quietly breaks while the bar climbs. Guardrails, ratified with the bar, are the
  antidote; a win that broke its guardrail says so.

## When to bring help

Everything above is self-serve, free, forever. The paid layer
([Fluent by Design](https://fluentxdesign.com/?utm_source=github&utm_medium=adoption)) is
someone who has run this before doing the install with you — the baseline, the pilot pod,
the workshops, the cadence run for you until your team runs it alone — and proving the
result on the scorecard. Same system either way; the difference is who holds the line
while it becomes habit.
