# ADR-005: Homepage Dashboard Architecture

## Status

Proposed

## Date

2026-01-03

## Context

The Physical AI & Humanoid Robotics Textbook needs an engaging homepage that:

- Provides clear navigation to course modules
- Offers quick access to important resources
- Presents an organized, dashboard-style layout
- Works well across different device sizes
- Encourages exploration of the content

## Decision

We will implement a custom React homepage with a dashboard layout using CSS Grid for module cards and a sidebar for quick links to important resources.

## Alternatives Considered

1. **Docs homepage with custom MDX**:
   - Pros: Simpler integration with Docusaurus, less custom code
   - Cons: Less flexibility in layout design, limited React component options

2. **Redirect `/` to `/docs`**:
   - Pros: Simpler implementation, follows standard Docusaurus pattern
   - Cons: Misses opportunity for engaging dashboard UX, less clear navigation

3. **Different layout approaches**:
   - Pros: Alternative layouts might work better for specific use cases
   - Cons: Other layouts might be less intuitive for educational content organization

4. **Static HTML/CSS only**:
   - Pros: Simpler, smaller bundle size
   - Cons: Less interactive, harder to maintain consistency with Docusaurus

## Consequences

### Positive
- Custom React component allows full control over dashboard layout and user experience
- Module cards provide clear visual organization of content
- Quick links sidebar offers easy access to important resources
- Responsive CSS Grid layout works well on different device sizes
- Consistent with Docusaurus component architecture

### Negative
- Requires additional React component development and maintenance
- More complex than default Docusaurus homepage
- Additional CSS to maintain consistency
- Potential for layout issues on different screen sizes if not properly tested

## References

- plan.md (Technical Context section)
- research.md (Dashboard Homepage Patterns section)
- src/pages/index.tsx (homepage implementation)
- src/components/ModuleCard.tsx (module card component)