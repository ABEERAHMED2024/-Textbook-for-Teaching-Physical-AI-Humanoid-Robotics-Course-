# GitHub Issues Summary for 001-book-master-plan

This document summarizes the tasks from `specs/001-book-master-plan/tasks.md` that need to be created as GitHub issues.

## Issue Template

For each issue, use the following template:

```
## Task: [TASK_ID] - [TASK_DESCRIPTION]

**Status**: Not Started
**Priority**: [PRIORITY]
**User Story**: [USER_STORY]

### Description
[TASK_DESCRIPTION]

### Requirements
- [REQUIREMENT_1]
- [REQUIREMENT_2]
- [REQUIREMENT_3]

### Implementation Notes
[Any specific implementation notes]

### Success Criteria
- [ ] [SUCCESS_CRITERIA_1]
- [ ] [SUCCESS_CRITERIA_2]
- [ ] [SUCCESS_CRITERIA_3]

### Dependencies
- [DEPENDENCY_1]

### Linked to
- Feature: 001-book-master-plan
- User Story: [USER_STORY]
```

## Issues to Create

### User Story 2 Issues

1. **T035: Create docs/references/glossary.md with initial 100+ robotics terms**
   - Priority: P2
   - User Story: US2
   - Requirements: Create glossary.md file with 100+ robotics terms, each as H2 with definition, links to relevant chapters, alphabetically organized

2. **T038: Integrate GlossarySearch component into homepage quick links and glossary page**
   - Priority: P2
   - User Story: US2
   - Requirements: Integrate GlossarySearch component into homepage quick links and glossary page

### User Story 3 Issues

3. **T040: Update docs/module-1-ros2/index.md to add capstone integration section**
   - Priority: P2
   - User Story: US3
   - Requirements: Add capstone integration section explaining how ROS 2 serves as communication layer for autonomous humanoid

4. **T041: Update docs/module-2-digital-twin/index.md to add capstone integration section**
   - Priority: P2
   - User Story: US3
   - Requirements: Add capstone integration section explaining simulation testing for humanoid navigation

5. **T042: Update docs/module-3-isaac/index.md to add capstone integration section**
   - Priority: P2
   - User Story: US3
   - Requirements: Add capstone integration section explaining Isaac perception and manipulation for capstone

6. **T043: Update docs/module-4-vla-humanoids/index.md to add capstone integration section**
   - Priority: P2
   - User Story: US3
   - Requirements: Add capstone integration section explaining VLA integration for voice → action pipeline

7. **T044: Create docs/capstone/autonomous-humanoid.md with 5-step architecture guide**
   - Priority: P2
   - User Story: US3
   - Requirements: Create 5-step architecture guide (voice → plan → navigate → perceive → manipulate) and chapter mappings

8. **T045: Update sidebars.js to add Capstone Project Guide category**
   - Priority: P2
   - User Story: US3
   - Requirements: Add Capstone Project Guide category after Module 4

9. **T046: Add module summary sections to each module index page**
   - Priority: P2
   - User Story: US3
   - Requirements: Add module summary sections with time commitment estimates (aggregate estimated_time from chapters)

10. **T047: Create visual learning pathway diagram**
    - Priority: P2
    - User Story: US3
    - Requirements: Create visual learning pathway diagram (Mermaid.js or static SVG) showing module progression and capstone dependencies

### User Story 4 Issues

11. **T048: Create docs/assessments/ros2-package.md with ROS 2 package project requirements**
    - Priority: P2
    - User Story: US4
    - Requirements: Create ROS 2 package project requirements and 3-level rubric

12. **T049: Create docs/assessments/gazebo-simulation.md with Gazebo simulation project requirements**
    - Priority: P2
    - User Story: US4
    - Requirements: Create Gazebo simulation project requirements and 3-level rubric

13. **T050: Create docs/assessments/isaac-perception.md with Isaac perception pipeline project requirements**
    - Priority: P2
    - User Story: US4
    - Requirements: Create Isaac perception pipeline project requirements and 3-level rubric

14. **T051: Create docs/assessments/capstone.md with autonomous humanoid capstone requirements**
    - Priority: P2
    - User Story: US4
    - Requirements: Create autonomous humanoid capstone requirements and 3-level rubric

15. **T052: Update sidebars.js to add Assessments category**
    - Priority: P2
    - User Story: US4
    - Requirements: Add Assessments category with all 4 assessment guides after Capstone section

16. **T053: Add self-assessment checklists to each assessment guide**
    - Priority: P2
    - User Story: US4
    - Requirements: Add self-assessment checklists to each assessment guide with measurable criteria

17. **T054: Link assessment guides from relevant module index pages**
    - Priority: P2
    - User Story: US4
    - Requirements: Link assessment guides from relevant module index pages

### User Story 5 Issues

