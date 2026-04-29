# Install and Host Reference

## Claude Code
Claude Code should receive this plugin as native skills plus project instructions.

Preferred install shape:

```bash
mkdir -p ~/.claude/skills
cp -R skills/ios-* ~/.claude/skills/
```

For a project/team repository, add a `CLAUDE.md` section that says:

- use `claude-ios-arch` for iOS app discovery, bootstrap, feature implementation, review, release, and plugin maintenance
- load the host adapter first: `adapters/claude-code/CLAUDE.md`
- then load `core/manifest.json`
- select the matching command + skill for the task
- use Context7/MCP documentation lookup when configured and the decision is API/version-sensitive
- use LSP/SourceKit diagnostics when available before risky refactors
- run review/quality gates before reporting success

## Codex
Codex should receive the same capability as Codex-readable skills and repo instructions.

Preferred install shape:

```bash
mkdir -p ~/.codex/skills
cp -R skills/ios-* ~/.codex/skills/
```

For a project/team repository, add an `AGENTS.md` section that says:

- use `claude-ios-arch` for iOS app work and plugin operations
- load `adapters/codex/AGENTS.md`, then `core/manifest.json`
- route to matching commands/skills instead of relying on one giant prompt
- prefer official/local references; use Context7 if configured
- inspect with LSP/SourceKit/build/test before broad edits

## Team / Repo-Local Mode
Team installs should avoid copying opaque state into app repos. Prefer:

- a small `CLAUDE.md` / `AGENTS.md` pointer
- stable plugin version or commit
- explicit setup/check command
- no surprise global installs

## External Capability Approval
Ask before installing or modifying:

- MCP servers such as Context7
- global CLIs
- Xcode toolchain changes
- signing/provisioning/App Store credentials
- network-publishing or repo-writing actions
