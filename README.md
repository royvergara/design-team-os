# Design Team OS

**An open source Claude skill library for product design teams running on AI.**

Most AI skill libraries are built for a single designer trying to move faster. This one is built for the whole team. It is the operating layer that connects a company's AI mandate to what its design team actually ships, so every fast, cheap prototype stays tied to something that matters.

---

## Who this is for

Heads of Design, VPs of Design, and Design Directors at product led companies, usually 50 to 500 people, running a team of 5 to 20 designers.

You have the AI tools. Your team is experimenting in private. Quality is all over the place, engineering is racing ahead, and you do not yet have a shared way of working that turns all that motion into proof. That gap is what this library closes.

## What it is

A growing set of Claude skills that take a design team from a PRD to a validated, code ready prototype in days instead of weeks. Each skill is a small, focused unit of judgment you can drop into Claude Code or a Claude Project. MIT licensed. New skills drop every Friday.

## The spine

The skills are not random utilities. They map to three decision gates. The gates are the point. They are what keep speed intentional once anyone can generate a prototype in an afternoon.

**Gate 1, Intent.** Does this map to a business goal and a real customer pain? Governs which work is worth starting.

**Gate 2, Decision.** What do we prototype, and what does good look like? Governs what gets built and what the quality bar is. This is where design judgment lives, and it is the part AI cannot do for you.

**Gate 3, Value.** Did it solve the pain and move the needle? Governs the proof that the work mattered, and the loop back to strategy.

Speed without these gates is fifty prototypes and no way to choose. Speed with them is a team that learns faster and can show the learning paid off.

## Skills

The first eight shipped in v0.1 on June 12, 2026. All eight are live under `skills/`.

| Skill | Gate | What it does | Status |
| --- | --- | --- | --- |
| prd-to-ia | Intent | Turns a PRD into a first pass information architecture | v0.1 |
| design-system-enforcement | Decision | Holds generated UI to your design system | v0.1 |
| critique-synthesis | Decision | Synthesizes scattered critique into clear direction | v0.1 |
| user-journey-mapping | Intent | Drafts a journey map from a brief and known signals | v0.1 |
| prototype-to-spec | Value | Turns a chosen prototype into a buildable spec | v0.1 |
| brief-to-prompt-v0 | Decision | Converts a brief into a clean v0 by Vercel prompt | v0.1 |
| brief-to-prompt-bolt | Decision | Converts a brief into a clean Bolt.new prompt | v0.1 |
| figma-plugin-orchestration | Decision | Coordinates Figma plugin steps from one instruction | v0.1 |

Each skill enforces its gate in practice, not just on paper. It refuses or flags when the inputs are not there: `prd-to-ia` will not draft without both a stated business goal and a customer pain, `user-journey-mapping` will not map without real evidence behind the pain, `prototype-to-spec` will not write a spec without a validation signal, and `design-system-enforcement` will not audit against a system it had to imagine. That refusal behavior is the point of each skill, and it is what the tests in [TESTING.md](TESTING.md) verify.

## Install

Each skill is a folder under `skills/` containing a `SKILL.md`. To use one:

1. Clone or download this repo.
2. Drop the skill folder into your Claude Code skills directory, or paste the contents of its `SKILL.md` into a Claude Project's instructions.
3. Call the skill the way the `SKILL.md` describes.

Each skill's `description` frontmatter says when it triggers and what it always returns. The `skills/` folder explains the file convention if you want to read or adapt the skills yourself.

## This is the open layer

The skills are free and stay free. They are the open core of a larger system, Design Team OS, which installs the three gates into your team's actual workflow, trains the team, and proves the result with an outcomes scorecard. If that is interesting, the writing lives in the newsletter below and the door is open from there. No pitch in the repo.

## Who made this

Roy Vergara. Ten plus years in product design leadership. The library exists because the trust gap is real and measured: far fewer designers trust AI output than developers do. Closing it takes someone with deep design judgment and AI fluency, not another dev flavored tool drop. That is the lane this fills.

Newsletter: **[Fluent by Design](https://fluentxdesign.substack.com/)**. AI made production cheap, judgment got expensive, and this is the weekly working through of what that means for design teams.

## License

MIT. See [LICENSE](LICENSE). Use it, fork it, ship it.

## Status

v0.1, shipped June 12, 2026. The first eight skills are live, tested against their gates across smoke and adversarial rounds (see [TESTING.md](TESTING.md)), and ready to use. New skills drop every Friday.
