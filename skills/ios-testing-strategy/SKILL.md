---
name: ios-testing-strategy
description: Design pragmatic testing strategies for iOS apps and features. Use when deciding what to test in a new or evolving iOS app, how to divide unit vs integration vs UI testing, how much testing an MVP needs, or how to improve confidence without slowing delivery.
---

# iOS Testing Strategy

Use this skill to recommend a testing approach that matches product risk, project state, and delivery speed.

## Core Operating Rule
Testing strategy must match **project state, failure cost, and team sustainability**.

## Required Decision Inputs
- current project state
- release pressure
- critical business flows
- refactor frequency
- testability of the current architecture
- current flakiness / CI health
- team capacity to maintain tests

## Default Principles
- test business-critical logic before broad UI coverage
- prefer unit tests for domain/use-case logic
- prefer targeted integration tests for boundaries that can silently break
- keep UI tests narrow and high-value
- do not recommend exhaustive testing for early-stage apps unless justified
- choose the simplest official testing stack the team can sustain

## Required Output
1. Context assumptions
2. Detected project state and risk profile
3. Testing priorities
4. Unit-test recommendations
5. Integration-test recommendations
6. UI-test recommendations
7. What to postpone
8. Why this level of testing is enough for now

## References
Read when needed:
- `../../platforms/ios/state-detection.md`
- `../../platforms/ios/scorecards/testing.md`
- `../../references/apple/xctest-vs-swift-testing.md`
- `../../references/apple/performance-baseline.md`
- `../../templates/testing-plan.md`
