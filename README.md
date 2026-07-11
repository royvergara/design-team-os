# Design Team OS

**The open source operating system for design teams running on AI — from mandate to proof.**

Most AI skill libraries are built for a single designer trying to move faster. This is an operating system for the whole team: three gates that keep speed intentional, skills that enforce them and refuse when the inputs aren't earned, a ledger that carries the evidence from pain to shipped outcome, and a conductor that always knows what can run next. It connects a company's AI mandate to what its design team actually ships, so every fast, cheap prototype stays tied to something that matters.

---

## Who this is for

Heads of Design, VPs of Design, and Design Directors at product led companies, usually 50 to 500 people, running a team of 5 to 20 designers.

You have the AI tools. Your team is experimenting in private. Quality is all over the place, engineering is racing ahead, and you do not yet have a shared way of working that turns all that motion into proof. That gap is what this library closes.

And if you're the designer on that team, not the one leading it: the skills work for you alone, in a browser, today — copy one file into a Claude Project and go ([60-second path](PROJECTS.md)). The system is built for the team; every piece of it is useful solo.

Want to see it work before reading another word? [EXAMPLES.md](EXAMPLES.md) walks one feature through the whole loop — including the moments the skills refuse, which is the point.

## What it is

A set of Claude skills that takes a design team from raw research to a shipped, measured outcome in days instead of weeks. Each skill is a small, focused unit of judgment you can drop into Claude Code or a Claude Project. MIT licensed. It grows by release: each version either extends the machine — a new gate skill, the work ledger, the `conductor` — or sharpens a capability it already has ([CHANGELOG.md](CHANGELOG.md) has the history).

## The spine

The skills are not random utilities. They map to three decision gates. The gates are the point. They are what keep speed intentional once anyone can generate a prototype in an afternoon.

**Gate 1, Intent.** Does this map to a business goal and a real customer pain? Governs which work is worth starting.

**Gate 2, Decision.** What do we prototype, and what does good look like? Governs what gets built and what the quality bar is. This is where design judgment lives, and it is the part AI cannot do for you.

**Gate 3, Value.** Did it solve the pain and move the needle? Governs the proof that the work mattered, and the loop back to strategy.

Speed without these gates is fifty prototypes and no way to choose. Speed with them is a team that learns faster and can show the learning paid off.

## The machine

The gates take judgment; the routing between them never should have. Two pieces carry the routing so nobody has to hold the sequence in their head — and neither ever makes a judgment call:

**The work ledger** (`design-os.work/<slug>.yaml`, schema in [templates/work-ledger.schema.md](templates/work-ledger.schema.md)) is one file per piece of work that carries its state across sessions, people, and weeks: which gates are proven, with the evidence itself embedded. Its one rule: **artifacts, never checkmarks.** There is no `done: true` in the schema, deliberately — an entry is the evidence, the pre-registered bar, the quoted validation signal, or the gate is open. Skills write their own artifacts; humans see the work's state change as a diff in a PR.

**The conductor** (`skills/conductor/`) reads that state — or, with no ledger, whatever artifacts you describe — and reports which gates are proven, which are open, and what can run right now. Resume after two weeks out, hand work to a teammate, or walk in mid-stream with a PM's prototype that never saw Gate 1: ask "where are we?" and it answers with the state set and the runnable moves, several at once when several apply. **It routes; it never judges.** It will not certify a gate, and it refuses to carry a checkmark forward — a `validated: true` with no evidence behind it reads as an open gate, and it says so.

And because real organizations sometimes proceed without evidence on purpose — a contract commitment, a compliance deadline, a strategic call — a gate can carry an **owned bet** instead of its artifact: a named owner, a declared acknowledgment that the evidence is absent, the reason, and a review date that will judge the bet ([schema](templates/work-ledger.schema.md)). A bet never reads as proven and never excuses the bar; it makes the exception loud and owned instead of silent. What separates a bet from a laundered gate: laundering claims the evidence exists, a bet declares it absent and signs for it.

