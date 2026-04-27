# Golden Example: Existing Project Adoption

## Current-State Summary
A journaling app already ships to TestFlight with SwiftUI screens, a thin networking layer, and mixed folder discipline. The app works, but new features are spreading shared models and side effects into presentation code.

## Detected Project State
- state: architecture-drift
- why: the original feature-first intent still exists, but repeated feature delivery has introduced inconsistent patterns, shared-folder growth, and mixed ownership boundaries.

## Strengths To Preserve
- SwiftUI baseline is already established
- URLSession networking exists and is understandable
- release flow is active; the team can already ship
- some feature boundaries still exist and can be reinforced

## Structural Risks
- presentation files are starting to absorb side effects
- shared folder growth is weakening feature ownership
- analytics and logging are inconsistent across new flows

## Debt Containment Opportunities
- stop adding new cross-feature shared models without proof of reuse
- standardize mapping boundaries before presentation
- make one bootstrap/composition root clearer before expanding DI complexity

## Migration Priorities
1. reinforce feature ownership in the next feature change
2. introduce explicit DTO -> UI mapping at unstable seams
3. standardize observability on critical flows
4. delay broad modularization until ownership pain becomes sustained

## What To Postpone
- full rewrite of existing flows
- DI framework adoption
- package/module breakup

## Environment / Toolchain Notes
- keep current URLSession baseline
- do not add project tooling unless current Xcode project pain becomes recurring
