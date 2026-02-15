from dotenv import load_dotenv
load_dotenv() # Load before importing any local modules that use os.getenv

from fastapi import FastAPI
from server.api import chat
from server.db.neon import initialize_db
import os

initialize_db()

app = FastAPI(title="Physical AI & Humanoid Robotics RAG Backend")

# Register routes
app.include_router(chat.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to the Physical AI Chatbot Backend", "status": "active"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
