#!/usr/bin/env bash
# Brand drift guard — no LLM, runs in milliseconds.
#
# brand/tokens.css is a verbatim copy of fluentxdesign's app/tokens.css. Two checks:
#   1. No file under brand/ other than tokens.css carries a raw hex colour — every
#      colour resolves through a --fxd-* token, so the surfaces cannot drift.
#   2. If a fluentxdesign checkout is beside this repo (../fluentxdesign, or
#      FXD_ROOT), tokens.css must match it byte for byte.
#
# Usage: tests/check-brand.sh   (exit non-zero on drift)
set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
fail=0

for f in brand/*.css; do
  [ "$f" = "brand/tokens.css" ] && continue
  # strip /* … */ comments first so a hex inside a comment neither passes nor hides one
  if sed -E ':a;N;$!ba;s#/\*[^*]*\*+([^/*][^*]*\*+)*/##g' "$f" | grep -nE '#[0-9a-fA-F]{3,8}\b' >/dev/null; then
    fail=1
    echo "RAW HEX outside tokens.css: $f"
    sed -E ':a;N;$!ba;s#/\*[^*]*\*+([^/*][^*]*\*+)*/##g' "$f" | grep -nE '#[0-9a-fA-F]{3,8}\b' | sed 's/^/    /'
  fi
done

FXD="${FXD_ROOT:-$ROOT/../fluentxdesign}"
if [ -f "$FXD/app/tokens.css" ]; then
  if ! diff -q "$FXD/app/tokens.css" brand/tokens.css >/dev/null; then
    fail=1
    echo "TOKENS DRIFT: brand/tokens.css differs from $FXD/app/tokens.css — re-copy upstream"
  else
    echo "tokens: in sync with $FXD/app/tokens.css"
  fi
else
  echo "tokens: no fluentxdesign checkout found (set FXD_ROOT to compare) — skipped"
fi

if [ "$fail" -ne 0 ]; then echo "brand check: FAILED"; exit 1; fi
echo "brand check: OK"
