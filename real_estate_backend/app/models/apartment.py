from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Apartment(Base):
    __tablename__ = "apartments"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    location = Column(String, nullable=False)   # ✅ Add this
    address = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    size = Column(Float, nullable=False)        # ✅ Add this
    rooms = Column(Integer, nullable=False)     # ✅ Add this
    bedrooms = Column(Integer, nullable=False)
    bathrooms = Column(Integer, nullable=False)
    floor = Column(Integer, nullable=False)
    image_url = Column(String, nullable=True)

