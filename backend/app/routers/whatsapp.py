from fastapi import APIRouter, Request, HTTPException
from ..config import settings
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/whatsapp")
async def verify_webhook(request: Request):
    params = request.query_params
    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == settings.WHATSAPP_WEBHOOK_VERIFY_TOKEN:
        return int(challenge)
    
    raise HTTPException(status_code=403, detail="Verification failed")

from ..services.whatsapp import process_incoming_message
import asyncio

@router.post("/whatsapp")
async def handle_whatsapp_webhook(request: Request):
    body = await request.json()
    logger.info(f"Received WABA Body: {body}")
    
    # Process message in background to respond quickly to Meta
    asyncio.create_task(process_incoming_message(body))
    
    return {"status": "success"}
