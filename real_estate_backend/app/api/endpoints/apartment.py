from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import os
import shutil

from app.schemas import apartment as schema
from app.crud import apartment as crud
from app.dependencies import get_db
from app.models.apartment import Apartment  # SQLAlchemy model

router = APIRouter(tags=["apartments"])

UPLOAD_FOLDER = "uploads/apartments"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/", response_model=schema.ApartmentOut)
def create_apartment(apartment: schema.ApartmentCreate, db: Session = Depends(get_db)):
    return crud.create_apartment(db, apartment)

@router.get("/", response_model=List[schema.ApartmentOut])
def read_apartments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_apartments(db, skip=skip, limit=limit)

@router.get("/{apartment_id}", response_model=schema.ApartmentOut)
def read_apartment(apartment_id: int, db: Session = Depends(get_db)):
    db_apartment = crud.get_apartment(db, apartment_id)
    if not db_apartment:
        raise HTTPException(status_code=404, detail="Apartment not found")
    return db_apartment

@router.put("/{apartment_id}", response_model=schema.ApartmentOut)
def update_apartment(apartment_id: int, apartment: schema.ApartmentUpdate, db: Session = Depends(get_db)):
    db_apartment = crud.update_apartment(db, apartment_id, apartment)
    if not db_apartment:
        raise HTTPException(status_code=404, detail="Apartment not found")
    return db_apartment

@router.delete("/{apartment_id}")
def delete_apartment(apartment_id: int, db: Session = Depends(get_db)):
    db_apartment = crud.delete_apartment(db, apartment_id)
    if not db_apartment:
        raise HTTPException(status_code=404, detail="Apartment not found")
    return {"message": "Apartment deleted"}

@router.post("/{apartment_id}/upload-image")
async def upload_apartment_image(
    apartment_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    apartment = db.query(Apartment).filter(Apartment.id == apartment_id).first()
    if not apartment:
        raise HTTPException(status_code=404, detail="Apartment not found")

    filename = f"apartment_{apartment_id}_{file.filename}"
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Save file path (or URL) in the apartment record
    apartment.image_url = file_path
    db.commit()
    db.refresh(apartment)

    return {"message": "Image uploaded successfully", "image_url": file_path}
