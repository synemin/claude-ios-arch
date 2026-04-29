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
5. `../skills/ios-plugin-operations/SKILL.md` when the task involves installation, capability routing, Context7/MCP docs, LSP, review gates, or plugin maintenance
6. relevant references, scorecards, commands, and skills

The point is to make the host load **state awareness, source-of-truth knowledge, and executable capability routing early**, not only task prompts.

## For Claude-style Coding Agents
Use:
- `../adapters/claude-code/CLAUDE.md`
- `../core/manifest.json`

Install native skills into Claude Code when using the plugin globally:

```bash
mkdir -p ~/.claude/skills
cp -R skills/ios-* ~/.claude/skills/
```

For repo/team use, add a small `CLAUDE.md` section that points Claude Code at this plugin rather than copying all docs into the app repository.

Recommended loading order:
1. `../adapters/claude-code/CLAUDE.md`
2. `../core/manifest.json`
3. `../docs/PRODUCT-REQUIREMENTS.md`
4. `../platforms/ios/state-detection.md`
5. `../skills/ios-plugin-operations/SKILL.md` for install/capability/tooling operations
6. relevant files from `../references/`
7. relevant files from `../platforms/ios/scorecards/`
8. relevant files from `../rules/`
9. relevant files from `../commands/`
10. relevant files from `../skills/`
11. optional templates/examples/workflows

## For Codex-style Coding Agents
Use:
- `../adapters/codex/AGENTS.md`
- `../core/manifest.json`

Install native skills into Codex when using the plugin globally:

```bash
mkdir -p ~/.codex/skills
cp -R skills/ios-* ~/.codex/skills/
```

For repo/team use, add a small `AGENTS.md` section that points Codex at this plugin and tells it to use commands/skills by task.

Recommended loading order:
1. `../adapters/codex/AGENTS.md`
2. `../core/manifest.json`
3. `../docs/PRODUCT-REQUIREMENTS.md`
4. `../platforms/ios/state-detection.md`
5. `../skills/ios-plugin-operations/SKILL.md` for install/capability/tooling operations
6. relevant files from `../references/`
7. relevant files from `../platforms/ios/scorecards/`
8. relevant files from `../rules/`
9. relevant files from `../commands/`
10. relevant files from `../skills/`
11. optional templates/examples/workflows

## Setup / Verify Script

For repeatable host installs, use the setup script instead of hand-copying skills:

```bash
# Preview without writing
python3 scripts/setup_plugin.py --host claude-code --dry-run
python3 scripts/setup_plugin.py --host codex --dry-run

# Install native skills
python3 scripts/setup_plugin.py --host claude-code
python3 scripts/setup_plugin.py --host codex

# Verify installed skills
python3 scripts/setup_plugin.py --host claude-code --verify
python3 scripts/setup_plugin.py --host codex --verify
```

The script copies plugin skills only. It does not silently install MCP servers, LSP tools, signing assets, or global CLIs.

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
- Claude Code / Codex host installation and packaging
- capability routing across commands, skills, references, hooks, and scripts
- Context7/MCP-aware documentation lookup when available
- LSP/SourceKit-aware source intelligence and diagnostics when available
- review and quality-gate orchestration

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
