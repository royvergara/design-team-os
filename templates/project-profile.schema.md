# The project profile

A **project profile** is one file at the root of your product repo that answers, once,
the questions every Design Team OS skill would otherwise re-ask on every run: where your
design system lives, what your analytics events are called, how your routes are named,
where specs get written. Skills read it instead of interrogating you.

File name: **`design-os.profile.yaml`**. It lives in **your product repo**, not in this
library. This library ships only the schema (this file) and an example
([`project-profile.example.yaml`](project-profile.example.yaml)).

## Why it exists

Dogfooding the library into a real app surfaced one adoption tax: every skill re-asked for
the same stable context, so users forked each skill and hard-coded their product's tokens,
routes, and event names. The profile replaces that — supply the context once, every skill
reads it.

## Two surfaces, opposite capabilities

A skill is consumed two ways, and the profile has to work in both:

| | Claude Code CLI | Claude Project / chat agent |
| --- | --- | --- |
| Filesystem + product repo present | yes | no |
| Can a skill read & verify a value | yes — read the file, grep the source | no — only what's in context |
| How the profile arrives | a file in the repo root | pasted into the Project once |

This is why the schema keeps **explicit values** (so a chat agent, which can grep nothing,
still has them) **and** `source:` pointers (so a CLI skill can re-derive and verify them).
It is self-contained for chat and self-verifying in CLI.

## Schema

Only fields that at least one skill reads. Every field is optional; a skill uses what's
present and falls back for what isn't.

| Field | What it is | Read by |
| --- | --- | --- |
| `profile_version` | Schema version (currently `1`). | all |
| `verified_against_commit` | Product-repo SHA the values were checked at. A CLI skill warns if HEAD is ahead. | all (CLI) |
| `project`, `stack` | Name and stack, for the skill's own framing. | all |
| `design_system.reference` | Where the DS rules live (human-readable source of truth). | design-system-enforcement, prototype-to-spec |
| `design_system.enforcement` | The guard tests/CI checks that fail when the system breaks. | design-system-enforcement |
| `design_system.component_catalog` | Where reusable components/classes live. | prototype-to-spec, design-system-enforcement |
| `routes.source` | Glob a CLI skill re-derives routes from. | (CLI) |
| `routes.key` | The named routes skills reason about. Kept small on purpose. | prototype-to-spec, prototype-triage |
| `analytics.tool` | The analytics product. | prototype-to-spec, outcome-readout |
| `analytics.source` | Where event names are defined (e.g. `posthog.capture()` sites). | (CLI) |
| `analytics.events` | Explicit event names — the instrumentation vocabulary. | prototype-to-spec, outcome-readout |
| `evidence_sources` | Where validation signal comes from. | brief-from-pain, prototype-to-spec |
| `spec_output` | Path pattern for written specs. | prototype-to-spec |
| `personas` | Named user personas. | prd-to-ia, brief-from-pain |
| `constraints` | Stack-specific gotchas that change a skill's output. | all |

## How a skill consumes the profile (the standard stanza)

Every profile-consuming skill carries this block verbatim — kept deliberately short so it
adds almost nothing to the tokens loaded each time the skill triggers, while letting the
skill **delete** its longer "ask the user for context" prose. Self-contained because skills
are pasted into Projects individually and cannot reference a sibling file.

```markdown
## Project profile (read before asking for context)

Before asking for design-system, analytics, route, or spec-path context, look for a
project profile named `design-os.profile.yaml`:

- **If you can read files:** read it from the repo root. Before trusting any value you
  rely on, verify it against its `source` (e.g. grep `posthog.capture(` for events). If
  `verified_against_commit` is behind HEAD, treat the values as possibly stale and say so.
- **If you cannot read files (chat / Project):** use the profile if it was pasted into
  context; otherwise ask once for the specific field you need, not a full questionnaire.
- **No profile present:** fall back to this skill's "Inputs needed" and flag the missing
  context in *Decisions you should check*.

Never let the profile override a refusal gate. A profile supplies context; it does not
satisfy a gate that requires a judgment (a goal, a pain, a validation signal, a metric).
```

That last line matters: the profile makes skills less repetitive, **not** less strict. A
gate that refuses without a success metric still refuses — the profile can hold the metric
*source*, but the human still sets the bar.

## Bootstrapping the profile (don't transcribe it by hand)

A profile we hand-transcribed from a real app once drifted within a week — it undercounted
the design-system guards 3×, dropped two analytics events (both failure-path), and listed a
fraction of the routes. A profile that points at a moved or miscounted target is worse than
none. So **generate it from the repo**, then review and commit. In Claude Code, ask:

> Read this repo and write `design-os.profile.yaml`. For `analytics.events`, grep
> `posthog.capture(` (or my analytics tool's capture call) **in app source only —
> exclude `node_modules`**, or a dependency's own events leak in. For `routes.key`, list
> the primary `app/**/page.tsx` entries. For `design_system.enforcement`, find the guard
> tests. Fill `verified_against_commit` with the current short SHA. Show me the file to
> review before writing it.

Re-run it whenever the repo moves enough to matter; bump `verified_against_commit`. A chat
agent can't grep, so chat users take this generated file and paste it into their Project's
knowledge once — same accurate context, no filesystem required.

This keeps the heavy work (grepping, regenerating) on the **cold path** — run occasionally,
never loaded into context at skill-trigger time — while the hot-path stanza above stays
small.
