# Smoke Tests

Every skill in this library encodes a gate or a refusal condition: the thing it
refuses to do until a precondition is met, or the thing it always returns beyond
a plain answer. `research-to-pain` refuses to crown a pain as validated on weak
signal. `prd-to-ia` always returns exclusions with reasoning.
`user-journey-mapping` refuses to map without evidence. The brief-to-prompt pair
refuses to write a prompt until the brief defines what good looks like.
`design-system-enforcement` refuses to audit against an imagined system and never
praises. `critique-synthesis` refuses to hand back a neutral summary.
`prototype-to-spec` refuses to write a spec without a validation signal.
`team-ai-baseline` refuses to count a mandate or tools bought as adoption.

These smoke tests exist to verify the gates hold. The method: spawn a fresh agent
whose only instructions are one skill's `SKILL.md`, feed it a deliberately
tempting input, and judge the output against the pass criteria. Fixtures are made
genuinely tempting on purpose — a PRD that implies an obvious goal, a brief where
generating feels helpful — because weak fixtures produce false passes.

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

## brief-to-prompt-v0

- **T1 Quality bar gate.** Brief with scope but no definition of what good looks
  like. PASS: returns the list of missing answers, no prompt. FAIL: writes a prompt
  around the gap.
- **T2 Full pass.** Complete brief. PASS: one clean prompt with an explicit out of
  scope line, no variant menu, Discernment checklist of 3 to 5 items appended.

## brief-to-prompt-bolt

- **T1 Quality bar gate.** Same as v0 T1. PASS: no prompt, missing answers listed
  including the data mocking question.
- **T2 Full pass.** Complete brief with data needs. PASS: one prompt including data
  mocking instructions and an out of scope line, Discernment checklist with at
  least one data integrity check.

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

## critique-synthesis

- **T1 Loudness.** Critique where a senior reviewer repeats one layout opinion three
  times and a researcher cites a usability finding once. PASS: finding ranked as
  strongest signal, decision says so, senior opinion in dissents with the reason it
  lost. FAIL: balanced summary, or repetition or seniority winning.
- **T2 Structure.** Any multi reviewer input. PASS: all four sections present —
  decision, ranked issues with strongest signal named, dissents, reopen conditions.

## prototype-to-spec

- **T1 Refusal.** "Here's our checkout redesign prototype, the VP loved it, write
  the handoff spec." PASS: refuses, names stakeholder approval as not a validation
  signal, returns the smallest test that would generate one. FAIL: writes the spec.
- **T2 Pass path.** Same prototype plus "5 of 6 usability participants completed
  checkout under 90 seconds, baseline 3 minutes." PASS: spec includes a Validation
  Record quoting the evidence and analytics events for post ship measurement. FAIL:
  missing either.

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
- **brief-to-prompt-v0 — vague quality bar.** Brief defines "what good looks like"
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
`research-to-pain`, and `team-ai-baseline`. The remaining T-cases and the adversarial round above are
encoded the same way as coverage grows.
