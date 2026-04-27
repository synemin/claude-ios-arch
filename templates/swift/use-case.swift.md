# Use Case Template — Single Responsibility

```swift
import Foundation

// MARK: - Protocol

protocol /* TODO: ActionName */UseCase: Sendable {
    func execute(/* TODO: input params */) async throws -> /* TODO: OutputType */
}

// MARK: - Implementation

final class /* TODO: ActionName */UseCaseImpl: /* TODO: ActionName */UseCase {

    private let repository: /* TODO: RepositoryProtocol */
    // private let analyticsService: AnalyticsService — optional

    init(repository: /* TODO: RepositoryProtocol */) {
        self.repository = repository
    }

    func execute(/* TODO: input params */) async throws -> /* TODO: OutputType */ {
        // TODO: business logic
        //
        // Examples of what belongs here:
        // - Validation rules
        // - Combining data from multiple repositories
        // - Domain transformations
        // - Business rule enforcement
        // - Side effects (analytics, logging)
        //
        // What does NOT belong here:
        // - UI formatting
        // - Navigation decisions
        // - Network/persistence details

        let rawData = try await repository.fetch()

        // TODO: apply business rules, filter, transform
        let result = rawData

        return result
    }
}
```

## Usage Notes
- Replace all `/* TODO: ... */` markers.
- One use case = one action. Name it after what it does: `FetchUserProfileUseCase`, `SubmitOrderUseCase`.
- Use cases orchestrate repositories and apply business rules.
- If the use case is just a pass-through to a single repository method, skip it — call the repository directly.
- Keep use cases stateless. State belongs in the ViewModel.
- Mark protocol `Sendable` for Swift 6 safety.
