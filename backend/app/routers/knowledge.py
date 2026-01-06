from fastapi import APIRouter, UploadFile, File, Body
from typing import List, Optional

router = APIRouter()

from ..services.rag import add_to_memory, query_memory
import json

@router.post("/ingest")
async def ingest_knowledge(
    data: Optional[dict] = Body(None),
    files: Optional[List[UploadFile]] = File(None)
):
    if data:
        content = json.dumps(data)
        add_to_memory(content, metadata={"type": "json_import"})
    
    if files:
        for file in files:
            content = await file.read()
            add_to_memory(content.decode(), metadata={"type": "file_upload", "filename": file.filename})
            
    return {"status": "Knowledge ingested successfully"}

@router.get("/query")
async def query_knowledge(q: str):
    results = query_memory(q)
    return {"results": results}
