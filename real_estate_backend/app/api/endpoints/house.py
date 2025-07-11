from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
import os
import shutil

from typing import List

from app import schemas, crud
from app.database import get_db
from app.models.house import House

router = APIRouter(
    tags=["houses"],
)

UPLOAD_FOLDER = "uploads/houses"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/", response_model=schemas.HouseOut)
def create_house(house: schemas.HouseCreate, db: Session = Depends(get_db)):
    return crud.house.create_house(db=db, house=house)

@router.get("/{house_id}", response_model=schemas.HouseOut)
def read_house(house_id: int, db: Session = Depends(get_db)):
    db_house = crud.house.get_house(db, house_id=house_id)
    if not db_house:
        raise HTTPException(status_code=404, detail="House not found")
    return db_house

@router.get("/", response_model=List[schemas.HouseOut])
def read_houses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    houses = crud.house.get_houses(db, skip=skip, limit=limit)
    return houses

@router.put("/{house_id}", response_model=schemas.HouseOut)
def update_house(house_id: int, house_update: schemas.HouseUpdate, db: Session = Depends(get_db)):
    db_house = crud.house.update_house(db, house_id=house_id, house_update=house_update)
    if not db_house:
        raise HTTPException(status_code=404, detail="House not found")
    return db_house

@router.delete("/{house_id}", response_model=schemas.HouseOut)
def delete_house(house_id: int, db: Session = Depends(get_db)):
    db_house = crud.house.delete_house(db, house_id=house_id)
    if not db_house:
        raise HTTPException(status_code=404, detail="House not found")
    return db_house

@router.post("/{house_id}/upload-image")
async def upload_house_image(
    house_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    house = db.query(House).filter(House.id == house_id).first()
    if not house:
        raise HTTPException(status_code=404, detail="House not found")

    filename = f"house_{house_id}_{file.filename}"
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    house.image_url = file_path
    db.commit()
    db.refresh(house)

    return {"message": "Image uploaded successfully", "image_url": file_path}

