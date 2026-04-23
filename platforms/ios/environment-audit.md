# iOS Environment Audit Guide

## Audit Targets
- Xcode version
- Swift version
- iOS SDK and deployment target
- Package.swift / Package.resolved
- Podfile / Podfile.lock if present
- Cartfile if present
- Tuist / XcodeGen config if present
- lint/format/test tool declarations
- CI configuration references to Xcode or simulators

## Questions To Answer
- Is the environment reproducible?
- Are versions pinned where they should be?
- Is there obvious drift between local/dev/CI expectations?
- Are there tools in use that the team does not actually need?

## Output Bias
- facts first
- risks second
- standardization steps third
