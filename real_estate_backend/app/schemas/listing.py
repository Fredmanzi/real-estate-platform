from pydantic import BaseModel
from enum import Enum
from typing import Optional

class ListingType(str, Enum):
    house = "house"
    apartment = "apartment"
    land = "land"
    car = "car"

class ListingBase(BaseModel):
    title: str
    description: str
    price: float
    location: str
    listing_type: ListingType
    image_url: Optional[str] = None

class ListingCreate(ListingBase):
    pass

class ListingUpdate(ListingBase):
    pass

class ListingOut(ListingBase):
    id: int

    class Config:
        orm_mode = True
