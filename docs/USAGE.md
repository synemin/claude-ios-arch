# Usage Guide

## Example Intents
- Help me frame this iOS app idea into an MVP.
- Help me bootstrap a new iOS app.
- Help me design a new feature in this app.
- What testing strategy should we use?
- Should I use SwiftUI or UIKit?
- Should we add SwiftLint or Tuist?
- Review this iOS architecture.
- Check this project for technical debt.
- Help me get ready for TestFlight and App Store submission.

## Workflow Mapping
### Discovery
- `commands/ios-discovery.md` + `skills/ios-discovery/`

### Development
- app bootstrap -> `commands/ios-app-bootstrap.md` + `skills/ios-app-bootstrap/`
- feature bootstrap -> `commands/ios-feature-bootstrap.md` + `skills/ios-feature-bootstrap/`
- testing strategy -> `commands/ios-testing-strategy.md` + `skills/ios-testing-strategy/`
- tooling decision -> `commands/ios-tooling-decision.md` + `skills/ios-tooling-decision/`
- review -> `commands/ios-arch-review.md` + `skills/ios-arch-review/`
- tech decision -> `commands/ios-tech-decision.md` + `skills/ios-tech-decision/`
- debt check -> `commands/ios-debt-check.md` + `skills/ios-debt-check/`

### Release & Operations
- `commands/ios-release-operations.md` + `skills/ios-release-operations/`

## Output Assets
Use templates for stable outputs:
- `templates/discovery-brief.md`
- `templates/architecture-brief.md`
- `templates/feature-brief.md`
- `templates/testing-plan.md`
- `templates/tooling-decision-memo.md`
- `templates/decision-memo.md`
- `templates/debt-report.md`
- `templates/release-operations-checklist.md`

## Heuristic Check
When reviewing a real iOS repository, optionally run:

```bash
python3 hooks/ios_arch_guard.py /path/to/ios-repo
```
