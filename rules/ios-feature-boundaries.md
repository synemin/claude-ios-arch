# iOS Feature Boundary Rules

Use these rules when designing or reviewing individual iOS features.

## Ownership Rules
- A feature should own its user flow, presentation state, domain use cases, repository boundary, and analytics/error surface.
- Do not let one repository absorb unrelated feature concerns.
- Do not extract shared code just because two features look similar once.

## Presentation Rules
- Views should render state and emit user intents.
- View models should coordinate state and invoke use cases.
- Do not let view models become god objects with networking, persistence, analytics, and navigation all mixed together.

## Domain Rules
- Keep business rules in use cases or domain services.
- Keep feature models meaningful to the business, not just shaped like DTOs.

## Data Rules
- DTOs stay in data.
- Mapping must be explicit.
- Remote/local integration stays behind repository implementations.

## Feature Growth Heuristic
When a feature grows too large, split by user flow or bounded responsibility, not by arbitrary technical categories.