18. **T055: Create docs/references/ros2-quick-ref.md with ROS 2 command cheat sheet**
    - Priority: P3
    - User Story: US5
    - Requirements: Create ROS 2 command cheat sheet (topics, services, nodes, launch, common commands with examples)

19. **T056: Create docs/references/notation.md with mathematical notation guide**
    - Priority: P3
    - User Story: US5
    - Requirements: Create mathematical notation guide (vectors, matrices, coordinate frames, symbols used throughout book)

20. **T057: Create docs/references/troubleshooting.md with common errors and solutions**
    - Priority: P3
    - User Story: US5
    - Requirements: Create troubleshooting guide organized by module (ROS 2, Gazebo, Isaac Sim)

21. **T058: Update sidebars.js to add References category**
    - Priority: P3
    - User Story: US5
    - Requirements: Add References category with all reference materials (glossary, ros2-quick-ref, notation, troubleshooting)

22. **T059: Add external resources section to docs/references/troubleshooting.md**
    - Priority: P3
    - User Story: US5
    - Requirements: Add external resources section (links to official ROS 2 docs, Isaac Sim docs, community forums)

23. **T060: Create docs/instructors/guide.md with instructor customization guidelines**
    - Priority: P3
    - User Story: US5
    - Requirements: Create instructor customization guidelines (chapter reordering, lab exercises, semester vs. quarter adaptation)

24. **T061: Update sidebars.js to add Instructors Guide category**
    - Priority: P3
    - User Story: US5
    - Requirements: Update sidebars.js to add Instructors Guide category after References

### Polish & Cross-Cutting Concerns Issues

25. **T062: Add favicon and logo images to static/img/ directory**
    - Priority: P3
    - User Story: N/A
    - Requirements: Add favicon and logo images to static/img/ directory

26. **T063: Create README.md at repository root**
    - Priority: P3
    - User Story: N/A
    - Requirements: Create README.md at repository root with project overview and quickstart links

27. **T064: Update docusaurus.config.js with SEO metadata**
    - Priority: P3
    - User Story: N/A
    - Requirements: Update docusaurus.config.js with SEO metadata (Open Graph tags, Twitter cards, meta descriptions)

28. **T065: Configure navbar in docusaurus.config.js**
    - Priority: P3
    - User Story: N/A
    - Requirements: Configure navbar in docusaurus.config.js with logo, documentation link, GitHub link, search bar

29. **T066: Configure footer in docusaurus.config.js**
    - Priority: P3
    - User Story: N/A
    - Requirements: Configure footer in docusaurus.config.js with links to documentation, GitHub, community, constitution

30. **T067: Create placeholder chapter files for all 13 weeks**
    - Priority: P3
    - User Story: N/A
    - Requirements: Create placeholder chapter files for all 13 weeks (week-3-architecture.md through week-13-conversational-vla.md) with frontmatter metadata templates

31. **T068: Add placeholder chapter items to sidebars.js**
    - Priority: P3
    - User Story: N/A
    - Requirements: Add placeholder chapter items to sidebars.js under respective module categories

32. **T069: Optimize all images in static/img/ using sharp or imagemin**
    - Priority: P3
    - User Story: N/A
    - Requirements: Optimize all images in static/img/ using sharp or imagemin (ensure < 500KB per image)

33. **T070: Run metadata validation script**
    - Priority: P3
    - User Story: N/A
    - Requirements: Run metadata validation script (npm run validate-metadata) to verify all chapter frontmatter complies with chapter-metadata-schema.json

34. **T071: Run Docusaurus build**
    - Priority: P3
    - User Story: N/A
    - Requirements: Run Docusaurus build (npm run build) and verify 0 errors, 0 warnings

35. **T072: Run broken link checker**
    - Priority: P3
    - User Story: N/A
    - Requirements: Run broken link checker (npm run check-links) and verify 0 broken internal links

36. **T073: Run Lighthouse CI**
    - Priority: P3
    - User Story: N/A
    - Requirements: Run Lighthouse CI (npm run lighthouse) and verify scores (Performance ≥ 90, Accessibility ≥ 95, SEO ≥ 95)

37. **T074: Test incremental publishing**
    - Priority: P3
    - User Story: N/A
    - Requirements: Test incremental publishing by building only Week 1-2 content (intro + setup + glossary) and verify functional mini-textbook

38. **T075: Create CONTRIBUTING.md with contribution guidelines**
    - Priority: P3
    - User Story: N/A
    - Requirements: Create CONTRIBUTING.md with contribution guidelines (code of conduct, PR process, commit conventions, review process)

39. **T076: Verify quickstart.md instructions**
    - Priority: P3
    - User Story: N/A
    - Requirements: Verify quickstart.md instructions by following setup guide end-to-end (clone, npm install, npm start, verify localhost:3000 works)