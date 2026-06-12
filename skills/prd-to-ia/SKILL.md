---
name: prd-to-ia
description: Use when turning a PRD or requirements document into a first pass information architecture. Triggers on a pasted or linked PRD plus a request for an IA, sitemap, screen list, or structure. Always returns what was excluded and why, not just the IA.
---

# PRD to IA

You are doing the scoping judgment a senior designer does before any structure gets drawn: deciding which part of this document is actually a design problem.

## Before you draft

Read the entire PRD first. Identify the business goal and the customer pain the document claims to serve. If the PRD states neither, stop and say so. Name what is missing and ask for it. Do not invent a goal to make the work proceed.

An implied goal counts as missing. If the PRD suggests a goal without stating it, name your inference, then still stop and confirm it before drafting.

## Produce three sections, always in this order

**1. The IA.** Screens or sections, their hierarchy, and the primary flows between them. First pass means breadth over depth: every surface named, no surface fully specified.

**2. Exclusions.** Everything in the PRD you deliberately left out of the IA, each with one line of reasoning. Engineering constraints, GTM plans, legal requirements, and feature ideas without a stated user need all belong here. This section is the point of the skill. Nothing from the PRD gets silently dropped. Every piece of the document either appears in the IA or appears here with a reason.

**3. Open questions.** The gaps that block confidence in this structure, phrased so a Head of Design can take them straight into a stakeholder conversation.

## Quality bar

The IA is wrong if a reader cannot trace each top level section back to the stated goal or pain. The exclusions list is wrong if it is empty. A forty page PRD always contains things that are not design problems.
