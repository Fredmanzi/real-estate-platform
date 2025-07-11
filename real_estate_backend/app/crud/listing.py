from sqlalchemy.orm import Session
from app import models, schemas

def get_all_listings(db: Session):
    return db.query(models.listing.Listing).all()

def get_listing(db: Session, listing_id: int):
    return db.query(models.listing.Listing).filter(models.listing.Listing.id == listing_id).first()

def create_listing(db: Session, listing: schemas.listing.ListingCreate):
    db_listing = models.listing.Listing(**listing.dict())
    db.add(db_listing)
    db.commit()
    db.refresh(db_listing)
    return db_listing

def update_listing(db: Session, listing_id: int, updated: schemas.listing.ListingUpdate):
    db_listing = get_listing(db, listing_id)
    if db_listing:
        for key, value in updated.dict().items():
            setattr(db_listing, key, value)
        db.commit()
        db.refresh(db_listing)
    return db_listing

def delete_listing(db: Session, listing_id: int):
    db_listing = get_listing(db, listing_id)
    if db_listing:
        db.delete(db_listing)
        db.commit()
    return db_listing
