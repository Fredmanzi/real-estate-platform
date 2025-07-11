from fastapi import FastAPI
from app.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
# ✅ Import all routers once, clearly
from app.api.endpoints import house, car, apartment, land_plot, listing
from fastapi.staticfiles import StaticFiles
# ✅ Initialize FastAPI app
app = FastAPI(
    title="Real Estate Listings API",
    version="1.0.0"
)

# ✅ Create DB tables
Base.metadata.create_all(bind=engine)
# Allow frontend origin
origins = [
    "http://localhost:3000",
    # you can add more origins here if needed
]
# 👇 Mount the upload directory so files can be accessed publicly

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # <-- frontend URL(s) allowed
    allow_credentials=True,
    allow_methods=["*"],    # <-- allow all methods (GET, POST, etc.)
    allow_headers=["*"],    # <-- allow all headers
)
# ✅ Register routers with consistent prefixes
app.include_router(listing.router, prefix="/api/listings", tags=["Listings"])
app.include_router(house.router, prefix="/houses", tags=["Houses"])
app.include_router(car.router, prefix="/cars", tags=["Cars"])
app.include_router(apartment.router, prefix="/apartments", tags=["Apartments"])
app.include_router(land_plot.router, prefix="/land-plots", tags=["LandPlots"])

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")