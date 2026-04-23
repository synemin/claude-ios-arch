# claude-ios-arch

An **agent plugin for iOS app development**.

This project helps an agent design, bootstrap, review, and evolve **iOS apps** with strong architecture, pragmatic technical choices, and low technical debt.

## Architecture: Core + Adapters
This repository now follows a **core + adapters** model.

- `core/` contains the host-agnostic iOS app development capability.
- `adapters/` contains host-specific packaging for Claude-style and Codex-style coding agents.

This keeps the actual iOS engineering knowledge portable while allowing different agent hosts to consume it in their own preferred shape.

## Phase 1 Goal
Phase 1 focuses on **iOS-first app development**:
- new app architecture design
- technical selection
- directory structure and dependency boundaries
- low-debt bootstrap guidance
- architecture review
- debt/risk checks
- reusable delivery formats for architecture recommendations

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
1. Design a new iOS app architecture.
2. Recommend a default tech stack with trade-offs.
3. Propose a scalable but low-complexity directory structure.
4. Review an existing structure or architecture.
5. Identify technical debt and missing guardrails.
6. Generate reusable architecture briefs and checklists.

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
3. Identify whether the request is bootstrap / review / decision / debt-check.
4. Load the matching command and skill.
5. Apply rule files for consistency.
6. Use templates for stable output shape.
7. Optionally run hooks when reviewing codebases.

## Main Entry Points
- `core/manifest.json`
- `adapters/claude-code/CLAUDE.md`
- `adapters/codex/AGENTS.md`
- `plugin/manifest.json`
- `skills/ios-app-bootstrap/SKILL.md`
- `skills/ios-arch-review/SKILL.md`
- `skills/ios-tech-decision/SKILL.md`
- `skills/ios-debt-check/SKILL.md`

## Docs
- `docs/INSTALL.md`
- `docs/USAGE.md`

## Status
This is a **core + adapters plugin draft** for an iOS development agent plugin.
