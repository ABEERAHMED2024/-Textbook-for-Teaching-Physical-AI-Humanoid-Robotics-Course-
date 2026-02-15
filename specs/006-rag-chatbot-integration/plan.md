# Implementation Plan: RAG Chatbot Integration

**Branch**: `006-rag-chatbot-integration` | **Date**: 2025-02-14 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/006-rag-chatbot-integration/spec.md`

## Summary

Integrate a RAG-powered chatbot into the Physical AI textbook to help students ask questions about content and receive accurate, cited answers. The system uses FastAPI backend with OpenAI for response generation, Qdrant Cloud for semantic search, and Neon Postgres for chat history. A React-based chat widget integrates into the Docusaurus frontend.

**Technical Approach**: Chunk textbook MDX content by section headers, generate embeddings with OpenAI text-embedding-3-small, store in Qdrant Cloud. FastAPI backend queries Qdrant for relevant chunks, sends context to GPT-4, returns answer with citations. React chat component in Docusaurus theme calls backend API.

## Technical Context

**Language/Version**: Python 3.10+ (backend), TypeScript/React 18.x (frontend)
**Primary Dependencies**:
- Backend: FastAPI, OpenAI SDK, qdrant-client, asyncpg, python-dotenv
- Frontend: React 18.x, Docusaurus 3.x
- Infrastructure: Qdrant Cloud, Neon Serverless Postgres

**Storage**:
- Qdrant Cloud: Vector embeddings for ~100-500 content chunks
- Neon Postgres: Chat history (conversations, messages)

**Testing**:
- Backend: pytest for unit/integration tests
- Frontend: Jest + React Testing Library
- E2E: Manual testing of chat flow

**Target Platform**:
- Frontend: GitHub Pages (Docusaurus static site)
- Backend: Vercel, Railway, or similar serverless platform

**Performance Goals**:
- Chat response: < 5 seconds end-to-end
- Search retrieval: < 500ms
- Widget load: < 1 second

**Constraints**:
- No authentication required for MVP
- API keys must not be exposed client-side
- Must work with Docusaurus React theme

**Scale/Scope**:
- ~50-100 textbook pages to ingest
- ~100-500 content chunks
- 10 concurrent users expected (hackathon demo)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Principle I: Content Accuracy & Technical Rigor
- ✅ **Pass**: RAG ensures answers are grounded in textbook content
- 📝 **Requirement**: Citations must link to verified chapter URLs

### Principle II: Educational Clarity & Accessibility
- ✅ **Pass**: Chat widget helps students clarify concepts
- 📝 **Requirement**: Must support keyboard navigation and screen readers

### Principle III: Consistency & Standards
- ✅ **Pass**: Uses existing Docusaurus theming
- 📝 **Requirement**: Chat styling must match light/dark themes

### Principle IV: Docusaurus Structure & Quality
- ✅ **Pass**: Integrated as React component in theme
- 📝 **Requirement**: Must not break Docusaurus build

### Principle V: Code Example Quality
- ✅ **Pass**: N/A - no code examples in this feature

### Principle VI: Deployment & Publishing Standards
- ✅ **Pass**: Backend deployed separately, frontend builds with Docusaurus
- 📝 **Requirement**: Environment variables for secrets

**Overall Status**: ✅ PASS

## Project Structure

### Documentation (this feature)

```text
specs/006-rag-chatbot-integration/
├── spec.md                # Feature specification
├── plan.md                # This file
└── tasks.md               # Implementation tasks
```

### Source Code (repository root)

```text
server/
├── __init__.py
├── main.py                         # FastAPI entry point
├── core/
│   ├── __init__.py
│   ├── config.py                   # Environment config
│   └── agent.py                    # OpenAI Agent / RAG logic
├── api/
│   ├── __init__.py
│   └── chat.py                     # /api/chat endpoint
├── db/
│   ├── __init__.py
│   ├── neon.py                     # Neon Postgres connection
│   └── qdrant.py                   # Qdrant client
├── models/
│   ├── __init__.py
│   └── schemas.py                  # Pydantic models
└── requirements.txt

scripts/
└── ingest_content.py               # Content ingestion script

src/
├── components/
│   └── Chatbot/
│       ├── index.tsx               # Chat widget component
│       └── styles.css              # Chat widget styles
└── theme/
    └── Root.js                     # Inject chat widget into Docusaurus

