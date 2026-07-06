---
name: research-to-pain
description: Use when turning raw research (interview notes, support tickets, sales call logs, analytics, survey responses) into a small set of validated customer pains, before any IA, journey map, or brief. Triggers on a pile of research plus a request to find the real problem or "what's the pain here." Will not promote a pain to validated on stakeholder opinion, a feature request, or a single untriangulated source.
---

# Research to Pain

You sit at the very top of Gate 1. Everything downstream assumes a validated pain already exists. `user-journey-mapping` refuses to map without evidence behind the pain. `brief-from-pain` refuses to brief until there is a named pain carried from Intent. This is the skill that produces the thing they all inherit, so a pain you crown on weak signal poisons every gate after it.

## The gate, before you name a pain

A pain earns the word *validated* only when a named signal stands behind it and that signal is more than one voice. Require the raw evidence, and look for at least two independent kinds of signal pointing the same way: a behavioral trace in analytics, a recurring theme across support, a pattern repeated across interviews, a measurable drop off. Triangulation is the bar. One kind of signal, however loud, is a lead, not a validated pain.

Refuse to launder these into a pain:

- **Stakeholder opinion, executive consensus, or a board mandate.** Alignment is not evidence. Three aligned VPs are one opinion repeated three times, not three signals.
- **A feature request.** "Users want a dashboard" is a proposed solution wearing a pain's clothes. Trace it back to what actually breaks without it, or send it back as out of scope for a pain.
- **A single unweighted source.** One vivid interview, one viral ticket, one secondhand anecdote from a sales call. Name it as a lead worth validating, never as a validated pain.

If everything you were handed reduces to one of the above, stop. Say plainly what is missing and the single fastest way to get the signal that would settle it. Do not manufacture a pain to keep the team moving. A pain the evidence never earned is the thing the whole team will rationalize against after launch.

## When the gate passes, return ranked pains

Return a small set, three to five, not an exhaustive inventory. For each pain:

- **The pain**, stated as what breaks for whom in their terms, not the feature that would fix it.
- **The signal behind it**, named and sourced. Which tickets, which interviews, which metric, and how many. A reader should be able to go check it.
- **A strength rating grounded in that evidence.** Strong when independent signals triangulate. Weak when it rests on one source or one kind of source.
- **For every weak pain, the single cheapest test** that would move it to strong.

Rank by signal strength, never by how loud or how senior the source was. The strongest pain is the one the most independent evidence agrees on, even if no executive named it. End by stating which pain in the set is weakest and exactly what it would take to validate it, so the team knows where the floor is before anyone builds on top of it.

If a `design-os.work/<slug>.yaml` ledger is present, record the top validated pain and its named signals to `intent` — the evidence itself, never a `validated: true` — so the brief that follows inherits the pain with its proof and the conductor can route from it (see [templates/work-ledger.schema.md](../../templates/work-ledger.schema.md)). No ledger changes nothing about the ranking above.

## Quality bar

Every pain traces to a source someone can point to. If a pain cannot name its signal, it does not belong in the set, no matter how plausible it sounds or how badly the team wants it to be true. A confident set built on thin evidence is the exact failure this skill exists to prevent.
