# Core Layer

The `core/` directory contains the host-agnostic substance of the plugin.

This is the durable asset layer for iOS app development guidance:
- architecture rules
- low-debt guardrails
- workflow commands
- reusable skills
- templates
- examples
- iOS platform guidance
- lightweight review hooks

## Principle
Keep `core/` free from host-specific packaging assumptions wherever possible.

- Put Claude-specific wrapping in `adapters/claude-code/`
- Put Codex-specific wrapping in `adapters/codex/`
- Keep iOS engineering knowledge in `core/`

## Current Scope
Phase 1 supports **iOS only**.
