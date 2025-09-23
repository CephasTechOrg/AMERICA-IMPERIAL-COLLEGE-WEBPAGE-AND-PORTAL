from sqlalchemy.orm import Session
from . import models, schemas

def create_applicant(db: Session, applicant: schemas.ApplicantCreate):
    db_applicant = models.Applicant(**applicant.dict())
    db.add(db_applicant)
    db.commit()
    db.refresh(db_applicant)
    return db_applicant

def get_applicants(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Applicant).offset(skip).limit(limit).all()
