# ADR-008: Exercise Component Design

## Status

Proposed

## Date

2026-01-03

## Context

The Physical AI & Humanoid Robotics Textbook requires interactive exercises with progressive hints to enhance the learning experience. These components need to track user attempts, progressively unlock hints, and maintain accessibility standards while working within the static site generation constraints.

## Decision

We will implement a custom React component using HTML `<details>` elements for hints with progressive unlock logic based on attempt tracking. The component will use React useState for tracking attempts and hint visibility, with useEffect for cleanup when components unmount. ARIA attributes will ensure accessibility compliance.

## Alternatives Considered

1. **Pure CSS collapsible (checkbox hack)**:
   - Pros: No JavaScript required
   - Cons: Cannot integrate with attempt-based unlock logic

2. **Third-party accordion libraries**:
   - Pros: Feature-rich, well-tested
   - Cons: Adds dependency, over-engineered for simple use case, potential bundle size impact

3. **Custom div-based collapsible**:
   - Pros: Full control over behavior
   - Cons: Requires more ARIA work, reinvents `<details>` functionality

4. **localStorage persistence for attempts**:
   - Pros: Attempts persist across sessions
   - Cons: Unnecessary complexity; educational exercises should reset for fresh learning

## Consequences

### Positive
- Native HTML provides built-in accessibility and keyboard navigation
- Progressive hint unlocking encourages learning through attempts
- Clean, semantic HTML structure
- No external dependencies for core functionality
- Proper ARIA attributes ensure screen reader compatibility

### Negative
- Requires JavaScript for interactive functionality
- State resets on page reload (though this is also positive for learning)
- Slightly more complex implementation than simple static content

## References

- research.md (Exercise Block Component Design section)
- data-model.md (Exercise Block Component section)
- contracts/component-props.ts (ExerciseBlockProps interface)
- quickstart.md (ExerciseBlock component usage)