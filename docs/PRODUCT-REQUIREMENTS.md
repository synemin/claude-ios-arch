# Product Requirements

## Product Name
claude-ios-arch

## Product Vision
Build a **state-aware, delivery-oriented app development plugin** that any user can install into a compatible coding agent so the agent can help build real apps from any project state.

## Long-Term Goal
Support **app development across iOS and Android**.

## Phase 1 Goal
Deliver an **iOS-first plugin** that can:
- start from no project / greenfield
- adopt partially-built projects
- continue feature development in existing apps
- review and repair architecture drift
- make context-aware technical choices
- evolve the architecture over time without unnecessary rewrites
- prefer official platform capabilities by default
- stay aligned with official documentation through a repeatable refresh workflow

## Core Problem
Most agent plugins can give advice, but they cannot reliably determine the **current project state**, choose the **right level of architecture**, and make **context-aware implementation decisions** that stay aligned with official platform guidance.

This plugin should not just provide opinions. It should provide a **decision system** that helps an agent make good choices repeatedly.

## Target Users
- solo builders shipping iOS apps
- staff/principal mobile engineers
- experienced app developers who want strong default patterns
- coding agents that need structured iOS delivery knowledge

## Primary User Promise
After installing this plugin, a user should be able to ask the agent to work on an iOS app at almost any stage, and the agent should:
1. identify the project state,
2. understand constraints,
3. choose a context-appropriate technical approach,
4. implement or plan changes with low debt,
5. explain trade-offs,
6. preserve a clean evolution path.

## Product Principles
1. **State-aware before solution-aware** — detect project state first.
2. **Official sources first** — prefer Apple / Swift / official library documentation.
3. **Context-optimal over abstract best practice** — choose what is right for this app, team, and stage.
4. **Delivery-oriented** — optimize for real progress, not only elegant advice.
5. **Incremental evolution over rewrites** — refactor safely and in steps.
6. **Low debt by default** — make debt explicit and repayable.
7. **Host-portable core** — keep durable knowledge independent of a single agent host.

## Functional Requirements
### FR-1 Project State Detection
The plugin must classify a project into a meaningful working state before making major recommendations.

### FR-2 Constraint Extraction
The plugin must identify constraints such as:
- deployment target
- team size / skill mix
- release urgency
- current architecture maturity
- existing library lock-in
- test coverage and safety level
- performance / offline / realtime constraints

### FR-3 Context-Aware Technical Selection
The plugin must select or recommend:
- UI architecture
- state model
- navigation pattern
- networking stack
- persistence strategy
- DI approach
- testing strategy
- observability baseline
- third-party libraries only when justified

### FR-4 Existing Project Adoption
The plugin must be able to start work in an existing codebase without requiring a full rewrite.

### FR-5 Feature Delivery
The plugin must support feature-level delivery in both clean and messy repositories.

### FR-6 Architecture Evolution
The plugin must detect when the current architecture no longer fits and propose the smallest safe upgrade path.

### FR-7 Official-Source Knowledge Layer
The plugin must maintain references distilled from official documentation and use them as the factual basis for recommendations.

### FR-8 Continuous Refresh Workflow
The plugin must define how references, skills, commands, and templates are refreshed when official docs change.

## Non-Goals (Phase 1)
- being a generic agent framework
- replacing product design, QA, DevOps, and business judgment entirely
- generating a complete app without user constraints or review
- supporting every iOS stack equally
- optimizing for maximum abstraction instead of clarity and speed of change
- shipping Android support before iOS-first quality is strong

## Quality Bar
A recommendation is acceptable only if it is:
- consistent with official documentation or explicitly justified when it differs
- appropriate for the project state
- aware of migration cost
- low in accidental complexity
- compatible with incremental delivery
- explicit about trade-offs

## Knowledge System
The plugin should separate:
- **references/** → distilled facts from official documentation
- **skills/** → decision behavior using those facts
- **commands/** → task workflows
- **templates/** → output shapes
- **workflows/** → update and audit processes

## Update Contract
When an official source changes:
1. update the affected reference,
2. identify impacted skills / commands / templates,
3. update decision logic if the recommendation changed,
4. record freshness metadata.

## Success Criteria for Phase 1
The plugin can reliably help with:
- greenfield bootstrap
- existing-project adoption
- feature implementation planning
- iOS technical choice guidance
- architecture review
- debt detection
- architecture evolution planning
- release preparation guidance

## Acceptance Lens for Future Review
When reviewing this repository, ask:
1. Can it detect project state?
2. Can it make context-aware choices instead of static recommendations?
3. Does it prefer official sources and encode them well?
4. Can it work from messy real-world codebases?
5. Can it evolve projects incrementally?
6. Can it keep itself fresh when official docs move?
