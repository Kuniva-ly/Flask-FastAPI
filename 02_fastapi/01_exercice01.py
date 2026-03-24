from fastapi import FastAPI
from typing import Optional

from pydantic import BaseModel, EmailStr, Field
import uvicorn


app = FastAPI(
    title="FastAPI Pydantic User Demo",
    description="Simple FastAPI application with Pydantic models for user data",
    version="1.0.0"
)

class User(BaseModel):
    id: int = Field(..., frozen=True, description="Non-modifiable user ID")
    username: str = Field(..., min_length=2, max_length=50, description="Username must be between 2 and 50 characters")
    email: EmailStr
    age: Optional[int] = Field(None, ge=0, le=150, description="Age must be between 0 and 150")
    is_active: bool = Field(default=True, description="Indicates if the user is active")

@app.post("/users", tags=["Users"])
def create_user(user: User):
    return user

if __name__ == "__main__":
    uvicorn.run(app, port=8000)