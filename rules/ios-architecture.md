# iOS Architecture Rules

Use these rules when designing, reviewing, or generating structure for a new iOS app.

## 1. Boundary Rules
- Do not put networking, persistence, or business rules directly inside SwiftUI Views or UIKit view controllers.
- Do not allow API DTOs to cross into presentation unchanged.
- Keep business rules in domain/use-case logic, not in navigation code.
- Keep dependencies directional: Presentation -> Domain -> Data implementation -> Core infrastructure.

## 2. Feature Organization Rules
- Organize by feature first; layer inside each feature.
- Keep feature directories self-contained where possible.
- Move code into `Shared` only after stable reuse is proven.
- Treat `Shared`, `Helpers`, and `Utils` as high-risk areas requiring justification.

## 3. Abstraction Rules
- Prefer concrete code over speculative abstraction.
- Apply the third-use rule before extracting generalized abstractions unless the user explicitly wants a framework-level reusable primitive.
- Avoid premature modularization in greenfield apps.
- Avoid architecture patterns whose complexity exceeds the current product complexity.

## 4. State and Side-Effect Rules
- Keep UI state close to the feature.
- Keep cross-feature global state minimal and explicit.
- Isolate side effects behind injected collaborators or use cases.
- Keep navigation, analytics, network, and storage as explicit side effects.

## 5. Dependency Rules
- Default to initializer injection.
- Avoid service locators.
- Avoid heavy DI containers unless there is a concrete scaling need.
- Favor protocols at boundaries, not everywhere.

## 6. Naming Rules
- Avoid vague names like `Manager`, `Helper`, or `Util` unless the responsibility is singular and obvious.
- Prefer names that encode intent: `LoginUseCase`, `ProfileRepository`, `SessionStore`, `AppRouter`.

## 7. Review Questions
For every architecture recommendation, answer:
1. What current problem does this solve?
2. What future change does this preserve optionality for?
3. What complexity cost does it add?
4. Can most of the team understand and maintain it?
5. How will failures be observed and debugged?
