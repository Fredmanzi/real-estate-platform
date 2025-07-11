from pydantic import BaseModel
from typing import Optional

class HouseBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    address: str
    bedrooms: int
    bathrooms: int
    area: float
    image_url: Optional[str] = None  # ✅ Add this

class HouseCreate(HouseBase):
    pass

class HouseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    address: Optional[str] = None
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    area: Optional[float] = None
    image_url: Optional[str] = None  # ✅ Include here too

class HouseOut(HouseBase):
    id: int

    class Config:
        from_attributes = True  # ✅ For Pydantic v2 compatibility
