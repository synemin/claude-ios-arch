# /ios-feature-bootstrap

## Intent
Use when the user wants to add or design a new feature inside an iOS app with clean boundaries and low accidental complexity.

## Typical Inputs
- feature name
- user flow / core use case
- data sources
- whether the feature is read-only, transactional, or stateful

## Agent Workflow
1. Clarify the feature goal and core user flow.
2. Identify presentation, domain, and data responsibilities.
3. Propose a feature-local directory structure.
4. Define models, use cases, repositories, and side-effect boundaries.
5. Identify observability requirements: logging, analytics, errors.
6. Recommend the smallest viable implementation slice.

## Output Format
- Feature summary
- Responsibilities by layer
- Suggested file/module structure
- State/data flow
- Risks and guardrails
- First implementation slice
