---
name: ios-environment-audit
description: Audit iOS project environments and toolchain versions. Use when checking Xcode, Swift, iOS deployment targets, dependency managers, package versions, project-generation tools, lint/testing tools, or reproducibility risks in a new or existing iOS project.
---

# iOS Environment Audit

Use this skill when the user needs a clear view of the development environment and version/toolchain state.

## Default Principles
- prefer observable facts from project files and tool declarations
- distinguish critical compatibility risks from cleanup items
- recommend the smallest standardization steps first
- support both solo and team workflows

## Required Output
1. Environment snapshot
2. Version/toolchain findings
3. Compatibility risks
4. Standardization recommendations
5. What can wait

## References
Read when needed:
- `../../platforms/ios/environment-audit.md`
- `../../templates/environment-audit-report.md`
