from pydantic import BaseModel


class RankingEntry(BaseModel):
    participant_id: int
    matches_played: int
    wins: int
    losses: int
    draws: int
    goal_difference: int
    points: int
    