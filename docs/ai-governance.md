# AI governance, for the design-work layer

Every governance framework asks the same questions: who is accountable, can you show
your reasoning, who oversees it, is there an audit trail, and what governs the change
process itself. This page answers them for Design Team OS — and answers them the way
this library answers everything else.

**The rule this page obeys.** A governance claim with no artifact behind it is precisely
the checkmark this library refuses. So every row below cites the file that implements the
property and, where one exists, the **fixture that fails when it lapses** — a runnable
adversarial test, in [TESTING.md](../TESTING.md), where a fresh agent is handed a tempting
input and graded on whether the gate held. We do not assert governance. We point at the
test that fails when it stops being true.

Where a property is real but untested, this page says so rather than dressing it up.

## The crosswalk

| Property | How it works here | Implemented in | Fails visibly when |
| --- | --- | --- | --- |
| **Transparency** — no un-openable claims | *Artifacts, never checkmarks.* A ledger entry is the evidence itself; `validated: true` reads as an open gate, and the `conductor` says so | [`templates/work-ledger.schema.md`](../templates/work-ledger.schema.md), [`skills/conductor/`](../skills/conductor/SKILL.md) | `conductor/checkmarks-not-artifacts` |
| **Accountability** — a named human owns the exception | The **owned bet**: four required fields (owner, reason, declared, review_by). A team is not an owner; a departed owner orphans the bet rather than passing it on | schema · `conductor` · `weekly-review` | `conductor/owned-bet`, `conductor/bet-orphaned` |
| **Decision rights** — authority is a right, never a performed act | `people.bar_ratifiers` / `people.bet_authority` name who *may* ratify or own. A name in the profile never counts as the ratification | [`templates/project-profile.schema.md`](../templates/project-profile.schema.md), `brief-from-pain` | `brief-from-pain/profile-ratifier-laundering` |
| **Pre-registration** — success is defined before the build | The bar is ratified before generation, verbatim; nothing is scored against a criterion invented after launch | `brief-from-pain`, `outcome-readout` | `brief-from-pain/no-success-criteria`, `outcome-readout/post-hoc-no-number` |
| **Honest measurement** — a cleared bar never silences a broken guardrail | Verdicts come from a closed set (solved / partial / didn't) tied to the number; guardrails read held / broken / unread | `outcome-readout`, `outcomes-scorecard` | `outcome-readout/guardrail-broken`, `outcomes-scorecard/leverage-only-as-win` |
| **Oversight** — rituals orchestrate judgment, never add a judge | No gate is certified, softened or omitted in a meeting agenda; state changes in artifacts, not in standups | [`templates/rituals.md`](../templates/rituals.md), `weekly-review` | `weekly-review/certify-in-standup` |
| **Auditability** — the denominator is always shown | Coverage names what shipped against what ran through a ledger; work that bypassed the machine is reported, never dropped | `period-review` | `period-review/coverage-laundering` |
| **Strategy integrity** — no grading yourself in hindsight | The period's intent is declared before the period runs; a mid-course amendment is legal only dated at the moment strategy changed | `period-review` | `period-review/hindsight-amendment` |
| **Statistical honesty** — precision the sample did not earn | Below n=10, judgment renders as counts, never a percentage; one period is never a trend | `period-review` | `period-review/small-n-percentage`, `period-review/single-period-trend` |
| **Maturity honesty** — no placement the evidence did not earn | A team is placed at what the majority demonstrates, or not placed at all | `team-ai-baseline` | `team-ai-baseline/tools-and-mandate-only`, `uneven-team-flattery` |
| **Immutable record** | Frozen period reviews are never edited; the trend is a sequence of files, and `git log` is the event log | `design-os.reviews/`, git | *(structural — no fixture; git enforces it)* |
| **Change governance** — the rules are themselves tested | Every change to a judgment surface ships with an adversarial fixture, run before merge. v0.17 caught three of its own regressions this way | [TESTING.md](../TESTING.md), `.github/workflows/gates.yml` | the suite itself |

## What makes a team's own governance official

The crosswalk above says what this library guarantees. It does not say what makes *your*
commitments binding. That question matters more, and it has a mechanical answer.

Nothing here is official because a document declares it — authority asserted by role is
the governed checkmark this library refuses. A commitment is official when five things
are true, and each one is already mechanized:

1. **Declared.** Written into `design-os.profile.yaml` — decision rights, cadence, metric
   definitions and their sources, classification — or into the period's
   `<period>.intent.md` for goals, bet mix and bet budget. **The profile is the charter.**
   There is no second policy document to drift away from the system: the file the skills
   read is the file that binds.
2. **Ratified.** Landed by the human who holds that right, in a pull request. The merge is
   the ratifying act; the diff is its record. A declaration nobody with the right merged
   is a proposal.
3. **Enforced at the moment of work.** Skills read the declaration and refuse against it
   where the work happens — not in a quarterly audit that finds the breach a season late.
4. **Amendable, dated.** Commitments change by dated append, original intact. A
   retroactive edit is hindsight, and `period-review` refuses to credit it.
5. **Audited.** The close reads declared against observed; `git log` on the profile is the
   trail. Neither step requires a service, a dashboard, or a vendor.

A commitment missing any of the five is an aspiration, and should be described as one.

**For an auditor, in one sentence:** the control is not a signature — it is a refusal, with
a test behind it and a diff underneath it.

## Standards crosswalk

For teams that must map this to an existing framework. The mechanisms do not change; only
the vocabulary does.

| NIST AI RMF | Design Team OS |
| --- | --- |
| **Govern** | the profile (decision rights, cadence, definitions) · [`rituals.md`](../templates/rituals.md) · the five conditions above |
| **Map** | Gate 1 — a named pain with its evidence, the goal it maps to, the work's class |
| **Measure** | Gate 2 triage against a pre-registered bar · Gate 3 validation and outcome readout · calibration at the close |
| **Manage** | owned bets with named owners and review dates · recorded kills · the period review |

For ISO/IEC 42001: git history is the operational record, frozen period reviews are the
management-review artifacts, and the fixture suite is the evidence of control testing.

## How people run it

Authority is one thing; knowing what to do on Monday is another. The role lanes in
[ADOPTION.md](../ADOPTION.md#role-lanes) carry it: what each role runs, supplies and
reads — and what they may ratify, may never do, where their act is recorded, and what
happens if they skip it.

When a gate refuses you, that is the system working, and the refusal is meant to teach:
what is missing, why it is load-bearing, the smallest step that would change the verdict,
and what good looks like. The anatomy is written up in
[refusal-anatomy-and-evidence-contracts.md](refusal-anatomy-and-evidence-contracts.md).

## What this page does not claim

- **Not a compliance certification.** This is a set of mechanisms and the tests that prove
  they hold. It satisfies no regulator by itself.
- **Not model governance.** Nothing here governs weights, training data, or inference. It
  governs whether the *work* an AI helped produce earned what it claims.
- **Not a substitute for your own review boards.** A sign-off from your risk or
  architecture function is recorded here as an artifact of a decision — who signed, when,
  against which version — and it satisfies your organization's gate, never one of these
  three.
