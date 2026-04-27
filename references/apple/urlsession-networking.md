# URLSession Networking Baseline

Status: draft
Last reviewed: 2026-04-23
Confidence: medium

## Official sources
- https://developer.apple.com/documentation/foundation/urlsession

## Default recommendation
Prefer URLSession and typed request / response boundaries as the default networking baseline.

## Introduce a library only when
- request pipeline complexity is consistently high,
- existing stack lock-in is already real,
- the library genuinely reduces complexity at the current project scale.

## Related skills
- ios-tech-decision
- ios-feature-bootstrap
- ios-existing-project-adoption
