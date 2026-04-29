# Plugin Architecture Framework

This document defines the structural standard for `claude-ios-arch` as an agent plugin, not a prompt pack.

## Open-Source Plugin Lessons
From gstack, Understand-Anything, llm-wiki-style projects, and mature Swift tooling, strong plugins tend to share these properties:

1. **Host-native installation** — each agent host gets the shape it expects, not a generic README only.
2. **Small entrypoint, rich routed capabilities** — one install path, many discoverable commands/skills.
3. **Capability registry** — the agent can know what exists, when to use it, and what evidence is required.
4. **Pipeline over prompt** — inspect -> plan -> implement -> review -> verify -> document.
5. **Deterministic tools for fragile steps** — scripts/hooks for checks instead of relying only on model prose.
6. **Source-of-truth knowledge** — curated references, freshness policy, and live docs fallback.
7. **Code intelligence** — LSP/SourceKit/build/test evidence before broad edits.
8. **Output contracts** — templates and examples that force useful, reviewable results.
9. **Upgrade path** — install, update, readiness audit, migration, and rollback behavior.
10. **Safety and trust boundaries** — no silent global installs, network writes, signing changes, or credentials use.

## Framework Layers

### 1. Host Packaging Layer
Goal: Claude Code, Codex, and future hosts can install and load the plugin correctly.

Required assets:
- host adapter: `adapters/<host>/`
- install instructions: `docs/INSTALL.md`
- plugin operations skill: `skills/ios-plugin-operations/`
- setup/audit scripts when possible

Robustness questions:
- Can a host install without manual hidden decisions?
- Does the adapter say what to load first?
- Can the agent verify installation?
- Is update/uninstall/upgrade behavior documented or scripted?

### 2. Capability Discovery and Routing Layer
Goal: the agent can choose the right capability for the user's task.

Required assets:
- `plugin/manifest.json`
- `core/manifest.json`
- `manifests/capabilities.json`
- task-specific commands and skills

Robustness questions:
- Are capabilities named at product level, not just file level?
- Does each major user intent map to a command/skill?
- Are optional capabilities such as Context7/LSP treated as tools with fallback paths?
- Can the agent route from natural language to pipeline stage?

### 3. Knowledge and Documentation Layer
Goal: recommendations are grounded in stable sources and live docs when needed.

Required assets:
- `references/registry.json`
- `references/apple/`, `references/libraries/`, `references/policies/`
- `workflows/docs-refresh.md`
- Context7/MCP policy in `ios-plugin-operations`

Robustness questions:
- Is official-source policy explicit?
- Are references curated instead of raw dump only?
- Is there a freshness check?
- Is live docs lookup used only when it adds value?

### 4. Source Intelligence Layer
Goal: AI code output is based on the actual project, not imagined structure.

Required assets:
- LSP/SourceKit policy
- environment audit skill/command
- build/test/lint detection
- architecture guard hook

Robustness questions:
- Does the workflow inspect files, symbols, dependencies, and diagnostics before edits?
- Does it fall back gracefully if LSP is unavailable?
- Are build/test failures treated as blockers or evidence?

### 5. Development Pipeline Layer
Goal: code is produced through repeatable staff-level engineering flow.

Required stages:
```text
inspect -> classify state -> extract constraints -> retrieve docs -> decide -> implement -> review -> verify -> record ADR/debt -> report
```

Robustness questions:
- Does every non-trivial feature have a vertical slice?
- Are business rules, side effects, DTOs, and UI boundaries explicit?
- Are choices reversible or documented?
- Does the pipeline avoid premature heavy frameworks?

### 6. Code Output Pattern Layer
Goal: generated code is elegant, idiomatic, and maintainable.

Default iOS output pattern:
```text
Feature/
  Presentation/  View + ViewModel / Observable state
  Domain/        Use cases + domain models + repository protocols
  Data/          live repositories + DTO mapping + API/storage adapters
```

Quality rules:
- Views do not own networking/persistence/business rules.
- DTOs do not leak into presentation.
- Dependencies flow inward through protocols at boundaries, not everywhere.
- Initializer injection by default.
- Tests prove domain/use-case behavior first.
- Observability hooks exist before release pressure.

### 7. Review and Verification Layer
Goal: outputs are checked, not merely asserted.

Required assets:
- architecture review skill
- debt check skill
- review severity model
- architecture guard hook
- build/test/lint/format gates

Robustness questions:
- Are findings severity-ranked?
- Are auto-fix vs ask-first boundaries explicit?
- Is review connected to code changes and regression tests?
- Does the final answer include evidence?

### 8. Evolution and Maintenance Layer
Goal: the plugin and target app can evolve safely.

Required assets:
- architecture evolution skill
- skill regeneration workflow
- release audit workflow
- readiness/capability audits

Robustness questions:
- Can the plugin detect when current architecture no longer fits?
- Does it recommend the smallest safe migration?
- Are plugin changes reflected across manifests, skills, commands, docs, examples, and scripts?
- Are research findings promoted into policy through validation, not ad hoc copying?

## Current Gap Assessment

### Strong Today
- Core + adapter repo structure exists.
- Many iOS task skills and commands exist.
- Official-source references and refresh workflow exist.
- Architecture/debt/release review concepts exist.

### Recently Improved
- Added `ios-plugin-operations` skill for host installation, Context7/MCP, LSP, review gates, and maintenance routing.
- Added install/capability references for Claude Code and Codex.
- Added capability manifest entries for plugin operations.

### Still Weak / Next Work
1. **Setup automation** — add `setup` command/script with `--host claude-code|codex`, dry-run, verify, and upgrade.
2. **Capability readiness audit** — script should check framework layers, not only file existence.
3. **LSP integration detail** — document SourceKit-LSP invocation/discovery and fallback diagnostics.
4. **Context7 integration detail** — document exact MCP detection, use policy, and fallback to official fetch.
5. **Code generation contracts** — strengthen templates so AI produces consistent vertical-slice code, not prose.
6. **Fixture validation** — test default/offline/complex-state/bad-architecture project fixtures.
7. **Cross-model/review loop** — optional second-opinion review pattern for high-risk changes.
8. **Upgrade/uninstall story** — current install docs are better but not yet a polished open-source plugin lifecycle.

## Design Standard
A future change is not complete unless it answers:

1. Which framework layer does this improve?
2. Which host(s) can use it?
3. Which user intent routes to it?
4. Which evidence source grounds it?
5. Which deterministic check verifies it?
6. What is the fallback when the tool is unavailable?
7. What needs to be updated across manifests/docs/skills/commands/templates?
