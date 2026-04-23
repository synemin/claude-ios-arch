# iOS Debt Repayment Model

Use this model when reporting or accepting technical debt.

## Debt Record Shape
For each debt item, capture:
- name
- current shortcut
- why it exists
- risk if left alone
- repayment trigger
- smallest safe repayment path

## Repayment Trigger Examples
- third meaningful repetition
- repeated production bugs in same area
- onboarding confusion for new contributors
- feature delivery blocked by current structure
- inability to test critical logic without pain
- release risk grows because observability is weak

## Repayment Strategy
Prefer:
1. containment
2. local cleanup
3. boundary repair
4. selective refactor
5. rewrite only when evidence is overwhelming
