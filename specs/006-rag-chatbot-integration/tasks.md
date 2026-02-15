# Tasks: RAG Chatbot Integration

**Input**: Design documents from `/specs/006-rag-chatbot-integration/`
**Prerequisites**: spec.md (required), plan.md (required)

**Tests**: Backend tests via pytest, frontend tests via Jest, manual E2E testing

**Organization**: Tasks grouped by phase for sequential implementation

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- Backend: `server/` directory (Python/FastAPI)
- Frontend: `src/components/Chatbot/` directory (React/TypeScript)
- Scripts: `scripts/` directory (Python)
- Config: Root directory

---

## Phase 1: Backend Setup

**Purpose**: FastAPI project initialization and infrastructure configuration

- [ ] T001 Create `server/` directory structure with `__init__.py` files
- [ ] T002 [P] Create `server/requirements.txt` with FastAPI, openai, qdrant-client, asyncpg, python-dotenv, uvicorn
- [ ] T003 [P] Create `server/.env.example` with OPENAI_API_KEY, QDRANT_URL, QDRANT_API_KEY, DATABASE_URL placeholders
- [ ] T004 Create `server/core/config.py` with Pydantic settings for environment variables
- [ ] T005 [P] Create `server/main.py` with FastAPI app, CORS middleware, and health check endpoint
- [ ] T006 [P] Create `server/models/schemas.py` with Pydantic models (ChatRequest, ChatResponse, Citation, Message)
- [ ] T007 Set up Neon Postgres database and connection string

**Checkpoint**: Backend skeleton ready, can run `uvicorn server.main:app`

---

## Phase 2: Database Layer

**Purpose**: Qdrant and Neon Postgres integration

- [ ] T008 Create `server/db/qdrant.py` with Qdrant client initialization and collection creation
- [ ] T009 [P] Create `server/db/neon.py` with async Postgres connection pool
- [ ] T010 [P] Add database schema migration SQL for `conversations` and `messages` tables
- [ ] T011 Implement `create_conversation()` function in `server/db/neon.py`
- [ ] T012 [P] Implement `save_message()` function in `server/db/neon.py`
- [ ] T013 [P] Implement `get_conversation_messages()` function in `server/db/neon.py`
- [ ] T014 Create Qdrant collection `textbook_chunks` with vector size 1536
- [ ] T015 Test database connections with simple health check endpoints

**Checkpoint**: Database layer functional, can store and retrieve data

---

## Phase 3: Content Ingestion

**Purpose**: Parse MDX files and create embeddings

### User Story: Content Indexing

- [ ] T016 [P] Create `scripts/ingest_content.py` as the main ingestion script
- [ ] T017 Implement `parse_frontmatter()` to extract YAML frontmatter from MDX files
- [ ] T018 [P] Implement `split_by_headers()` to chunk content by H2/H3 sections
- [ ] T019 Implement `get_chapter_id()` to derive chapter ID from filepath
- [ ] T020 [P] Implement `get_url_path()` to generate Docusaurus URL from filepath and section
- [ ] T021 Implement `generate_embeddings()` using OpenAI text-embedding-3-small
- [ ] T022 Implement `upsert_chunks()` to store chunks in Qdrant with metadata
- [ ] T023 Add idempotency check to prevent duplicate chunks on re-ingestion
- [ ] T024 Add `npm run ingest` script to `package.json` that calls Python script
- [ ] T025 Ingest Module 1 chapters as initial test content
- [ ] T026 Verify embeddings in Qdrant dashboard

**Checkpoint**: Content indexed and searchable in Qdrant

---

## Phase 4: RAG Implementation

**Purpose**: Implement the RAG pipeline for chat

### User Story 1 - Ask Questions About Content (P1)

- [ ] T027 Create `server/core/agent.py` with RAG pipeline logic
- [ ] T028 Implement `embed_query()` to generate embedding for user message
- [ ] T029 [P] Implement `search_chunks()` to query Qdrant for top 5 relevant chunks
- [ ] T030 Implement `build_context()` to concatenate chunk content with citations
- [ ] T031 Implement `generate_response()` using OpenAI chat completion with RAG context
- [ ] T032 [P] Add system prompt that enforces textbook-only responses
- [ ] T033 Implement citation filtering (only include chunks with similarity > 0.7)

### User Story 2 - Receive Cited Answers (P1)

- [ ] T034 Create `server/api/chat.py` with `/api/chat` POST endpoint
- [ ] T035 [P] Implement request validation (message required, conversation_id optional)
- [ ] T036 Implement response formatting with citations array
- [ ] T037 Ensure citation URLs use correct Docusaurus format (`/docs/chapter#section`)
- [ ] T038 Add rate limiting middleware (10 requests per minute per IP)

**Checkpoint**: Can send message and receive response with citations

---

## Phase 5: Chat History

**Purpose**: Persist and retrieve conversation history

### User Story 3 - View Chat History (P2)

- [ ] T039 Add `GET /api/conversations/{id}` endpoint to retrieve last 10 messages
- [ ] T040 [P] Implement conversation ID generation (UUID)
- [ ] T041 Store both user and assistant messages in Neon
- [ ] T042 [P] Store citations JSON with assistant messages
- [ ] T043 Add conversation creation on first message
- [ ] T044 Test conversation persistence across requests

**Checkpoint**: Chat history persists in database

---

## Phase 6: Frontend Integration

**Purpose**: Create React chat widget for Docusaurus

### User Story 4 - Responsive and Accessible Chat Interface (P2)

