# Install / Integration Guide

This repository is an **agent plugin for iOS app development** built with a **core + adapters** structure.

## Repository Model
- `core/` = host-agnostic iOS app development capability
- `adapters/claude-code/` = Claude-style coding-agent adapter
- `adapters/codex/` = Codex-style coding-agent adapter

## For Claude-style Coding Agents
Use:
- `adapters/claude-code/CLAUDE.md`
- `core/manifest.json`

Recommended loading order:
1. `adapters/claude-code/CLAUDE.md`
2. `core/manifest.json`
3. relevant files from `rules/`
4. relevant files from `commands/`
5. relevant files from `skills/`
6. optional templates/examples/platform guide

## For Codex-style Coding Agents
Use:
- `adapters/codex/AGENTS.md`
- `core/manifest.json`

Recommended loading order:
1. `adapters/codex/AGENTS.md`
2. `core/manifest.json`
3. relevant files from `rules/`
4. relevant files from `commands/`
5. relevant files from `skills/`
6. optional templates/examples/platform guide

## Main iOS Tasks Supported
- bootstrap a new iOS app
- choose a stack and architecture
- review an existing architecture
- identify debt and missing guardrails
- generate briefs, decision memos, and debt reports

## Notes
This repository is not an MCP server. It is a host-adaptable agent plugin package for iOS development workflows.
