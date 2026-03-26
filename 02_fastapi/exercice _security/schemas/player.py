from pydantic import BaseModel

class PlayerCreate(BaseModel):
    nickname: str

class PlayerResponse(BaseModel):
    id: int
    nickname: str

    model_config = {"from_attributes": True}
