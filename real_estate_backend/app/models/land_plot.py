from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class LandPlot(Base):
    __tablename__ = "land_plots"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    location = Column(String)
    price = Column(Float)
    size = Column(Float)
    image_url = Column(String, nullable=True)  # ✅ NEW

