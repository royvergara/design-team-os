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

# --- docs scan: the living docs must not name a skill that no longer exists.
# CHANGELOG is historical and exempt; release narration in README uses italics,
# not backticks, for retired names so this stays strict.
DOCS="README.md EXAMPLES.md TESTING.md PROJECTS.md IMPLEMENTATION.md CONTRIBUTING.md"
DOC_WHITELIST=" run-gates "   # non-skill hyphenated tokens (CI job names etc.)
doc_tokens="$(grep -rhoE '`[a-z][a-z0-9]+(-[a-z0-9]+)+`' $DOCS 2>/dev/null | tr -d '`' | sort -u)"
for t in $doc_tokens; do
  [ -d "skills/$t" ] && continue
  case "$DOC_WHITELIST" in *" $t "*) continue ;; esac
  fail=1
  echo "STALE doc reference: \`$t\` — no skills/$t/ folder. Referenced in:"
  grep -l "\`$t\`" $DOCS | sed 's/^/    /'
done

# --- fixture bind: every fixture dir must have a skill, or run.sh silently skips it.
for d in tests/fixtures/*/; do
  sk="$(basename "$d")"
  if [ ! -f "skills/$sk/SKILL.md" ]; then
    fail=1
    echo "ORPHAN fixtures: tests/fixtures/$sk/ has no skills/$sk/SKILL.md — run.sh would skip it silently"
  fi
done

if [ "$fail" -eq 0 ]; then
  echo "reference check: OK — every skill reference resolves (SKILL.md + docs) and every fixture binds"
else
  echo "reference check: FAILED — see above"
fi
exit "$fail"
