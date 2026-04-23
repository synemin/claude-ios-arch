# iOS Engineering Quality Rules

Use these rules during development-oriented workflows.

## Testing Rules
- Recommend tests based on risk, not ideology.
- Default to unit tests for business logic.
- Keep UI tests limited to critical stable flows.
- Avoid recommending large UI suites for early-stage apps without justification.

## Review Rules
- Classify issues by severity: structural risk, maintainability drag, optional refinement.
- Do not collapse all findings into one flat list.
- Prefer incremental fixes over broad rewrites.

## Debt Rules
- Every debt item should have a trigger for repayment.
- Prefer containment and boundary repair before rewrite advice.
- Do not recommend “clean it up later” without naming the trigger.

## Delivery Rules
- Protect developer throughput.
- Do not recommend ceremonies whose cost exceeds the risk they address.
