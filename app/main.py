from fastapi import FastAPI, APIRouter
from app.routes import auth, salah, posture, qibla
from app.database import SessionLocal, engine
from app import models

app = FastAPI()
app.include_router(qibla.router, prefix="/qibla")
app.include_router(auth.router, prefix="/auth")
app.include_router(salah.router, prefix="/salah")
app.include_router(posture.router, prefix="/posture")

@app.get("/")
def root():
    return {"message": "Welcome to NoorTracker"}