.env.example                        # Environment variable template
vercel.json                         # Vercel deployment config (optional)
```

**Structure Decision**: FastAPI backend in `server/` directory, React frontend component in `src/components/Chatbot/`, content ingestion script in `scripts/`. This follows the existing project structure established in previous features.

## Phase 0: Research & Technology Decisions

**Status**: ⏳ PENDING

### Research Tasks

1. **Qdrant Cloud Setup**
   - Create Qdrant Cloud account and cluster
   - Determine collection schema and vector size (1536 for text-embedding-3-small)
   - Test connection and basic operations

2. **Neon Postgres Setup**
   - Create Neon project and database
   - Design chat history schema
   - Test connection from FastAPI

3. **OpenAI API Integration**
   - Test text-embedding-3-small for embeddings
   - Test GPT-4 or GPT-3.5-turbo for chat completion
   - Determine optimal chunk size and context window

4. **Docusaurus React Integration**
   - Research best approach for global React component in Docusaurus
   - Test theme/swizzle approach vs. Root.js injection
   - Verify theme switching works for chat widget

**Output**: Research notes and environment setup completion

---

## Phase 1: Backend Implementation

### 1.1 Project Setup

- Create `server/` directory structure
- Initialize FastAPI application with CORS middleware
- Configure environment variables (OPENAI_API_KEY, QDRANT_URL, DATABASE_URL)
- Set up Python dependencies in `requirements.txt`

### 1.2 Database Layer

**Neon Postgres Schema**:

```sql
CREATE TABLE conversations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_identifier VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE messages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    conversation_id UUID REFERENCES conversations(id),
    role VARCHAR(20) NOT NULL, -- 'user' or 'assistant'
    content TEXT NOT NULL,
    citations JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_messages_conversation ON messages(conversation_id);
```

**Qdrant Collection Schema**:

```json
{
  "name": "textbook_chunks",
  "vectors": {
    "size": 1536,
    "distance": "Cosine"
  },
  "payload_schema": {
    "chapter_id": "keyword",
    "chapter_title": "text",
    "section_title": "text",
    "url_path": "keyword",
    "content": "text",
    "chunk_index": "integer"
  }
}
```

### 1.3 API Endpoints

**POST /api/chat**
- Request: `{ "message": string, "conversation_id": string? }`
- Response: `{ "response": string, "citations": Citation[], "conversation_id": string }`
- Flow:
  1. Generate embedding for user message
  2. Query Qdrant for top 5 relevant chunks
  3. Build context from chunks
  4. Send to OpenAI with system prompt
  5. Store message pair in Neon
  6. Return response with citations

**GET /api/conversations/{id}**
- Response: `{ "messages": Message[] }`
- Returns last 10 messages for conversation

### 1.4 RAG Pipeline

```python
# Pseudocode for RAG flow
async def chat(message: str, conversation_id: str | None):
    # 1. Get embedding
    embedding = await openai.embed(message)

    # 2. Search Qdrant
    chunks = await qdrant.search(embedding, limit=5)

    # 3. Build context
    context = "\n\n".join([c.payload["content"] for c in chunks])

    # 4. Build prompt
    system_prompt = """You are a helpful assistant for the Physical AI textbook.
    Answer questions based ONLY on the provided context.
    Always cite your sources using the chapter titles provided.
    If you cannot find the answer in the context, say so clearly."""

    # 5. Get completion
    response = await openai.chat(system_prompt, context, message)

    # 6. Build citations
    citations = [Citation.from_chunk(c) for c in chunks if c.score > 0.7]

    # 7. Store and return
    await store_message(conversation_id, message, response, citations)
    return {"response": response, "citations": citations}
```

---

## Phase 2: Content Ingestion

### 2.1 MDX Parser

```python
# scripts/ingest_content.py

def parse_mdx_files(docs_dir: str) -> list[ContentChunk]:
    """Parse all MDX files and chunk by H2/H3 sections."""
    chunks = []
    for filepath in glob(f"{docs_dir}/**/*.mdx"):
        content = read_file(filepath)
        frontmatter, body = parse_frontmatter(content)

        # Chunk by sections
        sections = split_by_headers(body, ["##", "###"])
        for i, section in enumerate(sections):
            chunk = ContentChunk(
                chapter_id=get_chapter_id(filepath),
                chapter_title=frontmatter.get("title"),
                section_title=section.header,
                url_path=get_url_path(filepath, section.header),
                content=section.text,
                chunk_index=i
            )
            chunks.append(chunk)

    return chunks
```

### 2.2 Embedding Generation

```python
async def generate_embeddings(chunks: list[ContentChunk]) -> list[Embedding]:
    """Generate embeddings for all chunks using OpenAI."""
    embeddings = []
    for batch in batched(chunks, 100):  # Batch to avoid rate limits
        texts = [c.content for c in batch]
        response = await openai.embeddings.create(
            input=texts,
            model="text-embedding-3-small"
        )
        embeddings.extend([e.embedding for e in response.data])
    return embeddings
```

### 2.3 Qdrant Upsert

```python
async def upsert_chunks(chunks: list[ContentChunk], embeddings: list[Embedding]):
    """Upsert chunks with embeddings to Qdrant."""
    points = [
        PointStruct(
            id=generate_uuid(),
            vector=embedding,
            payload=chunk.dict()
        )
        for chunk, embedding in zip(chunks, embeddings)
    ]
    await qdrant.upsert(collection_name="textbook_chunks", points=points)
