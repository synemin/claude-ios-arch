# iOS Day-1 Checklist

Use this checklist when bootstrapping a new iOS app.

## Required
- app environments (`Debug` / `Staging` / `Release`)
- config/secrets discipline
- logging
- crash reporting
- analytics/event naming approach
- feature flag capability
- error taxonomy
- root router / app session boundary
- first feature boundary definition
- testing baseline for domain/use-case logic

## Strongly Recommended
- network request abstraction boundary
- DTO/domain/UI model split
- deep-link strategy
- onboarding/auth flow boundary
- release checklist ownership

## Avoid Early
- premature modularization
- heavy DI container
- giant global app state
- repository abstraction without concrete need
- design system over-engineering before real UI repetition
