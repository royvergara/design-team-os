# Testing

Skills in this library are judgment, not code — their value is the **refusal gate** each
one holds. So the test for a skill is behavioral: put a fresh agent under pressure and check
that the gate holds.

## The tempting-fixture philosophy

Every fixture is an input designed to **tempt the skill into breaking its gate** — a spec
request with no success metric, a "just tell me if it looks good" with no design system, a
PRD with a business goal but no customer pain. A skill passes when it resists the temptation:
flags the missing metric, refuses to praise an unstated system, names the absent pain.

A fixture that the skill passes easily isn't testing anything. Write inputs a careless agent
*would* fall for.

## The harness

```bash
tests/run.sh                  # run every fixture
tests/run.sh prototype-to-spec    # just one skill's fixtures
```

For each fixture it:

1. Spawns a **fresh agent** (`claude -p`, from a scratch working directory so it doesn't
   inherit this repo's context) with the skill's `SKILL.md` active and the tempting input.
2. Spawns a **judge agent** that grades the response against the fixture's `expect.md`
   (the `MUST` / `MUST NOT` criteria) — PASS or FAIL with one line of why.
3. Prints `PASS`/`FAIL` per fixture and a summary; exits non-zero if any fail (CI-friendly).

Requirements and knobs:

- The `claude` CLI on `PATH`.
- `CLAUDE_TEST_MODEL` — model for both the agent and the judge. Default is a cheap model on
  purpose: **a gate even a small model holds is a strong gate.** Bump it if you suspect a
  failure is model weakness rather than a skill weakness.
- `CLAUDE_TEST_TIMEOUT` — per-call wall-clock guard in seconds (default 120). A timeout
  counts as a FAIL.

These tests **cost tokens** — each fixture is two agent calls. Run a single skill while
iterating; run the full suite before merging.

## Adding a fixture

Fixtures live at `tests/fixtures/<skill-name>/<case-name>/` with two files:

```
tests/fixtures/prototype-to-spec/profile-present-no-metric/
  prompt.md    # the tempting input the agent receives (paste any profile/context inline)
  expect.md    # the grading criteria: MUST / MUST NOT lines
```

`<skill-name>` must match a folder under `skills/` (the harness loads
`skills/<skill-name>/SKILL.md`). Keep `expect.md` to checkable behaviors, not vibes — the
judge grades against it literally. Every new skill ships with at least one fixture aimed at
its gate.

## A note on non-determinism

Agents vary run to run. A lone FAIL on a fixture that usually passes is worth re-running
before treating it as a regression — but a fixture that flips often is itself too loose;
tighten `expect.md` so the pass condition is unambiguous.

## What these tests do and don't cover

They check **behavior under temptation** — the gates. They do not check prose quality,
formatting, or that a skill's output is *good*, only that it didn't break its rule. Quality
is a human read; the gate is what the harness defends.
