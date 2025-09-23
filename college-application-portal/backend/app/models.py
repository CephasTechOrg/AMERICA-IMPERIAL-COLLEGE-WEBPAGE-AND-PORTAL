from sqlalchemy import Column, Integer, String, Text, DateTime
from .database import Base
from datetime import datetime

class Application(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(120))
    last_name = Column(String(120))
    email = Column(String(255), index=True)
    phone = Column(String(50))
    essay = Column(Text)
    uploaded_files = Column(Text)  # JSON list of file paths
    status = Column(String(50), default="Pending")
    created_at = Column(DateTime, default=datetime.utcnow)
