# Case Study: RAG Chatbot Integration (006-rag-chatbot-integration)

## User Story
As a student of the Physical AI course, I want to ask questions about the textbook content and receive accurate, cited answers from an AI assistant, so that I can clarify complex robotics concepts in real-time.

## Success Criteria
- [ ] RAG Chatbot integrated into Docusaurus UI (floating chat or sidebar)
- [ ] Backend powered by FastAPI (Python)
- [ ] Vector database (Qdrant Cloud) contains embeddings for all 13 weeks of content
- [ ] Chat history persisted in Neon Serverless Postgres
- [ ] Integration with OpenAI Agents SDK or ChatKit
- [ ] Capability to provide source citations from the textbook
- [ ] 0 broken links in generated responses

## Assumptions
- Qdrant Cloud Cluster is available (Free Tier)
- Neon Postgres instance is provisioned
- OpenAI API Key is available
- Docusaurus content is structured in MDX

## Constraints
- MUST use standard Hackathon stack (FastAPI, Neon, Qdrant, OpenAI Agents/ChatKit)
- MUST avoid exposing API keys in client-side code
- Chat window MUST be responsive and accessible

## Risks
- Hallucination of robotics physical safety advice (must be strictly grounded)
- Token limit issues with large chapters
- latency in RAG response if indexing is inefficient

## Technical Context
- **Frontend**: React-based chat component integrated into Docusaurus theme
- **Backend**: FastAPI service with endpoints for ingestion and query
- **Orchestration**: OpenAI Agents SDK
- **Vector Store**: Qdrant (semantic search)
- **Database**: Neon (metadata and chat history)

## Acceptance Tests
- **Test 1**: Verify that selecting text in the book can trigger a chat question.
- **Test 2**: Verify that the chatbot can answer "What is ROS 2 Humble?" using book content.
- **Test 3**: Verify that citations point to correctly formatted Doc IDs.
