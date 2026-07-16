---
description: Client-facing test drive — run a client's real artifacts through the gates for real judgment, continue past the evidence with flagged inference to a final readout and scorecard, all inside a disposable sandbox that cleans up with one delete.
---

Run Design Team OS as a demonstration on **real client artifacts**. The gates judge for
real — nothing staged, no softened refusal — and where the client's evidence runs out, the
run continues on **flagged inference** so the audience sees the whole loop land on a final
readout and scorecard. The pitch is double: the system working on _their_ work, and the
**evidence boundary** — the exact line where their artifacts stop carrying the work and
inference takes over — which is an evidence-maturity audit they keep. Convention reference:
`docs/demo-mode.md`.

The argument is a verb: `run` (default), `status`, or `clean`.

## Ground rules — every verb, no exceptions

- **Everything writes inside `design-os.demo/`** at the repo root — never `design-os.work/`,
  never `design-os.reviews/`, never the profile, never the client's own files. The real
  state of this repo is untouchable by a demo.
- **On first creating the sandbox, append `design-os.demo/` to `.gitignore`** (create the
  file if the repo has none). Client artifacts and inferred numbers must never be
  committable, even by accident.
- **A profile may be read** for context (builder, event names); it is never written.
- **Every inferred value is flagged in the artifact it lands in** (`⚠️ inferred`, per
  `docs/demo-mode.md`), and every rendered page carries the demo ribbon — set
  `"states": { "demo": true }` in the render data. A render without the ribbon is only
  legal when every value on it is real.

## `demo run`

1. **Intake.** Ask once, one compact list: whatever exists — research (notes, tickets,
   strategy docs, links), a PRD, a prototype (URL, screenshots, or the live product),
   analytics (a GSC/PostHog read, an export). No questionnaire; work with what arrives.
2. **Map.** A conductor-style read of what the inputs cover: which gates these artifacts
   can feed, stated up front so the audience knows the route before it runs.
3. **The real pass.** Run the actual gate skills on the real inputs — `research-to-pain` on
   their research, `prd-to-ia` on their PRD, `prototype-triage` against whatever brief
   exists or gets ratified in the room — writing the ledger and artifacts inside
   `design-os.demo/` only. **Refusals are findings, not friction:** when a gate refuses
   (a pain that's really a feature request, an interview log that's empty scaffolding, a
   bar nobody set), record the refusal verbatim in the ledger and say it to the room — the
   refusal firing on their own input is the most convincing thirty seconds of the demo.
4. **The boundary.** The first gate that cannot pass on real evidence marks the evidence
   boundary. Record it explicitly in the ledger (`# ── EVIDENCE BOUNDARY — everything below
is inferred ──`), then continue by **systematic inference**: each value extrapolated
   from the client's actual context (their real metrics' order of magnitude, their real
   competitor findings, their real constraints — never generic numbers), each flagged
   `⚠️ inferred` with one line naming what it extrapolates from. One hybrid state recurs
   below the boundary and deserves its own honesty: a **real observation judged against an
   inferred bar** — e.g. the client's live product genuinely inspected, triaged against
   criteria nobody ratified. Record the observation as real (a `real_observation` field in
   the ledger entry, named as real on the board) and the _verdict_ as inferred; collapsing
   the two either way wastes the finding or launders the judgment. These are the cheapest
   conversions in the debrief — a ratified bar makes the same observation a real verdict
   the same day.
5. **Land.** Carry the inferred continuation through `outcome-readout` to a verdict, then
   render the conductor board and the scorecard. The script and templates live in the plugin,
   the data and output live in this repo — so run
   `node ${CLAUDE_PLUGIN_ROOT}/scripts/render.mjs ${CLAUDE_PLUGIN_ROOT}/templates/conductor.html design-os.demo/<data>.json design-os.demo/<out>.html`
   (and likewise `templates/scorecard.html`), always with `"states": { "demo": true }` in the
   data so the ribbon shows. Never reference `scripts/` or `templates/` as bare relative paths
   — the product repo is not the plugin, and the bare path resolves to nothing. On the board,
   real gates render solid, inferred ones hatched — the evidence boundary is _visible_, not
   narrated.
6. **Debrief.** Close with three things, plainly: the evidence boundary ("your artifacts
   carry this work through X; everything past it is inference"), each real refusal and the
   smallest evidence that would clear it (that list is their roadmap, and the follow-up
   engagement), and the offer to **export the two rendered pages** somewhere durable before
   cleanup — the renders are the leave-behind; the sandbox is not.

## `demo status`

Read the sandbox and report: which gates ran on real evidence, where the boundary sits,
what was inferred, which renders exist. If no sandbox exists, say so — never invent one.

## `demo clean`

Confirm once, delete `design-os.demo/` entirely, then show the repo's git status on screen —
the closing beat is that nothing real was touched. If renders were not exported and the
user wants them, export before deleting; deletion is not undoable.

**Permission-proof the delete** (learned in the first dry run — a harness permission mode
denied `rm -rf` mid-demo): try the delete; if denied, **move** the sandbox out of the repo
instead (a session temp directory works — same effect on the repo, no destructive
permission needed); if that is also denied, print the exact one-line delete for the user to
run themselves and say why. Never retry a denied command verbatim, and never let the demo's
closing beat become a permission prompt in front of the room.

## What `run` never does

Never writes outside the sandbox. Never counts an inferred value as proven — the conductor
reads everything past the boundary as open, exactly as `docs/demo-mode.md` binds. And never
skips or softens a refusal to keep the demo moving: a demo that only shows the passing path
is a brochure, and the gates are the product.
