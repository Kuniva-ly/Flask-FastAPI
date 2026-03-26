from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    """Schema for creating a new user."""
    username: str
    email: EmailStr
    full_name: str | None = None
    password: str

class UserLogin(BaseModel):
    """Schema for user login."""
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str | None = None

    model_config = {"from_attributes": True}
