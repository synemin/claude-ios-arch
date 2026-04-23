---
name: ios-arch-review
description: Review existing iOS app architectures, directory structures, layering, state flow, and dependency boundaries. Use when evaluating a current SwiftUI/UIKit codebase, reviewing a proposed iOS structure, assessing maintainability risks, or recommending incremental architecture improvements without over-engineering.
---

# iOS Architecture Review

Use this skill when the user already has an iOS structure, architecture, or codebase and wants staff-level review.

## Review Goals
- Identify structural risks.
- Identify maintainability drag.
- Separate severe issues from stylistic preferences.
- Prefer incremental fixes over rewrites.

## Review Dimensions
- feature boundaries
- dependency direction
- side-effect isolation
- state flow clarity
- DTO/domain/UI separation
- shared/common folder hygiene
- observability coverage
- team cognitive load

## Output Shape
1. Current architecture summary
2. Top risks
3. What to keep
4. What to change now
5. What to postpone
6. Suggested migration sequence

## References
Read when needed:
- `../ios-app-bootstrap/references/tech-stack.md`
- `../ios-app-bootstrap/references/debt-guardrails.md`
- `../../platforms/ios/review-checklist.md`
