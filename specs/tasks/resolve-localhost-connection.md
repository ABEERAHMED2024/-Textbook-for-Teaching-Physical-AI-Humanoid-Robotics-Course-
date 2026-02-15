# Task: Resolve Localhost Connection Refused

The goal is to successfully run the Docusaurus frontend (port 3000) and the FastAPI backend (port 8000) on localhost.

## Status: IN_PROGRESS

## Todo Checklist
- [ ] Verify Python dependencies and environment variables <!-- id: 0 -->
- [ ] Fix potential FastAPI startup errors (package structure, imports) <!-- id: 1 -->
- [ ] Successfully start and verify Backend on port 8000 <!-- id: 2 -->
- [ ] Successfully start and verify Frontend on port 3000 <!-- id: 3 -->
- [ ] Perform a health check via browser subagent <!-- id: 4 -->

## Acceptance Criteria
- [ ] FastAPI backend responds at `http://localhost:8000/api/chat` or `http://localhost:8000/`
- [ ] Docusaurus frontend is accessible at `http://localhost:3000`
- [ ] No "Connection Refused" errors in browser
