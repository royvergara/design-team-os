# Dogfood retro — Live Music Memoirs end-to-end run (2026-07-15)

First full-pipeline dogfood after CLI install: init → research-to-pain (real Notion research)
→ validation-plan → labeled-synthetic validation → brief-from-pain → brief-to-prompt →
prototype-triage (live site as stand-in) → outcome-readout → outcomes-scorecard, plus two
conductor readouts. One real work item (`relive-the-night` in the product repo), every
fabricated value labeled synthetic. This retro drove the v0.15 changes; findings below are
the record.

## What held (protect these)

- **The refusals were the best UX of the session.** Empty interview-log scaffolds in Notion
  read as an open gate, not conducted interviews; a feature request ("AI narrative") was
  refused as a pain; "what if validation was run" got routing-as-hypothetical plus a refusal
  to write state. The product is the refusal — none of the v0.15 ergonomics soften any gate.
- **The profile did its job.** Design system, event names, and builder were never re-asked.
- **Labeled-synthetic discipline worked** end-to-end and is now spec (docs/demo-mode.md).

## What failed, and what shipped for it (v0.15)

1. **Onboarding cliff.** Init ended with "hand research to the relevant skill" in front of
   twenty skill names. → Init's report now ends with the spine map + the doors in
   (commands/init.md §4); skipped profile questions become visible TODO comments.
2. **The pipeline was invisible until someone asked the conductor.** No live sense of
   position, criteria ahead, or why. → Orientation blocks in the seven gate skills (one line
   in, one line out — position on the spine + what the next gate will demand), and a
   first-class conductor render (templates/conductor.html) with gate cards, artifact
   manifest, runnable set, synthetic/bet states.
3. **Artifact sprawl.** Five homes by session end (profile, ledger dir, reviews dir, an
   invented briefs/ dir, published artifacts) with no consolidated view. → The conductor
   render's **artifact manifest** section lists every path the ledger points to. (Still
   open: init should pin artifact homes via the profile's `artifacts:` block — see Open.)
4. **Slow renders.** The scorecard fill was the session's biggest cost: a ~600-line template
   filled token-by-token by an LLM subagent (~5 min, ~107k tokens), which also had to catch
   a template collision bug by eye. → scripts/render.mjs: deterministic fill of tokens /
   repeats / state guards / DATA_JSON, loud failure on any missing token, milliseconds.
   Skills now produce the small data JSON (the judgment) and delegate the templating.
5. **Validation execution gap.** The product repo's real June arc died exactly here: plans
   and scripts existed, zero interviews ran. Nothing bridged plan → run. →
   templates/interview-capture.md, one file per session, tallies mapped verbatim onto the
   plan's pre-registered decision rules; validation-plan points at it.

## Open (not shipped in v0.15)

- **Init should pin `artifacts:` homes** (briefs, specs) so no session invents a directory.
- **A session-start state sniff** — profile present? ledgers? any gate due? — one line of
  orientation before the user asks. (Hook or conductor auto-run; needs a taste check on
  intrusiveness.)
- **Scorecard template fill-safety pass** — the hero value token sits against a hardcoded
  `%` superscript; render.mjs makes this survivable but the template should not have
  landmines.
- **check-references whitelist pressure** — new docs mention non-skill hyphenated names;
  kept out of backticks for now, which bends prose style to a test regex.

## The one-line lesson

The judgment layer (gates, refusals) was right all along; everything that hurt was the
_chrome_ around it — orientation, consolidation, and mechanical work the LLM should not have
been doing by hand.
