---
name: ios-testing-strategy
description: Design pragmatic testing strategies for iOS apps and features. Use when deciding what to test in a new or evolving iOS app, how to divide unit vs integration vs UI testing, how much testing an MVP needs, or how to improve confidence without slowing delivery.
---

# iOS Testing Strategy

Use this skill to recommend a testing approach that matches product risk, team size, and delivery speed.

## Default Principles
- Test business-critical logic before broad UI coverage.
- Prefer unit tests for domain/use-case logic.
- Prefer targeted integration tests for boundaries that can silently break.
- Keep UI tests narrow and high-value.
- Do not recommend exhaustive testing for early-stage apps unless justified.

## Required Output
1. Context assumptions
2. Testing priorities
3. Unit-test recommendations
4. Integration-test recommendations
5. UI-test recommendations
6. What to postpone
7. Why this level of testing is enough for now

## References
Read when needed:
- `../../platforms/ios/testing-pyramid.md`
- `../../platforms/ios/testing-scenarios.md`
- `../../templates/testing-plan.md`
