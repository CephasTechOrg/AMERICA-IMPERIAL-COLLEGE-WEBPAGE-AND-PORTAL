from fastapi import FastAPI
from .routers import applications
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Admissions API")

app.include_router(applications.router)
