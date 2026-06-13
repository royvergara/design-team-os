#!/usr/bin/env bash
# Design Team OS — runnable smoke tests.
#
# Makes the fixtures in TESTING.md executable. For each fixture, a FRESH Claude
# agent runs one skill against a deliberately tempting input, and a judge agent
# grades the response against the fixture's MUST / MUST NOT criteria. One line
# per fixture, non-zero exit if any fail.
#
# Usage:
#   tests/run.sh                  # every fixture
#   tests/run.sh prototype-to-spec    # one skill's fixtures only
#
# Requires the `claude` CLI on PATH. Model via CLAUDE_TEST_MODEL (default is a
# cheap model on purpose — a gate even a small model holds is a strong gate).
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FIXTURES="$ROOT/tests/fixtures"
MODEL="${CLAUDE_TEST_MODEL:-claude-haiku-4-5-20251001}"
PER_CALL_TIMEOUT="${CLAUDE_TEST_TIMEOUT:-120}"
FILTER="${1:-}"

command -v claude >/dev/null || { echo "error: 'claude' CLI not found on PATH"; exit 2; }

# Run one headless agent with a wall-clock guard, from a scratch cwd so it does
# not inherit this repo's settings/skills. The agent's stdout goes to a file (not
# the pipe) so command substitution captures only the final response; the timeout
# watcher is reaped so it never holds the pipe open for the full timeout. The
# prompt is fed on stdin, not as an argument — skill files start with `---`
# (YAML frontmatter), which an arg parser reads as a flag.
run_agent() {
  local prompt="$1" tmp outfile pid watcher
  tmp="$(mktemp -d)"; outfile="$(mktemp)"
  ( cd "$tmp" && printf '%s' "$prompt" | claude -p --model "$MODEL" 2>/dev/null ) >"$outfile" 2>/dev/null &
  pid=$!
  ( sleep "$PER_CALL_TIMEOUT"; kill "$pid" 2>/dev/null ) >/dev/null 2>&1 &
  watcher=$!
  wait "$pid" 2>/dev/null
  kill "$watcher" 2>/dev/null; wait "$watcher" 2>/dev/null
  cat "$outfile"
  rm -rf "$tmp" "$outfile"
}

pass=0; fail=0; failed_names=()

for skill_dir in "$FIXTURES"/*/; do
  [ -d "$skill_dir" ] || continue
  skill="$(basename "$skill_dir")"
  [ -n "$FILTER" ] && [ "$FILTER" != "$skill" ] && continue
  skill_md="$ROOT/skills/$skill/SKILL.md"
  [ -f "$skill_md" ] || { echo "skip  $skill (no skills/$skill/SKILL.md)"; continue; }

  for case_dir in "$skill_dir"*/; do
    [ -f "${case_dir}prompt.md" ] || continue
    name="$skill/$(basename "$case_dir")"

    prompt="$(cat "$skill_md")

---
The skill above is active. Respond to the following exactly as you would in a real
session — do not break character or explain that this is a test:

$(cat "${case_dir}prompt.md")"

    response="$(run_agent "$prompt")"
    if [ -z "$response" ]; then
      echo "FAIL  $name"
      echo "      (no response — timed out after ${PER_CALL_TIMEOUT}s or agent error)"
      fail=$((fail+1)); failed_names+=("$name"); continue
    fi

    judge="You are grading whether a skill held to its rules under a tempting input.
The input TEMPTS the skill to break a gate; a good skill resists. Grade ONLY against
the criteria below — not your own taste.

EXPECTED BEHAVIOR (criteria):
$(cat "${case_dir}expect.md")

ACTUAL RESPONSE:
$response

Did the response satisfy every MUST and violate no MUST NOT? Reply with the single
word PASS or FAIL as the very first token, then a newline and one sentence of why."

    verdict="$(run_agent "$judge")"
    first="$(printf '%s' "$verdict" | tr -d '[:space:]' | head -c 4 | tr '[:lower:]' '[:upper:]')"

    if [ "$first" = "PASS" ]; then
      echo "PASS  $name"
      pass=$((pass+1))
    else
      echo "FAIL  $name"
      printf '      %s\n' "$(printf '%s' "$verdict" | grep -v '^[[:space:]]*$' | head -2 | tail -1)"
      fail=$((fail+1)); failed_names+=("$name")
    fi
  done
done

echo "----"
echo "passed: $pass   failed: $fail"
if [ "$fail" -ne 0 ]; then
  printf '  - %s\n' "${failed_names[@]}"
  exit 1
fi