```

---

## Phase 3: Frontend Integration

### 3.1 Chat Widget Component

```tsx
// src/components/Chatbot/index.tsx

import React, { useState, useEffect, useRef } from 'react';
import './styles.css';

interface Message {
  role: 'user' | 'assistant';
  content: string;
  citations?: Citation[];
}

interface Citation {
  chapter_title: string;
  url_path: string;
  excerpt: string;
}

export default function Chatbot() {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Load conversation from localStorage on mount
  useEffect(() => {
    const saved = localStorage.getItem('chat-conversation');
    if (saved) {
      setMessages(JSON.parse(saved));
    }
  }, []);

  // Save conversation when messages change
  useEffect(() => {
    localStorage.setItem('chat-conversation', JSON.stringify(messages));
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim() || isLoading) return;

    const userMessage: Message = { role: 'user', content: input };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input })
      });

      const data = await response.json();
      const assistantMessage: Message = {
        role: 'assistant',
        content: data.response,
        citations: data.citations
      };
      setMessages(prev => [...prev, assistantMessage]);
    } catch (error) {
      // Handle error
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="chatbot-container">
      {isOpen ? (
        <div className="chatbot-window">
          <div className="chatbot-header">
            <span>Physical AI Assistant</span>
            <button onClick={() => setIsOpen(false)}>×</button>
          </div>
          <div className="chatbot-messages">
            {messages.map((msg, i) => (
              <div key={i} className={`chatbot-message ${msg.role}`}>
                <ReactMarkdown>{msg.content}</ReactMarkdown>
                {msg.citations?.map((c, j) => (
                  <a key={j} href={c.url_path} className="citation-link">
                    📖 {c.chapter_title}
                  </a>
                ))}
              </div>
            ))}
            {isLoading && <div className="chatbot-typing">...</div>}
            <div ref={messagesEndRef} />
          </div>
          <div className="chatbot-input">
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === 'Enter' && !e.shiftKey) {
                  e.preventDefault();
                  sendMessage();
                }
              }}
              placeholder="Ask about ROS 2, robotics, or the textbook..."
            />
            <button onClick={sendMessage} disabled={isLoading}>Send</button>
          </div>
        </div>
      ) : (
        <button className="chatbot-fab" onClick={() => setIsOpen(true)}>
          💬
        </button>
      )}
    </div>
  );
}
```

### 3.2 Theme Integration

```tsx
// src/theme/Root.js

import React from 'react';
import Root from '@theme-original/Root';
import Chatbot from '@site/src/components/Chatbot';

export default function RootWrapper(props) {
  return (
    <>
      <Root {...props} />
      <Chatbot />
    </>
  );
}
```

---

## Phase 4: Testing & Deployment

### 4.1 Backend Testing

```python
# server/tests/test_chat.py

import pytest
from fastapi.testclient import TestClient
from server.main import app

client = TestClient(app)

def test_chat_endpoint_returns_response():
    response = client.post("/api/chat", json={
        "message": "What is ROS 2 Humble?"
    })
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert "citations" in data

def test_chat_endpoint_with_conversation_id():
    response = client.post("/api/chat", json={
        "message": "Tell me more",
        "conversation_id": "test-id"
    })
    assert response.status_code == 200

def test_citations_have_valid_urls():
    response = client.post("/api/chat", json={
        "message": "What is a ROS 2 node?"
    })
    data = response.json()
    for citation in data.get("citations", []):
        assert citation["url_path"].startswith("/docs/")
```

### 4.2 Deployment Configuration

**Vercel (Backend)**:

```json
// vercel.json
{
  "builds": [
    { "src": "server/main.py", "use": "@vercel/python" }
  ],
  "routes": [
    { "src": "/api/(.*)", "dest": "server/main.py" }
  ],
  "env": {
    "OPENAI_API_KEY": "@openai-api-key",
    "QDRANT_URL": "@qdrant-url",
    "DATABASE_URL": "@database-url"
  }
}
```

**Environment Variables**:
- `OPENAI_API_KEY`: OpenAI API key
- `QDRANT_URL`: Qdrant Cloud cluster URL
- `QDRANT_API_KEY`: Qdrant API key
- `DATABASE_URL`: Neon Postgres connection string

---

## Next Steps

1. Set up Qdrant Cloud cluster and Neon database
2. Implement backend API (Phase 1)
3. Create content ingestion script (Phase 2)
4. Ingest textbook content
5. Implement frontend chat widget (Phase 3)
6. Test end-to-end flow (Phase 4)
7. Deploy backend and frontend

**Current Status**: Ready for implementation via `/sp.tasks`

**Branch**: `006-rag-chatbot-integration`
**Spec**: [specs/006-rag-chatbot-integration/spec.md](./spec.md)