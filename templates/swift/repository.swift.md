# Repository Template — Protocol + Implementation

```swift
import Foundation

// MARK: - Protocol

protocol /* TODO: FeatureName */Repository: Sendable {
    func fetch() async throws -> [/* TODO: DomainModel */]
    func fetchById(_ id: /* TODO: IDType */) async throws -> /* TODO: DomainModel */
    // TODO: add mutation methods if needed
    // func save(_ item: /* TODO: DomainModel */) async throws
    // func delete(_ id: /* TODO: IDType */) async throws
}

// MARK: - Implementation

final class /* TODO: FeatureName */RepositoryImpl: /* TODO: FeatureName */Repository {

    private let networkService: /* TODO: NetworkServiceProtocol */
    // private let cache: /* TODO: CacheProtocol — optional */

    init(networkService: /* TODO: NetworkServiceProtocol */) {
        self.networkService = networkService
    }

    func fetch() async throws -> [/* TODO: DomainModel */] {
        let dtos = try await networkService.request(
            /* TODO: endpoint */
            responseType: [/* TODO: DTO */].self
        )
        return dtos.map { $0.toDomain() }
    }

    func fetchById(_ id: /* TODO: IDType */) async throws -> /* TODO: DomainModel */ {
        let dto = try await networkService.request(
            /* TODO: endpoint with id */
            responseType: /* TODO: DTO */.self
        )
        return dto.toDomain()
    }
}

// MARK: - DTO → Domain Mapping

private extension /* TODO: DTO */ {
    func toDomain() -> /* TODO: DomainModel */ {
        .init(
            // TODO: map fields
        )
    }
}
```

## Usage Notes
- Replace all `/* TODO: ... */` markers.
- The protocol is the contract — view models and use cases depend on the protocol, never the impl.
- DTOs stay in the data layer; domain models cross layer boundaries.
- Mark the protocol `Sendable` for Swift 6 concurrency safety.
- Add caching as a second data source when needed, not upfront.
