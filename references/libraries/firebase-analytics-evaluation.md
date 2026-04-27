# Firebase Analytics Evaluation

Status: draft
Last reviewed: 2026-04-24
Confidence: low

## Official sources
- https://firebase.google.com/docs/analytics
- https://github.com/firebase/firebase-ios-sdk

## Default recommendation
Adopt Firebase Analytics only when product analytics needs are real and the team is comfortable with Firebase ecosystem trade-offs. Do not add analytics SDKs just because instrumentation feels “professional”.

## Use when
- activation / retention / conversion analysis matters now
- the team needs a practical hosted analytics baseline quickly

## Avoid when
- there is no clear event model yet
- the app is too early for analytics complexity
- privacy and dependency concerns outweigh current value

## Related skills
- ios-tooling-decision
- ios-release-operations
- ios-library-selection
