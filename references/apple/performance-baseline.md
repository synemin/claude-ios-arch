# Performance Baseline

Status: draft
Last reviewed: 2026-04-23
Confidence: low

## Official sources
- https://developer.apple.com/documentation/xcode/improving_your_app_s_performance

## Default recommendation
Do not optimize blindly. First identify user-visible bottlenecks, then improve the narrowest hotspot with the lowest structural cost.

## Focus areas
- main-thread pressure
- rendering hotspots
- heavy state propagation
- repeated decoding / mapping work
- large list / image handling paths

## Related skills
- ios-debt-check
- ios-testing-strategy
- ios-arch-review
