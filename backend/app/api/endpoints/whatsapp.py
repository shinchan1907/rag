from fastapi import APIRouter, Request, HTTPException, Query
from app.core.config import settings
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/webhook")
async def verify_webhook(
    mode: str = Query(..., alias="hub.mode"),
    token: str = Query(..., alias="hub.verify_token"),
    challenge: str = Query(..., alias="hub.challenge"),
):
    """
    Verify the webhook with WhatsApp.
    """
    if mode == "subscribe" and token == settings.WHATSAPP_VERIFY_TOKEN:
        logger.info("Webhook verified successfully!")
        return int(challenge)
    
    logger.error("Webhook verification failed.")
    raise HTTPException(status_code=403, detail="Verification failed")

@router.post("/webhook")
async def handle_webhook(request: Request):
    """
    Handle incoming WhatsApp messages.
    """
    payload = await request.json()
    logger.info(f"Received payload: {payload}")
    
    # Basic acknowledgment to avoid retries from Meta
    return {"status": "received"}
