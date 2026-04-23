# Tech Stack Reference

## Default Baseline
- UI: SwiftUI first
- Escape hatch: UIKit selectively
- Concurrency: async/await
- Networking: URLSession typed client
- State: local feature state + ViewModel/Observable pattern
- DI: initializer injection
- Architecture: feature-first + clean-ish layering
- Storage: UserDefaults/file first; GRDB or SwiftData only when warranted
- Navigation: app router / coordinator-ish for complex flows
- Testing: unit tests for domain/use cases; small set of critical integration/UI tests

## Deviation Guidance
### Prefer more UIKit when:
- advanced text input is central
- layout/performance constraints are known SwiftUI pain points
- existing UIKit assets are strategically important

### Prefer heavier state frameworks only when:
- state complexity is genuinely high
- effect modeling must be strict
- team fluency already exists

### Prefer modularization only when:
- compile times materially degrade delivery
- ownership boundaries are stable
- multiple teams or durable reuse justify it
