# /ios-tooling-decision

## Intent
Use when the user wants a recommendation on iOS development tooling, project tooling, or engineering workflow tools.

## Typical Questions
- Should we add SwiftLint?
- Do we need SwiftGen?
- Tuist or XcodeGen or neither?
- XCTest or Swift Testing or both?

## Agent Workflow
1. Detect current project state.
2. Identify product stage, team size, repo complexity, and current pain.
3. Prefer the lightest tool that solves the current problem.
4. Check official / lowest-complexity baseline first.
5. Explain default recommendation, deviation conditions, and migration cost.
6. Distinguish hygiene tools, project generation tools, architecture tools, and testing tools.

## Output Format
- context assumptions
- detected project state and current pain
- official / lowest-complexity baseline
- options considered
- default recommendation
- why it fits now
- when not to adopt it
- migration / rollback cost
- confidence level
