from fastapi import APIRouter
from models.settings import settings

router = APIRouter()

@router.get("/", tags=["Settings"])
def get_settings():
    return {
        "app_name": settings.app_name,
        "debug": settings.debug,
        "api_v1_prefix": settings.api_v1_prefix
    }
