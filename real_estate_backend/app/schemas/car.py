from pydantic import BaseModel
from typing import Optional

class CarBase(BaseModel):
    make: str
    model: str
    year: int
    price: float
    mileage: float
    fuel_type: str

class CarCreate(CarBase):
    pass

class CarUpdate(BaseModel):
    make: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    price: Optional[float] = None
    mileage: Optional[float] = None
    fuel_type: Optional[str] = None
    image_url: Optional[str] = None  # For updating image URL

class Car(CarBase):
    id: int
    image_url: Optional[str] = None

    class Config:
        orm_mode = True  # <-- Use orm_mode for FastAPI compatibility
