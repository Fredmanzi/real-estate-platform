from sqlalchemy.orm import Session
from app.models.land_plot import LandPlot
from app.schemas.land_plot import LandPlotCreate, LandPlotUpdate

def create_land_plot(db: Session, plot: LandPlotCreate):
    db_plot = LandPlot(**plot.dict())
    db.add(db_plot)
    db.commit()
    db.refresh(db_plot)
    return db_plot

def get_land_plots(db: Session, skip: int = 0, limit: int = 100):
    return db.query(LandPlot).offset(skip).limit(limit).all()

def get_land_plot(db: Session, plot_id: int):
    return db.query(LandPlot).filter(LandPlot.id == plot_id).first()

def update_land_plot(db: Session, plot_id: int, plot: LandPlotUpdate):
    db_plot = get_land_plot(db, plot_id)
    if not db_plot:
        return None
    for key, value in plot.dict(exclude_unset=True).items():
        setattr(db_plot, key, value)
    db.commit()
    db.refresh(db_plot)
    return db_plot

def delete_land_plot(db: Session, plot_id: int):
    db_plot = get_land_plot(db, plot_id)
    if not db_plot:
        return None
    db.delete(db_plot)
    db.commit()
    return db_plot
