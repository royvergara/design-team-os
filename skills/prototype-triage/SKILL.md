---
name: prototype-triage
description: Use right after a prototype is generated, to triage it against the brief before spending human review cycles on it. Triggers on a freshly generated prototype (v0 / Bolt output, code, or screenshots) plus the brief it was built from, or a request to "is this ready to review" / "does this meet the brief."
---

# Prototype Triage

*Readiness gate inside Decision (post-generate, pre-critique). Draft v0.1 — working starting point, expect to refine.*

## Purpose

Triage a freshly generated prototype against its brief *before* it earns human review. AI
generates prototypes faster than a team can review them; spending a critique session or a
design-system pass on a prototype that doesn't even address the brief is wasted motion. This
skill is the cheap gate that runs first: does this prototype demonstrably do what the brief
asked, in every state — yes, no, or can't-tell, per criterion. It does not critique taste
and it does not redesign. It checks readiness.

## When to use / not use

**Use it** the moment a prototype comes out of a generation step (`brief-to-prompt-v0` /
`brief-to-prompt-bolt`) and before any human review, design-system pass, or critique round.

**Do not use it** when there is no brief to check against (there is nothing to triage to —
go set the bar with `brief-from-pain` first), or for prototypes already past triage and into
critique. This is a one-time readiness gate, not an ongoing review.

## Project profile (read before asking for context)

Look for a project profile named `design-os.profile.yaml`:

- **If you can read files:** read it from the repo root; verify any value you rely on against
  its `source`; warn if `verified_against_commit` is behind HEAD.
- **If you cannot read files (chat / Project):** use the profile if pasted; otherwise ask
  once for the specific field you need, not a full questionnaire.
- **No profile present:** fall back to *Inputs needed* and flag the gap in *Decisions you
  should check*.

From the profile this skill pulls only `constraints` and `personas` (to sanity-check the
prototype against known limits and the intended user). **The brief — not the profile — is
the reference this skill triages against.** A profile cannot substitute for the brief, and
the gate below will not run without one.

## The gate question

Decision asks: *what do we prototype, and what does good look like?* Triage asks the
readiness half: *does this prototype demonstrably address every criterion the brief set,
before we spend a human on it?*

## The gate (this skill refuses)

1. **No brief, no triage.** If you are not given the brief (the pain, what's being built,
   and its pre-registered success criteria), you cannot triage — refuse and ask for it.
   Mirrors `design-system-enforcement`'s no-reference gate: you check against a stated bar,
   never an imagined one.
2. **No pass without each criterion addressed.** A prototype passes only when every brief
   criterion is demonstrably met. "Most of it looks done" is a fail. Partial coverage routes
   **back to generation** (`brief-to-prompt`) with the specific gaps, not forward to review.

**Never return "looks good."** This skill does not give taste verdicts or thumbs-up. Its
output is a per-criterion ledger, not an impression. If you find yourself writing "this looks
solid," stop — that is the critique step's job, and only on a prototype that already passed
triage.

## Process

1. **Read the brief** and extract its criteria as a checklist — every item under *what we're
   building* and *what good looks like*, plus the scope boundaries.
2. **Walk the prototype** against each criterion. For each, judge: **met** (demonstrably
   present), **missing** (not there), or **can't-tell** (can't verify from what you were
   given — say what you'd need).
3. **Check the non-happy states** the brief implies — empty, loading, and error. Prototypes
   default to the happy path; a prototype with no empty/error states is not review-ready.
4. **Check scope** — flag anything the prototype added that the brief put out of scope
   (silent scope creep is a fail signal, not a bonus).
5. **Decide the verdict** — pass only if every criterion is met and the required states
   exist; otherwise fail.
6. **If fail, write the punch list** — the specific gaps, phrased as fixes to feed back to
   the generation step, not vague notes.

## Output format

Produce a single markdown triage report:

- **Verdict** — one line: **pass** (ready for review) or **fail** (back to generate). No
  third "looks good" option.
- **Criteria ledger** — a table: each brief criterion → met / missing / can't-tell → the
  evidence (or what's absent).
- **States** — empty / loading / error: present or missing.
- **Scope** — anything out-of-scope that crept in.
- **Punch list** (fail only) — the specific gaps to fix, written as instructions back to
  `brief-to-prompt`.
- **Decisions you should check** — assumptions made for missing inputs.

## Quality bar (self-check)

Before handing off, confirm:

- Every brief criterion appears in the ledger — none skipped, none merged away.
- The verdict matches the ledger (no "pass" sitting above a "missing" row).
- Each can't-tell says what evidence would resolve it — it is not a polite fail.
- The empty / loading / error states were actually checked, not assumed.
- A fail's punch list is specific enough to regenerate from — no "make it better."
- Nowhere does the report praise the prototype or render a taste judgment.

## Handoff → next gate

- **Pass** → the prototype has earned human attention: send it to `critique-synthesis` (for
  human critique) and `design-system-enforcement` (for the quality bar).
- **Fail** → the punch list goes **back** to `brief-to-prompt-v0` / `brief-to-prompt-bolt`
  to regenerate against the gaps — before any human review cycle is spent. That back-edge is
  the point: triage is what keeps fast generation from flooding the team with prototypes that
  never met the brief.
