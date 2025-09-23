from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
import os, uuid, json

from .. import schemas, crud, models, database
from ..email_utils import send_confirmation_to_student, notify_admissions

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/applications/")
async def submit_application(
    first_name: str = Form(...),
    last_name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    essay: str = Form(...),
    files: List[UploadFile] = File([]),
    db: Session = Depends(get_db),
):
    # save files
    app_id = str(uuid.uuid4())
    app_folder = os.path.join(UPLOAD_DIR, app_id)
    os.makedirs(app_folder, exist_ok=True)
    paths = []
    for f in files:
        filename = f.filename
        safe_path = os.path.join(app_folder, filename)
        with open(safe_path, "wb") as out:
            content = await f.read()
            out.write(content)
        # store public path
        paths.append(f"/uploads/{app_id}/{filename}")

    # build schema object
    app_in = schemas.ApplicationCreate(
        first_name = first_name,
        last_name = last_name,
        email = email,
        phone = phone,
        essay = essay
    )

    db_app = crud.create_application(db, app_in, paths)

    # notify student and admissions in background without delaying response
    # background tasks are immediate on server side
    try:
        notify_admissions(db_app)
        send_confirmation_to_student(db_app)
    except Exception as e:
        # log error, do not fail the request
        print("email error", e)

    return {"status": "success", "application_id": db_app.id}
