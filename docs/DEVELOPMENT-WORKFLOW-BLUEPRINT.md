# Development Workflow Blueprint

This document defines the **development workflow** as the primary automation core of the plugin.

## Principle
Development is not a single action. It is a set of linked sub-workflows that should work for:
- greenfield iOS apps
- existing iOS projects adopted midway
- solo builders
- dedicated iOS developers
- senior/staff engineers

## Development Sub-Workflows
1. **App Bootstrap**
2. **Existing Project Adoption**
3. **Architecture Evolution**
4. **Feature Delivery**
5. **Engineering Quality**
6. **Tooling / Pattern Fit**
7. **Environment / Version Audit**

---

## 1. App Bootstrap
### Use when
- starting a new iOS app
- defining the initial engineering baseline

### Main questions
- what architecture direction fits the current stage?
- what directory structure should exist from day 1?
- what baseline infra should be present?

### Typical outputs
- architecture brief
- project skeleton
- day-1 checklist
- first vertical slice plan

### Default bias
- SwiftUI first
- async/await first
- feature-first structure
- light layering
- strong observability

---

## 2. Existing Project Adoption
### Use when
- the plugin is introduced into an ongoing iOS project
- architecture and tooling choices already exist
- the team wants to improve without rewriting everything

### Main questions
- what architecture exists today?
- what is structurally risky vs acceptable for now?
- what should be preserved, contained, or migrated?
- what is the smallest high-leverage improvement sequence?

### Typical outputs
- current-state summary
- risk map
- migration priorities
- debt containment plan
- environment/toolchain snapshot

### Default bias
- do not recommend broad rewrites by default
- preserve working flows unless evidence says otherwise
- prefer incremental adoption of rules, tests, and guardrails

---

## 3. Architecture Evolution
### Use when
- an app is moving from MVP to PMF or from PMF to scale
- current architecture no longer matches delivery needs

### Main questions
- what should evolve now?
- what should not evolve yet?
- when is modularization justified?
- when should stronger state management or infra be adopted?

### Typical outputs
- current stage assessment
- evolution recommendation
- change-now vs later-now split
- migration sequence

---

## 4. Feature Delivery
### Use when
- adding or reshaping a feature

### Main questions
- how should the feature be decomposed?
- how should state, domain logic, and data boundaries flow?
- what is the first safe slice?

### Typical outputs
- feature brief
- layer responsibilities
- state/data flow
- first implementation slice

---

## 5. Engineering Quality
### Use when
- improving confidence, review quality, and debt control

### Main questions
- what should be tested?
- how severe are current review findings?
- what debt must be repaid now vs later?

### Typical outputs
- testing plan
- review severity report
- debt report with repayment triggers

---

## 6. Tooling / Pattern Fit
### Use when
- considering tooling or architecture patterns

### Main questions
- which tools solve current pain without excess complexity?
- which patterns fit current product and team stage?
- what is premature?

### Typical outputs
- tooling decision memo
- pattern-fit recommendation
- migration / rollback notes

---

## 7. Environment / Version Audit
### Use when
- joining an existing project
- debugging toolchain drift
- validating readiness for development, CI, or release

### Main questions
- what Xcode / Swift / iOS SDK / package / project-generation tool versions are in use?
- is the environment reproducible?
- are there obvious version or toolchain mismatches?
- what should be standardized first?

### Typical outputs
- environment snapshot
- version drift findings
- critical compatibility risks
- standardization recommendations

### Typical scope
- Xcode version
- Swift language version
- iOS deployment target
- Swift Package dependencies
- CocoaPods / Carthage if present
- Tuist / XcodeGen if present
- lint / formatting / CI tool versions

---

## Agent Requirement
The plugin must remain useful at **any project state**:
- idea stage
- new app bootstrap
- active MVP
- messy growing project
- mature project needing review
- pre-release stabilization

Do not assume greenfield by default.
When the project already exists, prefer **adopt / assess / improve** over **replace / restart**.

## Environment Requirement
The plugin must also remain useful across different environment states:
- older or newer Xcode versions
- different Swift language versions
- varied iOS deployment targets
- SwiftPM / CocoaPods / Carthage / mixed dependency setups
- Tuist / XcodeGen / plain Xcode projects
- solo local development or team/CI setups

Environment and toolchain reality should be treated as first-class context, not an afterthought.
