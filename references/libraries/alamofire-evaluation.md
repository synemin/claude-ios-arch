# Alamofire Evaluation

Status: draft
Last reviewed: 2026-04-24
Confidence: low

## Official sources
- https://github.com/Alamofire/Alamofire
- https://alamofire.github.io/Alamofire/

## Default recommendation
Do not adopt Alamofire by default. Prefer `URLSession` unless request composition, auth interception, retry policy, upload/download workflows, or existing team lock-in make Alamofire a net simplifier.

## Use when
- networking complexity is already high
- interceptors / retriers / request composition are repeated pain
- upload/download workflows are common enough that a richer client abstraction helps
- existing codebase already uses Alamofire and migration cost is not worth it

## Avoid when
- greenfield app with straightforward API calls
- small app where a typed URLSession client is enough
- the team does not want extra dependency and migration surface

## Migration implications
The official repository exposes broad request, authentication, response-handling, validation, caching, upload/download, and advanced session usage surfaces. That power can reduce implementation effort in complex apps, but it also increases dependency surface and architectural coupling around networking.

Retaining it in an existing codebase may be smarter than migrating if current usage is stable and not a major pain source.

## Related skills
- ios-tech-decision
- ios-library-selection
- ios-existing-project-adoption
