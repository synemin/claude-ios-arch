---
name: ios-feature-bootstrap
description: Design and bootstrap a new iOS feature with clean boundaries, low debt, and a pragmatic implementation path. Use when adding a new feature to an iOS app, decomposing presentation/domain/data responsibilities, proposing feature-local directory structure, defining state/data flow, or deciding the first safe implementation slice.
---

# iOS Feature Bootstrap

Use this skill when the user is not designing the entire app, but needs to add or shape a feature inside an iOS codebase.

## Goals
- Keep the feature locally understandable.
- Keep side effects explicit.
- Keep domain logic outside views.
- Keep the first slice implementable without over-abstracting.

## Required Output
1. Feature goal and assumptions
2. Layer responsibilities
3. Suggested directory structure
4. Key models and use cases
5. State and side-effect flow
6. Observability and error handling needs
7. First implementation slice

## Default Structure
Prefer a feature-local structure like:

```text
FeatureName/
├─ Presentation/
│  ├─ Views/
│  ├─ ViewModels/
│  └─ Routes/
├─ Domain/
│  ├─ Models/
│  ├─ UseCases/
│  └─ Repositories/
└─ Data/
   ├─ DTOs/
   ├─ Mappers/
   ├─ Remote/
   └─ Local/
```

## References
Read when needed:
- `../../platforms/ios/feature-patterns.md`
- `../ios-app-bootstrap/references/tech-stack.md`
- `../../templates/feature-brief.md`
