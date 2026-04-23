# Usage Guide

## Example Intents
- Help me bootstrap a new iOS app.
- Review this iOS architecture.
- Should I use SwiftUI or UIKit?
- Check this project for technical debt.

## Task Mapping
- bootstrap -> `commands/ios-app-bootstrap.md` + `skills/ios-app-bootstrap/`
- review -> `commands/ios-arch-review.md` + `skills/ios-arch-review/`
- tech decision -> `commands/ios-tech-decision.md` + `skills/ios-tech-decision/`
- debt check -> `commands/ios-debt-check.md` + `skills/ios-debt-check/`

## Output Assets
Use templates for stable outputs:
- `templates/architecture-brief.md`
- `templates/decision-memo.md`
- `templates/debt-report.md`

## Heuristic Check
When reviewing a real iOS repository, optionally run:

```bash
python3 hooks/ios_arch_guard.py /path/to/ios-repo
```
