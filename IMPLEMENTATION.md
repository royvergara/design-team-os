# Implementing Design Team OS

The [README](README.md) covers the basic install. This is the deeper guide: where skills
live, whether to use one as-is or fork it, and how to keep a fork from rotting. The short
version: **reference skills as-is and supply your stable context through a
[project profile](templates/project-profile.schema.md); fork only to change a skill's
behavior, never just to feed it your paths.**

## Where skills live

A skill is a folder with one `SKILL.md`. Three homes:

- **Claude Code, project level** — `.claude/skills/<skill>/` in the repo you work in.
  Versioned with the project, shared with the team, and next to the
  `design-os.profile.yaml` it can read. Best for skills your team relies on or tunes.
- **Claude Code, user level** — `~/.claude/skills/<skill>/`. Available across all your
  projects; good for reference-as-is skills you want everywhere. No single repo to read a
  profile from, so it leans on the paste-context path.
- **Claude Project (chat)** — paste the `SKILL.md` into the Project's instructions. No
  filesystem, so paste your profile into the Project knowledge too.

A skill isn't "called" — it triggers on its `description`. Give it the situation the
description names (a PRD, a chosen prototype, generated UI) and it activates.

## Reference-as-is vs. fork-and-tune

Decide by **what you want to change**, not by how custom your product feels.

| You want to change… | Do this | Why |
| --- | --- | --- |
| The **context** a skill uses (design-system reference, event names, spec path) | **Reference as-is** + a [project profile](templates/project-profile.schema.md) | The profile exists so you don't fork to hard-code context. You stay on the upstream skill and get Friday's updates for free. |
| A skill's **behavior** — its steps, output, or the strictness of a gate | **Fork and tune** | A behavior change is a real edit. Own it deliberately. |

**Forking just to feed a skill your paths and tokens is the adoption tax the profile
removes.** Reach for a fork only when the skill's *judgment* needs to differ from upstream —
and never to weaken a gate. The gates (a validation signal before a spec, evidence before a
journey map, a real reference before an audit) are the library's whole value; a fork that
softens one is a fork that breaks the thing you installed it for.

### Keeping a fork current

1. When a new version ships, diff your fork against upstream `SKILL.md`.
2. Re-apply your behavioral changes onto the new version.
3. Re-run the verification checklist below — upstream may cite new paths or symbols.
4. Run `tests/run.sh <skill>` ([TESTING.md](TESTING.md)) to confirm the gate still holds.

## The tuned-fork header + verification checklist

A tuned skill that points at a **moved file, renamed route, or deleted event is worse than
the generic one** — it fails confidently. Dogfooding hit exactly this. So verify every
reference against the live codebase before trusting a fork or a profile.

Drop this at the top of a forked `SKILL.md` body so its provenance and freshness are visible:

```markdown
<!--
FORK OF: prototype-to-spec (upstream v0.1)
CHANGED: <one line — what behavior you altered and why>
VERIFIED: <date> against <repo>@<commit-sha>
-->
```

Then confirm every reference resolves — most of this is greppable, don't eyeball it:

- [ ] **Paths** — every file path the skill or profile cites exists (`git ls-files`).
- [ ] **Routes** — every named route exists in your router.
- [ ] **Events** — every analytics event name appears at a real capture call site
      (`grep -r 'posthog.capture(' app components lib` — exclude `node_modules`).
- [ ] **Components / tokens** — every component, class, or token named is real.
- [ ] **Freshness** — the profile's `verified_against_commit` matches HEAD, or you've noted
      the drift and re-derived anything that moved.
- [ ] **Gate intact** — `tests/run.sh <skill>` still passes after your edits.

A stale pointer is the one failure mode that turns a helpful skill into a harmful one. Fix
the reference before you rely on the skill.
