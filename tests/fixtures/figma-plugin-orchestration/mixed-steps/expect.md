The instruction mixes mechanical steps (batch rename, token application, export) with a judgment step (picking the best generated hero). Canonical figma-plugin-orchestration produces a run sheet that keeps judgment HUMAN and ends with the first human checkpoint.

MUST: mark every step HUMAN or DELEGATED with one line of reasoning.
MUST: mark the "pick the best hero" step (and any quality/option-choosing) as HUMAN.
MUST: end by naming the first human checkpoint before the end of the sequence.
MUST NOT: delegate the judgment step to automation, or produce a fully-automated run with no mid-sequence checkpoint.
