from typing import Generic, TypeVar
from datetime import datetime
from pydantic import BaseModel

T = TypeVar('T')

class ResponseModel(BaseModel, Generic[T]):
    success: bool
    data: T
    message: str | None = None
    timestamp: datetime | None = None