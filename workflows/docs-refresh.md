# Docs Refresh Workflow

## Goal
Refresh official-source references before knowledge drift becomes harmful.

## Inputs
- `../references/registry.json`
- the current reference files
- current date / last-reviewed metadata

## Steps
1. Select due sources by priority and review cadence.
2. Revisit official documentation only.
3. Prefer repeatable retrieval paths for routine updates.
4. If the default retrieval path is blocked by environment or network policy, use another viable official retrieval method such as `../scripts/fetch_official_source.py`.
5. If one official source remains inaccessible, switch to another official source for the same product instead of falling back to blogs.
6. Identify whether baseline recommendations changed.
7. Update the affected references.
8. List impacted skills / commands / templates.
9. Trigger follow-up skill regeneration only when recommendations changed.

## Output
- refresh summary
- updated references
- impacted assets list
