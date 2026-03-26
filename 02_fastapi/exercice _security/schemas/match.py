from pydantic import BaseModel
from datetime import datetime

class MatchCreate(BaseModel):
    match_type: str  
    participant_1_id: int
    participant_2_id: int
    score_1: int
    score_2: int

class MatchResponse(BaseModel):
    id: int
    match_type: str
    participant_1_id: int
    participant_2_id: int
    score_1: int
    score_2: int
    timestamp: datetime

    model_config = {"from_attributes": True}
