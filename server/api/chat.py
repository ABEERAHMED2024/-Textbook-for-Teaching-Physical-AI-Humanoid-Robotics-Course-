from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from server.core.agent import PhysicalAIAgent
from server.db.neon import save_chat
import logging

router = APIRouter()
agent = PhysicalAIAgent()

class ChatRequest(BaseModel):
    message: str
    history: Optional[List[dict]] = []

class ChatResponse(BaseModel):
    answer: str
    citations: List[str] = []

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        response = await agent.generate_response(request.message, request.history)
        # Save to Neon
        save_chat(request.message, response["answer"])
        return ChatResponse(
            answer=response["answer"],
            citations=response["citations"]
        )
    except Exception as e:
        logging.error(f"Error in chat endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))
