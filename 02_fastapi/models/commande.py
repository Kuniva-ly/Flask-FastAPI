from typing import List
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field, computed_field, model_validator


class ItemModel(BaseModel):
    product_id: int
    name: str
    quantity: int = Field(..., ge=1, description="La quantité doit être supérieure à zéro")
    price: float = Field(..., gt=0, description="Le prix doit être supérieur à zéro")


class Commande(BaseModel):
    order_id: UUID
    customer_email: EmailStr
    items: List[ItemModel] = Field(..., min_length=1)

    @model_validator(mode="after")
    def total_price(self) -> float:
        self.total = sum(item.quantity * item.price for item in self.items)
        return self
    
    # @computed_field
    # @property
    # def total(self) -> float:
    #     return sum(item.quantity * item.price for item in self.items)

