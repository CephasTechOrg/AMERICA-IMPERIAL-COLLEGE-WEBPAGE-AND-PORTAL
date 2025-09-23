from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter(prefix="/applications", tags=["applications"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ApplicantOut)
def submit_application(applicant: schemas.ApplicantCreate, db: Session = Depends(get_db)):
    return crud.create_applicant(db, applicant)

@router.get("/", response_model=list[schemas.ApplicantOut])
def list_applications(db: Session = Depends(get_db)):
    return crud.get_applicants(db)
