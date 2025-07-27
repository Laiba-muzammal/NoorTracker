# app/routes/qibla.py

from fastapi import APIRouter

router = APIRouter(tags=["Qibla"]  )

@router.get("/direction")
def get_qibla_direction():
    return {"message": "This is Qibla Route"}
