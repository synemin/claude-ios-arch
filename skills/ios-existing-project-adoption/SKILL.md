---
name: ios-existing-project-adoption
description: Adopt this plugin into an existing iOS project without assuming a rewrite. Use when assessing a current codebase, identifying strengths to preserve, prioritizing structural fixes, containing debt, or planning incremental architecture and tooling improvements in a project already in motion.
---

# iOS Existing Project Adoption

Use this skill when the project already exists and the goal is to improve it pragmatically instead of treating it like greenfield.

## Core Operating Rule
Detect the **current project state first**, then adapt recommendations to that state.

Possible states include:
- greenfield
- bootstrap-in-progress
- feature-on-existing
- legacy-rescue
- architecture-drift
- pre-release-hardening
- migration-window

## Required Decision Inputs
Before making major recommendations, identify:
- current project state
- release pressure / delivery urgency
- existing architecture shape
- existing library and tooling lock-in
- deployment target / platform constraints
- team skill and change tolerance
- testing / rollback safety
- biggest recurring pain points

## Default Principles
- do not assume greenfield
- preserve working delivery flows when possible
- distinguish structural risk from acceptable mess
- prefer incremental migration over broad rewrites
- contain debt before trying to perfect architecture
- respect migration cost and team comprehension cost

## Default Workflow
1. Detect the current project state.
2. Summarize what is already working and should be preserved.
3. Identify structural risks vs acceptable local mess.
4. Identify the smallest high-leverage adoption or cleanup moves.
5. Recommend a migration sequence that preserves delivery momentum.
6. Call out what should explicitly **not** be changed yet.

## Required Output
1. Current-state summary
2. Detected project state and why
3. Strengths to preserve
4. Structural risks
5. Debt containment opportunities
6. Recommended next migration steps
7. What to postpone
8. Environment / toolchain notes when relevant

## References
Read when needed:
- `../../platforms/ios/state-detection.md`
- `../../platforms/ios/architecture-evolution.md`
- `../../platforms/ios/review-checklist.md`
- `../../references/policies/third-party-adoption-policy.md`
- `../ios-app-bootstrap/references/debt-guardrails.md`