- [ ] T045 Create `src/components/Chatbot/index.tsx` with chat widget component
- [ ] T046 [P] Create `src/components/Chatbot/styles.css` with light/dark theme support
- [ ] T047 Implement floating action button (FAB) to toggle chat open/close
- [ ] T048 Implement chat window with header, messages area, and input
- [ ] T049 [P] Add typing indicator animation while waiting for response
- [ ] T050 Implement message rendering with Markdown support (react-markdown)
- [ ] T051 Implement citation link rendering with chapter titles
- [ ] T052 [P] Add auto-scroll to bottom on new messages
- [ ] T053 Implement localStorage persistence for conversation state
- [ ] T054 [P] Add keyboard shortcuts (Enter to send, Shift+Enter for newline)
- [ ] T055 Implement error handling with user-friendly error messages
- [ ] T056 Add accessibility attributes (ARIA labels, keyboard navigation)
- [ ] T057 [P] Test responsive design on mobile viewport
- [ ] T058 Create `src/theme/Root.js` to inject Chatbot component globally
- [ ] T059 Configure backend API URL for production vs development

**Checkpoint**: Chat widget renders in Docusaurus and communicates with backend

---

## Phase 7: Testing

**Purpose**: Ensure quality and correctness

- [ ] T060 [P] Create `server/tests/__init__.py` and test configuration
- [ ] T061 [P] Create `server/tests/test_chat.py` with unit tests for chat endpoint
- [ ] T062 [P] Create `server/tests/test_qdrant.py` with unit tests for search
- [ ] T063 [P] Create `server/tests/test_neon.py` with unit tests for database operations
- [ ] T064 Write integration test for full RAG pipeline
- [ ] T065 [P] Create `src/components/Chatbot/__tests__/index.test.tsx` with Jest tests
- [ ] T066 Test citation link resolution (no broken links)
- [ ] T067 Test rate limiting (more than 10 requests should fail)
- [ ] T068 Manual test: Ask "What is ROS 2 Humble?" and verify citation
- [ ] T069 Manual test: Test chat widget in both light and dark themes

**Checkpoint**: All tests passing, chat working end-to-end

---

## Phase 8: Deployment

**Purpose**: Deploy backend and configure production

- [ ] T070 Create `vercel.json` for backend deployment configuration
- [ ] T071 [P] Add environment variable secrets to Vercel project
- [ ] T072 Configure CORS to allow requests from textbook domain
- [ ] T073 [P] Update frontend API URL to production backend
- [ ] T074 Deploy FastAPI backend to Vercel/Railway
- [ ] T075 [P] Verify production API health check works
- [ ] T076 Test end-to-end chat flow in production
- [ ] T077 Add error monitoring (optional: Sentry integration)
- [ ] T078 [P] Document deployment process in README

**Checkpoint**: Chatbot live in production

---

## Phase 9: Polish & Documentation

**Purpose**: Final improvements and documentation

- [ ] T079 [P] Add loading states and error boundaries to chat widget
- [ ] T080 [P] Add chatbot disclaimer message ("Answers are based on textbook content...")
- [ ] T081 Optimize bundle size for chat widget
- [ ] T082 [P] Add analytics tracking for chat usage (optional)
- [ ] T083 Create user documentation for chatbot feature
- [ ] T084 [P] Update project README with chatbot architecture

**Checkpoint**: Feature complete and documented

---

## Dependencies & Execution Order

### Critical Path

```
Phase 1 (Setup) → Phase 2 (Database) → Phase 3 (Ingestion) → Phase 4 (RAG) → Phase 6 (Frontend) → Phase 8 (Deploy)
                                          ↓
                                    Phase 5 (History)
```

### Parallel Opportunities

- T002, T003, T006 can run in parallel (different files)
- T009, T010, T012, T013 can run in parallel (database functions)
- T017, T018, T019, T020 can run in parallel (ingestion utilities)
- T029, T032, T035 can run in parallel (RAG components)
- T046, T049, T052, T054, T057 can run in parallel (frontend styling)
- T060-T063, T065 can run in parallel (test files)

---

## Task Summary

**Total Tasks**: 84

**Tasks per Phase**:
- Phase 1 (Backend Setup): 7 tasks
- Phase 2 (Database Layer): 8 tasks
- Phase 3 (Content Ingestion): 11 tasks
- Phase 4 (RAG Implementation): 12 tasks
- Phase 5 (Chat History): 6 tasks
- Phase 6 (Frontend Integration): 15 tasks
- Phase 7 (Testing): 10 tasks
- Phase 8 (Deployment): 9 tasks
- Phase 9 (Polish): 6 tasks

**Parallel Opportunities**: ~25 tasks marked [P] can run in parallel

**MVP Scope**: Phases 1-6 (59 tasks) deliver core chatbot functionality

---

## Success Criteria Mapping

| Success Criterion | Task IDs |
|-------------------|----------|
| SC-001: Chatbot answers in < 5 seconds | T027-T033 (RAG pipeline) |
| SC-002: 100% valid citation URLs | T037, T066 (citation formatting + testing) |
| SC-003: Widget loads in < 1 second | T081 (bundle optimization) |
| SC-004: 10 concurrent requests | T038, T067 (rate limiting + testing) |
| SC-005: Chat history persists | T039-T044 (history implementation) |
| SC-006: Retrieval similarity > 0.7 | T029, T033 (search + filtering) |
| SC-007: No exposed API keys | T003, T071 (env config + secrets) |
| SC-008: WCAG 2.1 AA for chat | T056-T057 (accessibility) |

---

**Status**: Ready for implementation via `/sp.implement 006-rag-chatbot-integration`