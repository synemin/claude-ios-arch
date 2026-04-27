# Golden Example: Release Operations Checklist

## Current Release Stage
TestFlight hardening before external beta.

## Detected Project State
- state: pre-release-hardening
- why: core flows exist, feature scope is mostly set, and the main priority is stability, compliance, and observability rather than architecture ambition.

## Release Risk Profile
- onboarding and auth are stable enough for beta
- sync and notifications still need failure visibility
- metadata and permission explanations need review

## Readiness Gaps
- crash reporting is not yet verified in staging
- analytics coverage on activation funnel is incomplete
- one permission rationale screen needs clearer copy

## Policy / Compliance Watchouts
- check notification permission timing and wording
- ensure privacy usage strings match actual behavior
- verify beta notes clearly explain unstable areas

## Observability / Crash Readiness
- confirm crash reporting pipeline works end to end
- log sync failures with enough context for triage
- track funnel events for onboarding completion and first save

## Launch Checklist
- validate onboarding, auth, first save, sync, notification prompt
- verify analytics and crash reporting in staging build
- confirm App Store / TestFlight metadata is complete
- confirm rollback / hotfix owner and path

## Post-Launch Monitoring Focus
- onboarding drop-off
- first-save failure rate
- sync error rate
- crash-free sessions on key flows

## Immediate Actions
1. verify crash pipeline in staging
2. add missing funnel events
3. review permission copy and metadata before external beta
