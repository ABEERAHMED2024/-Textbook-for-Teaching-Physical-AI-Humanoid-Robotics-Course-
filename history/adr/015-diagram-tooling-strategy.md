# ADR-015: Diagram Tooling Strategy

## Status

Proposed

## Date

2026-01-03

## Context

The Physical AI & Humanoid Robotics Textbook Module 1 requires effective diagrams to illustrate complex ROS 2 concepts like architecture, communication patterns, and system interactions. The diagram strategy must balance version control needs (text-based diagrams that can be tracked in Git), professional appearance for educational materials, and maintainability for future updates. The diagrams need to be accessible and clear for students learning ROS 2 concepts.

## Decision

We will use a hybrid approach with Mermaid.js for simple diagrams (sequence diagrams, flowcharts) and draw.io for complex architecture diagrams. Mermaid.js diagrams are text-based and version-controlled directly in MDX files, while draw.io diagrams are created as SVG files for professional appearance. This approach balances the need for version control with the need for high-quality visuals.

## Alternatives Considered

1. **Use only Mermaid.js**:
   - Pros: All diagrams in version control, simple to edit
   - Cons: Limited styling options, not suitable for complex architecture diagrams

2. **Use only draw.io**:
   - Pros: Professional appearance for all diagrams
   - Cons: Binary files harder to version control, more complex maintenance

3. **Use different tools (PlantUML, Graphviz, Lucidchart)**:
   - Pros: Different tools have different strengths
   - Cons: Additional learning curve, potential compatibility issues

4. **No diagrams at all**:
   - Pros: Simpler to implement
   - Cons: Doesn't meet educational needs for visualizing complex concepts

5. **Different export formats (PNG, HTML)**:
   - Pros: Could use different formats for different purposes
   - Cons: PNG files are larger and not scalable, HTML not suitable for static site

## Consequences

### Positive
- Simple diagrams remain in version control with content
- Complex diagrams have professional appearance
- Clear separation of diagram types by complexity
- SVG format ensures scalability and accessibility
- Maintains balance between version control and visual quality

### Negative
- Requires knowledge of two different tools
- More complex workflow for authors
- Need to maintain both text-based and binary diagram files
- Potential inconsistency in visual style between diagram types

## References

- research.md (Diagram Requirements section)
- quickstart.md (Mermaid.js Diagrams section)
- plan.md (Diagram Requirements section)
- data-model.md (Diagram section)