from fastapi import APIRouter, Body
from datetime import datetime

router = APIRouter()

@router.post("/log")
async def log_activity(data: dict = Body(...)):
    # Store daily PC activities for efficiency analysis
    # timestamp = datetime.now()
    return {"status": "Activity logged", "timestamp": datetime.now()}
