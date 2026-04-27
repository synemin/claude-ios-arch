# SwiftGen Evaluation

Status: draft
Last reviewed: 2026-04-24
Confidence: low

## Official sources
- https://github.com/SwiftGen/SwiftGen
- https://swiftpackageindex.com/SwiftGen/SwiftGen

## Default recommendation
Do not add SwiftGen unless asset / string / resource access is already causing consistency or safety pain worth solving with generation.

## Use when
- resource access errors are recurring
- localization / asset usage is broad enough to justify generation
- the team wants type-safe access for assets, strings, fonts, files, or similar resource surfaces

## Avoid when
- small app with light resource surface
- the team cannot afford another generation tool in the workflow
- customization and generation-template ownership would outweigh current benefit

## Official repository signal
The official README frames SwiftGen as a type-safe resource-code generator covering assets, strings, fonts, plists, files, and more, with customizable templates. That flexibility is valuable, but it also means teams inherit generation workflow and template ownership.

## Related skills
- ios-tooling-decision
- ios-library-selection
