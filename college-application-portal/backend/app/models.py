from sqlalchemy import Column, Integer, String, Text, DateTime
from .database import Base
from datetime import datetime

class Applicant(Base):
    __tablename__ = "applicants"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(120), unique=True)
    phone = Column(String(20))
    essay = Column(Text)
    status = Column(String(20), default="Pending")
    created_at = Column(DateTime, default=datetime.utcnow)
