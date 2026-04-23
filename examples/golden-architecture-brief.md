# Golden Example: Architecture Brief

## Assumptions
- Product: AI-assisted journaling app
- Team: 1 iOS engineer, 1 backend engineer
- Complexity: early-stage but likely to evolve quickly in onboarding, sync, and AI features
- Timeline: MVP in 6-8 weeks

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
