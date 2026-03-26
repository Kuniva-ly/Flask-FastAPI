from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.database import get_db
from models.team import Team
from models.player import Player
from models.user import User
from schemas.team import TeamCreate, TeamResponse
from core.dependencies import get_current_user

router = APIRouter(prefix="/teams", tags=["Teams"])


@router.post("/", response_model=TeamResponse, status_code=status.HTTP_201_CREATED)
def create_team(
    team_create: TeamCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if team_create.player1_id == team_create.player2_id:
        raise HTTPException(status_code=400, detail="Players must be different")

    if db.query(Team).filter(Team.name == team_create.name).first():
        raise HTTPException(status_code=400, detail="Team name already exists")

    player1 = db.query(Player).filter(Player.id == team_create.player1_id).first()
    player2 = db.query(Player).filter(Player.id == team_create.player2_id).first()

    if not player1 or not player2:
        raise HTTPException(status_code=400, detail="One or both players not found")

    new_team = Team(
        name=team_create.name,
        player1_id=team_create.player1_id,
        player2_id=team_create.player2_id,
    )

    db.add(new_team)
    db.commit()
    db.refresh(new_team)
    return new_team


@router.get("/", response_model=list[TeamResponse])
def get_teams(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return db.query(Team).all()


@router.get("/{team_id}", response_model=TeamResponse)
def get_team(
    team_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    team = db.query(Team).filter(Team.id == team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team
