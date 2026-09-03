# Design: the Fluent by Design system — one token layer, every surface

Slated, not built. This spec names the design system that Design Team OS renders, Fluent by
Design's site, its newsletter, its documents and its artifacts should all draw from, so
that a future increment can build it against a written target instead of re-deriving the
brand from whichever file was opened last. It records what exists today, where it lives,
what drifts, and the increments that would close the drift — in order.

## Why now

The brand already exists three times. `DESIGN-DNA.md` in the fluentxdesign repo is the
brief (essence, tokens, type, layout grammar, imagery, voice). `app/tokens.css` there is
the executable token layer — two tiers, primitives and semantic, a mist light theme, and a
guard script that fails the build on any raw hex outside the token file. This repo's
`templates/scorecard.html` and `templates/conductor.html` carry the same fonts and palette
by hand. And the published artifacts (the Unproven Velocity guide, the judgment workbook)
were built from memory of the brand, and drifted: a different body face, an accent that is
not a token. Three copies of a brand is how a fourth one gets invented.

## What is canonical, today

| Layer | Source of truth | Consumers today |
| --- | --- | --- |
| Essence, voice, imagery, do/don't | `fluentxdesign/DESIGN-DNA.md` | humans |
| Tokens (primitives, semantic, themes) | `fluentxdesign/app/tokens.css` | the site, the baseline, the four-stages guide |
| Fonts | `fluentxdesign/app/fonts.ts` — Gloock 400, Source Sans 3, Archivo | the site |
| Print idiom | `fluentxdesign/app/four-stages/guide.css` — page scaffold, cover, contents, chapter, template, sources | the four-stages guide |
| Document archetype | `fluentxdesign/docs/superpowers/specs/2026-07-27-maturity-benchmark-pdf-design.md` | the four-stages guide |
| Rendered artifacts in this repo | `templates/scorecard.html`, `templates/conductor.html` | `outcomes-scorecard`, `period-review`, the `conductor` |
| Token guard | `fluentxdesign/scripts/check-no-raw-hex.mjs` | CI, there only |

Nothing in this table is in dispute. The gap is that only the first column knows the
second exists.

## The system, named

Five parts, each already partly real:

1. **Tokens.** One file, two tiers. Primitives (`--fxd-teal-900`, `--fxd-turquoise-500`,
   the mist and forest scales, spacing, radii, type scale, tracking, leading, motion,
   elevation) and semantic (`--fxd-bg`, `--fxd-ink`, `--fxd-accent`, `--fxd-hairline`
   and their light-theme remaps). Components read semantic only. Raw hex exists in this
   file and nowhere else.
2. **Type.** Gloock for every heading and for serif subtitles in muted; Source Sans 3 for
   body and UI; Archivo for the wordmark's machine voice and wide-tracked labels; a mono
   for readouts. Three faces per view at most, two in most.
3. **Registers.** The recurring compositions: eyebrow with dash rule; serif headline with
   serif subtitle; hairline-divided rows; the machine treatment for data (turquoise
   numerals, small-caps labels); pull quote with turquoise left rule; pill buttons, one
   primary per view; the belief/practice pair for statistics, never a stat alone.
4. **Surfaces.** Screen (site, artifacts), document (print pages: dark cover and section
   openers, light reading pages, contents on page two, running footer), and render
   (the scorecard and review pages skills emit). Same tokens, three stylesheets.
5. **Guards.** The no-raw-hex check, extended to every surface; a visual regression page
   per surface (the styleguide route exists for screen); and the archetype checks for
   documents (contents on p2, chapter ends in a play, vendor once, sources page, no em
   dashes in body, no prices, "install" reserved).

## Increments, in order

Each increment is shippable alone and leaves the system more true than it found it.

1. **The brand port** (this release). Copy `tokens.css` primitives and semantic tiers into
   `brand/tokens.css` in this repo, verbatim, with a header naming fluentxdesign as
   canonical and a diff check against it. Add `brand/print.css` from the four-stages
   guide idiom and `brand/README.md` pointing at Design DNA. Rebuild the two published
   artifacts on it. Add the raw-hex guard for `brand/` and `templates/`.
2. **Templates onto tokens.** `scorecard.html` and `conductor.html` read `brand/tokens.css`
   instead of carrying their palette by hand. The renders skills emit stop drifting from
   the site. Verify by screenshot against the styleguide.
3. **The registers, documented.** One page per register, each with its markup, its tokens,
   and one do/don't pair — the component reference `design-system-extraction` would
   produce if it were run on the site, which is the honest way to write it: run the skill
   on `app/` and let it name the conflicts.
4. **One source, two repos.** Decide where the canonical token file lives once the port
   proves the copy stays in sync. The default is fluentxdesign, with this repo's copy
   checked in CI against it. A package is the other option and is probably not worth it
   for two consumers.
5. **The document surface, generalized.** Turn `guide.css` from one guide's stylesheet into
   the print surface: cover, contents, chapter opener, worksheet, sources, about, each as
   a register. The three PDFs in this release are its first real load.
6. **Guards everywhere.** The raw-hex check runs on both repos; the archetype check runs
   on every document source; the styleguide route gets a document twin.

## What this is not

- Not a new visual direction. Design DNA is the brief and stays it.
- Not a component library for product UI. This is the brand's own surfaces.
- Not a design-token pipeline product. Two consumers, one file, a diff check.

## Kill criteria

The system dies as a separate effort if, after increments 1 and 2, the artifacts and the
site stop drifting on their own — at which point the token file is the system and this
spec is documentation. It also dies if increment 3 produces registers nobody references
within two releases; a reference nobody reads is a brochure.
