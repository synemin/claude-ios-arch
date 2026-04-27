# /ios-tech-decision

## Intent
Use when the user wants a recommendation between iOS technologies, frameworks, or architectural approaches.

## Typical Questions
- SwiftUI or UIKit?
- async/await or older async styles?
- SwiftData or Core Data?
- local state or richer coordination?
- initializer injection or heavier DI?
- single target or modularized?

## Agent Workflow
1. Detect current project state.
2. Identify the actual decision topic.
3. Extract constraints and lock-in factors.
4. Check the official baseline first.
5. Apply the relevant scorecard.
6. Give a direct recommendation first.
7. Explain trade-offs, failure modes, migration cost, and team fit.
8. Separate current recommendation from future upgrade triggers.

## Output Format
- Context assumptions
- Detected project state and constraints
- Official baseline
- Options considered
- Recommendation
- Trade-offs
- When to deviate
- Migration/rollback cost
- Confidence level
