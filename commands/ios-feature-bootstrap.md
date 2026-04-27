# /ios-feature-bootstrap

## Intent
Use when the user wants to add or design a new feature inside an iOS app with clean boundaries and low accidental complexity.

## Typical Inputs
- feature name
- user flow / core use case
- data sources
- whether the feature is read-only, transactional, or stateful

## Agent Workflow
1. Detect current project state and architecture constraints.
2. Clarify the feature goal and smallest useful slice.
3. Identify presentation, domain, and data responsibilities in a way that fits the current app.
4. Reuse the current navigation, state, networking, and persistence baseline unless change is justified.
5. Identify observability requirements: logging, analytics, errors.
6. Recommend the first safe implementation slice.
7. Call out architecture upgrade triggers if this feature exposes a deeper mismatch.

## Output Format
- Feature summary
- Detected project state and constraints
- Responsibilities by layer
- Suggested file/module structure
- State/data flow
- Risks and guardrails
- First implementation slice
- Upgrade triggers
