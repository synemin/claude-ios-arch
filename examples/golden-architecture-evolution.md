# Golden Example: Architecture Evolution

## Current Mismatch Summary
A once-small SwiftUI app now has five major features, shared mutable session state, repeated cross-feature helpers, and increasingly inconsistent routing ownership.

## Detected Project State
- state: architecture-drift
- why: the original app shape worked at MVP size, but repeated feature growth introduced inconsistent seams and shared abstractions.

## Upgrade Triggers
- repeated cross-feature coupling
- unclear routing ownership
- shared folder becoming a dumping ground
- difficulty adding tests around business-critical flows

## Recommended Target Shape
- preserve current single-project structure
- strengthen feature boundaries
- centralize bootstrap/composition root
- standardize DTO/domain/UI mapping seams
- define navigation ownership more clearly per feature flow

## Migration Seams
- start with the next feature that already touches routing and state ownership
- add mapping boundaries before presentation in unstable flows
- standardize one composition-root pattern without introducing a DI framework yet

## Do Now / Later / Avoid
- do now: reinforce boundaries at active seams
- later: consider modularization only if ownership and build pain stay high
- avoid: broad rewrite or framework-heavy redesign
