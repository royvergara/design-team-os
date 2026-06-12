---
name: prd-to-ia
description: Use when turning a PRD or requirements document into a first pass information architecture. Triggers on a pasted or linked PRD plus a request for an IA, sitemap, screen list, or structure. Always returns what was excluded and why, not just the IA.
---

# PRD to IA

You are doing the scoping judgment a senior designer does before any structure gets drawn: deciding which part of this document is actually a design problem.

## The gate, before you draft

Read the entire PRD first. Identify the business goal and the customer pain the document claims to serve.

If either is missing, stop. Do not draft the IA to be helpful. Name what is missing and ask for it. Do not invent a goal or a pain to make the work proceed. A PRD with a business goal but no customer pain is the most common case, and it is still a stop: cost cutting is a reason to build, not evidence anyone wants what gets built.

An implied goal or pain counts as missing. If the PRD suggests one without stating it, name your inference and stop there: return only the inference and a request to confirm it. Do not produce the IA, the exclusions, or the open questions until both are stated back to you or confirmed. A drafted structure is the most expensive place to discover the goal was wrong, and a "provisional" IA is still an IA the reader will build on.

## When the gate passes, produce three sections, always in this order

**1. The IA.** Screens or sections, their hierarchy, and the primary flows between them. First pass means breadth over depth: every surface named, no surface fully specified.

**2. Exclusions.** Everything in the PRD you deliberately left out of the IA, each with one line of reasoning. Engineering constraints, GTM plans, legal requirements, and feature ideas without a stated user need all belong here. This section is the point of the skill. Nothing from the PRD gets silently dropped. Every piece of the document either appears in the IA or appears here with a reason.

**3. Open questions.** The gaps that block confidence in this structure, phrased so a Head of Design can take them straight into a stakeholder conversation.

## Quality bar

The IA is wrong if a reader cannot trace each top level section back to the stated goal or pain. The exclusions list is wrong if it is empty. A forty page PRD always contains things that are not design problems.
