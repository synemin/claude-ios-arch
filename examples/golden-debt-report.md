# Golden Example: Debt Report

## Detected Project State
- state: legacy-rescue
- why: the app is shipping, but core flows show singleton-heavy access, large view models, shared-folder sprawl, and presentation-layer side effects.

## Structural Debt
- multiple `.shared` access points across feature code
- network calls appearing in presentation-adjacent files
- DTOs leaking into UI state models

## Tactical Debt
- duplicated mapping logic in two features
- ad-hoc error presentation with inconsistent user messaging

## Missing Guardrails
- no explicit mapping boundary rule
- no observability baseline on critical save / sync flows
- no composition-root convention visible in the repo

## Evidence / Signals
- oversized view models
- catch-all shared directories
- repeated callback-era async patterns

## Containment Plan
- stop new singleton spread first
- isolate networking into existing data layer seams
- introduce one mapping convention and apply it to new work immediately

## Repayment Priority
1. presentation side effects
2. DTO leakage
3. singleton sprawl
4. shared-folder cleanup

## What Can Wait Safely
- aesthetic renames
- deeper modularization
- broad folder reshuffles without delivery leverage
