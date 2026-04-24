# Research Workflow

## Goal
Keep this plugin aligned with official sources while remaining resilient when one retrieval path is blocked.

## Source Policy
Always prefer:
1. Apple official documentation
2. Swift.org official documentation
3. Apple WWDC sessions / official sample code
4. Official library docs, official GitHub READMEs, official migration guides, official release notes

Do not treat random blogs as the steady-state source of truth.

## Default Research Posture
Use a **repeatable official-source-first workflow**.

Prefer:
- stable, scriptable retrieval for routine refresh work
- alternative official sources for the same product when one source is unavailable
- reproducible updates that can be reviewed and repeated later

## Practical Rule
For this repo, the preferred order is:
1. official source via the normal retrieval path
2. official source via another viable retrieval method
3. another official source for the same product

Do not jump to non-official articles just because one access path failed.

## What To Capture In References
When updating a reference, record:
- what changed in the official baseline
- whether the recommendation changed
- what project states are affected
- which skills / commands / scorecards need regeneration
- `Last reviewed` and `Confidence`

## Review Standard
A reference refresh is successful when it leaves the repo with:
- clearer provenance
- updated baseline guidance
- explicit trade-offs
- minimal drift between references, skills, commands, and examples
