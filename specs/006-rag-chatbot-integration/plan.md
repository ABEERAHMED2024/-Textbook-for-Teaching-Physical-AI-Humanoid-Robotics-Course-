# Implementation Plan - RAG Chatbot Integration

## Background
The hackathon requires a functional RAG chatbot to assist students. This plan outlines the setup of the FastAPI backend, Qdrant vector store, and Neon database integration.

## Proposed Changes

### Phase 1: Backend Infrastructure (FastAPI)
- [NEW] `server/main.py`: Main FastAPI entry point
- [NEW] `server/core/agent.py`: OpenAI Agent logic
- [NEW] `server/db/neon.py`: Neon Postgres integration for history
- [NEW] `server/db/qdrant.py`: Qdrant vector store service
- [NEW] `server/api/chat.py`: API endpoint for processing queries

### Phase 2: Content Ingestion
- [NEW] `scripts/ingest_content.py`: Script to parse MDX files and generate embeddings for Qdrant
- [MOD] `.github/workflows/deploy.yml`: Add ingestion step to CI/CD pipeline

### Phase 3: Frontend Integration
- [MOD] `src/theme/Root.js`: Inject the floating chat component
- [NEW] `src/components/Chatbot/index.tsx`: React chat component (ChatKit)
- [MOD] `index.css`: Styling for the chat interface

## Verification Plan

### Automated Tests
- `pytest server/tests`: Unit tests for agent logic and DB connections
- `npm run test`: Jest tests for React chat component

### Manual Verification
1. Ask the chatbot a question about the textbook.
2. Confirm the response contains a link to the correct chapter.
3. Check Neon dashboard for recorded chat history.
