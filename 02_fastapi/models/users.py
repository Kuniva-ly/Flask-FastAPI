from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    id: int = Field(..., frozen=True, description="Non-modifiable user ID")
    username: str = Field(..., min_length=2, max_length=50, description="Username must be between 2 and 50 characters")
    email: EmailStr
    age: Optional[int] = Field(None, ge=0, le=150, description="Age must be between 0 and 150")
    is_active: bool = Field(default=True, description="Indicates if the user is active")
