from better_auth import auth_handler, register_user, authenticate_user
from pydantic import BaseModel
from typing import Optional
import os


class UserRegistration(BaseModel):
    email: str
    password: str
    software_background: Optional[str] = None
    hardware_background: Optional[str] = None


class UserLogin(BaseModel):
    email: str
    password: str


# Initialize auth handler with environment variables
auth_secret = os.getenv("AUTH_SECRET", "dev-secret-key-change-in-production")
database_url = os.getenv("DATABASE_URL")


def get_auth_handler():
    """
    Initialize and return the authentication handler
    """
    handler = auth_handler(
        secret=auth_secret,
        database_url=database_url,
    )
    return handler