from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.database import get_db
from models.match import Match
from models.player import Player
from models.team import Team
from models.user import User
from schemas.match import MatchCreate, MatchResponse
from core.dependencies import get_current_user

router = APIRouter(prefix="/matches", tags=["Matches"])


@router.post("/", response_model=MatchResponse, status_code=status.HTTP_201_CREATED)
def create_match(
    match_create: MatchCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if match_create.participant_1_id == match_create.participant_2_id:
        raise HTTPException(status_code=400, detail="Participants must be different")

    if match_create.score_1 < 0 or match_create.score_2 < 0:
        raise HTTPException(status_code=400, detail="Scores must be positive")

    if match_create.match_type == "single":
        p1 = db.query(Player).filter(Player.id == match_create.participant_1_id).first()
        p2 = db.query(Player).filter(Player.id == match_create.participant_2_id).first()
        if not p1 or not p2:
            raise HTTPException(status_code=400, detail="One or both players not found")

    elif match_create.match_type == "team":
        t1 = db.query(Team).filter(Team.id == match_create.participant_1_id).first()
        t2 = db.query(Team).filter(Team.id == match_create.participant_2_id).first()
        if not t1 or not t2:
            raise HTTPException(status_code=400, detail="One or both teams not found")

    else:
        raise HTTPException(status_code=400, detail="match_type must be 'single' or 'team'")

    new_match = Match(
        match_type=match_create.match_type,
        participant_1_id=match_create.participant_1_id,
        participant_2_id=match_create.participant_2_id,
        score_1=match_create.score_1,
        score_2=match_create.score_2,
    )

    db.add(new_match)
    db.commit()
    db.refresh(new_match)
    return new_match


@router.get("/", response_model=list[MatchResponse])
def get_matches(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return db.query(Match).all()


@router.get("/{match_id}", response_model=MatchResponse)
def get_match(
    match_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    match = db.query(Match).filter(Match.id == match_id).first()
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    return match