None of this is required. Every skill still gates its own inputs and works alone in a chat with nothing else installed; the machine is what makes the loop resumable and shared. Work is a state set, not an assembly line — cycles are normal, parallel work items are normal, and entering anywhere is normal, because the gates themselves route wrong-order entry back to what's missing.

## Skills

Fourteen skills are live under `skills/` — every skill's primary refusal is encoded as a runnable fixture, with adversarial coverage growing release by release ([TESTING.md](TESTING.md)): the original eight (v0.1, June 12, 2026), three loop-closing skills (v0.2) that wire the gates into a full Intent → Decision → Value → Intent loop, the most upstream skill in the library (v0.3) that produces the validated pain everything else assumes, `team-ai-baseline` (v0.4), which sits above the gates and tells a team whether it is actually running them, and the `conductor` (v0.5), the machine's routing layer.

| Skill | Gate | What it does | Status |
| --- | --- | --- | --- |
| conductor | Routing | Reads a work ledger and reports which gates are proven, which are open, and what can run now | v0.5 |
| team-ai-baseline | All gates | Places a team honestly on the AI maturity curve and names the one gate holding it back | v0.4 |
| research-to-pain | Intent | Turns raw research into a small set of ranked, evidence-backed customer pains | v0.3 |
| brief-from-pain | Intent → Decision | Turns a validated pain into a brief with a measurable bar set up front | v0.2 |
| prototype-triage | Decision | Triages a generated prototype against the brief before human review | v0.2 |
| outcome-readout | Value | Reads shipped analytics against the bar and names the next problem | v0.2 |
| prd-to-ia | Intent | Turns a PRD into a first pass information architecture | v0.1 |
| design-system-enforcement | Decision | Holds generated UI to your design system | v0.1 |
| critique-synthesis | Decision | Synthesizes scattered critique into clear direction | v0.1 |
| user-journey-mapping | Intent | Drafts a journey map from a brief and known signals | v0.1 |
| prototype-to-spec | Value | Turns a chosen prototype into a buildable spec | v0.1 |
| brief-to-prompt-v0 | Decision | Converts a brief into a clean v0 by Vercel prompt | v0.1 |
| brief-to-prompt-bolt | Decision | Converts a brief into a clean Bolt.new prompt | v0.1 |
| figma-plugin-orchestration | Decision | Coordinates Figma plugin steps from one instruction | v0.1 |

`research-to-pain` sits one step above everything else. The rest of Gate 1 assumes a validated pain already exists, but nothing produced it until now: it takes interview notes, support tickets, and analytics and returns a short set of pains, each with the signal behind it named and the weakest flagged for more validation. The three v0.2 skills close the loop end to end: Intent → Decision → Value → back to Intent. `brief-from-pain` bridges a validated pain into a brief, `prototype-triage` is the cheap readiness gate before human review, and `outcome-readout` reads the shipped result and hands strategy the next problem.

Each skill enforces its gate in practice, not just on paper. It refuses or flags when the inputs are not there: `research-to-pain` will not crown a pain as validated on stakeholder opinion or thin, untriangulated signal, `prd-to-ia` will not draft without both a stated business goal and a customer pain, `user-journey-mapping` will not map without real evidence behind the pain, `prototype-to-spec` will not write a spec without a validation signal, `design-system-enforcement` will not audit against a system it had to imagine, `brief-from-pain` will not write a brief until success is defined in advance, `prototype-triage` will not pass a review candidate that misses its brief (and leaves divergent exploration alone), `outcome-readout` will not call a launch a win without the pre-registered number, `team-ai-baseline` will not count a mandate or tools bought as adoption or place a team above what its actual practice supports, and the `conductor` will not treat a checkmark as a passed gate or route work into a skill whose own gate would refuse it. The one sanctioned exception is the [owned bet](templates/work-ledger.schema.md) — proceeding without evidence, on the record, with a named owner and a review date. That refusal behavior is the point of each skill, and it is what the tests in [TESTING.md](TESTING.md) verify.

## Templates

Three files under `templates/` carry the state the skills read and write, plus the one artifact you take upward.

