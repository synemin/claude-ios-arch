# iOS Platform Guide

This plugin currently supports **iOS only** in Phase 1, with a long-term roadmap toward broader app-development support.

## Platform Scope
Use this plugin for:
- SwiftUI/UIKit architecture design
- iOS app technical selection
- project-state detection
- existing-project adoption
- directory structure and feature decomposition
- low-debt startup guidance
- architecture review and debt checks
- feature bootstrap and layering
- architecture evolution planning
- release readiness and post-launch operations guidance

## Core Operating Model
Before giving major recommendations, the agent should usually:
1. detect current project state,
2. extract constraints,
3. check official-source references,
4. apply the relevant scorecard,
5. recommend the smallest context-appropriate next move.

## Default Baseline
- SwiftUI first
- async/await first
- feature-first structure
- clean-ish layering
- initializer injection
- URLSession typed client
- explicit model boundaries
- day-1 observability
- official-platform capabilities before third-party libraries unless constraints justify deviation

## Key Platform Assets
### State & Evolution
- `state-detection.md`
- `architecture-evolution.md`
- `review-checklist.md`
- `release-checklist.md`
- `app-store-risk-screen.md`

### Scorecards
- `scorecards/state-management.md`
- `scorecards/navigation.md`
- `scorecards/networking.md`
- `scorecards/persistence.md`
- `scorecards/di.md`
- `scorecards/testing.md`

### Reference Themes
Use `../../references/apple/` and `../../references/libraries/` for:
- UI baseline
- concurrency
- observation/state model
- navigation
- networking
- persistence
- testing
- performance
- accessibility
- background work
- observability
- modularization timing
- third-party library evaluation

## Phase-1 Boundary
This guide is intentionally optimized for **iOS-first quality** rather than broad multi-platform coverage.
Android, Flutter, and React Native remain future roadmap directions, not current operating scope.
