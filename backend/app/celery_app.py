from celery import Celery
from app.core.config import settings

celery_app = Celery("worker", broker=settings.REDIS_URL, backend=settings.REDIS_URL)

celery_app.conf.task_routes = {
    "app.worker.test_task": "main-queue",
}

celery_app.conf.beat_schedule = {
    "check-emails-every-5-minutes": {
        "task": "app.worker.check_emails",
        "schedule": 300.0,
    },
}
