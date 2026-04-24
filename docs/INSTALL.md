# Install / Integration Guide

This repository is an **agent plugin for state-aware iOS app development** built with a **core + adapters** structure.

## Repository Model
- `core/` = host-agnostic iOS app development capability
- `adapters/claude-code/` = Claude-style coding-agent adapter
- `adapters/codex/` = Codex-style coding-agent adapter
- `references/` = distilled official-source knowledge
- `platforms/ios/` = state detection, evolution guidance, and scorecards
- `workflows/` = refresh and audit processes

## Recommended Loading Model
When integrating this plugin into a host, prefer this loading order:
1. host adapter contract
2. `../core/manifest.json`
3. `../docs/PRODUCT-REQUIREMENTS.md`
4. `../platforms/ios/state-detection.md`
5. relevant references, scorecards, commands, and skills

The point is to make the host load **state awareness and source-of-truth knowledge early**, not only task prompts.

## For Claude-style Coding Agents
Use:
- `../adapters/claude-code/CLAUDE.md`
- `../core/manifest.json`

Recommended loading order:
1. `../adapters/claude-code/CLAUDE.md`
2. `../core/manifest.json`
3. `../docs/PRODUCT-REQUIREMENTS.md`
4. `../platforms/ios/state-detection.md`
5. relevant files from `../references/`
6. relevant files from `../platforms/ios/scorecards/`
7. relevant files from `../rules/`
8. relevant files from `../commands/`
9. relevant files from `../skills/`
10. optional templates/examples/workflows

## For Codex-style Coding Agents
Use:
- `../adapters/codex/AGENTS.md`
- `../core/manifest.json`

Recommended loading order:
1. `../adapters/codex/AGENTS.md`
2. `../core/manifest.json`
3. `../docs/PRODUCT-REQUIREMENTS.md`
4. `../platforms/ios/state-detection.md`
5. relevant files from `../references/`
6. relevant files from `../platforms/ios/scorecards/`
7. relevant files from `../rules/`
8. relevant files from `../commands/`
9. relevant files from `../skills/`
10. optional templates/examples/workflows

## Main Phase-1 iOS Capabilities
- discovery and MVP framing
- project-state detection
- greenfield bootstrap
- existing-project adoption
- feature bootstrap and delivery guidance
- architecture review
- debt detection
- architecture evolution planning
- official-baseline-first technical selection
- third-party library selection
- testing strategy guidance
- release / App Store workflows
- knowledge refresh workflows

## Notes
This repository is not an MCP server. It is a host-adaptable agent plugin package for iOS development workflows.

For reference maintenance and research operations, use the workflow stack documented in:
- `../docs/RESEARCH-WORKFLOW.md`
- `../workflows/docs-refresh.md`
- `../workflows/reference-review.md`

Recommended operational posture:
- official-source first
- favor repeatable refresh methods
- prefer another official source over non-official material when one path fails
