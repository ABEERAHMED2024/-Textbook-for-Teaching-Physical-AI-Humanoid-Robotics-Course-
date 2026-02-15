from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from server.services.translation_service import TranslationService
from server.api.auth import get_current_user
import asyncio

router = APIRouter()
translation_service = TranslationService()

class TranslateRequest(BaseModel):
    text: str
    source_lang: str = "en"
    target_lang: str = "ur"

class TranslateResponse(BaseModel):
    original_text: str
    translated_text: str
    source_lang: str
    target_lang: str

@router.post("/translate", response_model=TranslateResponse)
async def translate_text(
    request: TranslateRequest,
    current_user: dict = Depends(get_current_user)
):
    """
    Translate text to Urdu
    """
    try:
        # Only allow translation to Urdu for this implementation
        if request.target_lang != "ur":
            raise HTTPException(status_code=400, detail="Only Urdu translation is supported")
        
        # Perform translation
        translated_text = await translation_service.translate_to_urdu_async(request.text)
        
        return TranslateResponse(
            original_text=request.text,
            translated_text=translated_text,
            source_lang=request.source_lang,
            target_lang=request.target_lang
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error translating text: {str(e)}")

class TranslateDocumentRequest(BaseModel):
    content: str
    source_lang: str = "en"
    target_lang: str = "ur"

class TranslateDocumentResponse(BaseModel):
    original_content: str
    translated_content: str
    source_lang: str
    target_lang: str

@router.post("/translate-document", response_model=TranslateDocumentResponse)
async def translate_document(
    request: TranslateDocumentRequest,
    current_user: dict = Depends(get_current_user)
):
    """
    Translate a document to Urdu
    """
    try:
        # Only allow translation to Urdu for this implementation
        if request.target_lang != "ur":
            raise HTTPException(status_code=400, detail="Only Urdu translation is supported")
        
        # Perform document translation
        translated_content = translation_service.translate_document(request.content)
        
        return TranslateDocumentResponse(
            original_content=request.content,
            translated_content=translated_content,
            source_lang=request.source_lang,
            target_lang=request.target_lang
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error translating document: {str(e)}")