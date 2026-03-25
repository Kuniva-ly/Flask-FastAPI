from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional, List
from datetime import datetime
import uvicorn
import re


app = FastAPI(
    title="Password avec validation",
    description="API pour gérer les mots de passe avec validation",
    version="1.0.0"
)
router = APIRouter()
# Créez un modèle `Password` avec validation:
# - `password`: au moins 8 caractères, doit contenir minuscule, majuscule, chiffre, symbole
# - `confirm_password`: doit égaler `password`

class Password(BaseModel):
    password : str = Field(..., min_length=8, description="Le mot de passe doit comporter au moins 8 caractères")
    confirm_password : str = Field(..., min_length=8, description="La confirmation du mot de passe doit correspondre au mot de passe")

    @field_validator('password')
    @classmethod
    def validate_password_strength(cls, v):
        """
        Custom password strength validation
        Must contain uppercase, lowercase, digit, and special char
        """
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'\d', v):
            raise ValueError('Password must contain at least one digit')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', v):
            raise ValueError('Password must contain at least one special character')
        return v

    @field_validator('confirm_password')
    @classmethod
    def validate_passwords_match(cls, v, info):
        if 'password' in info.data and v != info.data['password']:
            raise ValueError('Passwords do not match')
        return v
    
@router.get("/", tags=["Root"])
def root():
    """Root endpoint"""
    return {"message": "FastAPI Custom Validation Demo"}

@router.post("/validate-password", tags=["Password Validation"])
def validate_password(password_data: Password):
    """Endpoint to validate password strength and confirmation"""
    return {"message": "Password is valid!"}

app.include_router(router)
