# Examples

Two things here: a **trigger cheat sheet** (what to say to set each skill off), and a
**worked walkthrough** of one real feature traveling the whole loop, gates and all.

## Trigger cheat sheet

You don't call a skill by name — it activates on the situation its `description` names. Give
Claude the input below and the skill takes over.

| Skill | Gate | Give Claude… |
| --- | --- | --- |
| `research-to-pain` | Intent | raw research (interview notes, tickets, analytics) + "what's the real pain here?" |
| `prd-to-ia` | Intent | a PRD + "turn this into an information architecture" |
| `user-journey-mapping` | Intent | a named pain with evidence + "map the user journey" |
| `brief-from-pain` | Intent → Decision | a validated pain + "write the brief / what should we build" |
| `brief-to-prompt` | Decision | a brief + "write a prompt to prototype this in v0 / Bolt / Lovable / …" |
| `figma-plugin-orchestration` | Decision | a multi-plugin Figma task + "sequence this into one run" |
| `prototype-triage` | Decision | a generated prototype + its brief + "is this ready for review?" |
| `design-system-enforcement` | Decision | UI + your design system + "audit this against our system" |
| `critique-synthesis` | Decision | feedback from 2+ reviewers + "synthesize this into a direction" |
| `prototype-to-spec` | Value | a chosen prototype + its validation signal + "write the spec" |
| `outcome-readout` | Value | a shipped feature + its spec + live numbers + "did it work?" |
| `outcomes-scorecard` | Value / Program | a filled scorecard + its ledgers + "render the scorecard as a shareable page" |
| `period-review` | Program | a quarter's closed ledgers + "run the period review / close out the quarter" |
| `team-ai-baseline` | All gates | how your team actually works with AI + "where are we on the maturity curve?" |
| `conductor` | Routing | a work ledger, or whatever artifacts exist + "where are we / what's next?" |

Each skill also gates its own inputs, so a single skill is useful on its own. The sequence
below is where the full "PRD to validated, shipped, measured" path lives — and with the
`conductor` and a [work ledger](templates/work-ledger.schema.md), you never have to hold
that sequence in your head: ask "where are we?" and get the open gates and runnable moves.

---

## Worked walkthrough: a guided setup checklist for Acme

**Acme** is a B2B workspace product. New teams sign up but many never finish setup, so they
never reach the "aha" and churn. This walks one feature — a guided setup checklist — from PRD
to a measured outcome, through all three gates. Watch where the skills **refuse**: those
moments are the library doing its job, not failing.

### Gate 1 — Intent

**1. `prd-to-ia`** — *in:* the "Activation improvements" PRD. *out:* an IA (Setup Checklist
home, step screens, a progress indicator, an empty/return state), an **exclusions** list
(the PRD's billing changes and a GTM launch plan, each with one line on why they're not part
of this structure), and open questions (does the checklist live in the nav or a dismissible
panel?).

**2. `user-journey-mapping`** — *in:* the activation pain + evidence (PostHog funnel: 62% of
new workspaces never complete a second setup step; 4 onboarding interviews). *out:* a journey
across sign-up → first-run → drop-off, each cell grounded in the cited evidence, inferences
marked `INFERENCE`, and a closing line naming the **weakest evidence link** — "we assume
users *want* guidance rather than a faster empty product; validate next."

**3. `brief-from-pain`** — *in:* the named pain + IA. **It refuses.** The team hadn't said
what good looks like, and the skill won't write a brief without a pre-registered bar:

> Before I write this brief, set the success criteria. What measured result counts as solving
> the activation drop-off? I won't invent the bar.

The team commits: **activation rate (workspaces completing setup within 7 days) from 38% to
55% in 6 weeks.** *out:* the brief — pain, who it's for, scope (with the billing work
explicitly out, carried from the IA's exclusions), constraints, and a ratified "what good
looks like."

### Gate 2 — Decision

**4. `brief-to-prompt`** — *in:* the brief (target: v0). *out:* one clean v0 prompt (context, scope
with an explicit out-of-scope line, the design-system constraints, the must-have behaviors)
plus a **Discernment checklist** of what to inspect in the output.

**5. `prototype-triage`** — *in:* the generated prototype + the brief. **It fails the first
pass:**

> FAIL — not ready for review. Criteria table: progress indicator MET; one-screen flow MET;
> **empty/return state MISSING** (no view for a user coming back to a half-done checklist);
> **skip-for-now path MISSING** (brief criterion 4). Punch list back to `brief-to-prompt`:
> add the returning-user state and a always-available skip.

The prompt is regenerated with the gaps; the second prototype **passes** triage — so no human
review cycle was spent on the incomplete version.

**6. `design-system-enforcement`** — *in:* the passing prototype + Acme's design system. *out:*
violations only, each citing a rule — "checklist item uses `#2D7FF9`, off-token; use
`--color-accent`," "20px gap is off the 4px scale; use `--space-6`" — with severities. No
praise section.

**7. `critique-synthesis`** — *in:* review feedback from three people. *out:* a ranked
decision — the usability finding (testers missed the skip control) outranks a director's
repeated "make it bigger" styling opinion, which is recorded in dissents with the reason it
lost, plus reopen conditions.

### Gate 3 — Value

**8. `prototype-to-spec`** — *in:* the chosen prototype + its **validation signal** (a 6-person
test where 5 completed setup, up from a 2/6 baseline). *out:* the buildable spec — flows,
all states, components mapped to the design system by name, and the analytics events that must
ship (`setup_step_completed`, `setup_checklist_finished`, `setup_skipped`) — plus a
**Validation Record** quoting the test. (Hand it the prototype with only "the VP loved it" and
it refuses, and returns the smallest test that would earn a signal.)

**9. Ship.** Engineering builds from the spec; the analytics events ship with it.

**10. `outcome-readout`** — *in:* the spec's Validation Record + six weeks of live numbers.
The team is tempted to call it a win because signups look healthy — but **the skill holds:**

> Pre-registered bar: activation 38% → 55% in 6 weeks. Measured: **49%**. Verdict: **partial.**
> Real movement (+11 points), short of the bar. The funnel shows the new drop-off is now at the
> integration step, not the checklist. Next Intent input → take "integration-step drop-off" to
> `prd-to-ia` / `user-journey-mapping`. Don't claim the 55% target as met.

And the loop closes: that next-Intent line is where the cycle starts again.

---

### What the walkthrough shows

- **The gates refuse, and that's the value.** `brief-from-pain` forced a real success bar;
  `prototype-triage` caught an incomplete prototype before a human spent time on it;
  `outcome-readout` reported "partial" honestly instead of laundering a miss into a win.
- **Each output is the next input.** The IA's exclusions became the brief's scope; the brief's
  criteria became the triage table; the pre-registered bar became the readout's yardstick.
- **You can drop in anywhere.** Every skill gates its own inputs, so use one alone — but run
  them in sequence and you get the connective tissue: PRD to validated, shipped, measured.
- **The state survives the chat.** Run with a [work ledger](templates/work-ledger.schema.md)
  and every artifact above — the pain's evidence, the 38%→55% bar, the triage verdict, the
  Validation Record — lives in one file in the repo. Six weeks later, a teammate who never
  saw this conversation asks "where are we on the checklist?" and the `conductor` answers
  from the ledger: which gates are proven (with the artifacts), which are open, what runs
  next. That is the difference between a sequence you remember and a machine you resume.
