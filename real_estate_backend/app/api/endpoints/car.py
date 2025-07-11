from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import os
import shutil

from app.schemas import car as car_schema
from app.crud import car as crud_car
from app.dependencies import get_db
from app.models.car import Car

router = APIRouter(tags=["cars"])

UPLOAD_FOLDER = "uploads/cars"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/", response_model=car_schema.Car)
def create_car(car: car_schema.CarCreate, db: Session = Depends(get_db)):
    return crud_car.create_car(db, car)

@router.get("/", response_model=List[car_schema.Car])
def read_cars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_car.get_cars(db, skip, limit)

@router.get("/{car_id}", response_model=car_schema.Car)
def read_car(car_id: int, db: Session = Depends(get_db)):
    db_car = crud_car.get_car(db, car_id)
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

@router.put("/{car_id}", response_model=car_schema.Car)
def update_car(car_id: int, car: car_schema.CarUpdate, db: Session = Depends(get_db)):
    updated_car = crud_car.update_car(db, car_id, car)
    if not updated_car:
        raise HTTPException(status_code=404, detail="Car not found")
    return updated_car

@router.delete("/{car_id}", response_model=car_schema.Car)
def delete_car(car_id: int, db: Session = Depends(get_db)):
    deleted_car = crud_car.delete_car(db, car_id)
    if not deleted_car:
        raise HTTPException(status_code=404, detail="Car not found")
    return deleted_car

@router.post("/{car_id}/upload-image")
async def upload_car_image(
    car_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    car = crud_car.get_car(db, car_id)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")

    filename = f"car_{car_id}_{file.filename}"
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    updated_car = crud_car.update_car_image(db, car_id, file_path)

    return {"message": "Image uploaded successfully", "image_url": updated_car.image_url}
