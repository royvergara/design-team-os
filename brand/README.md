# brand/ — the Fluent by Design token layer, ported

Design Team OS renders pages (the scorecard, the conductor, the period review) and
Fluent by Design publishes documents and artifacts. They should look like one thing.
This folder is the port of the brand's token layer into this repo so that they can.

**Canonical lives elsewhere.** The source of truth is the fluentxdesign repo:
`DESIGN-DNA.md` (the brief: essence, palette, type, layout grammar, imagery, voice) and
`app/tokens.css` (the executable token layer). `tokens.css` here is a verbatim copy of
that file; `tests/check-brand.sh` fails if the two drift or if any other file in this
folder carries a raw hex colour. Edit tokens upstream, then re-copy.

| File | What it is |
| --- | --- |
| `tokens.css` | Verbatim copy of `fluentxdesign/app/tokens.css`. Two tiers: primitives (`--fxd-teal-900`, `--fxd-turquoise-500`, scales for space, type, tracking, leading, motion, elevation) and semantic (`--fxd-bg`, `--fxd-ink`, `--fxd-accent`, `--fxd-hairline`), plus the mist light theme under `[data-theme="light"]`. The only file allowed to contain raw hex. |
| `fonts.css` | The three faces — Gloock 400 (display), Source Sans 3 (body, UI), Archivo (machine voice) — loaded from Google Fonts, and the `--fxd-font-*` variables the tokens expect on `body`. For offline print rendering, swap the `@import` for local `@font-face` rules. |
| `print.css` | The document surface: fixed Letter pages, dark cover and section openers, light reading pages, running head and page number, and the registers a document needs (kicker, display title, lede, hairline rows, worksheet table, machine tiles, pull quote, refusal specimen, fill-in fields, contents, sources). Namespaced under `.doc`. |

The registers and their rules are in
[docs/superpowers/specs/2026-09-03-fluent-design-system-design.md](../docs/superpowers/specs/2026-09-03-fluent-design-system-design.md),
which also lists the increments that would turn this port into the system.
