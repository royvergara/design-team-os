---
name: design-system-enforcement
description: Use when checking AI-generated or hand-built UI against a design system before it ships or gets reviewed. Triggers on a chunk of UI (code, screenshot, or component spec) plus a design system reference and a request to "make this match our system" or "check this against the DS."
---

# Design System Enforcement

*Decision gate. Draft v0.1 — working starting point, expect to refine.*

## Purpose

Hold generated UI to your design system. AI makes plausible-looking interfaces fast, and "plausible" drifts from your system in ways that are tedious to catch by eye. This skill produces a conformance report: where the UI breaks the system, and the specific fix for each break. It does not redesign — it enforces.

## When to use / not use

**Use it** on UI that is supposed to live inside an existing design system — a v0 / Bolt output, a generated component, a hand-built screen heading into review.

**Do not use it** for net-new exploration where the system does not exist yet, or when the goal is to *challenge* the system rather than conform to it. Enforcing a system on work meant to question it is the wrong tool.

## Inputs needed

- **Required:** the UI under review (code, screenshot, or component spec) and a design system reference (tokens, component docs, a Figma library description, or even a short written ruleset).
- **Helpful:** which surface this is (marketing vs product vs internal tool), the platform, and which rules are hard (tokens, spacing) vs soft (tone, density).

If the DS reference is thin, enforce what you can verify, say what you could not check, and record it in *Decisions you should check*. Do not invent rules the system has not stated.

## The gate question

Decision asks: *what do we prototype, and what does good look like?* Quality is half of that, and the design system is the written form of "good."

For this skill, made concrete: **Does this UI conform to the system, and where it does not, what is the exact change that brings it back in line?**

## Process

1. **Read the system reference first** and note the rules you can actually check against (tokens, type scale, spacing scale, component variants, states, content rules). You enforce only what the system defines.
2. **Inventory the UI** — list the components, tokens, and patterns it uses.
3. **Compare element by element** against the system. For each, decide: conforms, violates, or cannot verify.
4. **Classify each violation** by severity — *blocker* (breaks a token or accessibility rule), *should-fix* (off-scale spacing, wrong variant), *nit* (polish).
5. **Write the fix** for each violation: the specific token, value, or component to use instead. Concrete, not "use the right spacing."
6. **Flag anything the system does not cover** — UI that is neither conforming nor violating because the system is silent. That is feedback for the system, not the designer.

## Output format

Produce a single markdown report:

- **Verdict** — one line: ships as-is / minor fixes / needs work.
- **Violations** — a table or list, each with: element, rule broken, severity, and the exact fix.
- **Cannot verify** — checks you could not run, and why (missing reference, ambiguous rule).
- **Gaps in the system** — UI the system does not have an answer for; route to whoever owns the DS.
- **Decisions you should check** — assumptions made about thin or missing reference material.

## Quality bar (self-check)

Before handing off, confirm:

- Every violation names a specific rule from the system, not a personal preference. If you cannot cite the rule, it is a nit or a system gap, not a violation.
- Every fix is actionable — a value, a token, a component name — not a direction.
- Severity is honest: blockers are genuinely broken, not just things you would do differently.
- The verdict matches the violation list (no "ships as-is" sitting above three blockers).

## Handoff → next gate

A clean conformance report means the UI has met the quality half of the Decision gate. From here the work moves toward the **Value gate**: once a prototype is chosen, run `prototype-to-spec` to turn it into something buildable.
