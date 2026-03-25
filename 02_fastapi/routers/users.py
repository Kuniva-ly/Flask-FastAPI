from datetime import datetime
from fastapi import APIRouter
from models.users import User
from models.respond_complet import ResponseModel

router = APIRouter()

users_db: list[User] = []

@router.get("/", tags=["Users"], response_model=ResponseModel[list[User]])
def read_users():
    return ResponseModel(
        success=True,
        data=users_db,
        message="Liste des utilisateurs",
        timestamp=datetime.now()
    )

@router.post("/", tags=["Users"], response_model=ResponseModel[User])
def create_user(user: User):
    users_db.append(user)
    return ResponseModel(
        success=True,
        data=user,
        message="Utilisateur créé avec succès",
        timestamp=datetime.now()
    )
