# Capability Routing Reference

## Capability Types

### 1. Static Plugin Knowledge
Use for stable policy and decision rules:

- `references/apple/`
- `references/libraries/`
- `references/policies/`
- `platforms/ios/scorecards/`

### 2. Live Documentation Lookup
Use Context7/MCP or official fetch when:

- API behavior may have changed
- package versions matter
- an Apple/Swift/library recommendation depends on current docs
- generated code uses a less familiar API

Fallback order:

1. Context7/MCP docs lookup if configured
2. official docs via `scripts/fetch_official_source.py` or equivalent
3. existing curated reference if still fresh enough
4. alternate official source

### 3. Source Intelligence / LSP
Use LSP/SourceKit before risky implementation or refactor work:

- symbol resolution
- diagnostics
- rename/reference checks
- API availability
- type mismatch investigation

Fallback gates:

- `xcodebuild`
- `swift build`
- `swift test`
- targeted file inspection/search

### 4. Review and Quality Gates
Use these for review tasks and before completion claims:

- `hooks/ios_arch_guard.py`
- build/test commands detected from the repo
- SwiftLint/SwiftFormat/swift-format when configured
- dependency and architecture scorecards

### 5. Agentic Workflow Stages
For non-trivial work, use a pipeline instead of one-shot advice:

```text
inspect -> plan -> docs/reference lookup -> implement -> review -> verify -> ADR/debt/report
```

## Routing Examples

- “Install this plugin for Claude Code” -> `ios-plugin-operations`, install host reference, adapter update, smoke test.
- “Use latest SwiftData correctly” -> app skill + Context7/official docs lookup + reference policy.
- “Review this app architecture” -> `ios-arch-review` + LSP/build/test + arch guard + scorecards.
- “Implement login feature” -> `ios-feature-implementation` + project state detection + docs lookup for chosen APIs + tests.
- “Add Tuist” -> `ios-tooling-decision` + large-team/project-generation criteria + ADR.
