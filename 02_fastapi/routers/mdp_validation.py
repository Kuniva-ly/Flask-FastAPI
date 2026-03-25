from fastapi import APIRouter
from models.mdp_validation import Password

router = APIRouter()


@router.get("/", tags=["Password Validation"])
def root():
    return {"message": "FastAPI Custom Validation Demo"}


@router.post("/", tags=["Password Validation"])
def validate_password(password_data: Password):
    return {"message": "Password is valid!"}
