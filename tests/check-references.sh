#!/usr/bin/env bash
# Static drift guard — no LLM, runs in milliseconds.
#
# Every hyphenated skill name a SKILL.md mentions in backticks must resolve to a
# real skills/<name>/ folder. Catches a routing table (or any cross-reference)
# going stale when a skill is renamed, deleted, or typo'd — e.g. the conductor
# naming a skill that no longer exists.
#
# Usage: tests/check-references.sh   (exit non-zero if any reference is unresolved)
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# Family shorthands that intentionally name a set, not one folder. (None at present —
# brief-to-prompt is now a real consolidated skill, so it resolves on its own.)
WHITELIST=" "

fail=0
tokens="$(grep -rhoE '`[a-z][a-z0-9]+(-[a-z0-9]+)+`' skills/*/SKILL.md | tr -d '`' | sort -u)"

for t in $tokens; do
  [ -d "skills/$t" ] && continue
  case "$WHITELIST" in *" $t "*) continue ;; esac
  fail=1
  echo "UNRESOLVED skill reference: \`$t\` — no skills/$t/ folder. Referenced in:"
  grep -rl "\`$t\`" skills/*/SKILL.md | sed 's/^/    /'
done

if [ "$fail" -eq 0 ]; then
  echo "reference check: OK — every skill reference resolves to a real folder"
else
  echo "reference check: FAILED — a SKILL.md references a skill that does not exist"
fi
exit "$fail"
