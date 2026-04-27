# Tuist Evaluation

Status: draft
Last reviewed: 2026-04-23
Confidence: low

## Official sources
- https://docs.tuist.io/
- https://github.com/tuist/tuist

## Default recommendation
Do not adopt Tuist unless project generation pain, workspace sprawl, or multi-project management complexity is real enough to justify an extra toolchain.

## Official-source signal
The official docs position Tuist as a broader project/workspace generation and management system, not just a one-off project file generator. That makes it more suitable when the repo truly needs ongoing workspace orchestration, not merely cleaner `.xcodeproj` generation.

## Use when
- larger repo with repeated project configuration pain
- multiple modules / apps / environments need consistent generation

## Avoid when
- small repo with low Xcode project churn
- the team cannot afford extra tooling ownership

## Related skills
- ios-tooling-decision
