from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def ingest_endpoint():
    return {"message": "Ingest endpoint"}
