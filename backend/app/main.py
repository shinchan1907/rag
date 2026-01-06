from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
import redis
import psycopg2
from psycopg2 import OperationalError

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """
    Root endpoint to verify the service is running.
    """
    return {
        "message": f"Welcome to {settings.PROJECT_NAME}",
        "status": "online",
        "docs": f"https://{settings.DOMAIN}/docs"
    }

@app.get("/health")
async def health_check():
    """
    Health check endpoint for Docker and monitoring.
    """
    health_status = {"status": "healthy", "components": {}}
    
    # Check Postgres
    try:
        conn = psycopg2.connect(settings.get_database_url())
        conn.close()
        health_status["components"]["db"] = "connected"
    except OperationalError as e:
        health_status["status"] = "degraded"
        health_status["components"]["db"] = f"disconnected: {str(e)}"

    # Check Redis
    try:
        r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, socket_connect_timeout=1)
        r.ping()
        health_status["components"]["redis"] = "connected"
    except Exception as e:
        health_status["status"] = "degraded"
        health_status["components"]["redis"] = f"disconnected: {str(e)}"

    return health_status
