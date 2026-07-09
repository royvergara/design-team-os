---
name: critique-synthesis
description: Use when synthesizing scattered critique from multiple reviewers into a direction. Triggers on pasted feedback from two or more people plus a request to make sense of it. Returns a ranked decision with the strongest signal named, not a summary.
---

# Critique Synthesis

You are killing the loudest voice problem. The output is a decision with reasoning, never a neutral summary that pushes the choosing back onto whoever reads it.

## Separate constraints from opinions before weighing anything

Some feedback is not a vote — it is a claim about the world: "legal requires the disclosure above the fold," "this must match the pattern shipping in Q3," "that component is deprecated." Constraints do not compete with user evidence; they bound the decision space the evidence gets weighed inside. Pull them out first and verify rather than weigh: a confirmed constraint frames the decision, a claimed-but-unverifiable one gets named as an open verification with an owner, and a preference dressed as a constraint ("we can't ship anything this dense" from taste, not fact) goes back in the pile as opinion. Filing a real constraint under dissents is how a synthesis gets ignored by everyone who knows the constraint is real — and remember that a senior reviewer's flat objection is sometimes a constraint with the claim left unstated: when a comment smells like context rather than taste, ask what is behind it before you rank it.

## Cluster, then weigh

Cluster the remaining feedback into distinct issues. Then weigh each issue by signal strength, in this order: direct user evidence beats everything on questions user behavior can answer, independent convergence (multiple reviewers raising the same issue separately) beats a single voice, domain relevance (the accessibility expert on an accessibility issue) beats general seniority.

Weigh user evidence by its quality, not just its type: sample size, task realism, and whether the finding could be an artifact of prototype fidelity (users "missing" a control that was low-fidelity placeholder is a fidelity artifact, not a finding). Thin user evidence — a two-person hallway test — still outranks pure opinion on a usability question, but name its thinness in the ranking so the decision carries its real confidence. And user evidence only trumps on questions it can answer: task success, findability, comprehension. On brand, strategic fit, or portfolio coherence it is one input, not the trump card.

Explicitly do not weight: volume, repetition by one person, seniority on issues outside the person's domain, or how recently the comment was made.

## Produce four sections

**1. The decision.** What changes and what stays, stated plainly. When two signals of genuinely equal strength conflict, the decision is the specific test that settles them — named as precisely as any other decision: what to run, with whom, and what result decides it. That is still a decision; a neutral summary is not.

**2. Ranked issues.** Each issue with the strongest signal behind it named: who or what the signal is, and why it outranked the others.

**3. Dissents.** The feedback that lost, recorded with the reason it lost. Dissent that vanishes from the record comes back in the next review twice as loud.

**4. Reopen conditions.** For each major call, the evidence that would legitimately reopen it. This is what makes the decision a decision instead of a mood.

## Quality bar

A reader who disagrees with the decision should still be able to see exactly which signal beat their position, and exactly what evidence would change the outcome.
