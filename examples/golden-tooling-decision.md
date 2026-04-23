# Golden Example: Tooling Decision

## Context
A new iOS app with one staff engineer and one mid-level iOS engineer. Single target, fast MVP timeline, likely to grow but not yet multi-module.

## Default Recommendation
- add SwiftLint now
- delay SwiftGen unless resource surface grows quickly
- avoid XcodeGen for now
- avoid Tuist for now
- avoid TCA by default
- keep XCTest as baseline; adopt Swift Testing incrementally if ergonomics matter

## Why It Fits Now
This setup keeps hygiene high while avoiding tools whose operational and cognitive cost would exceed the current repo complexity.

## When Not To Adopt It
If the repo quickly grows into many targets, config drift becomes painful, or state complexity becomes unusually high, revisit XcodeGen, Tuist, or TCA.

## Migration / Rollback Cost
- SwiftLint: low
- SwiftGen: low to medium
- XcodeGen: medium
- Tuist: medium to high
- TCA: medium to high

## Confidence
High for SwiftLint and avoiding Tuist/TCA early. Medium for SwiftGen depending on resource growth.
