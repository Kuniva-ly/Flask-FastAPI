from fastapi import APIRouter
from models.produits import Produit

router = APIRouter()


@router.get("/", tags=["Products"])
def root():
    return {"message": "FastAPI Nested Models Demo"}


@router.post("/", tags=["Products"])
def create_product(product: Produit):
    return {"message": "Produit créé avec succès", "product": product}
