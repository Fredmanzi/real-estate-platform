from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import os
import shutil

from app.schemas import land_plot as schema
from app.crud import land_plot as crud
from app.models.land_plot import LandPlot
from app.dependencies import get_db

router = APIRouter(tags=["LandPlots"])
UPLOAD_FOLDER = "uploads/land_plots"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/", response_model=schema.LandPlotOut)
def create_plot(plot: schema.LandPlotCreate, db: Session = Depends(get_db)):
    return crud.create_land_plot(db, plot)

@router.get("/", response_model=List[schema.LandPlotOut])
def read_plots(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_land_plots(db, skip, limit)

@router.get("/{plot_id}", response_model=schema.LandPlotOut)
def read_plot(plot_id: int, db: Session = Depends(get_db)):
    db_plot = crud.get_land_plot(db, plot_id)
    if not db_plot:
        raise HTTPException(status_code=404, detail="Plot not found")
    return db_plot

@router.put("/{plot_id}", response_model=schema.LandPlotOut)
def update_plot(plot_id: int, plot: schema.LandPlotUpdate, db: Session = Depends(get_db)):
    updated = crud.update_land_plot(db, plot_id, plot)
    if not updated:
        raise HTTPException(status_code=404, detail="Plot not found")
    return updated

@router.delete("/{plot_id}", response_model=schema.LandPlotOut)
def delete_plot(plot_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_land_plot(db, plot_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Plot not found")
    return deleted

@router.post("/{plot_id}/upload-image")
async def upload_plot_image(
    plot_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    plot = db.query(LandPlot).filter(LandPlot.id == plot_id).first()
    if not plot:
        raise HTTPException(status_code=404, detail="Plot not found")

    filename = f"plot_{plot_id}_{file.filename}"
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    plot.image_url = file_path
    db.commit()
    db.refresh(plot)

    return {"message": "Image uploaded successfully", "image_url": file_path}
