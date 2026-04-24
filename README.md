# claude-ios-arch

An **agent plugin for iOS app development**.

This project helps an agent **start from any real project state** and design, bootstrap, adopt, review, implement, and evolve **iOS apps** with strong architecture, pragmatic technical choices, low technical debt, and official-source-aligned decisions.

## Architecture: Core + Adapters
This repository now follows a **core + adapters** model.

- `core/` contains the host-agnostic iOS app development capability.
- `adapters/` contains host-specific packaging for Claude-style and Codex-style coding agents.

This keeps the actual iOS engineering knowledge portable while allowing different agent hosts to consume it in their own preferred shape.

## Phase 1 Goal
Phase 1 focuses on **iOS-first app development** from idea to App Store shipment, with explicit emphasis on working from **any project state**:
- discovery and MVP framing
- new app architecture design
- technical selection
- directory structure and dependency boundaries
- low-debt bootstrap guidance
- existing-project adoption
- feature bootstrap and delivery guidance
- testing strategy and tooling choices
- architecture review and debt/risk checks
- architecture evolution planning
- third-party library selection with official-baseline-first bias
- release / App Store publishing workflows
- reusable delivery formats for agent output
- knowledge refresh workflows tied to official documentation

## Future Direction
The long-term goal is to expand into a broader **app development agent plugin** that supports more platforms, especially Android. For now, this repository intentionally focuses on **iOS only** so Phase 1 can become genuinely strong before platform expansion.

## What This Plugin Is
This repository is an **agent-usable plugin package** made of:
- `core/` — host-agnostic capability manifest
- `adapters/claude-code/` — Claude-style adapter
- `adapters/codex/` — Codex-style adapter
- `plugin/manifest.json` — repo-level plugin identity
- `rules/` — reusable architecture and debt guardrails
- `commands/` — repeatable workflows for common iOS engineering tasks
- `skills/` — focused agent skills for bootstrap, review, decision-making, evolution, and library selection
- `references/` — distilled official-source knowledge and third-party library evaluations used as the factual basis for recommendations
- `workflows/` — refresh and audit processes that keep references and skills aligned with official documentation
- `manifests/` — machine-readable capability, decision-topic, and project-state metadata
- `hooks/` — lightweight automated checks for common architecture smells
- `templates/` — reusable output templates and starter skeletons
- `examples/` — example prompts and state-aware example outputs for agent usage
- `platforms/ios/` — platform-specific guidance and conventions

## What This Plugin Is Not
This project is **not**:
- an MCP server
- a generic agent infrastructure framework
- a complete Xcode project generator
- a replacement for engineering judgment

It is a **specialized agent plugin** that improves how an agent helps users develop iOS apps.

## Core Jobs This Plugin Should Help With
1. Help frame an iOS app idea into a shippable MVP.
2. Detect the current project state before giving major recommendations.
3. Design a new iOS app architecture.
4. Adopt an existing iOS project without defaulting to rewrites.
5. Recommend a context-aware tech stack with trade-offs.
6. Propose a scalable but low-complexity directory structure.
7. Review an existing structure or architecture.
8. Identify technical debt and missing guardrails.
9. Evolve architecture incrementally when current patterns no longer fit.
10. Evaluate third-party libraries against the official baseline.
11. Help prepare release / App Store publishing workflows.

## Workflow Model
This plugin follows a three-part workflow:
- **需求 / Discovery** — manual trigger
- **开发 / Development** — highest automation, main leverage area
- **发布运营 / Release & Operations** — manual trigger

The design goal is to support both:
- professional developers who want best-practice engineering help
- solo founders / one-person companies who still need help shipping an iOS app

## Default iOS Baseline
Unless user constraints override it, the plugin should bias toward:
- SwiftUI-first UI architecture
- Swift Concurrency (`async/await`) for concurrency
- feature-first structure
- lightweight clean layering
- initializer injection
- `URLSession`-based networking
- explicit DTO/domain/UI model boundaries
- day-1 observability (logging, analytics, crash reporting, flags)
- official-platform capabilities first, third-party libraries only when justified by project constraints

## Repository Layout
```text
claude-ios-arch/
├─ core/
│  ├─ manifest.json
│  └─ README.md
├─ adapters/
│  ├─ claude-code/
│  │  ├─ CLAUDE.md
│  │  └─ manifest.json
│  └─ codex/
│     ├─ AGENTS.md
│     └─ manifest.json
├─ plugin/
│  └─ manifest.json
├─ manifests/
├─ references/
├─ workflows/
├─ rules/
├─ commands/
├─ skills/
├─ hooks/
├─ templates/
├─ examples/
└─ platforms/
   └─ ios/
```

## Suggested Agent Flow
When an agent uses this plugin, it should generally:
1. Choose the correct host adapter.
2. Load `core/manifest.json`.
3. Detect the current project state and constraints.
4. Identify whether the request belongs to **discovery**, **development**, or **release-operations**.
5. Load the matching command and skill.
6. Use `references/` and platform scorecards for factual and decision support.
7. Apply rule files for consistency.
8. Use templates and golden examples for stable output shape.
9. Optionally run hooks when reviewing codebases.
10. Use workflows to keep knowledge fresh over time.

## Main Entry Points
- `core/manifest.json`
- `adapters/claude-code/CLAUDE.md`
- `adapters/codex/AGENTS.md`
- `plugin/manifest.json`
- `docs/PRODUCT-REQUIREMENTS.md`
- `docs/WORKFLOW-MODEL.md`
- `platforms/ios/state-detection.md`
- `platforms/ios/architecture-evolution.md`
- `references/registry.json`
- `skills/ios-discovery/SKILL.md`
- `skills/ios-app-bootstrap/SKILL.md`
- `skills/ios-feature-bootstrap/SKILL.md`
- `skills/ios-testing-strategy/SKILL.md`
- `skills/ios-tooling-decision/SKILL.md`
- `skills/ios-arch-review/SKILL.md`
- `skills/ios-debt-check/SKILL.md`
- `skills/ios-architecture-evolution/SKILL.md`
- `skills/ios-library-selection/SKILL.md`
- `skills/ios-release-operations/SKILL.md`
- `examples/golden-existing-project-adoption.md`
- `examples/golden-debt-report.md`
- `examples/golden-release-operations.md`
- `examples/golden-library-selection.md`
- `examples/golden-architecture-evolution.md`

## Docs
- `docs/PRODUCT-REQUIREMENTS.md`
- `docs/PRODUCTION-READINESS.md`
- `docs/INSTALL.md`
- `docs/USAGE.md`
- `docs/WORKFLOW-MODEL.md`
- `docs/RESEARCH-WORKFLOW.md`

## Status
This is an **agent-first core + adapters plugin beta** for iOS app development that is evolving toward a state-aware, delivery-oriented, official-source-aligned decision system.
