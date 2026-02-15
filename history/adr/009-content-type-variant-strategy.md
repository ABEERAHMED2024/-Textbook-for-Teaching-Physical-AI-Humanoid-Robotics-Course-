# ADR-009: Content Type Variant Strategy

## Status

Proposed

## Date

2026-01-03

## Context

The Physical AI & Humanoid Robotics Textbook needs to support different types of educational content (tutorials, concepts, hands-on labs, references) while maintaining consistency across all chapters. We need a strategy that allows authors to create appropriate content for each type while following a standardized structure.

## Decision

We will use a single template with HTML comment guidance for different content types. The template will include a decision tree at the top to help authors choose the correct variant, and HTML comments throughout the template will indicate which sections apply to which content types. This approach provides clear guidance without creating multiple template files.

## Alternatives Considered

1. **Separate template files per variant**:
   - Pros: Each variant is clearly isolated
   - Cons: 4x maintenance burden; duplicate common sections; harder to keep in sync

2. **Markdown frontmatter flag only**:
   - Pros: Simple implementation
   - Cons: Doesn't provide inline guidance on section content/emphasis

3. **Docusaurus tabs component**:
   - Pros: Visual separation of variants
   - Cons: Adds visual clutter to source; harder to edit; not intended for authoring guidance

4. **No variant guidance**:
   - Pros: Simpler template
   - Cons: Authors would have inconsistent approaches; defeats purpose of standardization

## Consequences

### Positive
- Single file to maintain instead of multiple templates
- Clear guidance for authors on which sections to include
- HTML comments visible to authors but invisible in output
- Consistent structure across all content types
- Reduces maintenance overhead

### Negative
- Template file is more complex due to conditional comments
- Authors need to understand HTML comment syntax
- Potential for confusion if comments are not clear enough

## References

- research.md (Content Type Variant Guidance section)
- quickstart.md (Understanding Content Types section)
- plan.md (Phase 1: Design & Contracts section)
- data-model.md (Content Type Enum definition)