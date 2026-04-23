---
name: ios-app-bootstrap
description: Design, bootstrap, review, and evolve new iOS app architectures with low technical debt. Use when discussing SwiftUI/UIKit selection, async-await concurrency, feature-first directory structure, clean-ish layering, state/data flow, dependency direction, dependency injection, observability, modularization timing, testing strategy, or debt prevention for greenfield or early-stage iOS apps.
---

# iOS App Bootstrap

Use this skill to produce staff-level recommendations for new or early-stage iOS apps.

## Core Defaults
Unless the user gives constraints that override them, recommend:
- SwiftUI first, UIKit selectively.
- Swift Concurrency first.
- Feature-first structure with layers inside features.
- Lightweight clean layering: Presentation / Domain / Data.
- Initializer injection.
- `URLSession`-based typed API client.
- Local feature state before global state.
- Strong day-1 observability.

## Required Operating Principles
- Optimize for simplicity, maintainability, and speed of change.
- Avoid speculative abstractions.
- Avoid over-modularization in greenfield apps.
- Keep side effects out of Views.
- Keep DTOs out of Presentation.
- Treat technical debt as explicit and repayable, not invisible.

## Output Shape
When designing a new app, produce:
1. Assumptions and constraints
2. Recommended baseline stack
3. Tech selection trade-offs
4. Directory structure
5. Dependency and data/state flow
6. Day-1 infrastructure
7. Debt guardrails
8. Evolution path from MVP -> PMF -> Scale

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

## Review Checklist
Use this checklist when reviewing an app or proposed architecture:
- Are feature boundaries obvious?
- Are side effects isolated?
- Are domain rules separated from Views?
- Are DTOs mapped before presentation?
- Is shared code genuinely shared?
- Is observability present from day 1?
- Is complexity justified by current needs?

## References
Read these files when needed:
- `references/tech-stack.md` for default tech choices and deviation rules.
- `references/debt-guardrails.md` for debt prevention and repayment policy.
- `references/output-template.md` for a standard answer shape.

## Bundled Script
Use `scripts/render_ios_bootstrap_template.py` when the user wants a generated starter brief with placeholders filled.
