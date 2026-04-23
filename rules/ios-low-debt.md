# iOS Low-Debt Startup Rules

Use these rules when the goal is to start a new app with minimal technical debt and good repayment discipline.

## Core Principle
Do not optimize for mythical zero debt. Optimize for:
- low accidental complexity
- explicit shortcuts
- easy rollback
- clear ownership
- observable failure modes

## Required Day-1 Capabilities
Every new app baseline should account for:
- crash reporting
- structured logging
- analytics/event taxonomy
- feature flags / remote config hooks
- environment separation (`Debug`, `Staging`, `Release`)
- secrets/config discipline
- error taxonomy

## Debt Guardrails
- Record every known shortcut with reason, risk, and repayment trigger.
- Prefer temporary concrete code over permanent premature abstractions.
- Treat “we’ll clean this later” as invalid unless repayment conditions are stated.
- Prefer duplication over brittle abstractions early, but revisit at the third meaningful repetition.

## Forbidden Patterns For Greenfield Apps
- Global singleton sprawl
- DTOs shared as app-wide models
- Giant `AppState` without clear need
- Heavy state-management framework by default
- Multi-module decomposition before feature boundaries stabilize
- Catch-all directories (`Utils`, `Common`, `Managers`) without ownership rules

## Required Questions Before Adding Complexity
1. Is this solving a current problem or an imagined future one?
2. What is the rollback cost if we choose wrong?
3. Can a new team member explain this structure in 10 minutes?
4. Does this improve debuggability, testability, or delivery speed enough to justify itself?

## MVP -> PMF -> Scale Guidance
- MVP: keep structure simple, observability strong.
- PMF: reinforce domain boundaries, design system, analytics taxonomy, and feature flags.
- Scale: modularize selectively, strengthen CI/test automation, and refactor hot spots based on evidence.
