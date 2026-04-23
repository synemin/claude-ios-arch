# /ios-app-bootstrap

## Intent
Use when the user wants to design or start a new iOS app with a low-debt baseline.

## Agent Workflow
1. Clarify only the minimum needed constraints:
   - product type
   - team size / skill mix
   - expected scale or complexity
   - platform scope (iOS-only or cross-platform adjacent)
2. Recommend a default baseline unless constraints clearly override it.
3. Produce:
   - architecture baseline
   - technology selection
   - directory structure
   - dependency direction
   - debt guardrails
   - phased evolution plan
4. Call out explicit trade-offs and likely failure modes.
5. If asked, provide code skeletons next.

## Default Output Sections
- Assumptions
- Recommended stack
- Directory structure
- Data/state flow
- Day-1 infrastructure
- Debt prevention rules
- Next implementation steps
