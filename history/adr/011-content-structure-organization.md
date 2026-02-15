# ADR-011: Content Structure and Organization

## Status

Proposed

## Date

2026-01-03

## Context

The Physical AI & Humanoid Robotics Textbook Module 1 requires a clear, consistent structure for delivering ROS 2 educational content. The content must support progressive learning where concepts build upon each other, with examples and exercises integrated throughout. Students with AI/ML backgrounds but no robotics experience need a logical flow that introduces concepts gradually.

## Decision

We will use a hierarchical content structure with 5 chapters, each with H2/H3 headings, following a "Concept → Example → Exercise" pattern. The structure follows: Module → Chapter → Section (H2) → Subsection (H3), with heading level rules to maintain consistency. Each chapter follows a recommended flow: Learning Objectives → Introduction → Concept Sections → Examples → Exercises → Key Takeaways → Next Steps.

## Alternatives Considered

1. **Different hierarchical approaches (topic-based, skill-based)**:
   - Pros: Could organize by skill level or specific topics
   - Cons: Would be less intuitive for progressive learning, harder to maintain prerequisite chains

2. **Flat structure without clear sections**:
   - Pros: Simpler to implement initially
   - Cons: Would make navigation difficult,不利于 learning progression

3. **Different heading level conventions**:
   - Pros: Could use different conventions
   - Cons: Would break consistency with existing documentation patterns

## Consequences

### Positive
- Clear learning progression with concepts building on each other
- Consistent navigation structure across all chapters
- Follows established educational patterns (Concept → Example → Exercise)
- Maintains prerequisite chains for progressive learning
- Easy for authors to follow consistent structure

### Negative
- Rigid structure may not accommodate all content types equally well
- Authors must follow strict heading level conventions
- Requires more planning to maintain consistency across chapters

## References

- data-model.md (Content Hierarchy section)
- quickstart.md (Heading Styles section)
- plan.md (Content Structure section)
- research.md (Content Sources section)