---
name: figma-plugin-orchestration
description: Use when a design task spans multiple Figma plugins or steps and needs to be sequenced from one instruction. Triggers on a request to coordinate, sequence, or automate plugin work in Figma. Always names which steps stay human.
---

# Figma Plugin Orchestration

You are producing a run sheet, and the run sheet's most important column is the one that says which steps a human keeps.

## Produce a run sheet

Decompose the instruction into ordered steps. For each step: the plugin or tool, the input it needs, the output it produces, and a marker, HUMAN or DELEGATED, with one line of reasoning.

## The delegation rule

Judgment calls are always HUMAN: choosing among generated options, assessing visual quality, brand fit, and anything that sets the quality bar for downstream steps. Mechanical transforms are DELEGATED: batch renames, token application, export pipelines, content population.

If a step mixes both, split it into two steps so the human part is visible and small rather than buried inside an automated one.

## Close the run sheet

End with the first human checkpoint: the earliest point in the sequence where a person should look at intermediate output before letting the rest run. A sequence with no checkpoint before the end is a sequence that wastes its own speed when step two was wrong.
