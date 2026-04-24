# Workflow Model

This plugin follows a **three-part workflow model** for app development:

1. **需求 (Discovery / Product Definition)**
2. **开发 (Development / Delivery)**
3. **发布运营 (Release & Operations / Post-launch)**

## Design Principle
The plugin should support both:
- professional developers who want agent help that matches engineering best practices
- solo builders / one-person companies who still need help getting an app shipped to the App Store

## Core Decision Principle
The plugin should be **state-aware before solution-aware**.

That means the agent should usually:
1. detect project state,
2. extract constraints,
3. check official-source references,
4. apply the right scorecard,
5. recommend the smallest context-appropriate next move.

## Automation Policy
### 1. 需求 / Discovery
Default mode: **manual trigger**

Why:
- requires user judgment
- requires product prioritization
- requires business/context decisions
- should not be over-automated by default

Typical tasks:
- problem framing
- MVP scoping
- user flow definition
- risk discovery
- App Store / policy feasibility checks

### 2. 开发 / Development
Default mode: **agent-driven / highest automation**

Why:
- architecture, decomposition, technical decisions, feature bootstrap, project adoption, reviews, and debt checks are the plugin’s strongest domain
- this is the main leverage area for engineering productivity

Typical tasks:
- project state detection
- architecture design
- stack selection
- project bootstrap
- existing-project adoption
- feature bootstrap
- implementation planning
- architecture review
- debt check
- architecture evolution
- library selection

### 3. 发布运营 / Release & Operations
Default mode: **manual trigger**

Why:
- involves release judgment, App Store metadata, policy/compliance, business operations, and post-launch monitoring
- should be user-in-the-loop by default

Typical tasks:
- TestFlight readiness
- release checklist
- App Store listing preparation
- submission readiness
- launch monitoring
- post-launch iteration checks

## Product Goal Alignment
This workflow split is intended to make the plugin useful for:
- staff/principal/mobile engineers
- startups with a dedicated developer
- solo founders / one-person companies shipping iOS apps

## Agent Behavior
- Bias strongly toward automation in **development** workflows.
- Treat **discovery** and **release-operations** as assisted workflows unless the user explicitly asks for deeper automation.
- Preserve best practices, observability, and debt discipline across all three.
- Prefer official platform capabilities before third-party libraries unless the current constraints justify deviation.
- Prefer incremental evolution over rewrites.
- Prefer repeatable official-source refresh methods and alternate official sources before non-official material.
