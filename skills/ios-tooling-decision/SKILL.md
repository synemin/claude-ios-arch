---
name: ios-tooling-decision
description: Make pragmatic decisions about iOS engineering tools and project tooling. Use when comparing SwiftLint, SwiftGen, XcodeGen, Tuist, XCTest vs Swift Testing, or other iOS development tools where team size, product stage, repo complexity, and maintenance cost matter.
---

# iOS Tooling Decision

Use this skill to recommend the right amount of tooling for an iOS project.

## Core Operating Rule
Tooling must solve a **real current pain** in the current project state. Do not add tooling just because mature teams use it.

## Required Decision Inputs
- current project state
- team size and discipline level
- repo complexity
- current friction and repetition
- CI maturity
- maintenance appetite
- migration / rollback cost

## Default Principles
- prefer the smallest useful tool
- do not add tooling just because mature teams use it
- match tooling complexity to repo complexity and team scale
- explain when the tool becomes worth it
- explain when the tool is premature
- prefer official / low-lock-in tooling where possible

## Required Output
1. Context assumptions
2. Detected project state and current pain
3. Official / lowest-complexity baseline
4. Options considered
5. Default recommendation
6. Why it fits now
7. When not to adopt it
8. Migration / rollback cost
9. Confidence level

## References
Read when needed:
- `../../platforms/ios/state-detection.md`
- `../../references/apple/xctest-vs-swift-testing.md`
- `../../references/apple/modularization-timing.md`
- `../../references/libraries/tuist-evaluation.md`
- `../../templates/tooling-decision-memo.md`
