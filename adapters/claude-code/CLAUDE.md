# CLAUDE.md

Use this adapter when the host is Claude Code or another Claude-style coding agent that consumes repository instructions.

## Adapter Role
Translate the host-agnostic iOS app development core into Claude-friendly operating behavior.

## Default Behavior
When the user asks about building, reviewing, or evolving an iOS app:
- Load the iOS app development core.
- Prefer pragmatic, low-debt architecture recommendations.
- Recommend the simplest architecture that preserves future flexibility.
- Explain trade-offs and delivery implications.
- Bias toward maintainability, observability, and team comprehension.

## Load Order
Apply these assets in order when relevant:
1. `../../core/manifest.json`
2. `../../rules/ios-architecture.md`
3. `../../rules/ios-low-debt.md`
4. `../../rules/ios-tech-selection.md`
5. Matching command under `../../commands/`
6. Matching skill under `../../skills/`
7. Matching template under `../../templates/`

## Supported Task Shapes
- discovery — understand the user's goals, constraints, and context
- project-state-detection — detect the current project's architecture state
- constraint-extraction — extract tech/team/business constraints
- architecture-design — design or recommend iOS app architecture
- tech-selection — evaluate and choose iOS technology stack
- directory-structure — propose feature-first directory layout
- bootstrap — scaffold a new iOS app from scratch
- existing-project-adoption — adopt the plugin's architecture in an existing codebase
- feature-bootstrap — design a new feature with clean boundaries
- feature-implementation — implement a feature in existing code with minimal-impact changes
- architecture-review — review and score an existing architecture
- debt-check — identify and prioritize technical debt
- architecture-evolution — plan incremental architecture evolution
- library-selection — evaluate and select third-party libraries
- release-operations — pre-release audit and checklist

## Default iOS Bias
- SwiftUI first
- async/await first
- feature-first organization
- clean-ish layering
- initializer injection
- URLSession typed networking
- DTO/domain/UI separation
- day-1 observability

## Output Preference
Use concise, staff-level output with:
- direct recommendation first
- trade-offs second
- migration/evolution notes last
