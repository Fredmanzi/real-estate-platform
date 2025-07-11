from pydantic import BaseModel
from typing import Optional

class LandPlotBase(BaseModel):
    title: str
    description: Optional[str] = None
    location: str
    price: float
    size: float

class LandPlotCreate(LandPlotBase):
    pass

class LandPlotUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    price: Optional[float] = None
    size: Optional[float] = None
    image_url: Optional[str] = None

class LandPlotOut(LandPlotBase):
    id: int
    image_url: Optional[str] = None  # ✅ Add this

    class Config:
        from_attributes = True
