# Skills

Each skill lives in its own folder here and contains a single `SKILL.md`. That file is the whole skill. Drop the folder into your Claude Code skills directory, or paste the `SKILL.md` contents into a Claude Project.

## File convention

A `SKILL.md` starts with YAML frontmatter, then a body written as instructions to Claude.

```markdown
---
name: prd-to-ia
description: Use when turning a PRD into a first pass information architecture for a product design team. Triggers on a pasted or linked PRD plus a request for IA, sitemap, or screen list.
---

# PRD to IA

Step by step instructions Claude follows to do the work.
```

Two rules that keep the library usable:

The `description` is how Claude decides when to reach for the skill, so it names the trigger and the situation, not just the topic. Write it for the buyer's real moment, not for a catalog.

One skill does one thing. If a skill is trying to cover two jobs, it is two skills.

## What lands in v0.1

Eight starter skills shipped June 12, 2026, one folder each:

- `prd-to-ia`
- `design-system-enforcement`
- `critique-synthesis`
- `user-journey-mapping`
- `prototype-to-spec`
- `brief-to-prompt-v0`
- `brief-to-prompt-bolt`
- `figma-plugin-orchestration`

After that, new skills drop every Friday.
