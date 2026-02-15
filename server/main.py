from dotenv import load_dotenv
load_dotenv() # Load before importing any local modules that use os.getenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.api import chat
from server.api import auth
from server.api import personalization
from server.api import translation
from server.db.neon import initialize_db
import os

initialize_db()

app = FastAPI(title="Physical AI & Humanoid Robotics RAG Backend")

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(chat.router, prefix="/api")
app.include_router(auth.router, prefix="/api/auth")
app.include_router(personalization.router, prefix="/api/personalization")
app.include_router(translation.router, prefix="/api/translation")

@app.get("/")
async def root():
    return {"message": "Welcome to the Physical AI Chatbot Backend", "status": "active"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
