# ADR-010: Metadata Schema Validation

## Status

Proposed

## Date

2026-01-03

## Context

The Physical AI & Humanoid Robotics Textbook requires consistent and valid metadata across all chapters to ensure proper functionality of educational features like learning objectives, prerequisites, and navigation. We need a robust validation mechanism that enforces the required metadata structure while providing clear feedback to authors.

## Decision

We will use JSON Schema with AJV for build-time validation of chapter frontmatter metadata. The JSON Schema will define all required fields with their constraints, and the AJV library will validate all chapter metadata during the build process. This approach provides industry-standard validation with clear error messages.

## Alternatives Considered

1. **Joi validation library**:
   - Pros: Alternative validation approach with different API
   - Cons: AJV is faster, JSON Schema is standard format, easier to share schema with tools

2. **Manual file traversal with fs.readdirSync**:
   - Pros: No additional dependencies
   - Cons: Reinvents wheel; glob handles edge cases (symlinks, permissions) better

3. **Custom YAML parser**:
   - Pros: Full control over parsing
   - Cons: Unnecessary complexity; gray-matter is battle-tested and handles edge cases

4. **JSON output for errors**:
   - Pros: Structured output for tooling
   - Cons: Harder for humans to read; build scripts should be developer-friendly

## Consequences

### Positive
- Industry-standard JSON Schema validation
- Clear, actionable error messages with file paths and field names
- Fast performance with compiled schemas
- Type safety with TypeScript interfaces
- Schema can be shared across tools and teams
- Comprehensive validation of all required fields

### Negative
- Additional dependency (AJV) in build pipeline
- Learning curve for JSON Schema syntax
- Schema maintenance overhead when requirements change
- Validation errors may be complex for new authors

## References

- research.md (Metadata Validation Implementation section)
- data-model.md (JSON Schema Definition section)
- contracts/chapter-metadata-schema.json (JSON Schema file)
- contracts/chapter-metadata.ts (TypeScript interfaces)
- quickstart.md (Validation and Error Handling section)