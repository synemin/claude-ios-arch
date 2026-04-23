# /ios-arch-review

## Intent
Use when reviewing an existing iOS architecture, PR, directory structure, or technology choice.

## Agent Workflow
1. Identify current architecture and product context.
2. Evaluate against:
   - boundary clarity
   - state flow clarity
   - dependency direction
   - observability
   - team cognitive load
   - debt hotspots
3. Classify issues by severity:
   - structural risk
   - maintainability drag
   - stylistic / optional
4. Recommend fixes in priority order.
5. Prefer incremental refactors over “rewrite everything” advice.

## Output Format
- Current pattern summary
- Top 3 architecture risks
- What to keep
- What to change now
- What to postpone
- Suggested migration sequence
