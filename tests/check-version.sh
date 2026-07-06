#!/usr/bin/env bash
# Version-consistency guard — no LLM, runs in milliseconds.
#
# The plugin manifest carries an EXPLICIT version, so installed users only get
# updates when it is bumped. This check forces the release ritual: the manifest
# version must equal the newest version heading in CHANGELOG.md. Editing skills
# without bumping both fails CI, instead of silently stranding installed users
# on an old version.
#
# Usage: tests/check-version.sh   (exit non-zero on mismatch)
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

manifest_version="$(sed -n 's/.*"version"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' .claude-plugin/plugin.json | head -1)"
changelog_version="$(grep -m1 -oE '^## v[0-9]+\.[0-9]+(\.[0-9]+)?' CHANGELOG.md | sed 's/^## v//')"

# CHANGELOG headings use v0.5 style; the manifest uses 0.5.0. Compare on the
# major.minor prefix so both conventions can coexist.
mm_manifest="$(printf '%s' "$manifest_version" | cut -d. -f1,2)"
mm_changelog="$(printf '%s' "$changelog_version" | cut -d. -f1,2)"

if [ -z "$manifest_version" ] || [ -z "$changelog_version" ]; then
  echo "version check: FAILED — could not read a version"
  echo "  manifest:  '${manifest_version:-<none>}' (.claude-plugin/plugin.json)"
  echo "  changelog: '${changelog_version:-<none>}' (first '## vX.Y' heading in CHANGELOG.md)"
  exit 1
fi

if [ "$mm_manifest" != "$mm_changelog" ]; then
  echo "version check: FAILED — manifest and CHANGELOG disagree"
  echo "  manifest:  $manifest_version (.claude-plugin/plugin.json)"
  echo "  changelog: v$changelog_version (newest heading in CHANGELOG.md)"
  echo "  A release bumps BOTH: the manifest version (or installed users never"
  echo "  get the update) and a new CHANGELOG heading describing it."
  exit 1
fi

echo "version check: OK — manifest $manifest_version matches CHANGELOG v$changelog_version"
