# /ios-tooling-decision

## Intent
Use when the user wants a recommendation on iOS development tooling, project tooling, or engineering workflow tools.

## Typical Questions
- Should we add SwiftLint?
- Do we need SwiftGen?
- Tuist or XcodeGen or neither?
- Should we adopt TCA?
- XCTest or Swift Testing or both?

## Agent Workflow
1. Identify product stage, team size, repo complexity, and current pain.
2. Prefer the lightest tool that solves the current problem.
3. Explain default recommendation, deviation conditions, and migration cost.
4. Distinguish hygiene tools, project generation tools, architecture tools, and testing tools.

## Output Format
- context assumptions
- default recommendation
- why it fits now
- when not to adopt it
- migration / rollback cost
- confidence level
