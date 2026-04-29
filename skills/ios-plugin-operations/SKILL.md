---
name: ios-plugin-operations
description: Operate the claude-ios-arch plugin as a Claude Code or Codex installable capability bundle, including host installation, capability routing, Context7/official documentation lookup, LSP/SourceKit diagnostics, architecture review, quality gates, and plugin maintenance. Use when discussing plugin installation, Claude Code/Codex packaging, MCP/Context7 docs lookup, LSP integration, review workflows, or how an agent should execute this iOS plugin beyond static architecture advice.
---

# iOS Plugin Operations

Use this skill when the task is about **running, installing, auditing, or extending the plugin itself**, not just designing one app feature.

## Core Principle
Treat `claude-ios-arch` as a **capability bundle for coding agents**:

- host adapters tell Claude Code / Codex how to load the plugin
- skills encode task behavior
- commands encode repeatable workflows
- references hold curated official-source knowledge
- scripts/hooks provide deterministic checks
- optional external capabilities, such as Context7 or LSP, are detected and used when available

Do not reduce the project to model guidance or static architecture tips.

## Host Installation Model
Read `references/install-and-hosts.md` when installing or fixing packaging.

Default expectations:
- Claude Code uses `~/.claude/skills/<skill-name>/` style skill installs plus project `CLAUDE.md` guidance.
- Codex uses `~/.codex/skills/<skill-name>/` style skill installs plus project `AGENTS.md` guidance.
- Repo-local/team installs should include adapter instructions and avoid hidden manual steps.
- Do not silently install external tools, MCP servers, or global CLIs without user approval.

## Capability Routing
Read `references/capability-routing.md` before changing routing, manifests, adapters, or workflow docs.

When a user asks for iOS work, route through this order:
1. detect host and project state
2. choose the right command/skill
3. retrieve docs/reference evidence if the decision depends on current API behavior
4. inspect code with file search and LSP/SourceKit diagnostics when available
5. implement or plan the smallest safe change
6. run quality gates and architecture review
7. record ADR/debt when a material choice is made

## Documentation Lookup Policy
Use official, fresh sources in this order:
1. local curated references in `references/` when already sufficient
2. Context7/MCP documentation lookup when available and the question is API/version-sensitive
3. official Apple / Swift / library docs via scriptable fetch
4. alternate official source for the same technology

Never fall back to random blogs just because Context7 or web fetch is unavailable.

## LSP / Source Intelligence Policy
Use LSP/SourceKit when available for:
- compile errors and diagnostics
- symbol navigation and rename safety
- API availability and type mismatch checks
- impact analysis before refactors

If LSP is unavailable, fall back to `xcodebuild`, `swift build`, `swift test`, grep/search, and targeted source inspection. State the lower confidence only when it affects the recommendation.

## Review Pipeline
For architecture/review tasks, do not only give prose. Prefer evidence:
- inspect project state and dependency markers
- run `hooks/ios_arch_guard.py` when relevant
- run build/test/lint/format gates when available
- classify findings by severity and repayment trigger
- propose minimal repairs before rewrites

## Maintenance Pipeline
When plugin behavior changes:
- update the matching skill/command/reference/template together
- update `plugin/manifest.json`, `core/manifest.json`, and `manifests/capabilities.json` if capability surface changes
- update host adapters if Claude Code or Codex loading behavior changes
- run readiness scripts before claiming completion
