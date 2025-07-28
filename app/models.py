from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from enum import Enum as PyEnum
from app.database import Base,engine

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    hashed_password = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class SalahType(str, PyEnum):
    Fajr = "Fajr"
    Duhr = "Duhr"
    Asr = "Asr"
    Maghrib = "Maghrib"
    Isha = "Isha"

class SalahStatus(str, PyEnum):
    Performed = "Performed"
    Missed = "Missed"
    ToBeOffer = "To be offer"

class SalahLog(Base):
    __tablename__ = "salah_log"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    salah = Column(SQLEnum(SalahType), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(SQLEnum(SalahStatus), nullable=False)

class PostureLog(Base):
    __tablename__ = "posture_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)
    salah_name = Column(SQLEnum(SalahType), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    posture_accuracy = Column(Integer)

Base.metadata.create_all(bind=engine)