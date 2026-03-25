from datetime import datetime
from fastapi import APIRouter
from models.produits import Produit
from models.respond_complet import ResponseModel

router = APIRouter()

produits_db: list[Produit] = []

@router.get("/", tags=["Products"], response_model=ResponseModel[list[Produit]])
def read_produits():
    return ResponseModel(
        success=True,
        data=produits_db,
        message="Liste des produits",
        timestamp=datetime.now()
    )

@router.post("/", tags=["Products"], response_model=ResponseModel[Produit])
def create_product(product: Produit):
    produits_db.append(product)
    return ResponseModel(
        success=True,
        data=product,
        message="Produit créé avec succès",
        timestamp=datetime.now()
    )
