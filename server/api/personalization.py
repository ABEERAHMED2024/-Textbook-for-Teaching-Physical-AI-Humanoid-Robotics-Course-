from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from server.services.personalization_service import PersonalizationService, BackgroundType
from server.api.auth import get_current_user
import os
import psycopg2
from datetime import datetime, timedelta
import jwt

router = APIRouter()
personalization_service = PersonalizationService()

class PersonalizeContentRequest(BaseModel):
    content: str
    user_id: Optional[str] = None

class PersonalizeContentResponse(BaseModel):
    personalized_content: str

@router.post("/personalize-content", response_model=PersonalizeContentResponse)
async def personalize_content(
    request: PersonalizeContentRequest,
    current_user: dict = Depends(get_current_user)
):
    """
    Personalize content based on user background
    """
    try:
        # Get user background from database
        user_background_str = personalization_service.get_user_background(current_user.get("user_id"))
        
        # Default to 'both' if no background is set
        if not user_background_str:
            user_background = BackgroundType.BOTH
        else:
            user_background = BackgroundType(user_background_str)
        
        # Personalize the content
        personalized_content = personalization_service.personalize_content(
            request.content, 
            user_background
        )
        
        return PersonalizeContentResponse(personalized_content=personalized_content)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error personalizing content: {str(e)}")

class GetUserBackgroundResponse(BaseModel):
    background: Optional[str]
    software_background: Optional[str]
    hardware_background: Optional[str]

@router.get("/user-background", response_model=GetUserBackgroundResponse)
async def get_user_background(
    current_user: dict = Depends(get_current_user)
):
    """
    Get the user's background information
    """
    try:
        # Connect to the database to get user background info
        db_url = os.getenv("NEON_DATABASE_URL")
        if not db_url:
            raise HTTPException(status_code=500, detail="Database URL not configured")
        
        conn = psycopg2.connect(db_url)
        with conn.cursor() as cur:
            cur.execute(
                "SELECT software_background, hardware_background FROM users WHERE email = %s", 
                (current_user.get("sub"),)
            )
            user_data = cur.fetchone()
        
        conn.close()
        
        if not user_data:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Determine overall background type based on provided information
        software_bg, hardware_bg = user_data
        
        if software_bg and hardware_bg:
            background_type = "both"
        elif software_bg:
            background_type = "software"
        elif hardware_bg:
            background_type = "hardware"
        else:
            background_type = None
        
        return GetUserBackgroundResponse(
            background=background_type,
            software_background=software_bg,
            hardware_background=hardware_bg
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving user background: {str(e)}")