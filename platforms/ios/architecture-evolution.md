# iOS Architecture Evolution

## Goal
Upgrade architecture only when the current shape no longer matches the product or team reality.

## Upgrade Triggers
- repeated cross-feature coupling
- unclear dependency direction
- networking / persistence complexity outgrowing the current baseline
- state ownership confusion causing defects
- release quality suffering from structural debt

## Default Rule
Prefer the **smallest safe upgrade** over the most impressive redesign.

## Evolution Questions
- what pain is recurring?
- what is the smallest structural fix?
- what would we postpone?
- what migration seam keeps delivery moving?

## Typical Evolutions
- add clearer feature boundaries
- introduce mapping boundaries between DTO / domain / UI models
- centralize bootstrap / composition root
- standardize navigation ownership
- tighten testing seams before bigger refactors
