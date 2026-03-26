from pydantic import BaseModel

class TeamCreate(BaseModel):
    name: str
    player1_id: int
    player2_id: int

class TeamResponse(BaseModel):
    id: int
    name: str
    player1_id: int
    player2_id: int

    model_config = {"from_attributes": True}
