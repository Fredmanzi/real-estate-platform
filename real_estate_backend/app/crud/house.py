from sqlalchemy.orm import Session
from app.models import House
from app.schemas.house import HouseCreate, HouseUpdate

def get_house(db: Session, house_id: int):
    return db.query(House).filter(House.id == house_id).first()

def get_houses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(House).offset(skip).limit(limit).all()

def create_house(db: Session, house: HouseCreate):
    db_house = House(
        title=house.title,
        description=house.description,
        price=house.price,
        address=house.address,
        bedrooms=house.bedrooms,
        bathrooms=house.bathrooms,
        area=house.area,
        image_url=getattr(house, "image_url", None)  # Optional image URL support
    )
    db.add(db_house)
    db.commit()
    db.refresh(db_house)
    return db_house

def update_house(db: Session, house_id: int, house_update: HouseUpdate):
    db_house = get_house(db, house_id)
    if not db_house:
        return None
    update_data = house_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_house, key, value)
    db.commit()
    db.refresh(db_house)
    return db_house

def delete_house(db: Session, house_id: int):
    db_house = get_house(db, house_id)
    if not db_house:
        return None
    db.delete(db_house)
    db.commit()
    return db_house
