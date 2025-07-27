from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserOut
from app.utils.hashing import hash_password

router=APIRouter(tags=["Auth"])

@router.post("/register",response_model=UserOut)

def register(user:UserCreate, db:Session =Depends(get_db)):

    existing_user=db.query(User).filter(User.email==user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User will this email already exists")
    
    hashed_password=hash_password(user.password)

    new_user=User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user