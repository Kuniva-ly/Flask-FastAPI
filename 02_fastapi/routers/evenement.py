from datetime import datetime
from fastapi import APIRouter, HTTPException
from models.Evenement import Evenement
from models.respond_complet import ResponseModel

router = APIRouter()

evenements_db: list[Evenement] = []

@router.get("/", tags=["Evenements"], response_model=ResponseModel[list[Evenement]])
def get_evenements():
    return ResponseModel(
        success=True,
        data=evenements_db,
        message=f"{len(evenements_db)} événement(s) trouvé(s)",
        timestamp=datetime.now()
    )

@router.post("/", tags=["Evenements"], response_model=ResponseModel[Evenement])
def create_evenement(evenement: Evenement):
    evenements_db.append(evenement)
    return ResponseModel(
        success=True,
        data=evenement,
        message="Événement créé avec succès",
        timestamp=datetime.now()
    )
