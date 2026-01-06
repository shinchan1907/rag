import httpx
from ..config import settings
from .openai import get_response
from .rag import add_to_memory
import logging

logger = logging.getLogger(__name__)

async def send_whatsapp_message(to_number: str, message: str):
    url = f"https://graph.facebook.com/v17.0/{settings.WHATSAPP_PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {settings.WHATSAPP_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "text",
        "text": {"body": message}
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            logger.error(f"Failed to send message: {response.text}")
        return response.json()

async def send_whatsapp_template(to_number: str, template_name: str, language_code: str = "en_US", components: list = None):
    url = f"https://graph.facebook.com/v17.0/{settings.WHATSAPP_PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {settings.WHATSAPP_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "template",
        "template": {
            "name": template_name,
            "language": {"code": language_code},
            "components": components or []
        }
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            logger.error(f"Failed to send template: {response.text}")
        return response.json()

async def process_incoming_message(body: dict):
    # Extract message details
    try:
        entry = body.get("entry", [])[0]
        changes = entry.get("changes", [])[0]
        value = changes.get("value", {})
        messages = value.get("messages", [])
        
        if not messages:
            return
            
        message = messages[0]
        from_number = message.get("from")
        text = message.get("text", {}).get("body")
        
        if not text:
            return

        is_owner = from_number in settings.owner_list
        
        # Get AI response
        # TODO: Fetch chat history from Redis/Postgres
        history = [] 
        ai_reply = await get_response(text, history, is_owner=is_owner)
        
        # Save to RAG memory for future context
        memory_metadata = {
            "from": from_number,
            "is_owner": is_owner,
            "timestamp": "now"
        }
        add_to_memory(f"User: {text}\nDonna: {ai_reply}", metadata=memory_metadata)

        # Send reply
        await send_whatsapp_message(from_number, ai_reply)
        
    except Exception as e:
        logger.error(f"Error processing WhatsApp message: {e}")
