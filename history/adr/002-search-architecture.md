# ADR-002: Search Architecture

## Status

Proposed

## Date

2026-01-03

## Context

The Physical AI & Humanoid Robotics Textbook requires a robust search capability that can:

- Handle full-text search across all content
- Support faceted search by week, module, and topic
- Provide fast glossary-specific search
- Work well in a static site environment
- Offer good user experience with search-as-you-type functionality

## Decision

We will implement a hybrid search architecture using Algolia DocSearch for main content search with custom facets and Flexsearch for client-side glossary search.

## Alternatives Considered

1. **Local search plugin (@easyops-cn/docusaurus-search-local)**:
   - Pros: No external dependencies, works offline, simpler setup
   - Cons: Limited faceting capabilities, slower for larger content sets, less sophisticated search algorithms

2. **Typesense**:
   - Pros: Good performance, good faceting, self-hosted option
   - Cons: Requires self-hosting infrastructure, more complex setup, additional maintenance

3. **Custom search implementation**:
   - Pros: Complete control over search behavior and UI
   - Cons: Significant development time, maintenance burden, reinventing search algorithms

4. **Lunr.js**:
   - Pros: Lightweight, client-side, good for smaller datasets
   - Cons: Larger bundle size than Flexsearch, slower indexing for larger content sets

## Consequences

### Positive
- Algolia provides enterprise-grade search with excellent performance and analytics
- Custom facets allow filtering by week, module, and other metadata
- Flexsearch provides fast glossary search without external dependencies
- Search-as-you-type experience with 150ms debounce
- Offline capability for glossary search

### Negative
- Algolia requires external service dependency and API keys
- Free tier limitations for Algolia DocSearch (though suitable for open source)
- Additional complexity with dual search systems
- Glossary index needs to be rebuilt on content changes

## References

- plan.md (Technical Context section)
- research.md (Search Integration Strategies section)
- docusaurus.config.js (Algolia configuration)