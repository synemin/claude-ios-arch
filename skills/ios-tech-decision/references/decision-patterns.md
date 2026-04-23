# Decision Patterns

## Default Decision Pattern
Use this shape for most iOS tech choices:
1. default pick
2. why it wins now
3. when it breaks down
4. migration cost if wrong
5. confidence level

## Examples
### SwiftUI vs UIKit
- Default: SwiftUI
- Deviation: advanced text input, difficult layouts, strategic UIKit reuse, known hotspots

### async/await vs Combine
- Default: async/await
- Deviation: genuine stream-heavy reactive problems or strong existing Combine fluency

### MVVM vs TCA
- Default: lightweight MVVM-ish state handling
- Deviation: unusually complex state machines, strong effect modeling needs, strong TCA team fluency
