# /ios-tech-decision

## Intent
Use when the user wants a recommendation between iOS technologies, frameworks, or architectural approaches.

## Typical Questions
- SwiftUI or UIKit?
- async/await or Combine?
- SwiftData or GRDB or Core Data?
- MVVM or TCA?
- single target or modularized?

## Agent Workflow
1. Identify the actual product/problem context.
2. Default to the simplest viable choice.
3. Explain trade-offs, failure modes, migration cost, and team fit.
4. Give a direct recommendation first.
5. Separate default advice from exceptions.

## Output Format
- Context assumptions
- Default recommendation
- Why it wins by default
- When to deviate
- Migration/rollback cost
- Confidence level
