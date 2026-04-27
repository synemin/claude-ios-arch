# iOS State Detection

## Goal
Detect the current project state before choosing architecture or implementation guidance.

## Supported States
### greenfield
Signals:
- no Xcode project / package / app module yet
- only notes or product idea exists

Default strategy:
- establish baseline architecture
- choose minimum viable stack
- set guardrails early

### bootstrap-in-progress
Signals:
- project exists but foundational choices are still fluid
- app shell exists without stable feature boundaries

Default strategy:
- stabilize composition root and directory structure
- avoid over-modularization

### feature-on-existing
Signals:
- app is active and user asks for one feature or workflow change
- most architecture decisions already exist

Default strategy:
- respect current structure unless it blocks delivery
- implement incrementally
- isolate new debt instead of spreading it

### legacy-rescue
Signals:
- weak boundaries
- catch-all folders
- high coupling
- large presentation files with side effects

Default strategy:
- stop the bleeding first
- propose smallest refactor with leverage
- avoid rewrite advice by default

### architecture-drift
Signals:
- original patterns exist but have become inconsistent
- feature work added repeated exceptions and duplicate patterns

Default strategy:
- restore consistency
- define new guardrails
- refactor selectively around high-value seams

### pre-release-hardening
Signals:
- release or TestFlight pressure
- focus on stability, observability, defects, and checklist readiness

Default strategy:
- prioritize correctness over ambitious refactors

### migration-window
Signals:
- deliberate migration in flight: UIKit→SwiftUI, callbacks→async/await, old stack→new stack

Default strategy:
- stage the migration
- preserve rollback paths
- keep old/new boundaries explicit
