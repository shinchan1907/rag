from app.celery_app import celery_app
import logging

logger = logging.getLogger(__name__)

@celery_app.task(acks_late=True)
def check_emails():
    logger.info("Checking emails for owner...")
    # TODO: Implement Gmail API logic here
    return "Checked emails"

@celery_app.task(acks_late=True)
def ingest_document(content: str, metadata: dict):
    logger.info(f"Ingesting document: {metadata}")
    # TODO: Implement ChromaDB ingestion here
    return "Ingested"
