from sqlalchemy import Column, Integer, String, Float, Enum
from app.database import Base
import enum

class ListingType(str, enum.Enum):
    house = "house"
    apartment = "apartment"
    land = "land"
    car = "car"

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    location = Column(String)
    listing_type = Column(Enum(ListingType), index=True)
    image_url = Column(String, nullable=True)
