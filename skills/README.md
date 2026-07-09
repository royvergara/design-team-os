# Skills

Each skill lives in its own folder here and contains a single `SKILL.md`. That file is the whole skill.

Fourteen skills are live — the full table, with the gate each one serves, is in the [root README](../README.md#skills). The recommended install is the plugin (`/plugin marketplace add royvergara/design-team-os`, then `/plugin install design-team-os@fluent-by-design`), which brings in every skill plus the `/design-team-os:init` command in one step. To use a single skill without the plugin, drop its folder into `.claude/skills/` in your project (or `~/.claude/skills/` for every project), or paste its `SKILL.md` into a Claude Project's instructions. Every skill gates its own inputs and works alone — the ledger, profile, and `conductor` are optional connective tissue, never prerequisites.

## File convention

A `SKILL.md` starts with YAML frontmatter, then a body written as instructions to Claude.

```markdown
---
name: prd-to-ia
description: Use when turning a PRD or requirements document into a first pass information architecture. Triggers on a pasted or linked PRD plus a request for an IA, sitemap, screen list, or structure. Always returns what was excluded and why, not just the IA.
---

# PRD to IA

Step by step instructions Claude follows to do the work.
```

Two rules that keep the library usable:

The `description` is how Claude decides when to reach for the skill, so it names the trigger and the situation, not just the topic. Write it for the buyer's real moment, not for a catalog.

One skill does one thing. If a skill is trying to cover two jobs, it is two skills.

And one rule that makes it this library: **every skill enforces a gate.** It refuses or flags when its inputs aren't earned, and that refusal ships with a runnable test under [`tests/fixtures/`](../tests) (see [TESTING.md](../TESTING.md)). A skill that always produces output no matter what it's handed doesn't belong here — [CONTRIBUTING.md](../CONTRIBUTING.md) has the full bar for proposing one.
