---
name: brief-to-prompt-v0
description: Use when converting a design brief into a prompt for v0 by Vercel. Triggers on a brief plus a request to start a v0 prototype or write a v0 prompt. Will not output a prompt until the brief defines what good looks like.
---

# Brief to Prompt, v0

The prompt is the last step of this skill, not the first. Most bad generated UI comes from briefs that never defined the quality bar.

## The gate, before any prompt

Verify the brief answers four things: the user and their pain, the scope (which screen or flow, exactly), the design system constraints (tokens, components, patterns that must be honored), and what good looks like (the must have behaviors and the criteria the team will judge output against).

If any are missing, return one compact list of the missing answers. Do not write a prompt around the gaps.

## When the gate passes, write one prompt

Structure it as: context (user, pain, goal in two sentences), scope (the exact screens and flows, and an explicit out of scope line), components and constraints (named design system elements, spacing, type, color rules), and behavior (the must have interactions).

One prompt, clean enough to paste. No prompt menus, no variants. Choosing the direction is the team's judgment, not the prompt's.

## After the prompt, always append a Discernment checklist

Three to five specific things to inspect in the generated output before iterating, derived from the quality bar in the brief. The checklist is what separates this from a prompt pack: the skill hands the team the prompt and the eyes to judge what comes back.
