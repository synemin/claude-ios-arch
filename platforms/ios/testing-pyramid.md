# iOS Testing Pyramid

## Default Recommendation
For most new iOS apps:
- most confidence should come from unit tests
- a smaller set of confidence should come from integration tests
- only a narrow set should come from UI tests

## Unit Tests
Good targets:
- domain use cases
- pure business logic
- data mapping
- view model logic with low side effects
- formatting / validation rules

## Integration Tests
Good targets:
- repository implementations
- persistence boundaries
- networking/parsing boundaries
- auth/session transitions
- feature flag behavior that gates core flows

## UI Tests
Good targets:
- onboarding happy path
- sign-in/sign-up critical path
- purchase/paywall critical path
- app launch / routing smoke coverage

## Anti-Patterns
- excessive snapshot tests without clear value
- broad UI automation for unstable early-stage products
- duplicating the same confidence at all test layers
