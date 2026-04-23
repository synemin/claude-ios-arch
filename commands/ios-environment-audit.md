# /ios-environment-audit

## Intent
Use when the user wants to understand or standardize the development environment for an iOS project.

## Typical Questions
- What Xcode / Swift / SDK version is this project using?
- Are package and tool versions drifting?
- Is the project reproducible across machines?
- What should we standardize first?

## Agent Workflow
1. Inspect project files and visible toolchain declarations.
2. Summarize versions, targets, and tooling.
3. Identify compatibility or reproducibility risks.
4. Recommend the smallest standardization steps first.

## Output Format
- environment snapshot
- version/toolchain findings
- compatibility risks
- standardization recommendations
