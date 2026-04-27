# Crash Reporting Evaluation

Status: draft
Last reviewed: 2026-04-24
Confidence: low

## Official sources
- https://firebase.google.com/docs/crashlytics
- https://docs.sentry.io/platforms/apple/

## Default recommendation
Use crash reporting when release risk is meaningful enough that blind failure is unacceptable. The exact provider should be chosen based on existing ecosystem fit, privacy posture, and operational workflow.

## Decision focus
- current release risk
- team incident workflow
- ecosystem lock-in
- privacy / compliance expectations
- debug usefulness versus SDK cost

## Related skills
- ios-release-operations
- ios-library-selection
