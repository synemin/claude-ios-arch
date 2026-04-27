---
name: ios-tech-decision
description: Make iOS technology and architecture choices with clear trade-offs. Use when comparing SwiftUI vs UIKit, async-await vs older async styles, persistence options, modularization timing, dependency injection strategy, navigation patterns, testing choices, or other iOS engineering decisions where project context and migration cost matter.
---

# iOS Tech Decision

Use this skill when the user needs a recommendation, not just background information.

## Core Operating Rule
There is no context-free best choice. Recommendations must be **state-aware, constraint-aware, and official-source-aligned**.

## Decision Method
1. Detect the current project state.
2. Identify the real decision topic.
3. Extract constraints.
4. Check the official baseline first.
5. Apply the relevant scorecard.
6. Recommend the simplest option that preserves future flexibility.
7. Explain what would make that recommendation change later.

## Required Decision Inputs
- current project state
- current stack and lock-in
- team skill / maintenance ability
- release urgency
- migration / rollback cost
- scale and product complexity
- offline / realtime / performance constraints
- testing safety level

## Default Behavior
- recommend the simplest option that preserves future flexibility
- prefer official platform capabilities first
- explain why the default wins here
- explain when the default becomes wrong
- include migration and rollback costs
- avoid recommending third-party libraries just to look sophisticated

## Required Output
1. Problem framing
2. Detected project state and constraints
3. Official baseline
4. Options considered
5. Recommended pick
6. Trade-offs
7. When to deviate
8. Migration / rollback cost
9. Confidence level

## Decision Topics
Typical topics include:
- SwiftUI vs UIKit / mixed UI strategy
- state ownership and state-management style
- navigation shape
- URLSession baseline vs library adoption
- persistence choice
- dependency injection approach
- testing approach
- modularization timing

## References
Read when needed:
- `../../platforms/ios/state-detection.md`
- `../../references/policies/source-of-truth-policy.md`
- `../../references/policies/third-party-adoption-policy.md`
- `../../references/apple/swiftui-baseline.md`
- `../../references/apple/concurrency-guidelines.md`
- `../../references/apple/navigation-patterns.md`
- `../../references/apple/urlsession-networking.md`
- `../../references/apple/swiftdata-vs-coredata.md`
- `../../references/apple/xctest-vs-swift-testing.md`
- `../../platforms/ios/scorecards/state-management.md`
- `../../platforms/ios/scorecards/navigation.md`
- `../../platforms/ios/scorecards/networking.md`
- `../../platforms/ios/scorecards/persistence.md`
- `../../platforms/ios/scorecards/di.md`
- `../../platforms/ios/scorecards/testing.md`
