---
name: ios-library-selection
description: Decide whether an iOS project should keep the official platform baseline or adopt / retain a third-party library. Use when evaluating networking, image loading, persistence, analytics, DI, navigation helpers, or other infrastructure choices under real project constraints.
---

# iOS Library Selection

## Default Bias
Prefer the official platform baseline unless a third-party library meaningfully reduces net complexity.

## Required Evaluation
- official baseline sufficiency
- current codebase lock-in
- migration cost
- maintenance health
- debugging cost
- team comprehension cost

## Output Shape
1. Current need
2. Official baseline verdict
3. Options evaluated
4. Recommendation
5. Trade-offs
6. Exit trigger

## References
Read when needed:
- `../../references/policies/source-of-truth-policy.md`
- `../../references/policies/third-party-adoption-policy.md`
- `../../platforms/ios/scorecards/networking.md`
- `../../platforms/ios/scorecards/persistence.md`
