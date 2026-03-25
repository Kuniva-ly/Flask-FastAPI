from datetime import datetime
from fastapi import APIRouter
from models.respond_complet import ResponseModel

router = APIRouter()

@router.get("/text", tags=["ResponseModel"], response_model=ResponseModel[str])
def test_response_text():
    return ResponseModel(
        success=True,
        data="Bonjour depuis ResponseModel[str]",
        message="Test avec une chaîne",
        timestamp=datetime.now()
    )
