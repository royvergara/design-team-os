---
name: prototype-to-spec
description: Use when turning a chosen prototype into a buildable engineering spec for a product design team. Triggers on a selected prototype (link, code, or screenshots) plus a request for a spec, handoff doc, or "what do engineers need to build this."
---

# Prototype to Spec

*Value gate. Draft v0.1 — working starting point, expect to refine.*

## Purpose

Turn a chosen prototype into a buildable spec. A prototype proves an idea; a spec lets engineering ship it without guessing. This skill reads the prototype and produces the handoff: what to build, how it behaves, what it depends on, and how you will know it worked. The last part — how you will know it worked — is what ties the build back to the Value gate.

## When to use / not use

**Use it** once a prototype has been chosen and is heading to engineering, and you need a written spec rather than "here's the Figma, ping me with questions."

**Do not use it** while still exploring or comparing options (nothing is chosen yet), or for throwaway prototypes that will never be built. Spec'ing work that will not ship is wasted motion.

## Project profile (read before asking for context)

Before asking for design-system, analytics, route, or spec-path context, look for a
project profile named `design-os.profile.yaml`:

- **If you can read files:** read it from the repo root. Before trusting any value you
  rely on, verify it against its `source` (e.g. grep `posthog.capture(` for events). If
  `verified_against_commit` is behind HEAD, treat the values as possibly stale and say so.
- **If you cannot read files (chat / Project):** use the profile if it was pasted into
  context; otherwise ask once for the specific field you need, not a full questionnaire.
- **No profile present:** fall back to the *Inputs needed* below and flag the missing
  context in *Decisions you should check*.

From the profile this skill pulls: `design_system.reference` and `component_catalog` (for
the Components section), `analytics.tool` + `analytics.events` (for Instrumentation),
`spec_output` (where to write the spec), `personas`, and `constraints`.

Never let the profile override a refusal gate. The profile can supply the analytics
*vocabulary*, but it does not set the success metric — a human still does that, and a build
with no metric is still a Value-gate flag (below).

## Inputs needed

- **Required:** the chosen prototype (link, code, or screenshots) and the goal it is meant to serve.
- **Helpful:** the PRD or IA it came from, the success metric the work is supposed to move, known technical constraints, and the design system in play. *When a profile is present, the design system, analytics vocabulary, spec path, personas, and constraints come from it — don't re-ask for those.*

If the success metric is missing, that is a Value-gate flag — spec the build anyway, but call it out loudly in *Decisions you should check*. A build with no way to tell if it worked has not cleared the Value gate. **A profile does not satisfy this:** it can name the event vocabulary, but the metric and its target bar are a human judgment, not a profile field.

## The gate question

Value asks: *did it solve the pain and move the needle?* You cannot answer that after the fact unless the spec sets it up before the build.

For this skill, made concrete: **What exactly gets built, how does it behave in every state, and how will we know — with a real signal — whether it solved the pain?**

## Process

1. **Restate the goal and the success metric** the build is meant to move. If there is no metric, propose one and flag it.
2. **Walk the prototype** screen by screen and flow by flow. List every screen, component, and interaction.
3. **Specify behavior** for each: default, loading, empty, error, and edge states. Prototypes show the happy path; the spec owes the rest.
4. **Name the data and dependencies** — what each screen reads and writes, what services or APIs it leans on, what must exist for it to work.
5. **Capture the rules** — validation, permissions, business logic implied by the prototype but not visible in it.
6. **Define done** — acceptance criteria an engineer can check, plus the instrumentation needed to read the success metric later.
7. **List open questions** the prototype does not answer.

## Output format

Produce a single markdown spec:

- **Goal & success metric** — what this moves, and the signal that proves it.
- **Scope** — what is in, what is explicitly out.
- **Screens & flows** — each with its states (default / loading / empty / error / edge).
- **Components** — reused vs new; reference the profile's `component_catalog` and `design_system.reference` where they apply (e.g. name the existing primitive/class instead of describing a new one).
- **Data & dependencies** — reads, writes, services, preconditions.
- **Rules & logic** — validation, permissions, business rules.
- **Acceptance criteria** — checkable, per screen or flow.
- **Instrumentation** — what to track to read the success metric. Reuse the profile's existing `analytics.events` where one already covers the signal; only propose a new event when none fits, and name it in the profile's convention.
- **Open questions** — what the prototype left unanswered.
- **Decisions you should check** — assumptions made for missing inputs.

## Quality bar (self-check)

Before handing off, confirm:

- Every screen has its non-happy-path states specified, not just the default.
- The success metric has matching instrumentation — you can actually measure what you claimed.
- Acceptance criteria are checkable, not aspirational ("loads fast" → "first content under 1s on 4G").
- Scope says what is *out*, not only what is in.
- Nothing in the spec contradicts the design system the prototype was held to.

## Handoff → next gate

This spec closes the loop. It goes to engineering to build, and its **instrumentation feeds back to strategy**: once shipped, the success metric tells you whether the work solved the pain and moved the needle — the Value gate's real answer — which informs the next round of Intent.
