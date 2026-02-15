# ADR-007: Build Pipeline Validation

## Status

Proposed

## Date

2026-01-03

## Context

The Physical AI & Humanoid Robotics Textbook requires consistent, validated metadata across all chapters to ensure educational quality and proper site functionality. We need a validation mechanism that prevents invalid content from being deployed while providing clear feedback to authors.

## Decision

We will use npm `prebuild` hook with AJV validation script for metadata validation. The validation script will run automatically before the build process, parsing all chapter frontmatter and validating it against a JSON Schema. If validation fails, the script will exit with code 1, stopping the build pipeline.

## Alternatives Considered

1. **Manual script chaining (`npm run validate && npm run build`)**:
   - Pros: Simple to understand
   - Cons: Requires developers to remember; easy to skip validation

2. **Postbuild validation**:
   - Pros: Build completes first
   - Cons: Wasted build time if validation fails; too late in the process

3. **Git pre-commit hooks**:
   - Pros: Catches errors early in development
   - Cons: Doesn't run in CI; developers can bypass with `--no-verify`

4. **Different validation libraries (e.g., Joi)**:
   - Pros: Alternative validation approaches
   - Cons: AJV is the industry standard for JSON Schema validation, with better performance and TypeScript support

## Consequences

### Positive
- Validation runs automatically on every build
- Clear error messages with file paths and field names
- Build fails fast if validation errors exist
- Industry-standard JSON Schema for validation
- Fast performance (<100ms for 50+ files)

### Negative
- Build process depends on validation script
- Additional dependency (AJV) in build pipeline
- Authors must fix validation errors before seeing their changes

## References

- research.md (Build Pipeline Integration section)
- contracts/chapter-metadata-schema.json (JSON Schema)
- plan.md (Technical Context section)
- quickstart.md (Validation and Error Handling section)