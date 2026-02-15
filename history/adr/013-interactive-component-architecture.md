# ADR-013: Interactive Component Architecture

## Status

Proposed

## Date

2026-01-03

## Context

The Physical AI & Humanoid Robotics Textbook Module 1 requires specialized interactive components to enhance the learning experience beyond standard documentation. The content needs custom MDX components for displaying code examples with solution toggles, structured exercises with hints, concept callouts, assessment checklists, and ROS-specific indicators. Standard Docusaurus components are insufficient for the specific educational needs of ROS 2 content.

## Decision

We will create 5 new MDX components (CodeExample, ExerciseBlock, ConceptCallout, AssessmentChecklist, ROSVersionBadge) to enhance learning experience. These components will be built with React and TypeScript, following accessibility standards and integrating with the existing Docusaurus infrastructure. Each component has a detailed contract specifying props, behavior, validation rules, and usage patterns.

## Alternatives Considered

1. **Standard Docusaurus components only**:
   - Pros: Simpler implementation, uses existing patterns
   - Cons: Doesn't meet specific educational needs for ROS 2 content

2. **Third-party educational components**:
   - Pros: Might have advanced features
   - Cons: Less control, potential compatibility issues, additional dependencies

3. **No custom components (use markdown only)**:
   - Pros: Simpler implementation
   - Cons: Doesn't provide the interactive learning experience required

4. **Different component sets**:
   - Pros: Could focus on different aspects of learning
   - Cons: Less comprehensive approach to educational needs

## Consequences

### Positive
- Enhanced learning experience with interactive elements
- Consistent educational patterns across all content
- Better support for different learning activities (examples, exercises, concepts)
- Accessibility features built into components
- Clear contracts for component usage and maintenance

### Negative
- Additional development and maintenance overhead
- Learning curve for authors to use new components
- More complex build process with custom components
- Potential performance impact with multiple interactive elements

## References

- research.md (Interactive Components section)
- data-model.md (Component Usage Patterns section)
- quickstart.md (MDX Component Usage Patterns section)
- contracts/CodeExample.md, contracts/ExerciseBlock.md, contracts/ConceptCallout.md, contracts/AssessmentChecklist.md, contracts/ROSVersionBadge.md