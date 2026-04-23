# Golden Example: Feature Brief

## Feature Goal
Add onboarding that captures user intent, permissions timing, and first successful journal entry.

## Assumptions
- onboarding should optimize activation, not explain every feature
- notifications permission should be delayed until value is visible

## User Flow
- welcome
- choose intent
- create first entry
- optional notification prompt
- transition to home

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

## Observability
- track welcome_seen, intent_selected, first_entry_saved, onboarding_completed
- log save failures
- surface actionable user-facing error on first-entry failure

## Risks / Guardrails
- do not mix onboarding rules with auth/session rules prematurely
- do not ask for notification permission on first screen

## First Implementation Slice
Ship welcome -> first entry -> onboarding complete happy path first.
