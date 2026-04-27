# /ios-arch-review

## Intent
Use when reviewing an existing iOS architecture, PR, directory structure, or technology choice.

## Agent Workflow
1. Detect current project state and operating constraints.
2. Identify current architecture pattern and delivery reality.
3. Evaluate against:
   - boundary clarity
   - state flow clarity
   - dependency direction
   - observability
   - team cognitive load
   - debt hotspots
   - migration feasibility
4. Classify issues by severity:
   - structural risk
   - maintainability drag
   - stylistic / optional
5. Recommend fixes in priority order.
6. Prefer incremental refactors over “rewrite everything” advice.
7. If needed, identify architecture evolution triggers.

## Output Format
- Current pattern summary
- Detected project state and why
- Top 3 architecture risks
- What to keep
- What to change now
- What to postpone
- Suggested migration sequence
