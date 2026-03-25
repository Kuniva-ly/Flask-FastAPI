from typing import Optional
from enum import Enum
from pydantic import BaseModel, EmailStr, Field


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
