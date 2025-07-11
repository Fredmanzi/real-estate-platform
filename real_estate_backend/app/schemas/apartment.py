from pydantic import BaseModel
from typing import Optional

class ApartmentBase(BaseModel):
    title: str
    description: str
    location: str
    address: str
    price: float
    size: float
    rooms: int
    bedrooms: int
    bathrooms: int
    floor: int

class ApartmentCreate(ApartmentBase):
    pass

class ApartmentUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    address: Optional[str] = None
    price: Optional[float] = None
    size: Optional[float] = None
    rooms: Optional[int] = None
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    floor: Optional[int] = None
    image_url: Optional[str] = None

class Apartment(ApartmentBase):
    id: int
    image_url: Optional[str] = None

    class Config:
        from_attributes = True

# Optional alias for clarity in API responses
class ApartmentOut(Apartment):
    pass

