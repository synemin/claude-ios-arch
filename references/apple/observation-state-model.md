# Observation & State Model

Status: draft
Last reviewed: 2026-04-23
Confidence: medium

## Official sources
- https://developer.apple.com/documentation/swiftui

## Default recommendation
Keep state ownership explicit. Prefer local state close to usage, lift state only when multiple surfaces truly share ownership, and avoid global mutable state as the default escape hatch.

## Review focus
- who owns the state?
- what triggers mutations?
- where do side effects live?
- can UI models stay separate from DTOs?

## Related skills
- ios-app-bootstrap
- ios-arch-review
- ios-feature-bootstrap
