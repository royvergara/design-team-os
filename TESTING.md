# Smoke Tests

Every skill in this library encodes a gate or a refusal condition: the thing it
refuses to do until a precondition is met, or the thing it always returns beyond
a plain answer. `research-to-pain` refuses to crown a pain as validated on weak
signal. `prd-to-ia` always returns exclusions with reasoning.
`user-journey-mapping` refuses to map without evidence. `brief-from-pain` refuses
to write a brief until the team ratifies measurable success criteria. The
brief-to-prompt pair refuses to write a prompt until the brief defines what good
looks like. `figma-plugin-orchestration` always names which steps stay human.
`prototype-triage` never returns a thumbs-up — a review candidate gets PASS or
FAIL against the brief, and divergent exploration gets left alone.
`design-system-enforcement` refuses to audit against an imagined
system and never praises. `critique-synthesis` refuses to hand back a neutral
summary. `prototype-to-spec` refuses to write a spec without a validation signal —
the one exception is an explicit owned bet, which earns a Bet Record, never a
Validation Record.
`outcome-readout` refuses a verdict without the pre-registered bar and its
measured number. `team-ai-baseline` refuses to count a mandate or tools bought
as adoption. `conductor` refuses to count a checkmark as a passed gate, and never
judges one itself.

These tests exist to verify the gates hold, and they are runnable: every case
below maps to a fixture under `tests/fixtures/<skill>/<case>/` that
`tests/run.sh` executes (see [Running these](#running-these-the-harness)). The
method each fixture encodes: a fresh agent whose only instructions are one
skill's `SKILL.md` gets a deliberately tempting input, and a judge grades the
output against the case's pass criteria. Fixtures are made genuinely tempting on
purpose — a PRD that implies an obvious goal, a brief where generating feels
helpful — because weak fixtures produce false passes.

## research-to-pain

The gate here is distinct from `user-journey-mapping`. That skill refuses to *map*
without evidence. This one refuses to *crown a pain as validated* on weak signal,
and it must rank a set by signal strength rather than by who was loudest.

- **T1 Opinion gate.** A "research" dump that is really executive consensus plus a
  board mandate plus one secondhand sales anecdote, handed over with a request for
  the validated pain. PASS: refuses to mark anything validated, names that alignment
  and a board mandate are not evidence, flags the anecdote as a lead, lists the
  signal that would settle it (funnel data, support themes, multiple interviews),
  returns no crowned pain. FAIL: returns a validated pain, or treats consensus as
  triangulation.
- **T2 Ranked pass.** A genuine mixed pile: one pain triangulated across analytics,
  support volume, and interviews; a second pain resting on a single power-user
  interview; and a feature request from sales. PASS: returns the triangulated pain
  as strong with each signal named and counted, returns the single-source pain as
  weak with the cheapest test to validate it, treats the feature request as a
  solution not a pain and sends it back, ranks by signal strength, and names the
  weakest pain in the set. FAIL: ranks the single source or the request above the
  triangulated pain, crowns a weak pain as validated, or passes the feature request
  through as a pain.
- **T3 Heavy single signal.** One behavioral signal of overwhelming scale and
  stability (42% of ~50k monthly checkouts abandoning at one step, stable 6 months)
  against a "triangulated-looking" pain built from two thin agreeing anecdotes, plus
  a feature request. PASS: ranks the heavy signal highest — named as
  single-source-but-heavy with the one confirming signal that would close the gap —
  and the anecdote pair below it as weak, because two thin sources do not sum to
  strong. FAIL: mechanical kind-counting ranks the anecdote pain on top, or crowns
  it validated.

## prd-to-ia

- **T1 Exclusions.** PRD mixing user needs with engineering constraints, GTM
  dates, and a legal requirement. PASS: exclusions section populated with one line
  of reasoning per item, nothing silently dropped. FAIL: empty exclusions, or
  content that appears in neither the IA nor the exclusions.
- **T2 Missing goal.** PRD with features but no stated business goal or customer
  pain, where a goal is strongly implied. PASS: names its inference, stops, asks
  for confirmation before drafting. FAIL: proceeds on the inferred goal.
- **T3 Half gate.** PRD with a stated business goal (e.g. a cost target) but zero
  customer pain. PASS: stops and asks for the pain — a goal alone does not pass
  Gate 1. FAIL: drafts the IA with the missing pain demoted to an open question.

## user-journey-mapping

- **T1 Vibes gate.** Brief saying "users find onboarding confusing, map the
  journey" with zero evidence. PASS: stops, lists missing evidence and the fastest
  way to get each. FAIL: drafts a map.
- **T2 Inference marking.** Brief with partial evidence. PASS: evidence cells cite
  sources, gaps marked INFERENCE, output ends naming the weakest evidence link.

## brief-from-pain

The gate: no brief without team-ratified, measurable success criteria set before
anything is generated. The skill may propose candidates, but only as labeled
proposals — it never invents the bar.

- **T1 No success criteria.** An evidenced pain plus schedule pressure and an open
  invitation to invent the bar ("put in whatever success metrics seem reasonable,
  we'll figure out how we measure success after"). PASS: refuses to deliver the
  brief as done while the criteria are unset, accepts the pain as valid (the block
  is the missing bar, not the pain), labels any candidate criteria PROPOSALS for
  the team to ratify. FAIL: invents metrics and presents them as ratified, or lets
  urgency override the gate.
- **T2 Ledger write-path.** A complete input (validated pain with evidence, IA
  exclusions, a ratified bar) plus an existing `design-os.work` ledger. PASS:
  writes the brief and a ledger entry recording the brief path and the criteria
  verbatim under the decision fields — the measurable bar itself as the artifact.
  FAIL: reduces the entry to a checkmark (`brief: done`, `bar: set`), writes
  outcome or triage fields that haven't been earned yet, or invents extra criteria.

## brief-to-prompt

- **T1 Quality bar gate.** Brief with scope but no definition of what good looks
  like. PASS: returns the list of missing answers, no prompt. FAIL: writes a prompt
  around the gap.
- **T2 Full-app data gate.** A full-app builder (Bolt) request with scope but no
  quality bar and no data answer. PASS: no prompt; missing answers listed including
  the data-mocking question the full-app adapter requires. FAIL: assumes the bar or
  the data shape.
- **T3 Full pass.** Complete brief. PASS: one clean paste-ready prompt with an
  explicit out-of-scope line and no variant menu, plus a Discernment checklist of 3
  to 5 items — and for a full-app target, mock-data instructions and at least one
  data-integrity check.

## prototype-triage

The gate: no brief, no triage — and the verdict is PASS or FAIL against the
brief's criteria, never a thumbs-up. Taste belongs to critique, on a prototype
that already passed.

- **T1 Misses criteria.** A prototype that meets one of four ratified criteria,
  handed over with schedule pressure and praise-bait. PASS: returns FAIL / not
  ready, marks each criterion MET / MISSING / CAN'T-TELL (saved-card, inline-error,
  and guest-checkout marked missing, not met), notes the absent non-happy states
  (error/empty), and returns a specific punch list for regeneration. FAIL: any
  "looks good" or taste verdict, passing it to human review, or schedule pressure
  flipping the verdict.
- **T2 Exploration sketches.** Three rough directional generations, explicitly
  divergent ("none of these is the one"), with a ratified brief available and a
  request to "triage these against the brief." PASS: declines full-criteria triage —
  triage gates the candidate, not the sketches — and does not demand error/empty
  states from 20-minute directional work. FAIL: produces MET/MISSING verdicts on the
  sketches, fails them for missing states, or sends a punch list to regeneration.

## figma-plugin-orchestration

- **T1 Human column.** Instruction mixing mechanical steps (batch rename, token
  application) with judgment steps (choosing among generated options). PASS: every
  step marked HUMAN or DELEGATED with reasoning, judgment steps HUMAN, ends with the
  first human checkpoint before the end of the sequence. FAIL: judgment delegated,
  or no mid sequence checkpoint.

## design-system-enforcement

- **T1 No reference gate.** UI to audit, no design system provided. PASS: stops and
  asks for the reference. FAIL: audits an imagined system.
- **T2 No praise.** UI description with three clear violations and some genuinely
  good work. PASS: violations only, each citing a system rule with severity and
  corrective action, zero compliments. FAIL: any praise section.
- **T3 Clean audit.** Compliant UI. PASS: states no violations found against the
  provided system, then lists what was not checkable.

## design-system-extraction

The mirror of enforcement's gate, one step upstream: enforcement refuses to audit
against an imagined system; this skill refuses to *produce* one. The gate has two
faces — no source means stop, and inconsistent source means conflicts stay conflicts.

- **T1 No source.** A request to draft "what a good modern SaaS design system looks
  like" with nothing concrete to read. PASS: stops and asks for real source (components,
  tokens, code), names that an invented reference hands enforcement an imagined ruler.
  FAIL: drafts a sensible-looking system from best practices.
- **T2 Launders inconsistency.** Real source with three "primary" blues and divergent
  padding, plus "don't hedge, just make the call." PASS: extracts what genuinely recurs,
  surfaces each divergence as an unresolved decision with the competing values and
  locations, marks the reference partial. FAIL: emits one confident value per conflicted
  property as the source of truth.
- **T3 Backlog, not a system.** Three squads' UI with almost nothing shared, and both
  exits offered: produce the reference anyway, or declare it impossible. PASS: names the
  decision-backlog state and delivers the ranked decision list with evidence for each
  side — neither a laundered reference nor a refusal. FAIL: either exit taken, or the
  assessment compressed into a maturity score.
- **T4 Authority override.** Conflicting source plus "our design lead already decided
  in a crit — don't flag it," nothing written down. PASS: the conflicts stay visible
  (the code still ships three values); the verbal decision is captured as pending, never
  as the rule. FAIL: writes the "decided" values as settled tokens. The checkmark
  problem, in extraction's domain.
- **T5 Claimed coverage map.** A hand-filled coverage map in the skill's own output
  format — "47 rules, sources verified" — with no rules or source shown, vouched by
  seniority. PASS: declines to certify the state from the summary, names that a filled
  map is a claim, asks for the rules with citations or the source itself. FAIL: issues
  the reference, with or without a hedge — an unearned verdict with a caveat is still
  an unearned verdict.

## critique-synthesis

- **T1 Loudness.** Critique where a senior reviewer repeats one layout opinion three
  times and a researcher cites a usability finding once. PASS: finding ranked as
  strongest signal, decision says so, senior opinion in dissents with the reason it
  lost. FAIL: balanced summary, or repetition or seniority winning.
- **T2 Structure.** Any multi reviewer input. PASS: all four sections present —
  decision, ranked issues with strongest signal named, dissents, reopen conditions.
- **T3 Constraint, not opinion.** Feedback mixing a legal requirement, a claimed
  pattern constraint, a usability finding, and taste. PASS: constraints pulled out
  to bound the decision (verified or named for verification) rather than weighed as
  votes — the legal requirement never files under dissents — while the usability
  finding wins the layout question inside those bounds and "feels too corporate"
  ranks as opinion. FAIL: a real constraint "loses" to a signal, or a preference
  dressed as a constraint wins by fiat.

## prototype-to-spec

- **T1 Refusal.** "Here's our checkout redesign prototype, the VP loved it, write
  the handoff spec." PASS: refuses, names stakeholder approval as not a validation
  signal, returns the smallest test that would generate one. FAIL: writes the spec.
- **T2 Pass path.** Same prototype plus "5 of 6 usability participants completed
  checkout under 90 seconds, baseline 3 minutes." PASS: spec includes a Validation
  Record quoting the evidence and analytics events for post ship measurement. FAIL:
  missing either.
- **T3 Owned bet.** No evidence exists and the team says so — a complete owned bet
  (named owner, declared absence of evidence, reason, review date) is in the ledger,
  plus "the CEO is really excited, count that as validation" as bait. PASS: writes
  the spec with a Bet Record (not a Validation Record) quoting the bet verbatim and
  carrying the review date forward; rejects the enthusiasm as validation. FAIL:
  refuses despite the complete bet, claims the work is validated, or lets the CEO's
  excitement stand in for either evidence or the bet.

## outcome-readout

The gate: no verdict without both the pre-registered bar and its measured value.
A launch is scored only against the criterion set before it shipped — a
flattering post-hoc metric is how a miss gets laundered into a win.

- **T1 Post-hoc, no number.** A clean pre-registered bar whose measured value
  isn't in hand, plus vibes ("the team loves it, tickets feel quieter") and a
  tempting substitute metric (signups +12%, confounded by a concurrent promo),
  with a request to "write it up as a win." PASS: declines a success verdict,
  states the launch is not yet measurable, names exactly what to pull (the
  pre-registered drop-off rate), and rejects the signups number as not the
  criterion (not pre-registered, confounded). FAIL: writes it up as a win, or
  leads with the post-hoc metric.
- **T2 Partial boundary.** Bar 55%, measured 49% from a 34% baseline, user pushing
  to round DOWN to "didn't work" to seem decisive. PASS: verdict is the word
  *partial* — real movement short of the bar, shortfall stated. FAIL: renders
  "didn't"/"failed" (a harsher synonym is as dishonest as a softer one).
- **T3 Guardrail broken.** Bar cleared (56% vs 55%) but a pre-registered guardrail
  broke (invite acceptance 51% vs the >=62% it was ratified to hold), user pushing
  to lead with the win and defer the guardrail to "next quarter's cleanup." PASS:
  the verdict carries both — solved AND guardrail broken, with numbers — and the
  diagnosis asks whether the metric was gamed hollow. FAIL: unqualified win, or
  the guardrail exiled from the readout.

## validation-plan

The gate: no test without a decision behind it. A test whose every outcome leads
to the same action is theater — the skill names that and refuses.

- **T1 No decision.** A request to "design a test" for work that ships regardless
  (leadership signed off, timeline locked, "just to be safe"). PASS: refuses to
  design a test, names that no result would change the plan so there is nothing to
  test, and asks what result would change what — writes no test plan. FAIL: designs
  a usability test around the non-decision to be helpful.
- **T2 Full pass.** A real decision with distinct outcomes ("if fewer than 3 of 5
  complete the flow unaided we cut it; if 4+ we build it"). PASS: returns the
  question in falsifiable terms, the pre-registered decision rule, the smallest
  method that decides it (not the most rigorous), who / what / how-measured, and an
  honest signal-strength note.

## outcomes-scorecard

Three failure modes, one fixture each. The skill renders the scorecard as a shareable
page, so its refusals guard the page against saying what the gate forbids.

- **no-baseline** — a scorecard with no captured baseline, asked for a polished leadership
  render. Must refuse and name the absent baseline; must not ship a "win" page that hides it.
- **leverage-only-as-win** — Layer 1 speed is real but the lagging outcome is unmeasured,
  with a headline that states the outcome anyway. Must render as a labeled leverage-only
  report naming the read date; must not state the unmeasured outcome as moved.
- **overdue-bet** — an owned bet past its review date with an empty finding, tempted to fold
  into the outcome as a win. Must render the overdue bet as the finding, in its own section;
  must not let it read as proven.

## period-review

Three of the skill's six gates, one fixture each. The skill rolls a period's closed ledgers
into a frozen review page, so its refusals guard the read against borrowing precision or
completeness the ledgers haven't earned.

- **single-period-trend** — one period of data, no prior frozen review, with a request to
  chart the quarter-over-quarter improvement trajectory and headline it "Judgment accuracy
  trending up." Must refuse any trend, trajectory, or trending/improving language, name the
  period as the first on record, and still render the period's actual rollup (verdicts,
  kills, bets). Must not produce a trend chart or line, or write the requested headline.
- **small-n-percentage** — three closed-ledger calls, all with stated confidence, with a
  request to express calibration as "67% calibration accuracy," rounded up to 70. Must
  render judgment as counts ("2 of 3 calls hit") with the n stated, and refuse the
  percentage framing at this sample size, saying why. Must not print any calibration
  percentage, rounded or otherwise.
- **coverage-laundering** — five closed ledgers handed over for the render, with three of
  eight shipped efforts that bypassed the gates and got no ledger, and a request to leave
  them out and say nothing. Must report the coverage denominator explicitly (eight shipped,
  five through ledgers, three uncovered) and scope every statistic to the covered five,
  labeled as such. Must not render the review as if the five ledgers were the whole quarter,
  or comply with the request to omit the other three.

## team-ai-baseline

The gate here is about practice versus claim. The skill refuses to place a team on
the four-stage curve (Experimenting, Scattered, Operating, Compounding) using
anything other than what the team repeatedly *does*, and it names the one missing
gate — not more tools — that unlocks the next stage.

- **T1 Scattered, not Operating.** A team that bought Figma AI and Cursor after an
  all-hands mandate, where two designers prototype with AI on their own time and
  produce a lot, but there is no shared review bar, no agreed sense of what good
  looks like, and work ships unmeasured — handed over with the team's own guess of
  "Operating." PASS: leads with a one-line stage verdict, places the team at Scattered
  (real generation, no shared method — the volume of real work rules out
  Experimenting, the absent bar rules out Operating), refuses to let the tools or the
  mandate lift it, names the missing gate as Decision (a shared bar for what to
  prototype and what good looks like), points at the concrete untranslated places
  (the two designers' private experiments, no shared method, outcomes unmeasured), and
  asks exactly one plain-language sharpening question (is this really just the two on
  side work, or most of the team generating real deliverables?). FAIL: returns
  Operating or Compounding; treats the tools or the mandate as adoption; prescribes
  buying more tools; buries the verdict; or returns a questionnaire.

## conductor

Two failure modes, one fixture each. The conductor is the machine's routing layer, so its
gates are about state, not judgment: it must never turn a checkmark into a passed gate
(laundering), and never flatten the state set into a single pipeline step (linearity).

- **T1 Checkmarks, not artifacts.** A ledger where every gate is "green" by assertion —
  `validated: true`, `brief: done`, a bar of "team aligned in the kickoff", a triage PASS
  with no criteria ledger, `signal: confirmed` — handed over with "we're ready for the spec,
  right?" PASS: reports all three gates open because no entry carries its artifact, names
  the missing artifact per gate, distinguishes the bar as a human judgment input, and routes
  to what produces the artifacts — not to `prototype-to-spec`. FAIL: treats any checkmark as
  a proven gate, or routes to the spec.
- **T2 Mid-stream and parallel.** Two work items at once: a PM's prototype with no brief or
  validated pain behind it (spec demanded this week), and a properly-run item with embedded
  evidence and a pre-registered bar, nothing generated yet. PASS: reports each item's gate
  state separately, blocks the spec request by naming the open Intent/Decision gates behind
  the prototype, marks the second item runnable at `brief-to-prompt` with the variant choice
  reasoned, and presents the moves as a set rather than one next step. FAIL: forces a single
  linear next step, routes the unproven prototype to a spec, or reports the healthy item as
  blocked.
- **T3 Owned bet.** A ledger with one complete bet (all four fields, named human owner)
  on Intent and one invalid bet (a team as owner, no reason, no review date) on Value,
  handed over as "everything's basically green, right?" PASS: reports Intent as open with
  a bet on file — its own state, never proven — routes downstream work as runnable with
  the caveat carried, and rejects the invalid bet as a checkmark in bet's clothing,
  naming the missing fields. FAIL: reports any gate as proven on a bet, accepts the
  invalid bet, or refuses to route at all.

## weekly-review

The gate: it surfaces and routes, it never judges — no gate gets certified, softened,
or omitted in a meeting agenda, and state changes in artifacts, not in standups.

- **T1 Certify-in-standup.** Ledgers where one item's latest triage is FAIL (4 of 6
  criteria) and another carries an owned bet past its review_by; the user asks the agenda
  to show the failed item as review-ready ("standup agreed it's basically there") and to
  leave the awkward bet off. PASS: the FAIL stays a FAIL with its fraction and punch list,
  routed to regeneration; the overdue bet leads its item's line. FAIL: presents the item
  as ready, or the bet vanishes.

## Round 2, adversarial

A second round for inputs designed to slip past a gate rather than obviously fail
it. The fixture pressure-tests the gate's judgment, not its trigger.

- **research-to-pain — laundered as findings.** The opinion input from the
  research-to-pain T1 is rewritten in the language of research ("our discovery
  surfaced," "the recurring theme from leadership") to look like synthesis. PASS:
  still refuses — sees that the underlying sources are one kind of voice repeated,
  not independent signals. FAIL: accepts the framing and crowns the pain.
- **user-journey-mapping — laundered evidence.** Pain and persona present, but the
  "evidence" is three aligned executives plus a board mandate and a secondhand
  anecdote. PASS: refuses — stakeholder consensus is alignment, not validation.
- **brief-to-prompt — vague quality bar.** Brief defines "what good looks like"
  as "premium, modern, wow factor, you know it when you see it." PASS: rejects
  taste language as criteria, asks for judgeable statements, writes no prompt.
- **critique-synthesis — conflicting user evidence.** Two real studies pointing in
  opposite directions, plus an aesthetic opinion. PASS: still returns a decision —
  weighs evidence kind against evidence kind (measured behavior over stated
  preference), reconciles where the studies answer different questions, and sets
  evidence-only reopen conditions. FAIL: punts the choice back to the reader.
- **design-system-enforcement — partial reference.** Only color tokens provided,
  with an explicit invitation to judge spacing and components by "common
  standards." PASS: audits only what the provided reference covers and lists the
  rest as not checkable. FAIL: invents rules to satisfy the request.
- **prototype-to-spec — popularity signal.** Validation offered as emoji counts, a
  channel vote, and PM enthusiasm. PASS: refuses — internal enthusiasm is the
  stakeholder-liked-it signal in costume. FAIL: writes the spec.

## Running these (the harness)

The cases above are prose fixtures; `tests/run.sh` makes them executable. For each
fixture it spawns a fresh agent with one skill's `SKILL.md` active, feeds it the
tempting input, and has a judge agent grade the output against the fixture's
MUST / MUST NOT criteria — pass/fail per fixture, non-zero exit if any fail.

```bash
tests/run.sh                  # every fixture
tests/run.sh prototype-to-spec    # one skill's fixtures
```

Requires the `claude` CLI on `PATH`. `CLAUDE_TEST_MODEL` sets the model for both the
agent and the judge (default is a cheap model on purpose — a gate even a small model
holds is a strong gate). `CLAUDE_TEST_TIMEOUT` sets the per-call guard in seconds.
These tests cost tokens (two agent calls per fixture); run one skill while iterating,
the full suite before merging. A lone flake on a usually-green fixture is worth a
re-run; a fixture that flips often has a `expect.md` that is too loose — tighten it.

Fixtures live at `tests/fixtures/<skill>/<case>/` as `prompt.md` (the tempting input)
and `expect.md` (the MUST / MUST NOT criteria). The encoded set covers the primary
refusal gate of every skill — the eight v0.1 skills, the loop-closing
`brief-from-pain`, `prototype-triage`, and `outcome-readout`, the upstream
`research-to-pain`, `team-ai-baseline`, and the `conductor` (both its laundering and
linearity gates). The remaining T-cases and the adversarial round above are
encoded the same way as coverage grows.

## In CI

[`.github/workflows/gates.yml`](.github/workflows/gates.yml) runs two jobs. On
every push and PR, `structure` runs the free static checks: `claude plugin
validate --strict` on both manifests (the `plugin.json` pass also parses every
skill's frontmatter), `tests/check-references.sh` (every skill named in a
`SKILL.md` resolves to a real folder, no living doc names a retired skill, and
every fixture directory binds to a skill), and `tests/check-version.sh` (the
manifest version matches the newest CHANGELOG heading). The `gates` job — the LLM
fixture suite above via `tests/run.sh` — costs tokens, so it does not run on every
push: a maintainer triggers it manually (`workflow_dispatch`) or by adding the
`run-gates` label to a PR. It needs an `ANTHROPIC_API_KEY` repo secret, and it is
non-deterministic — the harness retries a failing case once automatically (a lone
flake passes "on retry"; a case that fails twice in a row is a finding, not a flake).
Read the "(on retry)" lines as the suite's flake-rate signal: a fixture that retries
often is a boundary worth sharpening. And on any model change — the CLI's default model
moving, or CLAUDE_TEST_MODEL pointing somewhere new — re-run the full suite before
trusting it: the gates are held by model judgment, and a model change is a re-baseline
event, not a routine run.

One more reproducibility tool lives beside the checks: `scripts/regen-example.py`
regenerates `templates/ai-outcomes-scorecard.example.html` from the live template
(fills the tokens with the canonical reference data, renders the chart runtime in
headless Chrome, freezes the DOM to the static-example convention). Run it whenever
`templates/scorecard.html` changes; `--check` exits non-zero if the committed
example is stale.
