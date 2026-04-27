# /ios-architecture-evolution

## Intent
Use when the current iOS architecture no longer fits the product, team, or codebase reality and a safe evolution path is needed.

## Agent Workflow
1. Detect current project state and pain signals.
2. Identify the smallest structural upgrade with clear leverage.
3. Separate urgent fixes from later cleanup.
4. Propose an incremental migration sequence with rollback awareness.
5. Call out what should not be changed yet.

## Output Format
- Current mismatch summary
- Upgrade triggers
- Recommended target shape
- Migration seams
- Do now / later / avoid
