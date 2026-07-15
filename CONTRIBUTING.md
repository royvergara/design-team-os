# Contributing

Glad you're here. Two ground rules keep this library what it is:

**Every skill enforces a gate.** A skill here is a unit of judgment, not a utility: it must
refuse or flag when its inputs aren't earned (see any `SKILL.md` — the refusal is the
feature). A skill that always produces output no matter what it's handed doesn't belong,
however useful.

**Every gate ships with a runnable test.** A new or changed skill needs a fixture under
`tests/fixtures/<skill>/<case>/` — `prompt.md` (a deliberately tempting input) and
`expect.md` (MUST / MUST NOT criteria). See [TESTING.md](TESTING.md).

**Verdicts are binary; distance is a gap report.** When a gate fails or refuses, it never
softens the verdict and never emits a readiness score ("78% ready" is banned — a scalar
invites negotiation and false precision, which is how a miss starts bargaining). Distance
gets communicated the way a compiler does it, and a FAIL/refusal carries all five parts:

1. **The verdict**, from the skill's closed set (PASS/FAIL, MET/MISSING/CAN'T-TELL,
   solved/partial/didn't, …) — prose explains, it never decides.
2. **The criteria fraction** where criteria exist — "4 of 6 MET." Fractions of binary,
   evidence-backed rows are honest; a weighted score is not.
3. **Close-first** — the one blocking gap, named.
4. **The ranked punch list** — each gap with what's missing and who or what produces it
   (a skill, or a human input), ordered by cost to close.
5. **Next** — the smallest action that would change the verdict, and where to take it.

`prototype-triage` is the reference implementation.

**The determinism boundary.** Anything that must be identical on every run belongs in
code, schema, or templates — never in a prompt. Prompts hold the judgment; the judgment's
*shape* (the verdict vocabulary, the output sections, the gap report) is fixed structure a
fixture can test. On any model change, re-run the full gate suite before trusting it
(see TESTING.md).

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
