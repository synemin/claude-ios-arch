# iOS Tool Categories

## Hygiene Tools
Examples:
- SwiftLint
- formatting tools

Use when:
- code consistency and review hygiene matter
- team size is growing
- style debates are wasting time

## Resource Safety / Codegen Tools
Examples:
- SwiftGen

Use when:
- asset, localization, or resource access is stringly typed and error-prone
- resource surface is growing enough to justify codegen

## Project Generation / Project Structure Tools
Examples:
- XcodeGen
- Tuist

Use when:
- project configuration drift is painful
- project growth is significant
- multi-target or modular complexity is becoming real

## Architecture / State Tools
Examples:
- TCA

Use when:
- state complexity is genuinely high
- effect modeling matters enough to justify added ceremony
- team fluency already exists or is worth investing in

## Testing Frameworks
Examples:
- XCTest
- Swift Testing

Use when:
- you need the right level of test authoring ergonomics and compatibility
- you want to modernize test writing without destabilizing delivery
