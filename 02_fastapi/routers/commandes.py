from datetime import datetime
from fastapi import APIRouter
from models.commande import Commande
from models.respond_complet import ResponseModel

router = APIRouter()

commandes_db: list[Commande] = []

@router.get("/", tags=["Commandes"], response_model=ResponseModel[list[Commande]])
def read_commandes():
    return ResponseModel(
        success=True,
        data=commandes_db,
        message="Liste des commandes",
        timestamp=datetime.now()
    )

@router.post("/", tags=["Commandes"], response_model=ResponseModel[Commande])
def create_commande(commande: Commande):
    commandes_db.append(commande)
    return ResponseModel(
        success=True,
        data=commande,
        message="Commande créée avec succès",
        timestamp=datetime.now()
    )
