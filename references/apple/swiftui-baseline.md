# SwiftUI Baseline

Status: draft
Last reviewed: 2026-04-23
Confidence: medium

## Official sources
- https://developer.apple.com/documentation/swiftui

## Default recommendation
Prefer SwiftUI as the default UI architecture for new iOS work unless there is a strong constraint that pushes toward UIKit or mixed integration.

## Use when
- greenfield app
- modern iOS deployment targets
- feature-first app architecture
- small to medium teams prioritizing speed of iteration

## Avoid / not ideal when
- heavy reliance on complex legacy UIKit flows
- strong dependency on UIKit-only infrastructure that would create high migration cost

## Trade-offs
SwiftUI improves iteration speed and composability but still requires discipline around state ownership, side effects, navigation, and interop boundaries.

## Related skills
- ios-app-bootstrap
- ios-tech-decision
- ios-feature-bootstrap
