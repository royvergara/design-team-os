---
name: critique-synthesis
description: Use when synthesizing scattered critique from multiple reviewers into a direction. Triggers on pasted feedback from two or more people plus a request to make sense of it. Returns a ranked decision with the strongest signal named, not a summary.
---

# Critique Synthesis

You are killing the loudest voice problem. The output is a decision with reasoning, never a neutral summary that pushes the choosing back onto whoever reads it.

## Cluster, then weigh

Cluster the feedback into distinct issues. Then weigh each issue by signal strength, in this order: direct user evidence beats everything, independent convergence (multiple reviewers raising the same issue separately) beats a single voice, domain relevance (the accessibility expert on an accessibility issue) beats general seniority.

Explicitly do not weight: volume, repetition by one person, seniority on issues outside the person's domain, or how recently the comment was made.

## Produce four sections

**1. The decision.** What changes and what stays, stated plainly.

**2. Ranked issues.** Each issue with the strongest signal behind it named: who or what the signal is, and why it outranked the others.

**3. Dissents.** The feedback that lost, recorded with the reason it lost. Dissent that vanishes from the record comes back in the next review twice as loud.

**4. Reopen conditions.** For each major call, the evidence that would legitimately reopen it. This is what makes the decision a decision instead of a mood.

## Quality bar

A reader who disagrees with the decision should still be able to see exactly which signal beat their position, and exactly what evidence would change the outcome.
