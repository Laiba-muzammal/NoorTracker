from pydantic import BaseModel
from datetime import datetime
class UserCreate(BaseModel):
    name:str
    password:str
    email:str

class UserOut(BaseModel):
    id:int
    name:str
    email:str
    created_at: datetime

    class Config:
        orm_mode = True
class SalahCreate(BaseModel):
    salah:str
    status:str

class SalahOut(BaseModel):
    salah:str
    status:str
    id:int
    created_at: datetime

    class Config:
        orm_mode = True

class PostureCreate(BaseModel):
    salah_name:str
    posture_accuracy: int

class PostureOut(BaseModel):
    salah_name:str
    posture_accuracy: int
    id:int
    created_at: datetime
    
    class Config:
        orm_mode = True