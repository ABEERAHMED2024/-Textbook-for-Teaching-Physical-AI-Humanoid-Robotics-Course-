# ADR-014: Assessment Design

## Status

Proposed

## Date

2026-01-03

## Context

The Physical AI & Humanoid Robotics Textbook Module 1 requires effective assessment mechanisms to validate student learning and provide feedback. The assessments must be practical and relevant to ROS 2 concepts, allowing students to demonstrate their understanding through implementation rather than just theoretical knowledge. The system needs to scale appropriately for different class sizes while providing consistent evaluation criteria.

## Decision

We will implement individual practical assessments with 4-level rubrics, GitHub repository submissions, and combined automated + manual grading. Each chapter has a corresponding assessment with specific functional and technical requirements. The rubrics use a 4-level scoring system (Exemplary, Proficient, Developing, Beginning) across multiple dimensions (Functionality, Code Quality, ROS 2 Best Practices, Documentation). Students submit GitHub repositories with specified directory structures for automated validation.

## Alternatives Considered

1. **Multiple choice assessments**:
   - Pros: Easier to grade automatically, consistent scoring
   - Cons: Doesn't test practical implementation skills, less relevant to ROS 2

2. **Peer review system**:
   - Pros: Scales well, provides different perspectives
   - Cons: Quality varies, harder to ensure consistency, students may not have expertise

3. **No formal assessments**:
   - Pros: Simpler to implement
   - Cons: Doesn't validate learning outcomes, no feedback mechanism

4. **Different rubric structures**:
   - Pros: Could use different evaluation approaches
   - Cons: Less comprehensive evaluation of practical skills

5. **Different submission formats**:
   - Pros: Could use different platforms or formats
   - Cons: Less integration with development workflow, harder to validate code

## Consequences

### Positive
- Validates practical implementation skills rather than just theoretical knowledge
- Provides clear, consistent feedback through structured rubrics
- Integrates with real development workflow (GitHub repositories)
- Scales with combination of automated and manual grading
- Encourages good development practices (documentation, code quality)

### Negative
- Complex to implement grading automation
- Time-consuming for instructors to provide manual feedback
- Students need GitHub accounts and understanding of repository structure
- More complex submission and evaluation process

## References

- research.md (Assessment Design section)
- data-model.md (Assessment Structure section)
- quickstart.md (Assessment section)
- plan.md (Assessment Requirements section)