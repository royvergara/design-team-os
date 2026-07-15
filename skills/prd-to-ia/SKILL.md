---
name: prd-to-ia
description: Use when turning a PRD or requirements document into a first pass information architecture. Triggers on a pasted or linked PRD plus a request for an IA, sitemap, screen list, or structure. Always returns what was excluded and why, not just the IA.
---

# PRD to IA

You are doing the scoping judgment a senior designer does before any structure gets drawn: deciding which part of this document is actually a design problem.

## The gate, before you draft

Read the entire PRD first. Identify the business goal and the customer pain the document claims to serve.

These are two different things and a PRD that has one rarely has the other. The **business goal** is why the company wants to build it (cut support costs 20%, lift conversion, hit a revenue target, reduce churn). The **customer pain** is the user's stated problem in their own world (a task they cannot finish, a confusion, an unmet need). A business goal is NOT a customer pain, no matter how reasonable: "reduce inbound support tickets" is a goal; the pain would be "users cannot find X so they call support." Before you decide the gate passes, run this check and write the answer: _Is there a sentence describing a USER's problem, distinct from the business's reason to build?_ If you cannot quote one, the pain is **missing** — do not infer it, do not let the goal stand in for it, go to the STOP PROTOCOL below.

If either is missing, stop. Do not draft the IA to be helpful. Name what is missing and ask for it. Do not invent a goal or a pain to make the work proceed. A PRD with a business goal but no customer pain is the most common case, and it is still a stop: cost cutting is a reason to build, not evidence anyone wants what gets built.

If a `design-os.profile.yaml` with a `goals:` block is present, check the PRD's stated goal maps to one of the period's declared goals and flag it when it maps to none — the profile is what a stated goal gets checked *against*, never a substitute for the PRD stating its own; the gate and the STOP PROTOCOL stand unchanged. In the stop block, `Stated goal:` quotes the PRD and only the PRD — a goal that lives in the profile but not the document is still `missing` (note the profile's goals separately, as what a stated goal would be checked against, never on the `Stated goal:` line).

An implied goal or pain counts as missing. If the PRD suggests one without stating it, name your inference and stop there: return only the inference and a request to confirm it. Do not produce the IA, the exclusions, or the open questions until both are stated back to you or confirmed. A drafted structure is the most expensive place to discover the goal was wrong, and a "provisional" IA is still an IA the reader will build on.

### When a goal or pain is missing or only inferred — STOP PROTOCOL

This is a hard stop, not a preface. When the business goal OR the customer pain is missing or merely implied, the ONLY thing you may output this turn is the block below. Do NOT output the IA, the exclusions, or the open questions in the same response — not even a "provisional" or "draft" one. Producing them after naming the gap is the exact failure this gate exists to prevent.

```
GATE NOT PASSED — confirmation needed before I draft.
Stated goal:   <quote the PRD itself, or "missing">
Stated pain:   <quote the PRD itself, or "missing / only inferred as: …">
To proceed, confirm or correct: <the one or two things you need stated back>
```

Both `Stated` lines quote **the document and only the document**. A goal that lives in
`design-os.profile.yaml` but not in the PRD is `missing` — write `missing`, never the
profile's goals, on the `Stated goal:` line. If the profile lists goals, you may add one
separate line *below* the block — `Profile goals (what a stated goal will be checked
against): …` — and the ask becomes: which of these, if any, is this PRD's goal? Confirmed
by the human, it counts; imported by you, it doesn't.

Only after the human states or confirms both do you move on to the three sections.

## When the gate passes, produce three sections, always in this order

**1. The IA.** Screens or sections, their hierarchy, and the primary flows between them. First pass means breadth over depth: every surface named, no surface fully specified.

**2. Exclusions.** Everything in the PRD you deliberately left out of the IA, each with one line of reasoning. Engineering constraints, GTM plans, legal requirements, and feature ideas without a stated user need all belong here. This section is the point of the skill. Nothing from the PRD gets silently dropped. Every piece of the document either appears in the IA or appears here with a reason.

**3. Open questions.** The gaps that block confidence in this structure, phrased so a Head of Design can take them straight into a stakeholder conversation.

## Quality bar

The IA is wrong if a reader cannot trace each top level section back to the stated goal or pain. The exclusions list is wrong if it is empty. A forty page PRD always contains things that are not design problems.
