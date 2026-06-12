---
name: brief-to-prompt-bolt
description: Use when converting a design brief into a prompt for Bolt.new. Triggers on a brief plus a request to start a Bolt prototype or write a Bolt prompt. Will not output a prompt until the brief defines what good looks like.
---

# Brief to Prompt, Bolt

Same discipline as brief-to-prompt-v0, tuned for Bolt's full app scaffolding. The prompt is the last step, not the first.

## The gate, before any prompt

Verify the brief answers: the user and their pain, the scope of the app or flow, the design system constraints, what good looks like, and one Bolt specific question: what data does the prototype need, and is mocked data acceptable. If any are missing, return the list of missing answers and stop.

## When the gate passes, write one prompt

Structure it as: context (user, pain, goal), the app scope with an explicit out of scope line, the screens and navigation between them, components and constraints from the design system, data instructions (what to mock and what shape the mock data takes so the prototype feels real), and the must have behaviors.

Bolt builds more than a screen, so the prompt must say what NOT to build. Scope creep in the prompt becomes a week of generated code nobody asked for.

## After the prompt, always append a Discernment checklist

Three to five specific things to inspect in the generated app before iterating, including at least one data integrity check, because mocked data that looks wrong undermines the validation the prototype exists to produce.
