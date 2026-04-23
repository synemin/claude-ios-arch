# iOS Tooling Decision Matrix

## SwiftLint
### Default
Adopt in most teams and most repos.
### Why
Low cost, high hygiene value.
### Avoid / Delay When
- tiny throwaway prototype
- no shared review surface yet
### Cost
Low adoption cost, low rollback cost.

## SwiftGen
### Default
Adopt when resource access becomes broad or error-prone.
### Why
Reduces string-based asset/localization mistakes.
### Avoid / Delay When
- very small app
- low resource complexity
### Cost
Low to medium adoption cost.

## XcodeGen
### Default
Consider when project configuration drift hurts, but do not force by default.
### Why
Improves reproducibility and config management.
### Avoid / Delay When
- simple single-target app
- project changes rarely
### Cost
Medium adoption cost.

## Tuist
### Default
Do not adopt by default for early-stage apps.
### Why
Powerful, but more justified when repo scale, modularization, or platform-team concerns become real.
### Avoid / Delay When
- single small team
- repo complexity is still low
### Cost
Medium to high adoption and process cost.

## TCA
### Default
Do not adopt by default.
### Why
Strong consistency and effect modeling, but significant ceremony.
### Avoid / Delay When
- simple to medium app complexity
- team wants fast onboarding and low ceremony
### Cost
Medium to high cognitive cost.

## XCTest vs Swift Testing
### Default
Use what best matches current compatibility needs; prefer pragmatic coexistence over dogma.
### Why
XCTest remains standard and compatible; Swift Testing improves ergonomics in newer setups.
### Avoid / Delay When
- test infra is already stable and migration adds churn with little value
### Cost
Low to medium depending on migration scope.
