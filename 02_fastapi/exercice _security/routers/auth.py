from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.dependencies import get_current_user

from db.database import get_db
from schemas.user import UserCreate, UserLogin, UserResponse
from schemas.token import Token
from models.user import User
from core.security import hash_password, verify_password, create_access_token


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_create: UserCreate, db: Session = Depends(get_db)):
    """Enregistre un nouvel utilisateur."""

    if db.query(User).filter(User.username == user_create.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")

    if db.query(User).filter(User.email == user_create.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = User(
        username=user_create.username,
        email=user_create.email,
        full_name=user_create.full_name,
        hashed_password=hash_password(user_create.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login", response_model=Token)
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    """Connecte un utilisateur et retourne un JWT."""

    user = db.query(User).filter(User.username == user_login.username).first()

    if not user or not verify_password(user_login.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
def read_current_user(current_user: User = Depends(get_current_user)):
    """Retourne les informations de l'utilisateur connecté."""
    return current_user

