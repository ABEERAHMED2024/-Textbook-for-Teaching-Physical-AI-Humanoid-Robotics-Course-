# ADR-001: Docusaurus Documentation Framework

## Status

Proposed

## Date

2026-01-03

## Context

We need to select a documentation framework for the Physical AI & Humanoid Robotics Textbook that will:

- Support educational content with structured navigation
- Enable rich metadata for chapters (time estimates, prerequisites, learning objectives)
- Provide responsive design for various devices
- Support custom components for enhanced user experience
- Integrate well with our Git-based workflow
- Be suitable for static site deployment

## Decision

We will use Docusaurus 3.x as the documentation framework with React 18.x for custom components and TypeScript 5.x for type safety.

## Alternatives Considered

1. **Next.js with custom documentation system**:
   - Pros: Full flexibility, modern React framework, excellent performance
   - Cons: Requires building documentation infrastructure from scratch, more complex routing and navigation setup

2. **Gatsby with documentation plugins**:
   - Pros: Strong plugin ecosystem, good performance, flexible data layer
   - Cons: Steeper learning curve, larger bundle sizes, slower build times for content-heavy sites

3. **GitBook or other hosted documentation platforms**:
   - Pros: Minimal setup, hosted solution, good default UX
   - Cons: Limited customization, potential vendor lock-in, less control over build process

4. **Custom solution with React and routing library**:
   - Pros: Complete control over features and design
   - Cons: Significant development time, maintenance burden, reinventing documentation patterns

## Consequences

### Positive
- Leverages proven documentation platform with educational use cases
- Built-in features like versioning, search integration, and internationalization
- Strong TypeScript support for type-safe custom components
- Active community and ecosystem
- Supports markdown content with frontmatter metadata
- Good performance and SEO out of the box

### Negative
- Learning curve for Docusaurus-specific concepts
- Potential limitations in customization compared to fully custom solution
- Dependency on Docusaurus ecosystem and release cycle
- Additional complexity with plugin system

## References

- plan.md (Technical Context section)
- research.md (Docusaurus 3 Best Practices section)
- docusaurus.config.js (project configuration)