# Modularization Timing

Status: draft
Last reviewed: 2026-04-23
Confidence: medium

## Official sources
- https://developer.apple.com/documentation/xcode/organizing_your_code_with_local_packages

## Default recommendation
Do not modularize early just to look scalable. Prefer clear feature boundaries inside one target first, and modularize when ownership, build cost, or dependency direction pain becomes persistent.

## Upgrade triggers
- sustained ownership boundaries across teams
- build times becoming meaningful pain
- dependency cycles and reuse pressure
- enforceable internal API boundaries becoming necessary

## Related skills
- ios-app-bootstrap
- ios-tooling-decision
- ios-architecture-evolution
