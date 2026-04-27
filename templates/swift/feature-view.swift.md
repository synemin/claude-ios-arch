# Feature View Template — SwiftUI + @Observable

```swift
import SwiftUI

struct /* TODO: FeatureName */View: View {
    @State private var viewModel: /* TODO: FeatureName */ViewModel

    init(viewModel: /* TODO: FeatureName */ViewModel) {
        self._viewModel = State(initialValue: viewModel)
    }

    var body: some View {
        content
            .navigationTitle("/* TODO: title */")
            .task { await viewModel.onAppear() }
            .alert(
                "Error",
                isPresented: $viewModel.showError,
                presenting: viewModel.errorMessage
            ) { _ in
                Button("OK", role: .cancel) {}
            } message: { message in
                Text(message)
            }
    }

    @ViewBuilder
    private var content: some View {
        switch viewModel.state {
        case .idle:
            Color.clear

        case .loading:
            ProgressView()
                .frame(maxWidth: .infinity, maxHeight: .infinity)

        case .loaded(let items):
            ScrollView {
                LazyVStack(spacing: 12) {
                    ForEach(items) { item in
                        // TODO: row view
                        Text(item.id)
                    }
                }
                .padding()
            }
            .refreshable { await viewModel.refresh() }

        case .empty:
            ContentUnavailableView(
                "/* TODO: empty title */",
                systemImage: "/* TODO: SF Symbol */",
                description: Text("/* TODO: empty message */")
            )
        }
    }
}

#Preview {
    NavigationStack {
        // TODO: inject preview dependencies
        /* TODO: FeatureName */View(
            viewModel: .init(/* TODO: dependencies */)
        )
    }
}
```

## Usage Notes
- Replace all `/* TODO: ... */` markers with your specifics.
- The view owns no business logic — delegate everything to the ViewModel.
- Use `@State` for `@Observable` view models (iOS 17+).
- Add `@Environment` properties for shared app-level state if needed.
