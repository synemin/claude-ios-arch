# Golden Example: Feature Brief

## Feature Goal
Add onboarding that captures user intent, permissions timing, and first successful journal entry.

## Detected Project State
- state: feature-on-existing
- why: the app already has auth, home, and storage flows; this task adds a scoped user-facing capability inside an active codebase.

## Constraints
- current architecture: SwiftUI app with feature-first structure and lightweight Presentation/Domain/Data split
- delivery urgency: moderate; onboarding is important for activation but not a hotfix
- current stack / lock-in: URLSession client exists, analytics baseline exists, persistence is light
- notable product constraints: notification permission should be delayed until value is visible

## User Flow
- welcome
- choose intent
- create first entry
- optional notification prompt
- transition to home

## Official Baseline
- relevant platform baseline: SwiftUI-first flow, local state close to usage, simple navigation until deeper routing is necessary
- why it fits: onboarding is a bounded feature and does not justify broader coordinator complexity yet

## Responsibilities By Layer
### Presentation
- screens, local view state, navigation events
### Domain
- onboarding progress model
- save first entry use case
- mark onboarding complete use case
### Data
- local persistence for progress
- remote sync only after first successful entry if account exists

## Proposed Directory Structure
Onboarding/
- Presentation/
- Domain/
- Data/

## State / Side-Effect Flow
- view emits intent
- view model updates local state
- use case handles save/complete logic
- repository persists progress
- analytics records activation milestones

## Scorecard Notes
- state management: local feature state is enough; no global state upgrade needed
- navigation: simple stack + completion handoff is enough
- networking: reuse current URLSession baseline
- persistence: reuse current lightweight persistence for onboarding progress

## Observability
- track welcome_seen, intent_selected, first_entry_saved, onboarding_completed
- log save failures
- surface actionable user-facing error on first-entry failure

## Risks / Guardrails
- do not mix onboarding rules with auth/session rules prematurely
- do not ask for notification permission on first screen
- keep onboarding-specific models out of shared/global folders unless reuse becomes real

## First Implementation Slice
Ship welcome -> first entry -> onboarding complete happy path first.

## Upgrade Triggers
- if onboarding becomes experiment-heavy, add clearer analytics taxonomy and experiment seams
- if cross-feature orchestration grows, revisit navigation ownership
