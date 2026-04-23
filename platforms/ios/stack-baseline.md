# iOS Stack Baseline

## Recommended Default Stack
- UI: SwiftUI-first
- Concurrency: Swift Concurrency
- State: local state + ViewModel/Observable pattern
- Networking: URLSession typed client
- DI: initializer injection
- Storage: UserDefaults/file first; GRDB/SwiftData when justified
- Navigation: app router/coordinator-ish where complexity warrants it
- Testing: domain/use-case unit tests + targeted integration/UI tests
- Observability: logging, analytics, crash reporting, feature flags
