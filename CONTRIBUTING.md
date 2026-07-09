# Contributing

Glad you're here. Two ground rules keep this library what it is:

**Every skill enforces a gate.** A skill here is a unit of judgment, not a utility: it must
refuse or flag when its inputs aren't earned (see any `SKILL.md` — the refusal is the
feature). A skill that always produces output no matter what it's handed doesn't belong,
however useful.

**Every gate ships with a runnable test.** A new or changed skill needs a fixture under
`tests/fixtures/<skill>/<case>/` — `prompt.md` (a deliberately tempting input) and
`expect.md` (MUST / MUST NOT criteria). See [TESTING.md](TESTING.md).

## Proposing a skill

Open an issue first, with three things: the **trigger** (the real moment a design team
reaches for it), the **gate** (what it refuses, and why that refusal protects the team),
and the **output shape**. One skill does one thing — if it covers two jobs, it's two
skills.

## Before you open a PR

```bash
bash tests/check-references.sh                               # every skill reference resolves
bash tests/check-version.sh                                  # manifest version matches CHANGELOG
claude plugin validate . --strict                            # marketplace manifest
claude plugin validate .claude-plugin/plugin.json --strict   # plugin manifest + every skill's frontmatter
tests/run.sh <your-skill>                                    # your gate holds (needs the claude CLI; costs tokens)
```

Run both `validate` commands — only the `plugin.json` one descends into `skills/`
and parses frontmatter, so it is the one that catches a broken `description`.

Add a CHANGELOG entry, and bump the version in `.claude-plugin/plugin.json` if your PR
should reach installed plugin users. CI runs the static checks on every PR; a maintainer
triggers the LLM gate tests with the `run-gates` label.

## Style

Match the existing skills: terse, second person, YAML frontmatter with a `description`
that names the trigger and the refusal (not the workflow). Read two or three existing
`SKILL.md` files before writing yours — consistency is a feature of the library.

MIT licensed — contributions land under the same license.
