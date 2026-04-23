# iOS Testing Scenarios

## MVP / Early Stage
Bias toward:
- domain/use-case tests
- key mapper/parser tests
- 1-3 UI smoke paths

## Growth Stage
Add:
- integration tests around repositories and session boundaries
- failure-path tests for critical user journeys
- release regression checklist alignment

## Complex App / Team Scale
Add selectively:
- stronger integration coverage
- performance tests for hotspots
- targeted UI automation on stable critical flows

## What To Defer Early
- exhaustive UI test suites
- highly coupled snapshot baselines
- complicated fake infrastructure that costs more than the bugs it catches
