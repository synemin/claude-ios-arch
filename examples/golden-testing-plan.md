# Golden Example: Testing Plan

## Context
New iOS MVP with auth, onboarding, and a journaling flow. Small team, fast iteration required.

## Testing Priorities
- auth/session correctness
- onboarding completion logic
- first-entry save flow

## Unit Test Targets
- onboarding completion use case
- first-entry validation
- DTO/domain mapping
- session state transitions with mocked boundaries

## Integration Test Targets
- auth repository login/logout behavior
- persistence of onboarding completion
- save-entry repository path

## UI Test Targets
- app launch smoke test
- onboarding happy path
- login happy path

## What To Postpone
- broad snapshot coverage
- deep UI permutations for unstable onboarding copy
- exhaustive failure-mode UI automation

## Why This Is Enough For Now
This plan protects the highest-value business flows while keeping test cost aligned with MVP speed.
