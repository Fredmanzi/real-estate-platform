from sqlalchemy.orm import Session
from app.models.car import Car
from app.schemas import car as car_schema
from typing import List, Optional

def get_car(db: Session, car_id: int) -> Optional[Car]:
    return db.query(Car).filter(Car.id == car_id).first()

def get_cars(db: Session, skip: int = 0, limit: int = 100) -> List[Car]:
    return db.query(Car).offset(skip).limit(limit).all()

def create_car(db: Session, car: car_schema.CarCreate) -> Car:
    db_car = Car(
        make=car.make,
        model=car.model,
        year=car.year,
        price=car.price,
        mileage=car.mileage,
        fuel_type=car.fuel_type,
        image_url=None  # default to None on creation
    )
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def update_car(db: Session, car_id: int, car: car_schema.CarUpdate) -> Optional[Car]:
    db_car = get_car(db, car_id)
    if not db_car:
        return None

    # Update only provided fields
    update_data = car.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_car, key, value)

    db.commit()
    db.refresh(db_car)
    return db_car

def delete_car(db: Session, car_id: int) -> Optional[Car]:
    db_car = get_car(db, car_id)
    if not db_car:
        return None
    db.delete(db_car)
    db.commit()
    return db_car

def update_car_image(db: Session, car_id: int, image_url: str) -> Optional[Car]:
    db_car = get_car(db, car_id)
    if not db_car:
        return None
    db_car.image_url = image_url
    db.commit()
    db.refresh(db_car)
    return db_car
