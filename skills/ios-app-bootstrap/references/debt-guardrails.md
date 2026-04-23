# Debt Guardrails Reference

## What To Prevent Early
- View-layer side effects
- DTO leakage
- global singletons without discipline
- `Manager` sprawl
- premature generic abstractions
- unstable code dumped into `Shared`

## Debt Recording Format
For each shortcut, capture:
- name
- why it exists
- risk
- trigger for repayment
- expected repayment scope

## Repayment Triggers
Common triggers:
- third meaningful repetition
- debugging pain
- onboarding confusion
- cross-feature coupling
- unstable requirements settling into stable patterns
