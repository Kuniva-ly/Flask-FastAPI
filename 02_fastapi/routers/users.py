from fastapi import APIRouter
from models.users import User

router = APIRouter()

users_db: list[User] = []

@router.get("/", tags=["Users"])
def read_users():
    return users_db

@router.post("/", tags=["Users"])
def create_user(user: User):
    users_db.append(user)
    return user
