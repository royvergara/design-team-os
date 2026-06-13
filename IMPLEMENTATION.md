# Implementing Design Team OS

How to install these skills into your workflow, decide whether to use a skill as-is or
tune it, and — if you tune it — keep it from rotting. The short version: **reference skills
as-is and supply your context through a [project profile](templates/project-profile.schema.md);
fork only to change a skill's behavior, never just to feed it your paths.**

## 1. Install

A skill is a folder with one `SKILL.md`. There are three places it can live.

### Claude Code — project level (recommended for teams)

```
your-product-repo/
  .claude/skills/
    prototype-to-spec/
      SKILL.md
```

Copy the skill folder into `.claude/skills/` in the repo you work in. It's versioned with
the project, so the whole team gets the same skill, and it sits next to the
`design-os.profile.yaml` it reads. Use this for any skill your team relies on or tunes.

### Claude Code — user level (for skills you use everywhere)

```
~/.claude/skills/
  prototype-to-spec/
    SKILL.md
```

Available across all your projects. Good for reference-as-is skills you want on hand
regardless of which repo you're in. Note a user-level skill has no single repo to read a
profile from — it works best in the reference-as-is + paste-context mode.

### Claude Project / chat (no filesystem)

Paste the contents of `SKILL.md` into the Project's custom instructions. The skill has no
filesystem here, so it can't read a profile file — paste your `design-os.profile.yaml` into
the Project knowledge too. See the [two-surface model](templates/project-profile.schema.md#two-surfaces-opposite-capabilities).

After installing, you don't "call" a skill — it triggers on its `description`. Give it the
situation the description names (a chosen prototype, a PRD, generated UI) and it activates.

## 2. Reference-as-is vs. fork-and-tune

This is the decision that determines whether your install stays healthy or rots. Decide by
**what you want to change**, not by how custom your product feels.

| You want to change… | Do this | Why |
| --- | --- | --- |
| The **context** the skill uses (your design system, event names, routes, spec path) | **Reference as-is** + a [project profile](templates/project-profile.schema.md) | The profile exists precisely so you don't fork to hard-code context. You stay on the upstream skill and get Friday's improvements for free. |
| The skill's **behavior** — its steps, its output format, the wording or strictness of a gate | **Fork and tune** | Behavior changes are real edits to the skill. Own them deliberately. |

**Forking just to feed a skill your paths and tokens is the adoption tax this library is
trying to remove.** Dogfooding showed teams forking every skill to hard-code their product's
context, then having to re-fork on every update. The profile is the fix: supply context
once, in data, and leave the skill unchanged. Reach for a fork only when the skill's
*judgment* needs to differ from upstream.

### Keeping a fork current

A fork stops getting Friday's updates — that's the cost. To manage it:

1. When a new version ships, diff your fork against the upstream `SKILL.md`.
2. Re-apply your behavioral changes onto the new version (not the other way around).
3. Re-run the verification checklist below — upstream may cite new paths/symbols.
4. Run the [harness](TESTING.md) for that skill to confirm your changes didn't break its gate.

## 3. The tuned-fork template + verification checklist

A tuned skill that points at a **moved file, renamed route, or deleted event is worse than
the generic one** — it fails confidently. Dogfooding hit exactly this: a tuned skill citing
a stale path misled more than a vanilla skill would have. So every fork (and every profile)
must be verified against the live codebase before you trust it.

### Fork header

Drop this comment block at the top of a forked `SKILL.md` body (below the frontmatter) so
the fork's provenance and freshness are visible:

```markdown
<!--
FORK OF: prototype-to-spec (upstream v0.1)
CHANGED: <one line — what behavior you altered and why>
VERIFIED: <date> against <repo>@<commit-sha>
-->
```

### Verification checklist

Before trusting a forked skill or a profile, confirm every reference resolves. Most of this
is greppable — don't eyeball it:

- [ ] **Paths** — every file path the skill or profile cites exists (`ls` / `git ls-files`).
- [ ] **Routes** — every named route exists in your router (`app/**/page.tsx` or equivalent).
- [ ] **Events** — every analytics event name appears at a real capture call site
      (`grep -r 'posthog.capture(' app components lib` — exclude `node_modules`).
- [ ] **Guards / tests** — every test or CI guard the skill names exists and runs.
- [ ] **Components / classes** — every component or utility class named is real.
- [ ] **Freshness** — the profile's `verified_against_commit` matches HEAD, or you've noted
      the drift and re-derived anything that moved.
- [ ] **Gate intact** — `tests/run.sh <skill>` still passes after your edits.

If a reference doesn't resolve, fix the reference (or the profile) before relying on the
skill — a stale pointer is the one failure mode that turns a helpful skill into a harmful
one.
