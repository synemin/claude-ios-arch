---
name: ios-debt-check
description: Identify technical debt, accidental complexity, and missing engineering guardrails in iOS apps. Use when inspecting an iOS codebase or architecture for debt hotspots such as view-layer side effects, DTO leakage, global singleton sprawl, uncontrolled shared folders, premature modularization, or missing observability.
---

# iOS Debt Check

Use this skill to produce a debt-oriented review of a greenfield or existing iOS app.

## Core Operating Rule
Debt evaluation must be **state-aware**. Not all mess is harmful, and not all cleanup is worth doing now.

## Focus Areas
- structural debt
- tactical debt
- hidden complexity
- missing observability
- poor ownership boundaries
- over-abstraction or under-structure
- architecture drift
- migration safety risk

## Default Workflow
1. Detect current project state.
2. Distinguish harmful structural debt from acceptable tactical shortcuts.
3. Identify debt that blocks delivery, testing, or future evolution.
4. Prefer containment and repayment sequencing over broad cleanup wishes.
5. Call out what is acceptable to leave alone for now.

## Output Shape
1. Detected project state and why
2. Structural debt
3. Tactical debt
4. Missing guardrails
5. Recommended repayment order
6. What is acceptable to leave alone for now

## Tooling
When a codebase is available, consider running `../../hooks/ios_arch_guard.py` for a heuristic pass before giving the final judgment.

## References
Read when needed:
- `../../platforms/ios/state-detection.md`
- `../../platforms/ios/architecture-evolution.md`
- `../../platforms/ios/review-checklist.md`
- `../../references/apple/performance-baseline.md`
- `../../references/apple/observability-baseline.md`
- `../ios-app-bootstrap/references/debt-guardrails.md`
