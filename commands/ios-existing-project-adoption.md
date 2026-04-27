# /ios-existing-project-adoption

## Intent
Use when the user wants to adopt this plugin into an existing iOS project that already has architecture, tooling, and delivery constraints.

## Default Mode
Development workflow. High automation is acceptable, but recommendations should favor incremental improvement over rewrites.

## Agent Workflow
1. Detect the current project state first.
2. Identify product pressure, release urgency, and safety constraints.
3. Inspect architecture, structure, dependency direction, and workflow constraints.
4. Identify what to preserve, what to contain, and what to improve first.
5. Produce an adoption / migration plan that fits current reality.
6. Explicitly call out what should not be changed yet.

## Output Format
- current-state summary
- detected project state and why
- strengths to preserve
- structural risks
- debt containment opportunities
- migration priorities
- what to postpone
- environment/toolchain notes
