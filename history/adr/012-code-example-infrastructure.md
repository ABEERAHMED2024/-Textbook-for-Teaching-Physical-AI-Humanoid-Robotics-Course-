# ADR-012: Code Example Infrastructure

## Status

Proposed

## Date

2026-01-03

## Context

The Physical AI & Humanoid Robotics Textbook Module 1 requires effective code examples that support active learning. Students need to engage with ROS 2 code practically rather than just reading about it. The infrastructure must support both student learning (with scaffolding) and instructor needs (with complete solutions), while ensuring code examples work correctly with ROS 2 Humble.

## Decision

We will implement skeleton code with TODO markers for student exercises, with separate complete solutions for instructors. The approach uses minimal scaffolding that provides enough structure for students to focus on key concepts while requiring them to implement important parts. Each code example has both a skeleton version (with TODOs) and a complete version, with in-file documentation standards to explain purpose, requirements, and usage.

## Alternatives Considered

1. **Complete examples only (no scaffolding)**:
   - Pros: Students can run working code immediately
   - Cons: Students don't actively engage with implementation, less effective for learning

2. **Interactive playgrounds in browser**:
   - Pros: Students can run code without local setup
   - Cons: Complex to implement, security concerns, doesn't match real development environment

3. **No code examples**:
   - Pros: Simpler to implement
   - Cons: Doesn't meet educational requirements for hands-on learning

4. **Different scaffolding approaches (more/less guidance)**:
   - Pros: Could provide more or less guidance depending on student level
   - Cons: Less balanced approach for the target audience

## Consequences

### Positive
- Students actively engage with code implementation
- Provides different versions for different user needs (students vs. instructors)
- Maintains consistency with educational best practices
- Ensures code examples are tested and functional
- Clear documentation helps with understanding and usage

### Negative
- Requires more maintenance (two versions of each example)
- Students might be frustrated if scaffolding is too minimal
- More complex to develop initially (creating both skeleton and complete versions)

## References

- research.md (Code Example Infrastructure section)
- data-model.md (Code Example Metadata section)
- quickstart.md (Code Example IDs section)
- plan.md (Code Example Quality section)