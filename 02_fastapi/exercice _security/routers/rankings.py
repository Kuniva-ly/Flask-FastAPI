from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from models.match import Match
from models.player import Player
from models.team import Team
from models.user import User
from schemas.ranking import RankingEntry
from core.dependencies import get_current_user

router = APIRouter(prefix="/rankings", tags=["Rankings"])


@router.get("/players", response_model=list[RankingEntry])
def get_players_ranking(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    players = db.query(Player).all()
    matches = db.query(Match).filter(Match.match_type == "single").all()

    rankings = []
    for player in players:
        wins = losses = draws = goals_for = goals_against = 0

        for match in matches:
            if match.participant_1_id == player.id:
                goals_for += match.score_1
                goals_against += match.score_2
                if match.score_1 > match.score_2:
                    wins += 1
                elif match.score_1 < match.score_2:
                    losses += 1
                else:
                    draws += 1
            elif match.participant_2_id == player.id:
                goals_for += match.score_2
                goals_against += match.score_1
                if match.score_2 > match.score_1:
                    wins += 1
                elif match.score_2 < match.score_1:
                    losses += 1
                else:
                    draws += 1

        rankings.append(RankingEntry(
            participant_id=player.id,
            matches_played=wins + losses + draws,
            wins=wins,
            losses=losses,
            draws=draws,
            goal_difference=goals_for - goals_against,
            points=wins * 3 + draws,
        ))

    return sorted(rankings, key=lambda r: (r.points, r.goal_difference), reverse=True)


@router.get("/teams", response_model=list[RankingEntry])
def get_teams_ranking(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    teams = db.query(Team).all()
    matches = db.query(Match).filter(Match.match_type == "team").all()

    rankings = []
    for team in teams:
        wins = losses = draws = goals_for = goals_against = 0

        for match in matches:
            if match.participant_1_id == team.id:
                goals_for += match.score_1
                goals_against += match.score_2
                if match.score_1 > match.score_2:
                    wins += 1
                elif match.score_1 < match.score_2:
                    losses += 1
                else:
                    draws += 1
            elif match.participant_2_id == team.id:
                goals_for += match.score_2
                goals_against += match.score_1
                if match.score_2 > match.score_1:
                    wins += 1
                elif match.score_2 < match.score_1:
                    losses += 1
                else:
                    draws += 1

        rankings.append(RankingEntry(
            participant_id=team.id,
            matches_played=wins + losses + draws,
            wins=wins,
            losses=losses,
            draws=draws,
            goal_difference=goals_for - goals_against,
            points=wins * 3 + draws,
        ))

    return sorted(rankings, key=lambda r: (r.points, r.goal_difference), reverse=True)
