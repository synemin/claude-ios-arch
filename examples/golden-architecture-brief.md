# Golden Example: Architecture Brief

## Assumptions
- Product: AI-assisted journaling app
- Team: 1 iOS engineer, 1 backend engineer
- Complexity: early-stage but likely to evolve quickly in onboarding, sync, and AI features
- Timeline: MVP in 6-8 weeks

## Detected Project State
- state: greenfield
- why: product definition exists, but there is no meaningful app structure yet

## Constraints
- current stack: none yet
- delivery pressure: MVP in 6-8 weeks
- lock-in: none yet
- notable requirements: likely sync later, analytics needed early, AI features will increase product complexity over time

## Official Baseline
- SwiftUI-first UI
- async/await concurrency
- typed URLSession client
- feature-first structure
- explicit model boundaries

## Recommended Baseline
- SwiftUI-first UI
- async/await concurrency
- feature-first structure with light Presentation/Domain/Data split
- initializer injection
- URLSession typed client
- UserDefaults + file cache at first; avoid database complexity until clearly needed

## Tech Selection and Trade-offs
- Default to SwiftUI for velocity and state-driven UI
- Avoid TCA by default; product complexity does not yet justify the ceremony
- Avoid early modularization; keep one project with strong internal boundaries first
- Do not adopt extra networking or persistence libraries without concrete pressure

## Scorecard Notes
- state management: local + feature-owned state is sufficient
- navigation: simple app routing is enough initially
- networking: URLSession wins by default at current complexity
- persistence: lightweight storage is enough for MVP
- dependency injection: initializer injection keeps bootstrap clear without framework overhead

## Directory Structure
- App/
- Core/
- Features/
- Resources/
- Config/
- Tests/

## Dependency / Data / State Flow
- Views render state and emit intents
- ViewModels coordinate state transitions
- UseCases hold business logic
- Repository protocols sit at domain boundaries
- Data implementations handle remote/local concerns and mapping

## Day-1 Infrastructure
- analytics
- crash reporting
- logging
- feature flags
- Debug/Staging/Release config separation

## Debt Guardrails
- keep DTOs out of presentation
- keep networking out of Views
- delay abstraction until third meaningful repetition
- record shortcuts with repayment triggers

## Evolution Path
- MVP: single project, feature-first, light layering
- PMF: strengthen domain boundaries and analytics taxonomy
- Scale: selectively modularize only with evidence

## Immediate Next Steps
1. define onboarding and auth boundaries
2. implement one vertical slice end to end
3. add observability before feature count grows
