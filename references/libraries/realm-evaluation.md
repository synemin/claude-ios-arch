# Realm Evaluation

Status: draft
Last reviewed: 2026-04-24
Confidence: low

## Official sources
- https://github.com/realm/realm-swift
- https://www.mongodb.com/docs/realm-sdks/swift/latest/

## Default recommendation
Do not adopt Realm by default. Consider it only when the project’s offline/local-data needs, object graph needs, or existing lock-in clearly justify it over official persistence paths.

## Current official-source note
The official repository README prominently warns that Atlas Device Sync + Realm SDKs were deprecated in 2024, and points users toward version 20 / community-branch style local-database usage without sync assumptions.

## Use when
- existing app already depends heavily on Realm
- local data complexity is significant and current persistence is a real bottleneck
- the team wants Realm primarily as a local database, not because it assumes the old sync story

## Avoid when
- greenfield app with modest persistence needs
- official persistence options are sufficient
- team wants lower lock-in and fewer custom abstractions
- the product requirement implicitly depends on Realm Sync era assumptions

## Migration implications
If a codebase already uses Realm, keeping it may still be cheaper than migrating. But new adoption should account for the post-deprecation reality and treat sync/backend assumptions as a separate decision.

## Related skills
- ios-tech-decision
- ios-library-selection
- ios-architecture-evolution
