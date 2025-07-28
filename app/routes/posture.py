from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import PostureLog, User
from app.schemas import PostureCreate, PostureOut
from app.utils.token import create_access_token
from app.utils.oauth2 import get_current_user

router=APIRouter(tags=["Posture"])

@router.post("/submit",response_model=PostureOut)

def submit_posture(posture_data: PostureCreate, current_user:User= Depends(get_current_user) , db:Session =Depends(get_db)):

    posture=PostureLog(
        salah_name=posture_data.salah_name,
        user_id=current_user.id,
        posture_accuracy=posture_data.posture_accuracy
    )

    db.add(posture)
    db.commit()
    db.refresh(posture)

    return posture



