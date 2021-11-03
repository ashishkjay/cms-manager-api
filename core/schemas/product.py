from typing import Optional
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    id: str
