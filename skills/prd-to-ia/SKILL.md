---
name: prd-to-ia
description: Use when turning a PRD into a first-pass information architecture for a product design team. Triggers on a pasted or linked PRD plus a request for IA, sitemap, screen list, or "what screens does this need."
---

# PRD to IA

*Intent gate. Draft v0.1 — working starting point, expect to refine.*

## Purpose

Turn a PRD into a first-pass information architecture so the team can see the shape of what they are about to build before anyone opens a prototyping tool. The output is a structure to react to, not a finished IA. It exists to make the next conversation faster.

## When to use / not use

**Use it** when you have a PRD (or a solid brief) and need a screen list, sitemap, and primary navigation to start from.

**Do not use it** when there is no agreed problem yet (the work has not cleared the Intent gate — fix that first), or when the product already has a settled IA and you are doing a small feature add inside it. For a single screen, this is overkill.

## Inputs needed

- **Required:** the PRD or brief (pasted or linked).
- **Helpful:** existing product structure or current nav, known user roles, target platform (web / mobile / both), and any hard constraints (must reuse X, cannot add a top-level nav item).

If a helpful input is missing, assume a sensible default, proceed, and record the assumption in *Decisions you should check*. Do not stop to ask.

## The gate question

Intent asks: *does this map to a business goal and a real customer pain, and is the shape of the solution clear enough to commit to building?*

For this skill, made concrete: **What are the screens and sections, how do they nest, and what is the primary navigation — and does that structure actually serve the goal and pain in the PRD?**

## Process

1. **Restate the goal and the pain** in one or two sentences each, pulled from the PRD. If the PRD does not state a customer pain, say so plainly — that is an Intent-gate flag.
2. **Extract the user roles** the product serves. Note which role each later screen primarily serves.
3. **List the jobs** each role needs to get done, in the PRD's language.
4. **Derive the screen / section list** from those jobs. One job may need several screens; several jobs may share one.
5. **Group and nest** the screens into a hierarchy. Decide what is top-level navigation, what is nested, and what is a flow rather than a destination.
6. **Name the primary navigation** — the 3 to 7 things a user moves between most.
7. **Flag the open questions** the structure exposes (an orphan screen, a job with no home, two roles fighting over the same nav slot).

## Output format

Produce a single markdown artifact:

- **Goal** — one to two sentences.
- **Customer pain** — one to two sentences (or an explicit "not stated in PRD" flag).
- **User roles** — bulleted, one line each.
- **Screen list** — flat list, each tagged with the role it serves and the job it supports.
- **Sitemap** — nested hierarchy showing what lives under what.
- **Primary navigation** — the 3 to 7 top-level items.
- **Open questions** — structural tensions worth resolving before prototyping.
- **Decisions you should check** — every assumption you made for a missing input, each as "I assumed X because Y; change this if Z."

## Quality bar (self-check)

Before handing off, confirm:

- Every screen traces to a job, and every job has a home. No orphans either direction.
- The primary nav has 3 to 7 items, not 12.
- Each top-level item is a thing the user thinks about, not an internal system boundary.
- The goal and pain at the top are recognizable to whoever wrote the PRD.
- *Decisions you should check* is not empty unless the PRD genuinely left nothing open.

## Handoff → next gate

This IA feeds the **Decision gate**. Once the structure looks right, take a slice of it into a prompt-generation skill (e.g. `brief-to-prompt-v0`) to prototype, and run generated UI through `design-system-enforcement` to hold the quality bar.
