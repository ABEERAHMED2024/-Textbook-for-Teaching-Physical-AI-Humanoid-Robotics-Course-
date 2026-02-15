# ADR-006: MDX Component Architecture

## Status

Proposed

## Date

2026-01-03

## Context

The Physical AI & Humanoid Robotics Textbook requires custom MDX components to display educational content elements like learning objectives, prerequisites, key takeaways, and interactive exercises. These components must work within Docusaurus's static site generation model while providing interactive features for the educational experience.

## Decision

We will use functional React components with SSR compatibility via two-pass rendering pattern for stateful components. Stateless components (LearningObjectives, Prerequisites, KeyTakeaways) will be pure SSR components with no client-side state, while stateful components (ExerciseBlock) will use the two-pass rendering pattern with useState and useEffect.

## Alternatives Considered

1. **Class components instead of functional components**:
   - Pros: Familiar to developers experienced with older React patterns
   - Cons: Functional components with hooks are modern React standard, better for SSR, more concise

2. **Different SSR patterns**:
   - Pros: Other patterns might offer different performance characteristics
   - Cons: Two-pass rendering is a well-established pattern for this exact use case

3. **Alternative component frameworks**:
   - Pros: Other frameworks might offer different features
   - Cons: React is already a dependency via Docusaurus, using it maintains consistency

## Consequences

### Positive
- Components render properly during static site generation
- Interactive elements work correctly after client hydration
- Follows modern React best practices
- Maintains compatibility with Docusaurus architecture
- Type safety through TypeScript interfaces

### Negative
- Slightly more complex implementation for stateful components
- Requires understanding of SSR vs client-side rendering differences
- Need to handle the two-pass rendering pattern correctly

## References

- research.md (Docusaurus MDX Component Best Practices section)
- data-model.md (Component definitions)
- contracts/component-props.ts (TypeScript interfaces)
- quickstart.md (Component usage examples)