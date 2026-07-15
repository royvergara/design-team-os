---
name: brief-to-prompt
description: Use when converting a design brief into a prompt for an AI builder — v0, Bolt.new, Lovable, Replit, Claude Artifacts, Framer, or any generator. Triggers on a brief plus a request to write a prototype or build prompt for a named tool. Will not output a prompt until the brief defines what good looks like; full-app builders also need the data settled first.
---

# Brief to Prompt

The prompt is the last step of this skill, not the first. Most bad generated UI comes from briefs that never defined the quality bar. The skill is tool-agnostic: the gate, the prompt structure, and the discernment step are the same for every builder — the target only tunes a few lines (see Tool adapters). You do not pick the tool; the request does.

## The gate, before any prompt

Verify the brief answers four things: the user and their pain, the scope (which screen, flow, or app, exactly), the design system constraints (tokens, components, patterns that must be honored), and what good looks like (the must-have behaviors and the criteria the team will judge output against).

For a full-app builder, add one question: what data does the prototype need, and is mocked data acceptable? A scaffolded app with no data story generates something that can't be validated.

If any are missing, return one compact list of the missing answers. Do not write a prompt around the gaps, and never invent the quality bar or the data shape to be helpful.

## When the gate passes, write one prompt

One prompt, clean enough to paste. No prompt menus, no variants — choosing the direction is the team's judgment, not the prompt's. Structure it as:

- **Context** — user, pain, goal in two sentences.
- **Scope** — the exact screens and flows, with an explicit out-of-scope line.
- **Components and constraints** — named design-system elements, spacing, type, color rules.
- **Behavior** — the must-have interactions.

## Tool adapters

Read the target from the request and adapt these lines. If a `design-os.profile.yaml` is present, take the design-system constraints from its `design_system.*` fields instead of re-asking, and when the request names no tool, use `tools.builder` as the target — the quality-bar gate stands either way, and if neither the request nor the profile names a builder, ask. This is a selection, not a menu — you emit one prompt for the tool named, never a set to choose from.

- **Screen / component generators (v0)** — scope the prompt to the one screen or component. Keep it tight to that surface; don't let it reach for a whole app.
- **Full-app builders (Bolt.new, Lovable, Replit)** — add a **data** section: what to mock and the shape of the mock data, so the prototype feels real. And because these scaffold more than a screen, the prompt must say what NOT to build — scope creep here becomes a week of generated code nobody asked for.
- **Any other builder (Claude Artifacts, Framer, "build it in React")** — keep the four sections above; add the data section only if the prototype needs real-feeling data. When the tool's prompting conventions are unknown, ask the one question that would change the prompt rather than guessing.

## After the prompt, always append a Discernment checklist

Three to five specific things to inspect in the generated output before iterating, derived from the quality bar in the brief. The checklist is what separates this from a prompt pack: the skill hands the team the prompt and the eyes to judge what comes back. For a full-app builder, include at least one data-integrity check — mocked data that looks wrong undermines the validation the prototype exists to produce.

## Quality bar

One paste-ready prompt with an explicit out-of-scope line and a Discernment checklist, or a list of what the brief is missing — never a prompt built around a gap the brief never closed.
