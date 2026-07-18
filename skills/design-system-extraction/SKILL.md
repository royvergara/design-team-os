---
name: design-system-extraction
description: Use when producing a design-system reference from a team's existing components, tokens, and patterns — the reference design-system-enforcement needs to audit against. Triggers on existing UI source (a component file, a codebase, exported tokens) plus a request to extract, document, or produce the design system. Returns an evidence-backed reference with its conflicts named, never an invented system.
---

# Design System Extraction

You extract the system a team already has. You do not design one. The output is a reference derived from real source, with every rule tied to where it was found and every inconsistency left standing as a decision the team still owes.

## Before you extract

Require real source: components, tokens, or patterns as a file, a codebase path, or a pasted excerpt. If there is nothing concrete to read — just a request for "our design system" with no artifacts behind it — stop and ask for the source. Authoring a reference from best practices or what a system like theirs usually looks like is worse than none, because it hands `design-system-enforcement` an imagined ruler and every later audit inherits the fiction.

If a `design-os.profile.yaml` is present, read `design_system.component_catalog` for where the components and tokens live, and offer to write the result to `design_system.reference` — the field `design-system-enforcement`, `brief-to-prompt`, and `prototype-to-spec` all read (see [templates/project-profile.schema.md](../../templates/project-profile.schema.md)). The profile tells you where to look; it never substitutes for source that isn't there.

## The extraction

Derive the reference in three parts, and put in it only what the source actually and consistently supports:

- **Tokens** — color, spacing, type, radius, elevation. A value earns a place as a rule only when it recurs across the source. Record each with where it was found.
- **Components** — the reusable set, with the variants and props they actually expose, not the ones they should.
- **Patterns** — the interaction and layout conventions the source repeats often enough to be a convention.

What earns "rule": at least two independent occurrences — the same value copy-pasted is one signal, not two. One occurrence is a sample, and some things are honest singletons (the app's one modal); say which. Unsure whether recurrence is real? Sample, not rule.

Fidelity is also capped by what the source can prove. Code and token files yield declared values; screenshots and mocks yield measured observations that cannot know intent. A value read off an image is an observation, never a token — mark the difference, because enforcement will lean on it.

## Conflicts and gaps

This is the part that separates a reference from confident noise. Real source is inconsistent — three shades called "primary," padding that is 16 in one place and 12 in another. When usage diverges, you do not pick a winner and present it as the rule. You record the divergence as an open conflict: the competing values, where each was found, and that the team still owes a decision. Crowning one variant silently is exactly the laundering `design-system-enforcement` exists to catch — do not manufacture it upstream.

Then name the gaps: what a complete reference needs that this source could not supply — no elevation scale defined anywhere, accessibility standards never stated, motion untouched — so a partial reference is never mistaken for a whole one.

## The coverage map and the verdict

Close every extraction with a coverage map: one line per dimension — color, spacing, type, radius, elevation, components, patterns, accessibility, motion — marked **covered**, **contested**, or **absent**. This map is the hand-off contract: `design-system-enforcement`'s "what was NOT checkable" is exactly your contested-plus-absent set, so the map is what makes a later clean audit honest.

Then say which of three states the source landed in — a state, never a score:

- **Reference** — enough consistent, evidence-backed rules that enforcement has a real surface to audit against.
- **Reference with open conflicts** — auditable rules exist, but the contested set is large enough that the team owes decisions before this is a stable ruler.
- **Decision backlog, not a system yet** — so little consistent signal that a reference-shaped artifact would be false precision. This is a finding, not a failure, and it is not a refusal: real source was read, so you still deliver — the ranked list of decisions (highest-collision first) that would create a reference worth enforcing, with the evidence for each side. Straining a confident reference out of divergence is the same laundering as crowning a winner, at larger scale.

Never compress any of this into a maturity score or a percentage. A number launders judgment into false precision; the state names what the team actually has.

If a `design-os.work/<slug>.yaml` ledger is present, this reference is a Decision-gate input, not a passed gate — record a pointer to it under the work's decision context, never a `validated: true`.

## Quality bar

Every rule in the reference cites the source it was derived from; a rule that cannot point to evidence is a preference you invented, and preferences are what this skill exists to keep out. A reference that reads clean while the source underneath it conflicts has failed, however polished it looks — the conflicts are not noise to smooth over, they are the most useful thing you produce, because they are the decisions the team has not yet made.
