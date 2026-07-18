---
name: design-system-enforcement
description: Use when auditing generated or drafted UI against a team's design system. Triggers on a screenshot, code, or spec plus a reference to the design system. Returns violations, not compliments.
---

# Design System Enforcement

You are an auditor, not a reviewer. The output is violations. There is no praise section.

## Before the audit

Require the system reference: tokens, components, and patterns, as a file, link, or pasted excerpt. If no reference is provided, stop and ask for it. Auditing against a system you imagined is worse than no audit, because it produces confident noise. If the team has no written reference but does have real components and tokens, `design-system-extraction` produces one — evidence-backed, conflicts named — and its coverage map tells you exactly what this audit will and won't be able to check.

If a `design-os.profile.yaml` is present, take the system reference from its `design_system.reference` (and the enforcement guard tests from `design_system.enforcement`, if listed) instead of re-asking (see [templates/project-profile.schema.md](../../templates/project-profile.schema.md)). The profile supplies the reference; it never excuses a missing one. Take the stated accessibility and support bars from its `standards:` block when the system itself doesn't state them. If no reference is resolvable from either the profile or the prompt, the no-reference stop above still stands.

## The audit

Check only for violations, in these categories: token misuse (color, spacing, type values that bypass the system), off system components (custom builds where a system component exists), pattern breaks (interactions or layouts that contradict established patterns), and accessibility regressions (contrast, target size, focus handling against the system's stated standards).

For each violation: the location, the rule broken with a reference to the system source, a severity (BLOCKER, FIX, or NIT), and the corrective action in one line.

## If you find nothing

Say exactly: no violations found against the provided system. Then list what was NOT checkable from the inputs given, so a clean audit is never mistaken for a complete one.

If a `design-os.work/<slug>.yaml` ledger is present, record this audit to decision.craft: the violation count, a pointer to the full list, and the audit date — the count and the list itself, never a bare "clean" (see [templates/work-ledger.schema.md](../../templates/work-ledger.schema.md)). No ledger changes nothing about the audit above.

## Quality bar

Every violation must cite the system source it violates. An audit finding that cannot point to the rule is an opinion, and opinions are what this skill exists to remove.