| Template | What it is |
| --- | --- |
| [`work-ledger.schema.md`](templates/work-ledger.schema.md) | One `design-os.work/<slug>.yaml` per feature. Gate state as artifacts, never checkmarks, plus the owned bet. What the conductor reads. |
| [`project-profile.schema.md`](templates/project-profile.schema.md) | The stable answers, once: design system, event names, repo conventions. So skills stop re-asking. |
| [`ai-outcomes-scorecard.md`](templates/ai-outcomes-scorecard.md) | The program level scorecard. `outcome-readout` scores one shipped feature; this rolls the whole effort up and refuses to call activity a result. |

The scorecard is the layer a Head of Design actually reports on. Two layers, Leverage and Outcome, and one headline sentence that only fills in when both halves are real: the work got faster, and the speed moved a number. It reads from the verdicts the ledgers already hold, lists every owned bet in its own section with the date that will judge it, and gives a leverage report no way to pass itself off as a result.

## Suggested workflow

The skills work ad hoc, but they were built to run in order, following the three gates. Used in sequence, each one's output is the next one's input, and the gates keep speed intentional from PRD to handoff. [EXAMPLES.md](EXAMPLES.md) walks one real feature through this whole sequence, gates and refusals included.

You don't have to memorize any of it: with the `conductor` installed, "where are we?" returns the work's gate state and the runnable next moves. The sequence below is the map; the conductor is the guide. Treat the numbered order as the common path, not a requirement — work enters anywhere, and the gates route wrong-order entry back to what's missing.

**Gate 1, Intent.**

1. `research-to-pain`: when you are starting from raw research instead of a clean PRD, turn interview notes, tickets, and analytics into a small set of ranked, evidence-backed pains, the weakest one flagged. The strongest validated pain is what the rest of Gate 1 builds on.
2. `prd-to-ia`: turn the PRD into a first pass IA and an explicit exclusions list. Its open questions feed the next step.
3. `user-journey-mapping`: map the journey for the validated pain, grounded in real evidence. The named pain becomes the spine of the brief.
4. `brief-from-pain`: turn that validated pain into a brief with scope and, before anything is generated, a measurable definition of what good looks like. This is the bar the Decision gate enforces.

**Gate 2, Decision.**

5. `brief-to-prompt-v0` or `brief-to-prompt-bolt`: convert the brief into a generation prompt. Pick by scope: v0 for a screen or component, Bolt for a full app or flow with data. Both refuse until the brief defines what good looks like, which sets the bar the next steps enforce.
6. `figma-plugin-orchestration`: when production work spans multiple Figma plugins. A utility inside this gate, not a fixed step.
7. `prototype-triage`: triage the generated prototype against the brief before it earns human review. A pass moves on; a fail routes back to the prompt step with the specific gaps, so review cycles are spent only on prototypes that meet the brief.
8. `design-system-enforcement`: audit what passed triage against your system.
9. `critique-synthesis`: fold scattered review feedback into one ranked direction.

**Gate 3, Value.**

10. `prototype-to-spec`: turn the chosen, validated prototype into a buildable spec. It refuses without a validation signal, which loops back to the evidence discipline from Gate 1.
11. `outcome-readout`: after the build ships, read the analytics against the brief's pre-registered bar, render the did-it-work verdict, and hand strategy the next problem worth starting. This is the loop back to Intent.

Each `SKILL.md` is self-contained and gates its own inputs, so you can drop into any single skill on its own. The sequence is where the full "PRD to validated, shipped, measured" path actually lives; ad hoc use gives you the unit of judgment without the connective tissue.

## Install — two doors

**Door one: your browser, 60 seconds, no install.** For designers (and anyone) who live in claude.ai, not a terminal. Pick a skill from the table above, copy its `SKILL.md`, paste it into a Claude Project's instructions, hand it your input. The gates hold there — tested, including several skills pasted into one Project. The full path, per-gate bundles, and the honest limits are in **[PROJECTS.md](PROJECTS.md)**.

**Door two: Claude Code — the full machine.** One command adds the marketplace, one installs everything: all fourteen skills, the `conductor` among them, and a `/design-team-os:init` setup command. Updates come through `/plugin`, no re-copying.

