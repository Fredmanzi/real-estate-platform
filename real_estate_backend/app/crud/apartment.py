from sqlalchemy.orm import Session
from app.models import Apartment
from app.schemas.apartment import ApartmentCreate, ApartmentUpdate

def get_apartments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Apartment).offset(skip).limit(limit).all()

def get_apartment(db: Session, apartment_id: int):
    return db.query(Apartment).filter(Apartment.id == apartment_id).first()

def create_apartment(db: Session, apartment: ApartmentCreate):
    db_apartment = Apartment(**apartment.dict())
    db.add(db_apartment)
    db.commit()
    db.refresh(db_apartment)
    return db_apartment

def update_apartment(db: Session, apartment_id: int, apartment: ApartmentUpdate):
    db_apartment = get_apartment(db, apartment_id)
    if not db_apartment:
        return None
    for field, value in apartment.dict(exclude_unset=True).items():
        setattr(db_apartment, field, value)
    db.commit()
    db.refresh(db_apartment)
    return db_apartment

def delete_apartment(db: Session, apartment_id: int):
    db_apartment = get_apartment(db, apartment_id)
    if not db_apartment:
        return None
    db.delete(db_apartment)
    db.commit()
    return db_apartment

def update_apartment_image(db: Session, apartment_id: int, image_url: str):
    db_apartment = get_apartment(db, apartment_id)
    if not db_apartment:
        return None
    db_apartment.image_url = image_url
    db.commit()
    db.refresh(db_apartment)
    return db_apartment
