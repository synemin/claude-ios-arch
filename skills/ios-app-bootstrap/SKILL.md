---
name: ios-app-bootstrap
description: Design, bootstrap, review, and evolve new iOS app architectures with low technical debt. Use when discussing SwiftUI/UIKit selection, async-await concurrency, feature-first directory structure, clean-ish layering, state/data flow, dependency direction, dependency injection, observability, modularization timing, testing strategy, or debt prevention for greenfield or early-stage iOS apps.
---

# iOS App Bootstrap

Use this skill to produce staff-level recommendations for new or early-stage iOS apps.

## Core Operating Rule
Treat greenfield and early-stage work as **state-aware bootstrap**, not as one universal template.

## Required Decision Inputs
Before proposing a baseline, identify:
- current project state
- product type and core flows
- team size / skill mix
- expected complexity and scale pressure
- platform scope (iOS-only or cross-platform adjacent)
- offline / realtime / performance constraints
- release urgency
- testing and observability expectations

## Core Defaults
Unless constraints override them, recommend:
- SwiftUI first, UIKit selectively.
- Swift Concurrency first.
- Feature-first structure with layers inside features.
- Lightweight clean layering: Presentation / Domain / Data.
- Initializer injection.
- `URLSession`-based typed API client.
- Local feature state before global state.
- Strong day-1 observability.
- Official-platform capabilities before third-party libraries.

## Required Operating Principles
- optimize for simplicity, maintainability, and speed of change
- avoid speculative abstractions
- avoid over-modularization in greenfield apps
- keep side effects out of Views
- keep DTOs out of Presentation
- treat technical debt as explicit and repayable, not invisible
- explain future upgrade triggers instead of front-loading complexity

## Output Shape
When designing a new app, produce:
1. Assumptions and constraints
2. Detected project state and why
3. Recommended baseline stack
4. Tech selection trade-offs
5. Directory structure
6. Dependency and data/state flow
7. Day-1 infrastructure
8. Debt guardrails
9. Evolution path from MVP -> PMF -> Scale

## Directory Template
Prefer this template unless the user has strong reasons to change it:

```text
MyApp/
├─ App/
│  ├─ MyAppApp.swift
│  ├─ AppBootstrap.swift
│  ├─ AppRouter.swift
│  ├─ AppEnvironment.swift
│  └─ AppSession.swift
├─ Core/
│  ├─ Networking/
│  ├─ Storage/
│  ├─ Logging/
│  ├─ Analytics/
│  ├─ DesignSystem/
│  └─ Configuration/
├─ Features/
│  ├─ Auth/
│  │  ├─ Presentation/
│  │  ├─ Domain/
│  │  └─ Data/
│  ├─ Home/
│  ├─ Profile/
│  └─ Settings/
├─ Shared/
├─ Resources/
├─ Config/
└─ Tests/
```

## References
Read these files when needed:
- `../../platforms/ios/state-detection.md`
- `../../platforms/ios/architecture-evolution.md`
- `../../references/apple/swiftui-baseline.md`
- `../../references/apple/concurrency-guidelines.md`
- `../../references/apple/observation-state-model.md`
- `../../references/apple/navigation-patterns.md`
- `../../references/apple/urlsession-networking.md`
- `../../references/apple/app-lifecycle-baseline.md`
- `../../references/policies/third-party-adoption-policy.md`
- `../../references/apple/modularization-timing.md`
- `../../platforms/ios/scorecards/state-management.md`
- `../../platforms/ios/scorecards/navigation.md`
- `../../platforms/ios/scorecards/networking.md`
- `../../platforms/ios/scorecards/di.md`
- `../ios-app-bootstrap/references/debt-guardrails.md`
