# Feature Specification: RAG Chatbot Integration

**Feature Branch**: `006-rag-chatbot-integration`
**Created**: 2025-01-05
**Status**: Draft
**Input**: User description: "Integrate a RAG-powered chatbot into the textbook to help students ask questions about content and receive cited answers"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ask Questions About Content (Priority: P1)

As a **student** of the Physical AI course, I need to ask natural language questions about the textbook content so that I can clarify complex robotics concepts in real-time without searching through multiple chapters.

**Why this priority**: This is the core value proposition of the chatbot. Students need immediate answers to questions that arise while studying.

**Independent Test**: Can be fully tested by opening the chat widget, asking a question about ROS 2 or robotics, and receiving an answer with citations.

**Acceptance Scenarios**:

1. **Given** I am on any textbook page, **When** I open the chat widget and type "What is ROS 2 Humble?", **Then** I receive an answer explaining ROS 2 Humble with citations from Module 1 chapters
2. **Given** I ask a question about a specific topic, **When** the chatbot responds, **Then** I see clickable links to the source chapter sections
3. **Given** I ask about a term defined in the glossary, **When** the chatbot responds, **Then** the glossary definition is included or referenced in the answer
4. **Given** I ask a question outside the textbook scope, **When** the chatbot responds, **Then** it clearly states "I couldn't find information about that in the textbook" instead of hallucinating

---

### User Story 2 - Receive Cited Answers (Priority: P1)

As a **student**, I need to see source citations for chatbot answers so that I can verify the information and read more context in the original chapters.

**Why this priority**: Citations are essential for academic integrity and for students to trust the chatbot's answers.

**Independent Test**: Can be fully tested by asking a question and verifying that each citation link navigates to the correct chapter.

**Acceptance Scenarios**:

1. **Given** the chatbot provides an answer, **When** I view the response, **Then** I see at least one citation with a clickable chapter link
2. **Given** I click a citation link, **When** the page opens, **Then** it navigates to the correct chapter URL (no broken links)
3. **Given** the chatbot quotes specific content, **When** I view the citation, **Then** the cited text exists in the referenced chapter
4. **Given** multiple sources are relevant, **When** the chatbot responds, **Then** I see up to 3 citations ranked by relevance

---

### User Story 3 - View Chat History (Priority: P2)

As a **student**, I need my chat history to persist across sessions so that I can review previous questions and answers without re-asking.

**Why this priority**: Improves user experience but not critical for MVP. Students can always re-ask questions.

**Independent Test**: Can be fully tested by asking questions, refreshing the page, and verifying the conversation is restored.

**Acceptance Scenarios**:

1. **Given** I have asked questions before, **When** I open the chat widget, **Then** I see my recent conversation history (last 10 messages)
2. **Given** I refresh the page, **When** I reopen the chat widget, **Then** my conversation is restored from the database
3. **Given** I clear my browser data, **When** I reopen the chat, **Then** I see an empty conversation (no cross-device sync required for MVP)

---

### User Story 4 - Responsive and Accessible Chat Interface (Priority: P2)

As a **student** using various devices, I need the chat widget to work on desktop and mobile with keyboard accessibility so that I can use it regardless of my setup.

**Why this priority**: Accessibility compliance and mobile support are important but secondary to core functionality.

**Independent Test**: Can be fully tested by opening chat on mobile viewport and navigating with keyboard only.

**Acceptance Scenarios**:

1. **Given** I am on a mobile device, **When** I open the chat widget, **Then** it expands to a usable size without overlapping content
2. **Given** I use keyboard navigation, **When** I tab through the chat interface, **Then** all interactive elements are reachable
3. **Given** I use a screen reader, **When** I interact with chat, **Then** messages are announced appropriately
4. **Given** the site is in dark mode, **When** I open the chat, **Then** the chat theme matches the site theme

---

### Edge Cases

- What happens when the Qdrant vector database is unavailable? → Display error message: "Search is temporarily unavailable. Please try again later."
- What happens when the OpenAI API times out? → Retry with exponential backoff (2 retries), then display error message
- What happens when a question is ambiguous? → Ask clarifying question: "Could you clarify what you mean by..."
- What happens when content is chunked mid-sentence? → Chunk by section headers (H2/H3) to avoid mid-sentence breaks
- What happens when the user enters an empty message? → Disable send button until text is entered
- What happens with very long questions (>500 chars)? → Truncate or summarize before sending to API

## Requirements *(mandatory)*

### Frontend Requirements

- **FR-001**: Chat widget MUST be accessible from all pages via a floating button in the bottom-right corner
- **FR-002**: Chat widget MUST support both light and dark Docusaurus themes automatically
- **FR-003**: Chat input MUST support multi-line questions (Shift+Enter for new line)
- **FR-004**: Chat responses MUST render Markdown formatting (code blocks, bold, lists, links)
- **FR-005**: Citation links MUST use correct Docusaurus URL format (relative URLs: `/docs/module-1-ros2/chapter-1#section`)
- **FR-006**: Chat widget MUST be collapsible and remember open/closed state in localStorage
- **FR-007**: Chat widget MUST show typing indicator while waiting for response

### Backend Requirements

