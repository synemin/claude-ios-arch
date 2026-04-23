# iOS Feature Patterns

## Feature Boundary Principle
Each feature should be understandable in isolation.

A feature should own:
- its user flow
- its presentation state
- its domain use cases
- its repository boundary
- its analytics/error surface

## Layer Split
### Presentation
Owns:
- views
- view models / presenters
- UI state
- navigation events

Should not own:
- API details
- persistence details
- business rules beyond presentation logic

### Domain
Owns:
- feature models with business meaning
- use cases
- repository contracts
- business rules

### Data
Owns:
- DTOs
- API / local storage integration
- mapping
- repository implementation

## First Slice Heuristic
For a new feature, prefer one thin vertical slice:
- one visible screen or user flow
- one use case
- one repository boundary
- one success path
- one analytics event set
- one error path

## Common Risks
- view model becomes a god object
- repository mixes unrelated feature concerns
- DTOs leak into UI
- analytics added too late
- cross-feature shared code extracted too early
