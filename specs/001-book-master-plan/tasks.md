---

description: "Task list for Book Master Plan - Physical AI & Humanoid Robotics Textbook"
---

# Tasks: Book Master Plan - Physical AI & Humanoid Robotics Textbook

**Input**: Design documents from `/specs/001-book-master-plan/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: No explicit tests requested in feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Docusaurus documentation site**: `docs/` for content, `src/` for custom components, `static/` for assets
- **Configuration**: `docusaurus.config.js`, `sidebars.js`
- **Custom components**: `src/components/`, `src/pages/`
- Paths shown below follow Docusaurus documentation site structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Docusaurus project initialization and basic structure

- [ ] T001 Create Docusaurus 3 project structure with TypeScript support
- [ ] T002 Initialize Node.js project with Docusaurus dependencies in package.json
- [ ] T003 [P] Configure TypeScript settings in tsconfig.json
- [ ] T004 [P] Configure ESLint and Prettier for consistent code formatting
- [ ] T005 Set up basic Docusaurus configuration in docusaurus.config.js
- [ ] T006 Create initial directory structure for docs/ based on plan.md

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T007 Configure sidebar structure in sidebars.js with nested categories
- [ ] T008 [P] Create basic module directory structure in docs/
- [ ] T009 [P] Create basic setup guides directory structure in docs/setup/
- [ ] T010 [P] Create basic module directory structures (module-1-ros2/, module-2-digital-twin/, etc.)
- [ ] T011 [P] Create basic assessment directory structure in docs/assessments/
- [ ] T012 [P] Create basic references directory structure in docs/references/
- [ ] T013 [P] Create basic capstone directory structure in docs/capstone/
- [ ] T014 [P] Create basic instructors directory structure in docs/instructors/
- [ ] T015 Create basic custom components structure in src/components/
- [ ] T016 Create basic pages structure in src/pages/
- [ ] T017 Create basic CSS structure in src/css/
- [ ] T018 Create static assets structure in static/img/
- [ ] T019 Configure Algolia DocSearch in docusaurus.config.js
- [ ] T020 [P] Create build scripts for metadata validation
- [ ] T021 [P] Create build scripts for glossary index generation
- [ ] T022 Configure GitHub Actions workflows for deployment and validation

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Navigate Complete Course Structure (Priority: P1) 🎯 MVP

**Goal**: Create dashboard homepage with module cards and nested sidebar navigation for complete course structure

**Independent Test**: Can be fully tested by viewing the table of contents, confirming all 13 weeks are represented, all 4 modules are clearly delineated, and prerequisite chains are visible.

### Implementation for User Story 1

- [ ] T023 [P] [US1] Create ModuleCard component in src/components/ModuleCard.tsx
- [ ] T024 [P] [US1] Create QuickLinks component in src/components/QuickLinks.tsx
- [ ] T025 [P] [US1] Create RecentUpdates component in src/components/RecentUpdates.tsx
- [ ] T026 [US1] Implement dashboard homepage layout in src/pages/index.tsx
- [ ] T027 [US1] Style dashboard with CSS Grid in src/css/custom.css
- [ ] T028 [US1] Create module overview pages (index.md) for each module
- [ ] T029 [US1] Create intro.md with course introduction (Weeks 1-2)
- [ ] T030 [US1] Create sidebar categories for all 4 modules with nested chapters
- [ ] T031 [US1] Implement responsive design for dashboard (mobile/desktop)
- [ ] T032 [US1] Add module cards with titles, week ranges, and learning outcomes
- [ ] T033 [US1] Add quick links sidebar with hardware setup, assessments, and glossary
- [ ] T034 [US1] Add recent updates section to homepage
- [ ] T035 [US1] Add navigation links between modules and chapters

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Access Foundational Setup Documentation (Priority: P1)

**Goal**: Create hardware setup guides and glossary search component for foundational documentation

**Independent Test**: Can be fully tested by accessing hardware setup guide, verifying all 3 hardware options are documented (Digital Twin Workstation, Edge Kit, Cloud setup), and confirming glossary is searchable.

### Implementation for User Story 2

- [ ] T036 [P] [US2] Create workstation setup guide in docs/setup/workstation.md
- [ ] T037 [P] [US2] Create edge-kit setup guide in docs/setup/edge-kit.md
- [ ] T038 [P] [US2] Create cloud setup guide in docs/setup/cloud.md
- [ ] T039 [US2] Create glossary search component in src/components/GlossarySearch.tsx
- [ ] T040 [US2] Create glossary data structure and indexing script
- [ ] T041 [US2] Implement glossary search with Flexsearch in build process
- [ ] T042 [US2] Create glossary page at docs/references/glossary.md
- [ ] T043 [US2] Create notation guide at docs/references/notation.md
- [ ] T044 [US2] Add setup guides to sidebar navigation
- [ ] T045 [US2] Add references section to sidebar navigation
- [ ] T046 [US2] Integrate glossary search component into navbar
- [ ] T047 [US2] Add hardware cost estimates and requirements to setup guides
- [ ] T048 [US2] Add troubleshooting sections to setup guides

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 4.5: Search Implementation (FR-007a)

**Purpose**: Implement hybrid search (Algolia DocSearch for content + custom glossary component)

**Goal**: Enable users to search textbook content and glossary terms with instant results

**Independent Test**: Can be tested by searching for a term and verifying results appear from both content and glossary

- [ ] T048a [P] Apply for Algolia DocSearch program (requires open-source, public project)
- [ ] T048b [P] Configure Algolia DocSearch in `docusaurus.config.js` with facet filters (week, module, topic)
- [ ] T048c Create glossary data file at `src/data/glossary.json` with term definitions and chapter cross-references
- [ ] T048d [P] Create `src/components/GlossarySearch.tsx` component with instant search functionality
- [ ] T048e Implement Flexsearch or Lunr.js for client-side glossary search
- [ ] T048f Add glossary search to navbar or homepage QuickLinks component
- [ ] T048g Test search responsiveness (< 200ms for glossary search)
- [ ] T048h Configure custom metadata indexing for week/module/topic facets in Algolia
- [ ] T048i Document search configuration in `docs/references/search-guide.md`

**Checkpoint**: Users can search textbook content (Algolia) and glossary terms (custom component) with instant results

---

## Phase 5: User Story 3 - Follow Module-Based Learning Path (Priority: P2)

**Goal**: Create module content with clear learning outcomes and capstone integration points

**Independent Test**: Can be fully tested by navigating through each module, verifying module learning outcomes are stated, and confirming capstone integration points are documented.

### Implementation for User Story 3

- [ ] T049 [P] [US3] Create Module 1 chapters (Weeks 3-5) in docs/module-1-ros2/
- [ ] T050 [P] [US3] Create Module 2 chapters (Weeks 6-7) in docs/module-2-digital-twin/
- [ ] T051 [P] [US3] Create Module 3 chapters (Weeks 8-10) in docs/module-3-isaac/
- [ ] T052 [P] [US3] Create Module 4 chapters (Weeks 11-13) in docs/module-4-vla-humanoids/
- [ ] T053 [US3] Add module learning outcomes to each module index page
- [ ] T054 [US3] Add capstone integration points to relevant chapters
- [ ] T055 [US3] Add estimated time metadata to all chapter frontmatter
- [ ] T056 [US3] Add prerequisites metadata to all chapter frontmatter
- [ ] T057 [US3] Add learning objectives metadata to all chapter frontmatter
- [ ] T058 [US3] Add module and week metadata to all chapter frontmatter
- [ ] T059 [US3] Add difficulty level and assessment type metadata to relevant chapters
- [ ] T060 [US3] Add capstone component metadata to relevant chapters
- [ ] T061 [US3] Validate all chapter metadata against schema
- [ ] T062 [US3] Add navigation links between chapters in each module

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Access Assessment and Project Guidelines (Priority: P2)

**Goal**: Create assessment guides with detailed rubrics and capstone project documentation

**Independent Test**: Can be fully tested by locating all 4 assessment types (ROS 2 package, Gazebo simulation, Isaac perception, Capstone) and verifying each has a detailed rubric.

### Implementation for User Story 4

- [ ] T063 [P] [US4] Create ROS 2 package assessment guide in docs/assessments/ros2-package.md
- [ ] T064 [P] [US4] Create Gazebo simulation assessment guide in docs/assessments/gazebo-simulation.md
- [ ] T065 [P] [US4] Create Isaac perception assessment guide in docs/assessments/isaac-perception.md
- [ ] T066 [P] [US4] Create capstone assessment guide in docs/assessments/capstone.md
- [ ] T067 [US4] Add assessment rubrics with 3 evaluation levels to each guide
- [ ] T068 [US4] Create capstone project guide in docs/capstone/autonomous-humanoid.md
- [ ] T069 [US4] Document 5-step capstone architecture (voice → plan → navigate → perceive → manipulate)
- [ ] T070 [US4] Add assessment links to sidebar navigation
- [ ] T071 [US4] Add capstone guide to sidebar navigation
- [ ] T072 [US4] Link assessments to relevant modules and chapters
- [ ] T073 [US4] Add assessment metadata to related chapters

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Reference Quick Guides and Troubleshooting (Priority: P3)

**Goal**: Create quick reference guides and troubleshooting documentation

**Independent Test**: Can be fully tested by accessing quick reference section, searching for a common error, and verifying troubleshooting steps are provided.

### Implementation for User Story 5

- [ ] T074 [P] [US5] Create ROS 2 quick reference guide in docs/references/ros2-quick-ref.md
- [ ] T075 [P] [US5] Create troubleshooting guide in docs/references/troubleshooting.md
- [ ] T076 [P] [US5] Create instructors guide in docs/instructors/guide.md
- [ ] T077 [US5] Add quick reference links to sidebar navigation
- [ ] T078 [US5] Add troubleshooting links to sidebar navigation
- [ ] T079 [US5] Add instructors guide to sidebar navigation
- [ ] T080 [US5] Create prerequisite dependency graph using Mermaid
- [ ] T081 [US5] Add course adaptation guidelines to instructors guide
- [ ] T082 [US5] Add external resources section to references

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T083 [P] Update documentation in docs/ based on implementation
- [ ] T084 [P] Add images and diagrams to chapters in static/img/
- [ ] T085 Run metadata validation across all chapters
- [ ] T086 Run broken link checker across entire site
- [ ] T087 Run Lighthouse audit and address issues
- [ ] T088 [P] Add additional content to glossary to reach 100+ terms
- [ ] T089 [P] Optimize images using Docusaurus ideal-image plugin
- [ ] T090 [P] Add SEO metadata to all pages
- [ ] T091 [P] Add accessibility improvements
- [ ] T092 Run quickstart.md validation
- [ ] T093 [P] Create README updates for project documentation
- [ ] T094 [P] Update package.json with project metadata

---

## Phase 9: Security, Accessibility & Monitoring (FR-014, FR-015, FR-016)

**Purpose**: Implement security headers, accessibility compliance, and monitoring

**Goal**: Meet security, accessibility, and observability requirements from spec

### Security (FR-014)

- [ ] T095 Configure security headers in `docusaurus.config.js` (Content-Security-Policy, X-Frame-Options, X-Content-Type-Options, X-XSS-Protection)
- [ ] T096 [P] Enable HTTPS enforcement in GitHub Pages settings
- [ ] T097 [P] Create `static/.well-known/security.txt` file with contact information
- [ ] T098 Verify no sensitive data in client-side code (API keys, secrets, credentials)
- [ ] T099 Run security headers test via securityheaders.com or similar tool

### Accessibility (FR-015)

- [ ] T100 Run axe-core accessibility audit on all pages using axe-cli or Lighthouse
- [ ] T101 [P] Verify all images have descriptive alt text (no missing or generic alt attributes)
- [ ] T102 [P] Verify color contrast ratios meet WCAG 2.1 AA (4.5:1 for normal text, 3:1 for large text)
- [ ] T103 [P] Test keyboard navigation through all interactive elements (Tab, Enter, Escape)
- [ ] T104 Add ARIA labels to custom components (GlossarySearch, ModuleCard, QuickLinks, RecentUpdates)
- [ ] T105 Test with screen reader (NVDA on Windows, VoiceOver on macOS)
- [ ] T106 Create accessibility statement page at `docs/accessibility.md`

### Monitoring (FR-016)

- [ ] T107 Configure Google Analytics or Plausible for traffic analytics
- [ ] T108 [P] Set up Lighthouse CI for automated performance monitoring in GitHub Actions
- [ ] T109 [P] Configure uptime monitoring (UptimeRobot, Pingdom, or similar free tier)
- [ ] T110 Add performance budget to `docusaurus.config.js` (max bundle size, max image size)
- [ ] T111 Create monitoring dashboard or status page
- [ ] T112 Document monitoring setup in `docs/references/monitoring.md`

**Checkpoint**: Site passes security headers test, WCAG 2.1 AA audit, and has monitoring configured

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May reference US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May reference US1/US2/US3 but should be independently testable
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - May reference other stories but should be independently testable

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Create ModuleCard component in src/components/ModuleCard.tsx"
Task: "Create QuickLinks component in src/components/QuickLinks.tsx"
Task: "Create RecentUpdates component in src/components/RecentUpdates.tsx"
```

---

## Implementation Strategy

### MVP First (User Stories 1 & 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 - Navigate Complete Course Structure
4. Complete Phase 4: User Story 2 - Access Foundational Setup Documentation
5. **STOP and VALIDATE**: Test User Stories 1 & 2 independently
6. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo (MVP!)
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence