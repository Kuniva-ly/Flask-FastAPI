from fastapi import FastAPI, APIRouter
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum
import uvicorn


app = FastAPI(
    title="Produits avec modèles imbriqués",
    description="API pour gérer des produits avec fournisseur imbriqué",
    version="1.0.0"
)
router = APIRouter()

class Category(str, Enum):
    ELECTRONICS = "ELECTRONICS"
    CLOTHING = "CLOTHING"
    FOOD = "FOOD"
    OTHER = "OTHER"


class Supplier(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None


class Produit(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Prix du produit (doit être > 0)")
    category: Category
    stock: int = Field(..., ge=0, description="Stock disponible (doit être >= 0)")
    supplier: Supplier


@router.get("/", tags=["Root"])
def root():
    return {"message": "FastAPI Nested Models Demo"}


@router.post("/products", tags=["Products"])
def create_product(product: Produit):
    return {"message": "Produit créé avec succès", "product": product}


app.include_router(router)
