#!/usr/bin/env python3
import argparse

TEMPLATE = '''# iOS App Bootstrap Brief

## Assumptions
- Product: {product}
- Team: {team}
- Complexity: {complexity}
- Platform scope: {platform_scope}

## Recommended Baseline
- UI: SwiftUI first, UIKit selectively
- Concurrency: async/await
- Architecture: feature-first + clean-ish layering
- State: local state + ViewModel/Observable pattern
- Networking: URLSession typed client
- DI: initializer injection
- Observability: analytics, logging, crash reporting, feature flags from day 1

## Directory Structure
```text
{app_name}/
├─ App/
├─ Core/
├─ Features/
├─ Shared/
├─ Resources/
├─ Config/
└─ Tests/
```

## Debt Guardrails
- Keep side effects out of Views
- Keep DTOs out of Presentation
- Delay abstractions until the third meaningful repetition
- Avoid premature modularization
- Record every shortcut with repayment triggers

## Next Steps
1. Define feature boundaries
2. Establish navigation/session model
3. Set up day-1 infra
4. Implement first vertical slice
'''


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--app-name', default='MyApp')
    p.add_argument('--product', default='TBD')
    p.add_argument('--team', default='small mobile team')
    p.add_argument('--complexity', default='early-stage')
    p.add_argument('--platform-scope', default='iOS-first')
    args = p.parse_args()
    print(TEMPLATE.format(
        app_name=args.app_name,
        product=args.product,
        team=args.team,
        complexity=args.complexity,
        platform_scope=args.platform_scope,
    ))

if __name__ == '__main__':
    main()
