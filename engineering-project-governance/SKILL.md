---
name: engineering-project-governance
description: Enforce an engineering-first workflow for software project work. Use when requests involve building, modifying, scaffolding, refactoring, or extending any code project. Always propose 2-3 technical方案 options first, compare tradeoffs, ask the user to choose and explicitly confirm before implementation, and organize folders/files by language or framework conventions instead of demo-style flat layouts.
---

# Engineering Project Governance

Follow this workflow for any project implementation request.

## Required Workflow

1. Confirm scope in one short sentence.
2. Propose 2-3 implementation options before writing code.
3. Include tradeoffs for each option: complexity, maintainability, delivery speed, and expansion potential.
4. Recommend one option clearly.
5. Ask the user to choose and confirm.
6. Start implementation only after explicit confirmation.

Do not skip the proposal-and-confirmation step unless the user explicitly says to bypass it.

## Proposal Format

Use this compact structure:

- `Option A`: stack + architecture summary
- `Option B`: stack + architecture summary
- `Option C` (optional): stack + architecture summary
- `Recommendation`: one option with concise rationale
- `Need your confirmation`: one clear confirmation question

## Project Structure Rule

Use language/framework-standard structure by default. Do not deliver single-file or flat demo layouts unless the user explicitly asks for demo mode.

Read `references/structure-standards.md` and pick only the relevant section for the chosen stack.

If the user already has a repository, preserve existing conventions unless they conflict with core maintainability.

## Change Governance

Before major restructuring, state:

- What will change
- Why it improves engineering quality
- Migration risk and rollback approach

When requirements are ambiguous, ask up to 3 focused questions, then continue.

## Delivery Checklist

Before final response, verify:

- Technical option was proposed and user confirmation was received
- Directory hierarchy follows selected language/framework standard
- Core quality gates were run or explicitly reported as not run
- Extension points are identified (where to add new modules/features)
