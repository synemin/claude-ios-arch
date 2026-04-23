# Golden Example: Debt Report

## Structural Debt
- DTOs are referenced directly from multiple SwiftUI Views.
- Auth and onboarding share one oversized repository with mixed concerns.

## Tactical Debt
- A temporary SessionManager owns logging, analytics, and token refresh in one class.

## Missing Guardrails
- No explicit debt register
- No crash reporting
- No feature flags

## Recommended Repayment Order
1. stop DTO leakage by adding mapping at repository boundary
2. split auth vs onboarding repository responsibilities
3. contain SessionManager responsibilities
4. add observability baseline

## Acceptable To Leave Alone For Now
- local file naming inconsistencies
- small shared helper files with narrow scope
