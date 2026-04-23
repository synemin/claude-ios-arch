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
1. Identify product stage and team constraints.
2. Identify critical business flows and failure surfaces.
3. Separate domain logic, integration boundaries, and UI-critical paths.
4. Recommend the smallest testing strategy that protects delivery.
5. Call out what not to test yet.

## Output Format
- context assumptions
- testing priorities
- unit-test targets
- integration-test targets
- UI-test targets
- what to defer
- rollout recommendation
