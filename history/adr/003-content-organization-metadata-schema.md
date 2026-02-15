# ADR-003: Content Organization and Metadata Schema

## Status

Proposed

## Date

2026-01-03

## Context

The Physical AI & Humanoid Robotics Textbook requires a structured approach to content organization that can:

- Support metadata for educational purposes (time estimates, prerequisites, learning objectives)
- Enable filtering and navigation by week, module, and difficulty
- Provide validation to ensure consistency across chapters
- Integrate with the documentation framework
- Support automated processing and aggregation

## Decision

We will use markdown frontmatter with JSON Schema validation for chapter metadata, following a structured schema that includes fields for educational content like time estimates, prerequisites, and learning objectives.

## Alternatives Considered

1. **Separate YAML files for metadata**:
   - Pros: Clear separation of content and metadata, easier to process programmatically
   - Cons: Requires managing two files per chapter, more complex authoring workflow

2. **Custom validation approaches**:
   - Pros: More flexible validation logic, potentially better error messages
   - Cons: More custom code to maintain, less standard than JSON Schema

3. **Alternative schema validation libraries**:
   - Pros: Different performance characteristics or features
   - Cons: Additional learning curve, potentially less community support than ajv

4. **No formal validation**:
   - Pros: Simpler initial setup
   - Cons: Risk of inconsistent metadata, harder to maintain quality across many chapters

## Consequences

### Positive
- Standardized approach using markdown frontmatter familiar to content authors
- JSON Schema provides clear validation rules and good error messages
- Enables automated processing and aggregation of metadata
- Supports rich navigation and filtering capabilities
- Integrates well with Docusaurus framework

### Negative
- Requires adherence to schema by content authors
- Additional build-time validation step
- Schema changes require updating all content
- Learning curve for authors to understand all metadata fields

## References

- plan.md (Phase 1: Design & Contracts section)
- data-model.md (Chapter entity definition)
- contracts/chapter-metadata-schema.json
- research.md (Chapter Metadata Schema Design section)