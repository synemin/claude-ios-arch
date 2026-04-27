# /ios-testing-strategy

## Intent
Use when the user wants a practical testing strategy for a new or existing iOS app, feature, or architecture.

## Default Mode
Development workflow. High automation is acceptable.

## Typical Questions
- What should we test first?
- Unit vs integration vs UI tests?
- What is enough testing for an MVP?
- How do we test SwiftUI features without over-investing?

## Agent Workflow
1. Detect current project state and risk profile.
2. Identify critical business flows and failure surfaces.
3. Separate domain logic, integration boundaries, and UI-critical paths.
4. Apply the testing scorecard.
5. Recommend the smallest testing strategy that protects delivery.
6. Call out what not to test yet.

## Output Format
- context assumptions
- detected project state and risk profile
- testing priorities
- unit-test targets
- integration-test targets
- UI-test targets
- what to defer
- rollout recommendation
