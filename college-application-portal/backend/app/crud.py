from sqlalchemy.orm import Session
from . import models, schemas
import json

def create_application(db: Session, app_in: schemas.ApplicationCreate, file_paths: list):
    db_app = models.Application(
        first_name = app_in.first_name,
        last_name = app_in.last_name,
        email = app_in.email,
        phone = app_in.phone,
        essay = app_in.essay,
        uploaded_files = json.dumps(file_paths)
    )
    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return db_app

def get_applications(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Application).offset(skip).limit(limit).all()

def get_application(db: Session, id: int):
    return db.query(models.Application).filter(models.Application.id == id).first()
