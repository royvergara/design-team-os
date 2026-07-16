# Post-v0.15 roadmap — phased, pull-driven

The carryover plan from the LMM dogfood (docs/retros/2026-07-15-lmm-dogfood.md), revised
after the flexibility assessment: team workflows and rituals vary widely, so **infrastructure
accretes by use, not by install** — the same rule the profile already lives by. Nothing in
any phase wires itself; recipes over wiring; every tool degrades silently for shapes it
doesn't fit.

**The four-persona test** — every addition must pass before it ships as a default:

1. Solo nights-and-weekends founder (git, one repo, no CI culture)
2. A pod inside an enterprise (their CI, their hooks, their compliance)
3. A Notion-native design team (`tools.state: notion`, no git fluency)
4. A chat-Project PM (no filesystem at all)

If a feature breaks or nags any of them, it ships as a documented recipe or degrades
silently — never as a default.

---

## Phase 0 — Settle v0.15 · NOW

**Purpose:** a stable base; nothing new lands on an unverified release.

- Merge PR #33 (the dogfood release + client test drive + this doc).
- Run the LLM fixture suite (`tests/run.sh`) — 9 SKILL.md files changed; the gates must
  still hold under tempting inputs.
- Reload the plugin; confirm the cache is at 0.15 (the dogfood ran an entire session on a
  stale 0.13.1 cache without noticing — the exact failure Phase 1's doctor detects).

**Exit gate:** fixtures green · installed cache = 0.15.

## Phase 1 — Guard rails · after Phase 0, no other trigger

**Purpose:** the system defends its rules when nobody is looking, and orientation arrives
without being asked. All pull, no push.

- **Ledger linter** (`scripts/` + a tests/ entry): checks ONLY declared invariants — a bet
  missing one of its four fields, a `review_by` past due with no finding, checkmark-shaped
  entries (`validated: true` and kin), unflagged content below an evidence-boundary marker.
  **Warn-first; error only in an opt-in CI mode. Never checks shape** — the schema's
  every-field-optional rule stays sovereign. Degrades to a no-op with a one-line notice
  when no file-resident ledgers exist (`tools.state: notion` is a supported shape, not an
  error).
- **Session-start sniff:** one line per work item — state set, next runnable, due bets and
  stale gates first. **Silent unless there is signal**; fast no-op in repos with no
  ledgers. Never a percent bar, never a pipeline position (the conductor's quality bar
  binds the tracker too).
- **`board` verb** (pull, not push): derive `board-data.json` from the ledgers
  mechanically — presence, flags, dates, staleness; **never judgment** — and render
  `board.html` via the existing render script. The data JSON is the documented extension
  point for any other surface; no other emitter ships until a real surface pulls for it.
- **Integrations recipes doc** (one page): statusline one-liner, a GitHub Action that
  re-renders the board on ledger pushes, a PostToolUse auto-render hook, formatter-ignore
  entries. All as copy-paste recipes the team wires themselves. `doctor` (below) may offer
  one **when it detects the matching problem** — never unprompted.
- **`doctor` verb:** read-only health check — install location, cached plugin version vs
  repo conventions, Node availability, formatter-hook detection, profile presence.
  Detection → offer; never auto-wire.

**Exit gate:** four-persona test passes — every Phase-1 feature is silent or gracefully
degraded for personas 2–4 · linter warn-mode runs clean on the dogfood repo's real ledger.

## Phase 2 — Pulled by the second work item

**Trigger:** a second real ledger exists (not before — portfolio tooling for one work item
is speculation).

- Portfolio rows on the board (one row per ledger; the program-level view).
- `artifacts:` homes in init — ask-on-detect, so no session invents a briefs/ directory.
- Staleness reads: gate-entry `date:` as a convention the tools reward (readouts appear
  when dates exist; nothing errors when absent).
- Scorecard template fill-safety pass (the hero-token `%` landmine and kin).
- Dogfood `weekly-review` for real once two items exist; retro it.

**Exit gate:** the board answers "where is everything?" in one glance for 2+ items · a
weekly-review runs off real ledgers.

## Phase 3 — Pulled by a real client or team

**Trigger:** first client test-drive booked, or first multi-person team adopts.

- Connector-aware intake (profile `evidence_sources` naming Notion/analytics connectors;
  `demo run` and research-to-pain read them directly). Shape it against the real client's
  stack, not speculatively.
- Practice-kit stage checkpoints (the audience tour with jump-to-gate) — build against a
  real presentation's needs.
- Additional board emitters (MD / ANSI / statusline) — each only when its surface has a
  user.
- Chat-parity statement in the docs: the honest floor (pasted ledger, inline render), not
  chased parity.
- Dogfood `period-review` at the first real period close; retro it.

**Exit gate:** one real client run end-to-end with the evidence boundary as the
deliverable · retro filed.

---

**Standing rule for every phase:** the judgment layer (gates, refusals, the conductor's
routing) is finished surface — phases change the chrome around it. Any proposal that
softens a refusal to improve "experience" is answering the wrong question.
