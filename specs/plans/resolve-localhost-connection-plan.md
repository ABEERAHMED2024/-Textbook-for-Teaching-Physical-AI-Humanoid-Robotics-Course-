# Architecture Plan: Localhost Deployment Fix

This plan addresses the "localhost refused to connect" error by systematic verification and controlled startup of the textbook application services.

## 1. Scope
- **In Scope**: Backend (FastAPI) and Frontend (Docusaurus) local execution.
- **Out of Scope**: External cloud deployment, SSL setup.

## 2. Key Decisions
- **Manual Verification**: Run services with explicit logging to detect immediate crashes.
- **Package Correction**: Ensure the Python backend is treated as a module to handle relative imports.
- **Port Conflict Check**: Ensure ports 3000 and 8000 are not occupied by other processes.

## 3. Implementation Steps
1. **Dependency Audit**: Run `pip install -r server/requirements.txt` to ensure the environment is ready.
2. **Backend Patching**: I have already added `__init__.py` files. I will now ensure the path handling in `main.py` is robust.
3. **Controlled Startup**: 
    - Use `python -m server.main` to start the backend.
    - Use `npm run start` for the frontend.
4. **Validation**: Check logs and use browser tools to verify.

##  acceptance_criteria
- Backend Root GET returns 200 OK.
- Frontend Home Page loads without error.
