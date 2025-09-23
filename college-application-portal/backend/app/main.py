from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .database import Base, engine
from .routers import applications

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Admissions API")

# mount uploads to serve files
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.include_router(applications.router)
