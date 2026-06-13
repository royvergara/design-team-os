---
name: brief-from-pain
description: Use when turning a validated customer pain and a first-pass IA into a design brief before anyone writes a prototype prompt. Triggers on a named pain (from journey mapping or research) plus a request for a brief, "what should we build," or "what does good look like" for a chosen problem.
---

# Brief from Pain

*Bridges Intent → Decision. Draft v0.1 — working starting point, expect to refine.*

## Purpose

Turn a validated pain into a brief that says what to build and — before anything is
generated — what good looks like. This is the missing handoff between the Intent gate
(which named the pain) and the Decision gate (which refuses to prototype without a quality
bar). A brief without measurable success criteria set up front isn't a brief; it's a wish.

## When to use / not use

**Use it** once a pain is named and evidenced and the team is about to prototype, and you
need a brief that a prompt-generation skill (`brief-to-prompt-v0` / `brief-to-prompt-bolt`)
can consume.

**Do not use it** when the pain is still a hunch with no evidence (go back to Gate 1 —
`user-journey-mapping` / research), or when you already have a brief with a success bar and
just want to prototype (skip ahead to the prompt skills). This skill exists to set the bar,
not to restate one that exists.

## Project profile (read before asking for context)

Before asking for analytics, persona, or evidence context, look for a project profile named
`design-os.profile.yaml`:

- **If you can read files:** read it from the repo root. Before trusting any value you rely
  on, verify it against its `source`. If `verified_against_commit` is behind HEAD, treat the
  values as possibly stale and say so.
- **If you cannot read files (chat / Project):** use the profile if it was pasted into
  context; otherwise ask once for the specific field you need, not a full questionnaire.
- **No profile present:** fall back to *Inputs needed* below and flag the missing context in
  *Decisions you should check*.

From the profile this skill pulls: `personas` (who the brief serves), `evidence_sources` and
`analytics.events` (so success criteria are grounded in signals you can actually measure),
and `constraints`.

Never let the profile satisfy this skill's gate. The profile can name the metric
*vocabulary*; it cannot supply the pain or set the success bar. Those are human inputs and
the gate below holds out for them.

## The gate question

Intent asks: *does this map to a business goal and a real customer pain?* The bridge to
Decision adds: *and have we said, in advance, what would prove we solved it?*

For this skill, made concrete: **What are we building, for whom, and what measurable result —
set before we generate anything — would tell us it worked?**

## The gate (this skill refuses)

Do not produce a brief unless both are present:

1. **A named pain carried from Gate 1** — a real, evidenced customer pain, not a feature
   request or a business goal wearing a pain's clothes. If all you have is "leadership wants
   X" or "we should add Y," stop: there is no pain, so there is nothing to brief. Send it
   back to the Intent gate.
2. **Success criteria the human sets before generating** — a pre-registered, measurable bar.
   If the team can't say what good looks like before building, that is the conversation to
   have now, not after fifty prototypes.

**Never invent the bar.** You may *propose* candidate criteria to react to, clearly labeled
as proposals, but the team ratifies them. A success criterion you made up and the team never
agreed to is not a bar — it's a number you'll rationalize against later. If the team won't
commit to criteria, say the brief is not ready and why; do not paper over it with a
plausible-sounding metric.

## Process

1. **Restate the pain and its evidence** in one or two sentences, pulled from the journey
   map or research. If you cannot point to evidence, that is a gate failure — stop and flag.
2. **Name who it's for** — the persona(s) the brief serves (from the profile if present).
3. **Define scope** — what this brief covers and, explicitly, what it does not. Carry
   forward the exclusions from `prd-to-ia` so the prototype doesn't quietly re-expand them.
4. **Set "what good looks like"** — work with the human to pre-register measurable success
   criteria. Ground each in a signal you can actually read (tie to `analytics.events` /
   `evidence_sources` where they exist). Propose candidates to react to, but make the team
   commit; never finalize criteria the team did not agree to.
5. **State constraints** the build must respect (platform, design system, technical limits).
6. **List open questions** the brief leaves for the prototype phase to resolve.

## Output format

Produce a single markdown brief:

- **Pain & evidence** — the validated pain and what proves it's real.
- **Who it's for** — the persona(s).
- **What we're building** — a tight description of the intended solution.
- **Scope** — in, and explicitly out (exclusions carried from the IA).
- **What good looks like** — the pre-registered, measurable success criteria, each tied to a
  signal that can read it. Marked clearly as team-ratified, not proposed.
- **Constraints** — what the build must respect.
- **Open questions** — left for the Decision gate to resolve.
- **Decisions you should check** — assumptions made for missing inputs, each as "I assumed X
  because Y; change this if Z."

## Quality bar (self-check)

Before handing off, confirm:

- The pain is a real customer pain with evidence, not a feature request or a business goal.
- Every success criterion is measurable and named *before* generating — no "we'll know it
  when we see it," no metric invented here and presented as agreed.
- Each criterion maps to a signal you could actually read (an event, a research method).
- Scope says what is *out*, and the exclusions match the IA's.
- *What good looks like* is the thing `brief-to-prompt`'s gate will demand — if it's thin,
  the brief is not ready.

## Handoff → next gate

This brief feeds the **Decision gate**. Its *what we're building* and *what good looks like*
are exactly what `brief-to-prompt-v0` / `brief-to-prompt-bolt` need to refuse-or-generate,
and the pre-registered success criteria are what `prototype-to-spec`'s Validation Record
will later score against. Set the bar well here and the rest of the spine can hold it.
