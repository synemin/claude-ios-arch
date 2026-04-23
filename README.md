# claude-ios-arch

An **agent plugin for iOS app development**.

This project helps an agent design, bootstrap, review, and evolve **iOS apps** with strong architecture, pragmatic technical choices, and low technical debt.

## Architecture: Core + Adapters
This repository now follows a **core + adapters** model.

- `core/` contains the host-agnostic iOS app development capability.
- `adapters/` contains host-specific packaging for Claude-style and Codex-style coding agents.

This keeps the actual iOS engineering knowledge portable while allowing different agent hosts to consume it in their own preferred shape.

## Phase 1 Goal
Phase 1 focuses on **iOS-first app development** from idea to App Store shipment:
- discovery and MVP framing
- new app architecture design
- technical selection
- directory structure and dependency boundaries
- low-debt bootstrap guidance
- feature bootstrap
- testing strategy and tooling choices
- architecture review and debt/risk checks
- release / App Store publishing workflows
- reusable delivery formats for agent output

## Future Direction
The long-term goal is to expand into a broader **app development agent plugin** that supports more platforms. For now, this repository intentionally focuses on **iOS only** so the plugin stays sharp and useful.

## What This Plugin Is
This repository is an **agent-usable plugin package** made of:
- `core/` — host-agnostic capability manifest
- `adapters/claude-code/` — Claude-style adapter
- `adapters/codex/` — Codex-style adapter
- `plugin/manifest.json` — repo-level plugin identity
- `rules/` — reusable architecture and debt guardrails
- `commands/` — repeatable workflows for common iOS engineering tasks
- `skills/` — focused agent skills for bootstrap, review, decision-making, and debt checks
- `hooks/` — lightweight automated checks for common architecture smells
- `templates/` — reusable output templates and starter skeletons
- `examples/` — example prompts and example outputs for agent usage
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
2. Design a new iOS app architecture.
3. Recommend a default tech stack with trade-offs.
4. Propose a scalable but low-complexity directory structure.
5. Review an existing structure or architecture.
6. Identify technical debt and missing guardrails.
7. Help prepare release / App Store publishing workflows.

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
3. Identify whether the request belongs to **discovery**, **development**, or **release-operations**.
4. Load the matching command and skill.
5. Apply rule files for consistency.
6. Use templates and golden examples for stable output shape.
7. Optionally run hooks when reviewing codebases.

## Main Entry Points
- `core/manifest.json`
- `adapters/claude-code/CLAUDE.md`
- `adapters/codex/AGENTS.md`
- `plugin/manifest.json`
- `docs/WORKFLOW-MODEL.md`
- `skills/ios-discovery/SKILL.md`
- `skills/ios-app-bootstrap/SKILL.md`
- `skills/ios-feature-bootstrap/SKILL.md`
- `skills/ios-testing-strategy/SKILL.md`
- `skills/ios-tooling-decision/SKILL.md`
- `skills/ios-arch-review/SKILL.md`
- `skills/ios-debt-check/SKILL.md`
- `skills/ios-release-operations/SKILL.md`

## Docs
- `docs/INSTALL.md`
- `docs/USAGE.md`
- `docs/WORKFLOW-MODEL.md`

## Status
This is an **agent-first core + adapters plugin draft** for iOS app development.
