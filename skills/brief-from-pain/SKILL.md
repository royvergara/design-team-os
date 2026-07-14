---
name: brief-from-pain
description: Use when turning a validated customer pain and a first-pass IA into a design brief, before any prototype prompt. Triggers on a named pain plus a request for a brief or "what should we build." Will not write a brief until success is defined in advance; an unvalidated pain proceeds only as an explicit owned bet, and the bar is never excused.
---

# Brief from Pain

You are setting the bar the next three skills will enforce. A brief without a pre-registered definition of success is a wish, and wishes generate fifty prototypes with no way to choose.

## The gate, before any brief

Require two things: a named customer pain carried from Gate 1 with the evidence behind it, and the success criteria the team commits to before anything is generated.

If the "pain" is a feature request or a business goal ("leadership wants it," "we should add it"), stop — there is no pain to brief; send it back to Intent. If the success criteria are missing, stop and ask the team to set them now. Never invent the bar to keep things moving: a number you made up and the team never ratified is not a target, it is the thing you will rationalize against after launch. You may propose candidates to react to, clearly labeled as proposals, but the team ratifies them.

**The one exception on the pain side: an owned bet.** Work sometimes proceeds on an unvalidated pain on purpose — a contract commitment, a compliance requirement, a strategic bet on a new market. That path opens only when someone owns it explicitly: a named human with authority, an acknowledgment that the pain is assumed rather than validated, the reason, and a review date with the evidence that will judge the bet (see the bet block in [templates/work-ledger.schema.md](../../templates/work-ledger.schema.md)). Given all four, write the brief — opening with a plain statement that it is built on a bet, not a validated pain, and quoting the bet — and the success criteria below become doubly non-negotiable, because the bar is the only evidence this work will ever have. A bet never excuses the bar. And enthusiasm is not a bet: "leadership wants it" claims merit and stays refused; a bet declares the evidence absent and names its owner. If someone wants the bet path, name the four fields they must supply — never fill them in yourself.

## When the gate passes, write the brief

Include: the pain and its evidence, who it is for, what is being built, the scope with an explicit out-of-scope line — carry the exclusions from the IA so the prototype cannot quietly re-expand them — and the constraints the build must honor.

## Always end with "what good looks like"

The pre-registered, measurable success criteria, each tied to a signal the team can actually read, marked team-ratified not proposed. This is the section `brief-to-prompt`'s gate demands and `prototype-to-spec`'s Validation Record later scores against.

If a `design-os.work/<slug>.yaml` ledger is present, record the brief path to `decision.brief` and these ratified criteria to `decision.bar` — the criteria verbatim, never a `brief: done` — so triage and the readout later score against the same bar you set here. Ask the team once, at the same moment, for their stated confidence (0-100) that the work clears this bar, and record it to decision.bar.confidence; if they decline or don't know, leave it out and note the call enters the record unrated — never refuse the brief over a missing number (see [templates/work-ledger.schema.md](../../templates/work-ledger.schema.md)). No ledger changes nothing about the brief above.

## Quality bar

Every criterion is measurable and set before generating. If "what good looks like" is vague, the brief is not done, no matter how clean the rest is.
