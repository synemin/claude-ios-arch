# Golden Example: Library Selection

## Problem Summary
The team is considering Alamofire for a growing iOS app with token refresh, retries, and multipart upload requirements.

## Detected Project State
- state: bootstrap-in-progress
- why: the app foundation exists and networking needs are becoming more complex, but the architecture is still flexible.

## Official Baseline Evaluation
- URLSession remains the default baseline
- current complexity is moderate: retries, auth refresh, and multipart upload are now recurring, not hypothetical

## Options Considered
- keep URLSession with a stronger internal client abstraction
- adopt Alamofire
- keep current mixed ad-hoc request code (rejected)

## Recommendation
Adopt Alamofire only if the team wants to standardize request pipelines quickly and accepts the dependency cost. Otherwise, a stronger internal URLSession client is still viable.

## Trade-offs
- URLSession keeps lock-in low but requires more internal infrastructure effort
- Alamofire lowers implementation friction for repeated networking concerns but adds dependency surface

## Replacement / Exit Trigger
If networking complexity later stabilizes or the dependency stops pulling its weight, reevaluate whether custom URLSession infrastructure is enough.
