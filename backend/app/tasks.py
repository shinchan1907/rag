from celery import Celery
from .config import settings
from .services.gmail import get_gmail_service, list_recent_emails
from .services.whatsapp import send_whatsapp_message
import asyncio

celery_app = Celery('jyoti_ai', broker=settings.REDIS_URL)

@celery_app.task
def check_emails_and_notify():
    # Sync wrapper for async operations
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_notify_job())

async def _notify_job():
    service = get_gmail_service()
    if not service:
        return
    
    emails = await list_recent_emails(service)
    if emails:
        # Simple logic: notify owner about new emails
        for owner in settings.OWNER_NUMBERS:
            await send_whatsapp_message(owner, f"Sir, you have {len(emails)} new emails. Should I summarize them for you?")

# Beat schedule
celery_app.conf.beat_schedule = {
    'check-emails-every-30-minutes': {
        'task': 'app.tasks.check_emails_and_notify',
        'schedule': 1800.0,
    },
}
