from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.listing import ListingCreate, ListingUpdate, ListingOut
from app.crud import listing as crud_listing
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=List[ListingOut])
def read_listings(db: Session = Depends(get_db)):
    return crud_listing.get_all_listings(db)

@router.get("/{listing_id}", response_model=ListingOut)
def read_listing(listing_id: int, db: Session = Depends(get_db)):
    db_listing = crud_listing.get_listing(db, listing_id)
    if db_listing is None:
        raise HTTPException(status_code=404, detail="Listing not found")
    return db_listing

@router.post("/", response_model=ListingOut)
def create_listing(listing: ListingCreate, db: Session = Depends(get_db)):
    return crud_listing.create_listing(db, listing)

@router.put("/{listing_id}", response_model=ListingOut)
def update_listing(listing_id: int, listing: ListingUpdate, db: Session = Depends(get_db)):
    updated = crud_listing.update_listing(db, listing_id, listing)
    if updated is None:
        raise HTTPException(status_code=404, detail="Listing not found")
    return updated

@router.delete("/{listing_id}", response_model=ListingOut)
def delete_listing(listing_id: int, db: Session = Depends(get_db)):
    deleted = crud_listing.delete_listing(db, listing_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Listing not found")
    return deleted
