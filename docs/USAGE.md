# Usage Guide

## Core Usage Model
This plugin should be used as a **state-aware app development system**, not as a static collection of architecture tips.

Before making major recommendations, the agent should usually:
1. detect the current project state,
2. extract key constraints,
3. check the official baseline,
4. apply the relevant scorecard,
5. recommend the smallest context-appropriate next move.

## Example Intents
- Help me frame this iOS app idea into an MVP.
- Help me bootstrap a new iOS app.
- Adopt this existing iOS project.
- Help me design a new feature in this app.
- What testing strategy should we use?
- Should I use SwiftUI or UIKit?
- Should we add this library?
- Review this iOS architecture.
- Check this project for technical debt.
- Help me get ready for TestFlight and App Store submission.

## Workflow Mapping
### Discovery
- `../commands/ios-discovery.md` + `../skills/ios-discovery/`

### Development
- app bootstrap -> `../commands/ios-app-bootstrap.md` + `../skills/ios-app-bootstrap/`
- existing project adoption -> `../commands/ios-existing-project-adoption.md` + `../skills/ios-existing-project-adoption/`
- feature bootstrap -> `../commands/ios-feature-bootstrap.md` + `../skills/ios-feature-bootstrap/`
- testing strategy -> `../commands/ios-testing-strategy.md` + `../skills/ios-testing-strategy/`
- tooling decision -> `../commands/ios-tooling-decision.md` + `../skills/ios-tooling-decision/`
- tech decision -> `../commands/ios-tech-decision.md` + `../skills/ios-tech-decision/`
- library selection -> `../commands/ios-library-selection.md` + `../skills/ios-library-selection/`
- review -> `../commands/ios-arch-review.md` + `../skills/ios-arch-review/`
- debt check -> `../commands/ios-debt-check.md` + `../skills/ios-debt-check/`
- architecture evolution -> `../commands/ios-architecture-evolution.md` + `../skills/ios-architecture-evolution/`

### Release & Operations
- `../commands/ios-release-operations.md` + `../skills/ios-release-operations/`

## Key Support Assets
### State & Decision Support
- `../platforms/ios/state-detection.md`
- `../platforms/ios/architecture-evolution.md`
- `../platforms/ios/scorecards/state-management.md`
- `../platforms/ios/scorecards/navigation.md`
- `../platforms/ios/scorecards/networking.md`
- `../platforms/ios/scorecards/persistence.md`
- `../platforms/ios/scorecards/di.md`
- `../platforms/ios/scorecards/testing.md`

### Official-Source References
- `../references/registry.json`
- `../references/apple/`
- `../references/policies/`
- `../references/libraries/`

Use `../references/libraries/` when a decision involves retaining, replacing, or introducing third-party dependencies under real project constraints.

### Output Assets
Use templates for stable outputs:
- `../templates/discovery-brief.md`
- `../templates/architecture-brief.md`
- `../templates/feature-brief.md`
- `../templates/testing-plan.md`
- `../templates/tooling-decision-memo.md`
- `../templates/decision-memo.md`
- `../templates/debt-report.md`
- `../templates/release-operations-checklist.md`

## Heuristic Check
When reviewing a real iOS repository, optionally run:

```bash
python3 ../hooks/ios_arch_guard.py /path/to/ios-repo
```

## Refresh Model
This plugin is intended to evolve with official documentation.

Use:
- `../docs/RESEARCH-WORKFLOW.md`
- `../workflows/docs-refresh.md`
- `../workflows/reference-review.md`
- `../workflows/skill-regeneration.md`
- `../workflows/release-audit.md`
- `../scripts/generate_refresh_report.py`
- `../scripts/audit_plugin_readiness.py`

Default refresh posture:
- favor repeatable official-source updates
- use another viable official retrieval method when the default path fails
- prefer alternate official sources before any non-official source

To keep references, skills, commands, templates, and release readiness aligned over time.
