from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import SalahCreate, SalahOut
from app.models import SalahLog
from app.utils.oauth2 import get_current_user
from app.models import User
from typing import List

router=APIRouter(tags=["Salah"])

@router.post("/", response_model=SalahOut)
def log_salah(
    salah: SalahCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_log = SalahLog(
        salah=salah.salah,
        status=salah.status,
        user_id=current_user.id
    )
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log


@router.get("/History", response_model=List[SalahOut] )
def history_salah( db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):

    history=db.query(SalahLog).filter(SalahLog.user_id == current_user.id).all()
    return history

