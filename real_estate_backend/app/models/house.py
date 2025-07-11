from sqlalchemy import Column, Integer, String, Float
from app.database import Base  # assuming you have Base defined in app/database.py

class House(Base):
    __tablename__ = "houses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float)
    address = Column(String, index=True)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    area = Column(Float)  # square meters, for example
    image_url = Column(String, nullable=True)  # ✅ NEW