from typing import Optional, Literal
from pydantic import BaseModel, Field, model_validator


class Evenement(BaseModel):
    type: Literal["online", "offline"] = Field(..., description="Type d'événement")
    title: str = Field(..., description="Titre de l'événement")
    location: Optional[str] = Field(None, description="Lieu (obligatoire si type='offline')")
    url: Optional[str] = Field(None, description="URL (obligatoire si type='online')")
    max_participants: int = Field(..., ge=1, description="Nombre maximum de participants")

    @model_validator(mode="after")
    def check_type_fields(self):
        if self.type == "offline" and not self.location:
            raise ValueError("'location' est obligatoire pour un événement offline")
        if self.type == "online" and not self.url:
            raise ValueError("'url' est obligatoire pour un événement online")
        return self
