# /ios-debt-check

## Intent
Use when the user wants a debt-oriented review of a new or existing iOS app.

## Agent Workflow
1. Search for accidental complexity and hidden debt sources.
2. Look especially for:
   - fat managers
   - DTO leakage
   - view-layer side effects
   - global singleton sprawl
   - uncontrolled shared/common folders
   - premature modularization
   - absent observability
3. For each debt item, report:
   - issue
   - risk
   - urgency
   - suggested repayment or containment
4. Distinguish acceptable tactical debt from harmful structural debt.

## Output Format
- Structural debt
- Tactical debt
- Missing guardrails
- Recommended repayment plan
