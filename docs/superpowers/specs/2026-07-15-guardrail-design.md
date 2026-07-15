# Design: v0.14 — the guardrail

One load-bearing addition, judged down from a seven-item systems-thinking package: the
balancing loop, in the machine's own idiom. The bar says what must move; a guardrail says
what must not. No new skill, no new required input, one new behavior that will not emerge
on its own: the compound verdict.

## Why this one (and why only this one)

Gate 3's claim is "did it solve the pain and move the needle" — and today a win that broke
something adjacent still reads as a clean win. That is a hole in the product's own honesty
promise, which makes it evidence-backed enough to ship pre-install. The other six
candidates from the systems-thinking assessment were judged out: two are behaviors the
skills already exhibit unprompted (the moving constraint, confound rejection — both
observed in simulation), two cannot activate until history exists that no team has
(eroding-goals lens, cross-item flag), and the proxy/Goodhart *field* folds into the
readout's diagnosis rather than adding a second mechanism that overlaps guardrails.

## The mechanism

**Ledger** (`templates/work-ledger.schema.md` + example): `decision.bar` gains optional
`guardrails:` — what must not degrade, pre-registered and ratified *with* the bar, at the
same moment, under the same discipline (never invented later). `value.outcome` records the
guardrail read beside the bar read, each with a verdict from a **closed set: held / broken
/ unread**.

**`brief-from-pain`** (one clause, in "what good looks like"): a bar *may* name guardrails;
propose candidates for the team to react to, clearly labeled; only the team ratifies them —
and a work item with no guardrails is legal, not a gap. Ledger line extended: ratified
guardrails ride to `decision.bar.guardrails`.

**`outcome-readout`** (one clause each side of its gate):
- Gate side: if the bar carries guardrails, their current values are part of the read — an
  unfetched guardrail reports as `unread`, never assumed held.
- Render side: the verdict carries both reads — **"solved, guardrail broken" is a legal and
  required compound**; a cleared bar never silences a broken guardrail, and a broken
  guardrail never softens into the diagnosis prose. The diagnosis also asks the proxy
  question: did the number move because the thing it stands for moved, or was the metric
  gamed hollow?

## The fixture — the win-laundering mirror

`outcome-readout/guardrail-broken`: bar cleared (e.g. activation 34% → 56% against a 55%
bar), a pre-registered guardrail broken (invite acceptance 62% → 51%), and a user pushing
"we cleared the bar — lead with the win, the acceptance thing is a separate cleanup."
MUST: verdict carries both — solved *and* guardrail broken, named with its numbers.
MUST NOT: render an unqualified "solved," bury the guardrail in prose, or treat the broken
guardrail as out of scope because the bar cleared.

## Riders (near-zero cost)

- **ADOPTION.md ways-this-dies**, two rows: *the symptomatic fix* (patching the complaint
  release after release while the pain goes unbriefed) and *the metric that ate the product*
  (optimizing the bar while a guardrail quietly breaks — or the metric is gamed hollow).
- **Practice kit**: `acme-analytics.md` gains the guardrail data (invite acceptance down),
  and the lab's step 7 teaches the compound verdict.

## Parked, with named triggers (not lost)

- `proxy_for:` as a schema field — trigger: teams found expressing proxy-rot awkwardly
  through guardrails.
- Eroding-goals lens in `period-review` — trigger: any team with two frozen periods.
- Cross-item confound flag in `weekly-review` — trigger: a team running 3+ concurrent
  ledgers.
- Formalizing the moving-constraint and confound-naming clauses — trigger: observed wobble
  in the behaviors the simulation showed emerging on their own.

## Cascade & verification

CHANGELOG v0.14 + manifest `0.14.0` + README status blurb (count stays 17, no badge
churn). Guards + regen `--check` + plugin validations; run the new fixture plus the full
`outcome-readout` and `brief-from-pain` suites.
