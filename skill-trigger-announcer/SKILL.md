---
name: skill-trigger-announcer
description: Announce triggered skills before executing a task. Use when the user asks for transparency about which skills are active, wants a short preface listing triggered skills, or requests that each turn starts with a concise skill-activation summary.
---

# Skill Trigger Announcer

Before doing substantive work in the current turn, print a concise preface that lists the triggered skills and one-line purpose for each.

## Output Rule

Use this format at the top of the assistant message:

- `Triggered skills:` comma-separated skill names in execution order
- `Purpose:` one short line per skill (max 12 Chinese words or 10 English words)

If only one skill is active, still use the same format.

If no additional skill is active, print:

- `Triggered skills:` none
- `Purpose:` no extra skill applied

## Brevity Constraint

Keep the preface under 4 lines total, then proceed with normal task execution.

## Ordering Rule

When multiple skills are used, list them in the actual execution order.

## Scope

Apply this announcement once per turn before actions that read, edit, run, or generate artifacts.
