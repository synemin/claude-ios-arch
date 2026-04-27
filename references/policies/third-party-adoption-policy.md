# Third-Party Adoption Policy

## Default Bias
Prefer official platform capabilities first.

## Only Introduce a Third-Party Library When
- the official baseline is meaningfully insufficient for the current constraints,
- the library reduces net complexity instead of increasing it,
- migration / lock-in cost is understood,
- maintenance health is acceptable,
- the team can realistically support it.

## Required Evaluation Dimensions
- official baseline sufficiency
- complexity reduction
- maintenance health
- API stability
- migration cost
- debugging cost
- testing impact
- future replacement risk

## Output Requirement
When recommending a third-party library, always include:
- why the official baseline is not enough,
- why this library is preferred over alternatives,
- when to avoid it,
- what would trigger future replacement.
