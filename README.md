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

Eleven skills are live under `skills/`: the original eight (v0.1, June 12, 2026) plus three loop-closing skills (v0.2) that wire the gates into a full Intent → Decision → Value → Intent loop.

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
| brief-from-pain | Intent → Decision | Turns a validated pain into a brief with a measurable bar set up front | v0.2 |
| prototype-triage | Decision | Triages a generated prototype against the brief before human review | v0.2 |
| outcome-readout | Value | Reads shipped analytics against the bar and names the next problem | v0.2 |

The last three close the loop end to end: Intent → Decision → Value → back to Intent. `brief-from-pain` bridges a validated pain into a brief, `prototype-triage` is the cheap readiness gate before human review, and `outcome-readout` reads the shipped result and hands strategy the next problem.

Each skill enforces its gate in practice, not just on paper. It refuses or flags when the inputs are not there: `prd-to-ia` will not draft without both a stated business goal and a customer pain, `user-journey-mapping` will not map without real evidence behind the pain, `prototype-to-spec` will not write a spec without a validation signal, `design-system-enforcement` will not audit against a system it had to imagine, `brief-from-pain` will not write a brief until success is defined in advance, `prototype-triage` will not pass a prototype that misses its brief, and `outcome-readout` will not call a launch a win without the pre-registered number. That refusal behavior is the point of each skill, and it is what the tests in [TESTING.md](TESTING.md) verify.

## Suggested workflow

The skills work ad hoc, but they were built to run in order, following the three gates. Used in sequence, each one's output is the next one's input, and the gates keep speed intentional from PRD to handoff.

**Gate 1, Intent.**

1. `prd-to-ia` — turn the PRD into a first pass IA and an explicit exclusions list. Its open questions feed the next step.
2. `user-journey-mapping` — map the journey for the validated pain, grounded in real evidence. The named pain becomes the spine of the brief.
3. `brief-from-pain` — turn that validated pain into a brief with scope and, before anything is generated, a measurable definition of what good looks like. This is the bar the Decision gate enforces.

**Gate 2, Decision.**

4. `brief-to-prompt-v0` or `brief-to-prompt-bolt` — convert the brief into a generation prompt. Pick by scope: v0 for a screen or component, Bolt for a full app or flow with data. Both refuse until the brief defines what good looks like, which sets the bar the next steps enforce.
5. `figma-plugin-orchestration` — when production work spans multiple Figma plugins. A utility inside this gate, not a fixed step.
6. `prototype-triage` — triage the generated prototype against the brief before it earns human review. A pass moves on; a fail routes back to the prompt step with the specific gaps, so review cycles are spent only on prototypes that meet the brief.
7. `design-system-enforcement` — audit what passed triage against your system.
8. `critique-synthesis` — fold scattered review feedback into one ranked direction.

**Gate 3, Value.**

9. `prototype-to-spec` — turn the chosen, validated prototype into a buildable spec. It refuses without a validation signal, which loops back to the evidence discipline from Gate 1.
10. `outcome-readout` — after the build ships, read the analytics against the brief's pre-registered bar, render the did-it-work verdict, and hand strategy the next problem worth starting. This is the loop back to Intent.

Each `SKILL.md` is self-contained and gates its own inputs, so you can drop into any single skill on its own. The sequence is where the "PRD to validated, code ready prototype" path actually lives; ad hoc use gives you the unit of judgment without the connective tissue.

## Install

Each skill is a folder under `skills/` containing a `SKILL.md`.

1. Clone or download this repo.
2. Drop the skill folder into your Claude Code skills directory — `.claude/skills/` in a project (shared with the team) or `~/.claude/skills/` for every project — or paste its `SKILL.md` into a Claude Project's instructions.

You don't invoke a skill by name. It triggers on the situation its `description` names — give Claude that input and the skill activates.

## Quickstart

Install `prd-to-ia`, then paste a PRD: *"Here's our PRD — turn it into an information architecture."* You get the IA, an explicit exclusions list, and the open questions worth taking to stakeholders.

Now feed it a PRD that states a business goal but no customer pain. It won't draft. It names what's missing and asks for the pain first. **That refusal is the skill working** — it is the whole point of the library, and the same discipline runs through every skill: `user-journey-mapping` won't map without evidence, `prototype-to-spec` won't spec without a validation signal, `design-system-enforcement` won't audit a system it had to imagine. The gates are what you're installing.

From there, follow the [Suggested workflow](#suggested-workflow) to run the skills in sequence, drop a [`design-os.profile.yaml`](templates/project-profile.schema.md) at your repo root so skills read your design system and event names instead of re-asking, and see [IMPLEMENTATION.md](IMPLEMENTATION.md) for project-vs-user install, reference-as-is vs. fork-and-tune, and the verification checklist. The tests in [TESTING.md](TESTING.md) show — and let you re-run — the gate behavior of every skill.

## This is the open layer

The skills are free and stay free. They are the open core of a larger system, Design Team OS, which installs the three gates into your team's actual workflow, trains the team, and proves the result with an outcomes scorecard. If that is interesting, the writing lives in the newsletter below and the door is open from there. No pitch in the repo.

## Who made this

Roy Vergara. Ten plus years in product design leadership. The library exists because the trust gap is real and measured: far fewer designers trust AI output than developers do. Closing it takes someone with deep design judgment and AI fluency, not another dev flavored tool drop. That is the lane this fills.

Newsletter: **[Fluent by Design](https://fluentxdesign.substack.com/)**. AI made production cheap, judgment got expensive, and this is the weekly working through of what that means for design teams.

## License

MIT. See [LICENSE](LICENSE). Use it, fork it, ship it.

## Status

v0.2. Eleven skills are live — the eight v0.1 skills plus three loop-closing additions (`brief-from-pain`, `prototype-triage`, `outcome-readout`) — each tested against its gate by a runnable harness (see [TESTING.md](TESTING.md)), and ready to use. New skills drop every Friday.
