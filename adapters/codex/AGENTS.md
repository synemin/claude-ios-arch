# AGENTS.md

Use this adapter when the host is Codex or a Codex-style coding agent.

## Role
Apply the host-agnostic iOS app development core in a Codex-friendly repo-instruction form.

## Working Bias
- Prefer simple, legible architectures.
- Avoid premature abstraction.
- Keep side effects out of Views.
- Keep DTOs out of Presentation.
- Prefer low-debt startup with explicit repayment triggers.

## Load Order
1. `../../core/manifest.json`
2. `../../rules/ios-architecture.md`
3. `../../rules/ios-low-debt.md`
4. `../../rules/ios-tech-selection.md`
5. Relevant command in `../../commands/`
6. Relevant skill in `../../skills/`
7. Relevant template in `../../templates/`

## Supported Tasks
- discovery — understand goals, constraints, and context
- project-state-detection — detect current architecture state
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

## Default Recommendation Bias
- SwiftUI first
- async/await first
- feature-first structure
- lightweight clean layering
- initializer injection
- day-1 observability
