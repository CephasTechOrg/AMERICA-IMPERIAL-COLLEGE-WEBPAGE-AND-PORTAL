from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class ApplicationCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    essay: str

class ApplicationOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    essay: str
    uploaded_files: Optional[List[str]]
    status: str
    created_at: datetime
    class Config:
        orm_mode = True
