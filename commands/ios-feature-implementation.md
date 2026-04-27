# /ios-feature-implementation

## Intent
Use when the user has a feature plan and needs to implement it: create files, write code, wire dependencies, and produce a reviewable PR.

## Typical Inputs
- Feature plan or brief (from `/ios-feature-bootstrap` or manual description)
- Target module/folder
- Scope constraints (e.g., "just the UI layer first")

## Agent Workflow
1. Read the codebase to understand existing conventions, patterns, and dependencies.
2. Identify the feature boundary and which module/folder it belongs in.
3. Map reusable code vs new code to create.
4. Define the smallest shippable implementation slice.
5. Generate a file-level implementation plan (create + modify).
6. Wire state, navigation, and data flow into existing patterns.
7. Add test hooks, observability, and error handling.
8. Review the change for accidental debt introduction.

## Output Format
- Current codebase snapshot (relevant areas)
- Implementation plan (files to create, files to modify, skeleton code)
- Dependency wiring
- State/navigation integration
- Test coverage plan
- PR scope and review notes
