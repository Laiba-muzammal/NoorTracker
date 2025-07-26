from fastapi import FastAPI
from app.routes import auth, salah, posture, qibla
from app.database import SessionLocal, engine
from app import models

app = FastAPI()
app.include_router(qibla.router, prefix="/qibla")



@app.get("/")
def root():
    return {"message": "Welcome to NoorTracker"}