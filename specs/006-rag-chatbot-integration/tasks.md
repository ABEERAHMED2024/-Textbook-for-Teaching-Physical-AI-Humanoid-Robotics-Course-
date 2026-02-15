# Tasks - RAG Chatbot Integration

## Phase 1: Planning & Specification
- [x] Create RAG chatbot specification (`spec.md`)
- [x] Create RAG chatbot implementation plan (`plan.md`)
- [ ] Review plan with user

## Phase 2: Ingestion Pipeline
- [x] Create `scripts/ingest_content.py`
- [/] Implement MDX chunking logic
- [/] Connect to Qdrant Cloud for embedding storage
- [ ] Verify ingestion of introductory chapters

## Phase 3: Backend Implementation (FastAPI)
- [/] Initialize FastAPI project in `server/`
- [ ] Implement `/api/chat` endpoint
- [ ] Integrate OpenAI Agents SDK
- [ ] Connect to Neon Postgres for history tracking
- [ ] Implement citation generation logic

## Phase 4: Frontend Integration (Docusaurus)
- [ ] Install `@chatkit/react` or equivalent (Custom implementation used)
- [x] Create `src/components/Chatbot` component
- [x] Inject chat component into `src/theme/Root.js`
- [x] Style chat interface to match textbook theme

## Phase 5: Testing & Deployment
- [ ] Verify end-to-end chat flow
- [ ] Test citation links (Doc IDs)
- [ ] Deploy FastAPI to cloud (e.g., Vercel or Railway)
- [ ] Finalize GitHub Pages deployment
