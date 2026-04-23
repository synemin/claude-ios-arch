---
name: ios-debt-check
description: Identify technical debt, accidental complexity, and missing engineering guardrails in iOS apps. Use when inspecting an iOS codebase or architecture for debt hotspots such as view-layer side effects, DTO leakage, global singleton sprawl, uncontrolled shared folders, premature modularization, or missing observability.
---

# iOS Debt Check

Use this skill to produce a debt-oriented review of a greenfield or existing iOS app.

## Focus Areas
- structural debt
- tactical debt
- hidden complexity
- missing observability
- poor ownership boundaries
- over-abstraction or under-structure

## Output Shape
1. Structural debt
2. Tactical debt
3. Missing guardrails
4. Recommended repayment order
5. What is acceptable to leave alone for now

## Tooling
When a codebase is available, consider running `hooks/ios_arch_guard.py` for a heuristic pass before giving the final judgment.

## References
Read when needed:
- `../ios-app-bootstrap/references/debt-guardrails.md`
- `../../platforms/ios/review-checklist.md`
