# ADR-004: Deployment Strategy

## Status

Proposed

## Date

2026-01-03

## Context

The Physical AI & Humanoid Robotics Textbook needs a deployment strategy that:

- Supports static site hosting for cost efficiency
- Integrates with the Git-based development workflow
- Provides quality gates to ensure content quality
- Offers good performance and reliability
- Supports automated deployment from the repository

## Decision

We will use GitHub Pages for hosting with GitHub Actions for automated deployment, including build validation quality gates for content quality assurance.

## Alternatives Considered

1. **Netlify deployment**:
   - Pros: Excellent developer experience, powerful build features, form handling
   - Cons: Additional service dependency, potential cost considerations for high traffic

2. **Vercel deployment**:
   - Pros: Excellent performance, great developer experience, preview deployments
   - Cons: Additional service dependency, potential cost considerations

3. **Self-hosted solution (AWS S3 + CloudFront)**:
   - Pros: Complete control, potentially lower cost at scale
   - Cons: More operational overhead, additional complexity for a static site

4. **No automated deployment**:
   - Pros: Simpler initial setup
   - Cons: Manual deployment process, higher risk of human error

## Consequences

### Positive
- Free hosting solution that integrates well with GitHub workflow
- Automated deployment on push to main branch
- Quality gates ensure no build errors, broken links, or performance issues
- Static site provides excellent performance and reliability
- No server maintenance or security patching required

### Negative
- Limited to GitHub's infrastructure and policies
- Less advanced build features compared to Netlify/Vercel
- Potential limitations on build time or traffic
- Less sophisticated preview deployment options

## References

- plan.md (Technical Context section)
- research.md (Build Pipeline & Deployment section)
- .github/workflows/deploy.yml
- .github/workflows/build-validation.yml