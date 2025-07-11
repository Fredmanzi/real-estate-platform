from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer)
    price = Column(Float)
    mileage = Column(Float)
    fuel_type = Column(String)
    image_url = Column(String, nullable=True)  # ✅ NEW
