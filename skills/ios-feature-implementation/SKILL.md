---
name: ios-feature-implementation
description: Implement a feature inside an existing iOS codebase by reading current code, respecting existing patterns, and making minimal-impact changes. Use when the feature plan exists and the user needs actual implementation guidance: where to add files, what code to write, how to wire dependencies, and how to keep the change safe and reviewable.
---

# iOS Feature Implementation

Use this skill when the feature plan already exists (via `ios-feature-bootstrap` or equivalent) and the user needs to **actually write the code**: create files, wire dependencies, integrate state and navigation, and ship a reviewable PR.

This is execution, not design.

## Core Operating Rule

Read the existing codebase first. Match its conventions exactly. The goal is a change that looks like it was written by the same developer who wrote the rest of the app.

## Required Inputs

Before writing any code, gather:
- The feature plan or brief (from `ios-feature-bootstrap` or user description)
- Current project structure (run `find` / `tree` on relevant directories)
- Existing patterns: naming conventions, architecture style, DI approach, navigation mechanism
- State management approach already in use (@Observable, ObservableObject, etc.)
- Networking layer (URLSession wrapper, Alamofire, custom)
- Persistence layer (SwiftData, CoreData, UserDefaults, custom)

## Workflow

### 1. Read Existing Code Structure and Conventions

Scan the project to understand:
- Directory layout and module boundaries
- Naming patterns (e.g., `XxxViewModel`, `XxxRepository`, `XxxService`)
- How existing features are structured
- Import patterns and dependency direction
- Error handling conventions

### 2. Identify the Feature Boundary

Determine:
- Which module/folder/target this feature belongs in
- Whether it needs a new folder or fits into an existing one
- Feature-local vs shared code split

### 3. Map Dependencies

For each responsibility in the feature:
- **Reuse**: existing networking, persistence, navigation, models, utilities
- **Extend**: existing protocols, base classes, or shared components
- **Create**: only what doesn't exist yet

Prefer reuse > extend > create.

### 4. Define the Implementation Slice

The smallest shippable unit that:
- Delivers visible user value
- Is independently testable
- Does not require follow-up PRs to be useful
- Keeps the PR under ~400 lines of meaningful change

### 5. Generate Implementation Plan

For each file:
- **New files**: full path, purpose, key types/functions
- **Modified files**: what changes, why, and the minimal diff

Structure the plan as:
```
Files to create:
  - Features/Xxx/Views/XxxView.swift — main screen
  - Features/Xxx/XxxViewModel.swift — state + async logic
  - Features/Xxx/XxxRepository.swift — data access

Files to modify:
  - Navigation/Router.swift — add route case
  - DI/Container.swift — register new dependencies
```

### 6. Wire State, Navigation, and Data Flow

- Register new types in the existing DI system (or create them inline if the app doesn't use DI)
- Add navigation routes using the app's existing navigation pattern
- Connect data flow: View → ViewModel → UseCase/Repository → Service
- Wire error handling into the existing error display mechanism

### 7. Add Test Hooks and Observability

- Make dependencies injectable (protocol or closure)
- Add logging/analytics calls matching existing patterns
- Create test file stubs with the most critical test cases identified
- Ensure async code is testable (injected clock/scheduler if needed)

### 8. Review the Change for Debt Introduction

Before finalizing, check:
- [ ] No new architectural pattern introduced that doesn't exist elsewhere
- [ ] No parallel abstraction created when extending an existing one would work
- [ ] PR scope is reviewable (single feature, no drive-by refactors)
- [ ] No force-unwraps, no unhandled errors on user-facing paths
- [ ] Naming matches existing conventions

## Key Principles

- **Match existing code style.** If the codebase uses `XxxViewModel`, don't introduce `XxxStore`. If it uses trailing closure style, use that too.
- **Prefer extending existing abstractions** over creating parallel ones. If there's already a `NetworkService` protocol, conform to it.
- **Keep PR scope reviewable.** One feature, one PR. No architecture upgrades smuggled in.
- **Don't upgrade architecture in a feature PR** unless explicitly requested. File a tech-debt ticket instead.
- **Wire into existing DI/navigation/state** without breaking other features. New registrations should be additive.

## Required Output

### 1. Current Codebase Snapshot
Summary of the relevant areas: directory structure, existing patterns, dependencies that will be reused.

### 2. Implementation Plan
Complete file list: files to create (with skeleton code) and files to modify (with targeted diffs).

### 3. Dependency Wiring
How new types connect to existing infrastructure: DI registrations, protocol conformances, shared services.

### 4. State/Navigation Integration
How the feature's state flows, how users navigate to/from it, and how it connects to the app's navigation graph.

### 5. Test Coverage Plan
Which tests to write, what they verify, and how dependencies are mocked/stubbed.

### 6. PR Scope and Review Notes
Summary for the reviewer: what changed, what was intentionally left out, any follow-up work.

## References

Read when needed:
- `../../platforms/ios/guide.md`
- `../../platforms/ios/state-detection.md`
- `../../platforms/ios/scorecards/state-management.md`
- `../../platforms/ios/scorecards/navigation.md`
- `../../platforms/ios/scorecards/networking.md`
- `../../platforms/ios/scorecards/di.md`
- `../../references/apple/observation-state-model.md`
- `../../references/apple/navigation-patterns.md`
- `../../references/apple/urlsession-networking.md`
- `../../templates/feature-brief.md`
