# iOS Technology Selection Rules

Use this file when asked to choose tools, frameworks, or architectural approaches for a new or evolving iOS app.

## Default Recommendations
- SwiftUI over UIKit for greenfield UI work.
- Swift Concurrency over callbacks and overusing Combine.
- URLSession over heavy network wrappers.
- Initializer injection over DI containers.
- Feature-first structure over layer-only top-level organization.
- Lightweight clean layering over framework-heavy architecture.

## When To Deviate
### Use UIKit more heavily when:
- text input is unusually complex
- layout requirements exceed SwiftUI comfort zones
- legacy reuse is important
- proven performance hotspots demand it

### Consider TCA or heavier state frameworks only when:
- state machines are genuinely complex
- strict effect modeling is valuable
- the team already has strong TCA fluency
- the product complexity justifies the ceremony

### Consider GRDB/Core Data/SwiftData based on need:
- `UserDefaults`/files for simple state and cache
- GRDB when you want predictable SQL-backed control
- SwiftData when Apple-native ergonomics outweigh its maturity concerns
- Core Data mainly when existing investment or advanced features justify it

### Consider modularization only when:
- compile times materially hurt flow
- ownership boundaries are stable
- multiple teams/features conflict in a single target
- code reuse has become durable, not hypothetical

## Decision Output Format
When making a tech choice, answer in this shape:
1. Default pick
2. Why it wins by default
3. When not to use it
4. Migration/rollback cost
5. Recommendation confidence
