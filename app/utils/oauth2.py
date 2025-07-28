from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.config import SECRET_KEY, ALGORITHM

oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    try:
        # Decode the token using secret and algorithm
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token missing user ID")

    except JWTError:
        raise HTTPException(status_code=401, detail="Token is invalid or expired")

    # Fetch the user from DB using the decoded user_id
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user
