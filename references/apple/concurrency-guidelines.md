# Concurrency Guidelines

Status: draft
Last reviewed: 2026-04-23
Confidence: medium

## Official sources
- https://developer.apple.com/documentation/swift

## Default recommendation
Prefer structured concurrency with async/await, clear actor ownership, and explicit cancellation handling.

## Use when
- new async code
- network-driven features
- task orchestration with readable flow

## Avoid / not ideal when
- backport constraints force legacy callback integration

## Trade-offs
Structured concurrency reduces incidental complexity, but misuse of detached tasks, implicit actor hopping, or unclear cancellation can still create hard-to-debug behavior.

## Related skills
- ios-app-bootstrap
- ios-feature-bootstrap
- ios-tech-decision
