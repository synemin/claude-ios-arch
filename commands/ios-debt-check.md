# /ios-debt-check

## Intent
Use when the user wants a debt-oriented review of a new or existing iOS app.

## Agent Workflow
1. Detect current project state.
2. Search for accidental complexity and hidden debt sources.
3. Look especially for:
   - fat managers
   - DTO leakage
   - view-layer side effects
   - global singleton sprawl
   - uncontrolled shared/common folders
   - premature modularization
   - absent observability
4. For each debt item, report:
   - issue
   - risk
   - urgency
   - suggested repayment or containment
5. Distinguish acceptable tactical debt from harmful structural debt.

## Output Format
- detected project state and why
- Structural debt
- Tactical debt
- Missing guardrails
- Recommended repayment plan
- What can wait safely
