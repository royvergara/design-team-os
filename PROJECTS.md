# Design Team OS in a Claude Project — no install

You don't need Claude Code, a terminal, or the product repo to use these skills. Every
`SKILL.md` is plain markdown that works pasted into [claude.ai](https://claude.ai) — and the
gates hold there. We've tested skills pasted into Projects whose own instructions push the
other way ("be action-oriented, provide deliverables directly," a deadline, an excited VP):
the refusals held, including with three skills pasted into one Project at once.

## Use one skill in 60 seconds

1. Pick a skill from the [table in the README](README.md#skills) and open its `SKILL.md`
   under [`skills/`](skills/).
2. Copy the whole file — frontmatter and all.
3. In claude.ai, create a Project (e.g. "Design Reviews") and paste it into the Project's
   instructions. No Project? Pasting the skill at the top of a plain chat works too.
4. Hand it your input — the situation named in the skill's `description` is what sets it
   off. Feedback from three reviewers for `critique-synthesis`, a prototype plus its brief
   for `prototype-triage`, a pile of research for `research-to-pain`.

When it refuses — no evidence behind the pain, no bar in the brief, "the VP loved it" as a
validation signal — **that refusal is the skill working**, and it always comes with the
smallest next step that would earn the output.

## One skill or several?

Both work. One skill per Project keeps the sharpest edge and is the right default. Bundling
a few related skills into one Project also works — the right skill activates on the shape of
your input — and makes sense per gate:

- **A review Project:** `prototype-triage` + `design-system-enforcement` + `critique-synthesis`
- **An intent Project:** `research-to-pain` + `user-journey-mapping` + `brief-from-pain`
- **A prompt Project:** `brief-to-prompt-v0` + `brief-to-prompt-bolt`

Keep bundles small and per-gate. Fifteen skills in one Project is untested territory.

## What about the machine — ledger, profile, conductor?

The machine is optional everywhere, and in a Project it degrades to text:

- **State** travels as a pasted YAML block (same shape as
  [templates/work-ledger.schema.md](templates/work-ledger.schema.md)) kept in the Project's
  knowledge — paste it in when you resume, paste the updated block back when a skill adds an
  artifact. Honest caveat: hand-carried state rots faster than committed files. If you find
  yourself maintaining several ledgers by hand, that's the sign to move to the
  [plugin](README.md#install--two-doors) — or to have one person on the team run the machine for
  everyone.
- **The conductor works with no ledger at all.** Paste `skills/conductor/SKILL.md` into a
  Project, describe what artifacts exist ("we have a PRD, a prototype the PM built, no
  brief"), and ask "where are we?" — it routes from the description.
- **The profile** becomes a pasted block of your stable context (design-system reference,
  event names) in Project knowledge, same as the ledger.

## Two honest limits

- **Pasted skills don't update.** The plugin gets new versions through `/plugin`; a pasted
  skill is frozen at the day you copied it. Check the [CHANGELOG](CHANGELOG.md) occasionally
  and re-paste skills that changed.
- **No files, no automation.** Skills can't write ledgers or read your repo from a chat.
  You carry the state; the judgment still shows up in full.