```
/plugin marketplace add royvergara/design-team-os
/plugin install design-team-os@fluent-by-design
```

Then, in your product repo, run `/design-team-os:init` once — it scaffolds the [project profile](templates/project-profile.schema.md) and the [work-ledger](templates/work-ledger.schema.md) directory the skills read and write. After that, just describe your work — hand Claude your research, a PRD, or a prototype and the skill that fits takes over. Not sure where things stand? Ask *"where are we?"* and the conductor tells you what's proven and what to run next. You never have to pick from a list of skills.

**Also fine: by hand.** Each skill is a folder under `skills/` with one `SKILL.md`. Clone the repo and drop folders into `.claude/skills/` in your project (shared with the team via git) or `~/.claude/skills/` for every project.

Whichever door: you don't invoke a skill by name — it triggers on the situation its `description` names. Give Claude that input and the skill activates.

The same skill files serve both doors, unchanged. The machine — ledger, conductor, init — is what makes the loop resumable and shared across a team; the skills alone are what make one person's next hour better. Start wherever you are.

## Quickstart

Through either door, hand Claude a pile of raw research: *"Here are our interview notes, support tickets, and the activation funnel. What's the real pain?"* — `research-to-pain` takes over. You get a short set of pains, each with the signal named, ranked by how much independent evidence agrees, the weakest one flagged with the cheapest test to firm it up.

Now hand it research that is really just opinion, three execs who agree and a board mandate. It won't crown a validated pain. It names what is missing and the fastest signal that would settle it. **That refusal is the skill working.** It is the whole point of the library, and the same discipline runs through every skill: `prd-to-ia` won't draft without a goal and a pain, `user-journey-mapping` won't map without evidence, `prototype-to-spec` won't spec without a validation signal. The gates are what you're installing.

For the fastest sense of how the pieces fit, read **[EXAMPLES.md](EXAMPLES.md)**, one feature walked through the core loop, plus a trigger cheat sheet for what to say to set each skill off. From there, follow the [Suggested workflow](#suggested-workflow) to run the skills in sequence, drop a [`design-os.profile.yaml`](templates/project-profile.schema.md) at your repo root so skills read your design system and event names instead of re-asking, and let [work ledgers](templates/work-ledger.schema.md) carry each feature's gate state so "where are we?" always has an answer. See [IMPLEMENTATION.md](IMPLEMENTATION.md) for project-vs-user install, reference-as-is vs. fork-and-tune, and the verification checklist. The tests in [TESTING.md](TESTING.md) show, and let you re-run, the gate behavior of every skill.

## This is the open layer

The skills are free and stay free, MIT, no strings. They are also the open core of a paid practice — Design Team OS as a service: installing the three gates into a team's actual workflow, training the team, and proving the result with an outcomes scorecard. That's the honest shape of this repo: everything a team needs to run the system itself is here; what's for sale is someone who has run it before doing the installation and holding the line. If that's interesting, the writing lives in the newsletter below.

## Who made this

Roy Vergara. Ten plus years in product design leadership. The library exists because the trust gap is real and measured: far fewer designers trust AI output than developers do. Closing it takes someone with deep design judgment and AI fluency, not another dev flavored tool drop. That is the lane this fills.

Newsletter: **[Fluent by Design](https://fluentxdesign.substack.com/)**. AI made production cheap, judgment got expensive, and this is the weekly working through of what that means for design teams.

## License

MIT. See [LICENSE](LICENSE). Use it, fork it, ship it.

## Status

v0.6 — the release where the gates learn to bend without breaking. Fourteen skills are live, now with the **owned bet**: a recorded, named, review-dated way to proceed without evidence on purpose, so the exception is loud instead of silent. Judgment tuned where fresh review found it too absolute (signal weight in `research-to-pain`, constraints and evidence quality in `critique-synthesis`, an exploration carve-out in `prototype-triage`), and a first-class browser path in [PROJECTS.md](PROJECTS.md). Every skill's primary refusal is encoded as a runnable fixture ([TESTING.md](TESTING.md)). Full version history in [CHANGELOG.md](CHANGELOG.md).
