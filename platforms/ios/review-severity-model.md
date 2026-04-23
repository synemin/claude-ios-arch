# iOS Review Severity Model

Use this model when reviewing iOS architecture, code structure, or engineering workflows.

## Severity Levels
### S1 — Structural Risk
Likely to create compounding architecture pain, coupling, or fragile evolution.
Examples:
- DTO leakage across layers
- feature boundaries collapsing
- global singletons driving core behavior
- views/controllers owning business logic and side effects

### S2 — Maintainability Drag
Not immediately fatal, but likely to slow development, onboarding, or refactors.
Examples:
- vague naming (`Manager`, `Helper`, `Common`)
- weak observability
- repeated ad hoc patterns
- inconsistent state handling

### S3 — Optional Refinement
Useful cleanup, but not urgent.
Examples:
- local naming cleanup
- minor file reorganization
- non-critical consistency improvements

## Output Rule
Always distinguish what must change now from what can wait.
