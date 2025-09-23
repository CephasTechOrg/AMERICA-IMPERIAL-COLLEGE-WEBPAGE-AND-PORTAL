from pydantic import BaseModel, EmailStr
from datetime import datetime

class ApplicantBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    essay: str

class ApplicantCreate(ApplicantBase):
    pass

class ApplicantOut(ApplicantBase):
    id: int
    status: str
    created_at: datetime
    class Config:
        orm_mode = True
