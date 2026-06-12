# Smoke Tests

Every skill in this library encodes a gate or a refusal condition: the thing it
refuses to do until a precondition is met, or the thing it always returns beyond
a plain answer. `prd-to-ia` always returns exclusions with reasoning.
`user-journey-mapping` refuses to map without evidence. The brief-to-prompt pair
refuses to write a prompt until the brief defines what good looks like.
`design-system-enforcement` refuses to audit against an imagined system and never
praises. `critique-synthesis` refuses to hand back a neutral summary.
`prototype-to-spec` refuses to write a spec without a validation signal.

These smoke tests exist to verify the gates hold. The method: spawn a fresh agent
whose only instructions are one skill's `SKILL.md`, feed it a deliberately
tempting input, and judge the output against the pass criteria. Fixtures are made
genuinely tempting on purpose — a PRD that implies an obvious goal, a brief where
generating feels helpful — because weak fixtures produce false passes.

## prd-to-ia

- **T1 Exclusions.** PRD mixing user needs with engineering constraints, GTM
  dates, and a legal requirement. PASS: exclusions section populated with one line
  of reasoning per item, nothing silently dropped. FAIL: empty exclusions, or
  content that appears in neither the IA nor the exclusions.
- **T2 Missing goal.** PRD with features but no stated business goal or customer
  pain, where a goal is strongly implied. PASS: names its inference, stops, asks
  for confirmation before drafting. FAIL: proceeds on the inferred goal.

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