- **FR-008**: FastAPI server MUST expose `/api/chat` endpoint accepting POST requests with `{ message, conversation_id? }`
- **FR-009**: Backend MUST use OpenAI API (GPT-4 or GPT-3.5-turbo) for response generation
- **FR-010**: Backend MUST query Qdrant Cloud for semantic search over textbook content chunks
- **FR-011**: Backend MUST store chat history in Neon Serverless Postgres with schema: `(id, conversation_id, role, content, citations, created_at)`
- **FR-012**: Backend MUST generate citations from Qdrant search results with format: `{ chapter_id, section_title, url_path, excerpt }`
- **FR-013**: Backend MUST limit context to top 5 most relevant chunks to avoid token limits
- **FR-014**: Backend MUST return responses within 10 seconds (timeout threshold)
- **FR-015**: Backend MUST validate and sanitize user input (no XSS, no SQL injection)
- **FR-016**: Backend MUST use environment variables for all secrets (OPENAI_API_KEY, QDRANT_URL, QDRANT_API_KEY, DATABASE_URL)

### Content Ingestion Requirements

- **FR-017**: Ingestion script MUST parse all MDX files in `docs/` directory recursively
- **FR-018**: Ingestion MUST chunk content by H2 and H3 section headers (not mid-sentence)
- **FR-019**: Each chunk MUST include metadata: `{ chapter_id, chapter_title, section_title, url_path, chunk_index }`
- **FR-020**: Embeddings MUST be generated using OpenAI text-embedding-3-small model
- **FR-021**: Ingestion MUST be idempotent (re-running doesn't create duplicates)
- **FR-022**: Ingestion script MUST be runnable via `npm run ingest` or `python scripts/ingest_content.py`

### Security Requirements

- **FR-023**: API keys MUST NOT be exposed in client-side code
- **FR-024**: Backend MUST implement rate limiting (10 requests per minute per IP)
- **FR-025**: Backend MUST validate CORS to only allow requests from the textbook domain

## Key Entities

- **ChatMessage**: Represents a single message in a conversation. Fields: `id`, `conversation_id`, `role` (user/assistant), `content`, `citations` (JSON array), `created_at`
- **Conversation**: Represents a chat session. Fields: `id`, `user_identifier` (optional), `created_at`, `updated_at`
- **ContentChunk**: Represents an indexed piece of textbook content. Fields: `id`, `chapter_id`, `chapter_title`, `section_title`, `url_path`, `content`, `embedding` (vector)
- **Citation**: Represents a reference to source content. Fields: `chapter_id`, `section_title`, `url_path`, `excerpt`

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Chatbot answers "What is ROS 2 Humble?" with correct citation within 5 seconds
- **SC-002**: 100% of citation links in generated responses point to valid, non-broken URLs
- **SC-003**: Chat widget loads and becomes interactive within 1 second on any page
- **SC-004**: Backend handles 10 concurrent requests without timeout or error
- **SC-005**: Chat history persists across page refreshes (retrieved from database)
- **SC-006**: RAG retrieval returns relevant chunks with cosine similarity > 0.7 for textbook questions
- **SC-007**: Zero API keys or secrets exposed in client-side JavaScript bundles
- **SC-008**: Chat widget passes WCAG 2.1 AA accessibility audit for keyboard navigation

## Assumptions *(mandatory)*

- Qdrant Cloud Free Tier is available and sufficient for textbook content (~100-500 chunks)
- Neon Serverless Postgres Free Tier is available for chat history storage
- OpenAI API access is available with sufficient rate limits
- Docusaurus content is structured in MDX with consistent heading hierarchy
- Students have internet access (chatbot requires backend connection)
- MVP does not require authentication (anonymous chat sessions identified by browser fingerprint or cookie)

## Dependencies *(mandatory)*

### External Dependencies
- **Qdrant Cloud**: Vector database for semantic search (Free Tier)
- **Neon Postgres**: Serverless Postgres for chat history (Free Tier)
- **OpenAI API**: GPT-4 or GPT-3.5-turbo for response generation, text-embedding-3-small for embeddings

### Internal Dependencies
- **Docusaurus**: React-based frontend for chat widget integration
- **001-book-master-plan**: Content structure defines chunking strategy
- **002-chapter-template-system**: Consistent chapter structure aids parsing

## Out of Scope *(optional)*

- User authentication and accounts (anonymous sessions only for MVP)
- Multi-language support (English only)
- Voice input/output
- Streaming responses (SSE) - can be added later
- Conversation export or sharing
- Admin dashboard for monitoring queries
- Fine-tuning the embedding model on textbook content
- Real-time collaborative chat

## Risks and Mitigations *(optional)*

- **Risk**: Hallucination of robotics physical safety advice
  - **Mitigation**: Strict RAG grounding - only answer from retrieved chunks, explicit disclaimer in UI

- **Risk**: Token limit issues with large chapters
  - **Mitigation**: Chunk by section headers, limit context to top 5 chunks (~15k tokens)

- **Risk**: Latency in RAG response
  - **Mitigation**: Use Qdrant Cloud with low-latency region, cache common queries

- **Risk**: API cost overruns
  - **Mitigation**: Set OpenAI usage limits, implement rate limiting, monitor daily spend

- **Risk**: Qdrant/Neon service outage
  - **Mitigation**: Graceful error messages, retry logic, consider fallback to static FAQ