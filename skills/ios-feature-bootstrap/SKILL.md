---
name: ios-feature-bootstrap
description: Design and bootstrap a new iOS feature with clean boundaries, low debt, and a pragmatic implementation path. Use when adding a new feature to an iOS app, decomposing presentation/domain/data responsibilities, proposing feature-local structure, defining state/data flow, or deciding the first safe implementation slice.
---

# iOS Feature Bootstrap

Use this skill when the user is not designing the entire app, but needs to add or shape a feature inside an iOS codebase.

## Core Operating Rule
A feature plan must fit the **current project state and current architecture reality**, not an idealized architecture from scratch.

## Required Decision Inputs
Before proposing structure, identify:
- current project state
- whether the feature is greenfield inside an existing app or an extension of existing flows
- current UI architecture and state model
- networking / persistence dependencies already in place
- release urgency and implementation radius
- whether current architecture should be respected, contained, or slightly upgraded

## Goals
- keep the feature locally understandable
- keep side effects explicit
- keep domain logic outside views
- keep the first slice implementable without over-abstracting
- avoid introducing architectural style that clashes with the existing app unless the benefit is clear

## Default Workflow
1. Detect the current project state and existing architecture constraints.
2. Define the smallest useful feature slice.
3. Assign responsibilities across presentation, domain, and data only to the degree the current app can sustain.
4. Use the current state model, navigation shape, and networking baseline unless there is a strong reason to upgrade.
5. Add observability and error handling appropriate to the feature risk.
6. Make upgrade triggers explicit if this feature exposes a deeper architecture mismatch.

## Required Output
1. Feature goal and assumptions
2. Detected project state and architecture constraints
3. Layer responsibilities
4. Suggested structure aligned to the current app
5. State and side-effect flow
6. Observability and error handling needs
7. First implementation slice
8. Upgrade triggers if the current app shape is no longer sufficient

## Default Structure
Prefer a feature-local structure only when it fits the current app reality:

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

If the app already uses a different legible structure, adapt to it instead of forcing this template mechanically.

## References
Read when needed:
- `../../platforms/ios/state-detection.md`
- `../../platforms/ios/scorecards/state-management.md`
- `../../platforms/ios/scorecards/navigation.md`
- `../../platforms/ios/scorecards/networking.md`
- `../../references/apple/observation-state-model.md`
- `../../references/apple/navigation-patterns.md`
- `../../references/apple/urlsession-networking.md`
- `../../templates/feature-brief.md`
