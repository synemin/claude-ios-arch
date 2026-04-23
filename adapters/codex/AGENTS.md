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
- bootstrap a new iOS app
- review iOS architecture
- make iOS tech choices
- check iOS debt

## Default Recommendation Bias
- SwiftUI first
- async/await first
- feature-first structure
- lightweight clean layering
- initializer injection
- day-1 observability
