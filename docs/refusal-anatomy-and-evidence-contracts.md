# Refusal anatomy + evidence contracts — validated design, not yet adopted

Design residue from the `design-system-extraction` drop (Jul 18, 2026). Two related
designs were pressure-tested and held; neither is wired into the library yet. This note
is the artifact so the thinking survives the session that produced it.

## 1. The four-layer refusal anatomy

Today a refusal carries two layers consistently: *what's missing* and *the smallest next
step*. The validated upgrade is four, so a refusal teaches instead of only stopping:

1. **What is missing** — the gap, named precisely.
2. **Why it is load-bearing** — which gate principle this protects, one line. Turns
   "computer says no" into "here is the failure this prevents."
3. **The smallest step that earns it** — `validation-plan`'s whole job; every skill
   already gestures at this.
4. **What good looks like** — the shape of a passing artifact: a worked exemplar, the
   citable standard where one truly exists, excellence described as a state.

Layer 4's discipline, non-negotiable:

- **Cite or own.** WCAG 2.2 is a standard; pre-registration is a methodological norm.
  Those get cited. Everything else is *this library's bar*, owned as such — claiming
  industry consensus that doesn't exist is itself laundering.
- **Exemplars over prescriptions.** Show a passing artifact, never an answer key. Teach
  the shape of excellence, never the content of the answer (what a triangulated pain
  looks like — yes; which pain this team has — never).
- **States, never scores.** Excellence is a describable state a team can see itself
  against, not a maturity grade.
- **Close with the line: shape is never the gate.** An input that copies the exemplar's
  format with no evidence underneath fails exactly as it failed before the teaching
  existed.

Teaching happens **alongside** the refusal, never instead of it. Anything that softens a
refusal to improve experience is answering the wrong question (the roadmap's standing
rule).

### Pressure test (Jul 18)

Method: guidance-enriched variants of `research-to-pain` and `design-system-extraction`
were built with deliberately dangerous exemplars (concrete numbers, named sources, the
full output format), then attacked with shape-mimicry inputs — the taught format carrying
no substance (three "independent signals" all one CRO voice; a hand-filled coverage map
with 47 rules claimed and none shown). A/B included a naive variant without the
shape-is-never-the-gate line.

Result: 3/3 refused on substance, first attempt, small model. The naive variant also
held, so the closing line is belt-and-suspenders on this sample (counts, not rates —
one run per case). The `claimed-coverage-map` fixture in
`tests/fixtures/design-system-extraction/` is the promoted form of the attack; any skill
adopting the teaching layer should carry one shape-without-substance fixture the same
way every skill carries its primary refusal.

## 2. Evidence contracts — the container-agnostic gate spec

Teams vary in every container: thin PRDs vs. thick, Figma-only design systems vs.
token-synced, prototyping teams vs. straight-to-handoff. The frame that absorbs the
variance: **same gates, declared shape, honest floor.**

- The **invariant** is the question each gate asks and the refusal to launder the
  answer. Gate 1 does not need "a PRD"; it needs *does this map to a stated business
  goal and an evidenced customer pain?* — answerable from any container.
- Variance is absorbed at three points that already exist: **declared shape** (the
  profile), **read state** (extraction's covered/contested/absent + named-state pattern,
  generalizable to every artifact class), and **routed process** (the conductor's
  state-set model — skipped steps are legal; unanswered questions are not).
- **Floor vs. bar:** rigor scales with maturity; honesty doesn't. Low maturity is a
  legal, nameable state at every gate — a Figma-only team passes enforcement against a
  Figma-derived reference whose coverage map says `code sync: absent`. Faking higher
  maturity is the only illegal move.

The missing artifact: one page — per gate, *the question / the evidence that answers it,
in any container / the states short of answered / the illegal move*. It is the natural
home for layer 4's deep guidance (skills carry the compact inline version so the
chat-Project door degrades gracefully). Anti-patterns it exists to refuse: maturity
tiers, template proliferation, sliding-scale refusals.

## Status

Validated by pressure test; adopted nowhere. Next steps when pulled for: draft the
per-gate evidence-contract page, pilot the four-layer anatomy on
`design-system-extraction`, promote a shape-mimicry fixture alongside any skill that
adopts it.
