# ViewModel Template — @Observable + async/await

```swift
import Foundation
import Observation

@Observable
final class /* TODO: FeatureName */ViewModel {

    // MARK: - State

    enum State {
        case idle
        case loading
        case loaded([/* TODO: ItemType */])
        case empty
    }

    private(set) var state: State = .idle
    var showError = false
    private(set) var errorMessage: String?

    // MARK: - Dependencies

    private let /* TODO: use case or repository */: /* TODO: Protocol */

    // MARK: - Init

    init(/* TODO: dependency */: /* TODO: Protocol */) {
        self./* TODO: dependency */ = /* TODO: dependency */
    }

    // MARK: - Actions

    @MainActor
    func onAppear() async {
        guard case .idle = state else { return }
        await load()
    }

    @MainActor
    func refresh() async {
        await load()
    }

    @MainActor
    private func load() async {
        state = .loading
        do {
            let items = try await /* TODO: use case/repository */.execute()
            state = items.isEmpty ? .empty : .loaded(items)
        } catch {
            errorMessage = error.localizedDescription
            showError = true
            // Restore previous state or show empty
            if case .loaded = state { return }
            state = .empty
        }
    }

    // MARK: - User Actions

    @MainActor
    func didTapItem(_ item: /* TODO: ItemType */) {
        // TODO: handle navigation or action
    }
}
```

## Usage Notes
- Replace all `/* TODO: ... */` markers.
- `@Observable` requires iOS 17+ / Swift 5.9+.
- All state mutations are `@MainActor` — no manual `DispatchQueue.main` needed.
- Keep the ViewModel free of UIKit/SwiftUI imports (only `Foundation` + `Observation`).
- Error handling restores previous state when possible — no silent failures.
- Dependencies are injected via init for testability.
