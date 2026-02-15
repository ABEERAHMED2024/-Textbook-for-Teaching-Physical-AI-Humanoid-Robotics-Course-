# Implementation Plan: Core Features Completion - Physical AI & Humanoid Robotics Textbook

**Branch**: `007-core-features-completion` | **Date**: 2026-02-15 | **Spec**: [spec.md](../007-core-features-completion/spec.md)

## Summary

This plan outlines the implementation of missing core features: personalization backend, Urdu translation backend, Claude Code subagents, and remaining textbook content as defined in the Hackathon PDF. The approach focuses on extending existing UI implementations with real backend functionality while maintaining a single source of truth for content.

## Technical Context

**Language/Version**: TypeScript/JavaScript, Python for backend services
**Primary Dependencies**: Docusaurus 3.x, FastAPI, React 18.x, Claude Code
**Storage**: Existing Docusaurus file structure for content, potential Redis for caching
**Testing**: Jest for frontend, pytest for backend
**Target Platform**: Node.js server environment, browser clients
**Project Type**: Docusaurus-based documentation site with custom backend services
**Performance Goals**: Sub-second response for personalization, under 5s for translation
**Constraints**: No content duplication, constitutional compliance, maintain existing UI
**Scale/Scope**: Educational platform for robotics practitioners

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ✅ Constitution Principle I (Constitution First): Following Spec-Kit Plus lifecycle: /sp.specify → /sp.plan → /sp.tasks → implementation
- ✅ Constitution Principle II (Authoritative Source of Truth): Using Hackathon PDF as source for required content
- ✅ Constitution Principle III (State-Aware Continuation): Extending existing UI implementations with real backend, not replacing
- ✅ Constitution Principle IV (Spec Before Code): Creating detailed plan before implementation
- ✅ Constitution Principle V (Non-Hallucination & Safety): Implementing real backend functionality rather than mocking
- ✅ Constitution Principle VI (Atomic & Traceable Changes): Breaking implementation into small, traceable tasks

## Project Structure

### Documentation (this feature)
```text
specs/007-core-features-completion/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)
```text
# Single project
src/
├── components/          # Custom React components for personalization/translation
├── pages/               # Custom pages if needed
├── utils/               # Utility functions
└── types/               # TypeScript type definitions

backend/                 # New backend services
├── api/                 # API routes
│   ├── personalization/ # Personalization endpoints
│   ├── translation/     # Translation endpoints
│   └── subagents/       # Subagent endpoints
├── services/            # Business logic
│   ├── personalization/ # Personalization engine
│   ├── translation/     # Translation service
│   └── subagents/       # Subagent orchestration
├── models/              # Data models
├── utils/               # Backend utilities
└── main.py              # Application entry point

scripts/                 # Scripts for subagents
├── subagent-content-gen.py
├── subagent-qa-validate.py
└── subagent-maintenance.py

docs/                    # Updated textbook content
├── intro.md
├── setup/
├── module-1-ros2/
├── module-2-digital-twin/
├── module-3-isaac/
├── module-4-vla-humanoids/
├── capstone/
└── references/

contracts/               # New API contracts and validation schemas
├── personalization-contract.json
├── translation-contract.json
└── subagent-task-contract.json
```

**Structure Decision**: Single project structure with new backend services directory to house API endpoints and business logic for the new features. This keeps the new functionality organized while maintaining integration with the existing Docusaurus frontend.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| New backend services | Required for personalization and translation features | Extending existing Docusaurus API directory would mix concerns |