from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.database import get_db
from models.player import Player
from models.user import User
from schemas.player import PlayerCreate, PlayerResponse
from core.dependencies import get_current_user

router = APIRouter(prefix="/players", tags=["Players"])


@router.post("/", response_model=PlayerResponse, status_code=status.HTTP_201_CREATED)
def create_player(
    player_create: PlayerCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if db.query(Player).filter(Player.nickname == player_create.nickname).first():
        raise HTTPException(status_code=400, detail="Nickname already exists")

    new_player = Player(nickname=player_create.nickname)
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player


@router.get("/", response_model=list[PlayerResponse])
def get_players(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return db.query(Player).all()


@router.get("/{player_id}", response_model=PlayerResponse)
def get_player(
    player_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    player = db.query(Player).filter(Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player
