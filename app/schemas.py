from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from app.models import SalahType  # make sure correct path
from typing import Literal

# ✅ Login Schema
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# ✅ User Create
class UserCreate(BaseModel):
    name: str
    password: str
    email: EmailStr

# ✅ User Output
class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True  # Pydantic v2

# ✅ Salah Creation
class SalahCreate(BaseModel):
    salah: Literal["Fajr", "Duhr", "Asr", "Maghrib", "Isha"]
    status: Literal["Performed", "Missed", "To be offer"]

# ✅ Salah Output
class SalahOut(BaseModel):
    salah: Literal["Fajr", "Duhr", "Asr", "Maghrib", "Isha"]
    status: Literal["Performed", "Missed", "To be offer"]
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# ✅ Posture Submission
class PostureCreate(BaseModel):
    salah_name: Literal["Fajr", "Duhr", "Asr", "Maghrib", "Isha"]
    posture_accuracy: conint(ge=0, le=100)  # type: ignore

# ✅ Posture Output
class PostureOut(BaseModel):
    salah_name: SalahType
    posture_accuracy: int
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
