# /ios-app-bootstrap

## Intent
Use when the user wants to design or start a new iOS app with a low-debt baseline.

## Agent Workflow
1. Detect current project state first.
2. Clarify only the minimum needed constraints:
   - product type
   - team size / skill mix
   - expected scale or complexity
   - platform scope (iOS-only or cross-platform adjacent)
   - release urgency
3. Recommend a default baseline unless constraints clearly override it.
4. Produce:
   - architecture baseline
   - technology selection
   - directory structure
   - dependency direction
   - debt guardrails
   - phased evolution plan
5. Call out explicit trade-offs and likely failure modes.
6. If asked, provide code skeletons next.

## Default Output Sections
- Assumptions
- Detected project state and constraints
- Recommended stack
- Directory structure
- Data/state flow
- Day-1 infrastructure
- Debt prevention rules
- Evolution path
- Next implementation steps
