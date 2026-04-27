---
name: ios-architecture-evolution
description: Evolve an existing iOS architecture when the current structure no longer matches project needs. Use when product scope, team size, technical debt, or operational complexity has outgrown the current app structure and the user needs an incremental architecture upgrade instead of a rewrite.
---

# iOS Architecture Evolution

Use this skill when a project needs a safe structural upgrade.

## Goals
- detect architecture mismatch
- recommend the smallest safe upgrade
- preserve delivery momentum
- make migration seams explicit

## Decision Inputs
- current project state
- recurring pain patterns
- coupling hotspots
- delivery pressure
- team ability to absorb change

## Output Shape
1. Current state summary
2. Why the current shape is failing
3. Recommended evolution target
4. Migration sequence
5. Guardrails to prevent drift

## References
Read when needed:
- `../../platforms/ios/state-detection.md`
- `../../platforms/ios/architecture-evolution.md`
- `../../references/policies/third-party-adoption-policy.md`
