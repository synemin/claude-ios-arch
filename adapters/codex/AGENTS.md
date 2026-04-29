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
2. `../../skills/ios-plugin-operations/SKILL.md` for install, capability routing, Context7/MCP docs, LSP, review gates, or plugin maintenance
3. `../../rules/ios-architecture.md`
4. `../../rules/ios-low-debt.md`
5. `../../rules/ios-tech-selection.md`
6. Relevant command in `../../commands/`
7. Relevant skill in `../../skills/`
8. Relevant template in `../../templates/`

## Capability Use
- Use Context7/MCP documentation lookup when configured and the decision depends on current Apple/Swift/library API behavior.
- Use SourceKit/LSP diagnostics when available before broad refactors, symbol moves, or API-sensitive fixes.
- Use build/test/lint/format and `hooks/ios_arch_guard.py` as evidence before claiming implementation success.
- Ask before installing MCP servers, global tools, signing/provisioning assets, or publishing externally.

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
- plugin-installation — install/package the plugin for Claude Code or Codex
- documentation-lookup — use Context7/MCP or official fetch paths for current docs
- lsp-source-intelligence — use SourceKit/LSP diagnostics and symbol intelligence when available
- plugin-maintenance — update manifests, adapters, skills, commands, references, and readiness checks together

## Default Recommendation Bias
- SwiftUI first
- async/await first
- feature-first structure
- lightweight clean layering
- initializer injection
- day-1 observability
