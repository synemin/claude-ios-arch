---
name: ios-arch-review
description: Review existing iOS app architectures, directory structures, layering, state flow, and dependency boundaries. Use when evaluating a current SwiftUI/UIKit codebase, reviewing a proposed iOS structure, assessing maintainability risks, or recommending incremental architecture improvements without over-engineering.
---

# iOS Architecture Review

Use this skill when the user already has an iOS structure, architecture, or codebase and wants a staff-level review.

## Core Operating Rule
Review the app against its **current project state and delivery reality**, not against an idealized greenfield architecture.

## Review Goals
- identify structural risks
- identify maintainability drag
- separate severe issues from stylistic preferences
- prefer incremental fixes over rewrites
- detect whether the app is suffering from architecture drift or broader legacy-rescue conditions

## Review Dimensions
- feature boundaries
- dependency direction
- side-effect isolation
- state flow clarity
- DTO/domain/UI separation
- shared/common folder hygiene
- observability coverage
- team cognitive load
- migration feasibility

## Default Workflow
1. Detect the current project state.
2. Summarize current architecture pattern and operating constraints.
3. Review using boundary, state, dependency, and observability criteria.
4. Classify issues into structural risk, maintainability drag, and optional/style.
5. Recommend the smallest high-leverage fixes first.
6. If needed, identify architecture evolution triggers instead of proposing a full rewrite.

## Output Shape
1. Current architecture summary
2. Detected project state and why
3. Top risks
4. What to keep
5. What to change now
6. What to postpone
7. Suggested migration sequence

## References
Read when needed:
- `../../platforms/ios/state-detection.md`
- `../../platforms/ios/architecture-evolution.md`
- `../../platforms/ios/review-checklist.md`
- `../../references/apple/observation-state-model.md`
- `../../references/policies/third-party-adoption-policy.md`
- `../ios-app-bootstrap/references/debt-guardrails.md`
