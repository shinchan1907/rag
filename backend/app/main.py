from fastapi import FastAPI
import os
import psycopg2
import redis

app = FastAPI(title="Jyoti AI MVP")

@app.get("/")
def read_root():
    return {"status": "online", "message": "Jyoti AI MVP is running"}

@app.get("/health")
def health_check():
    # Check DB
    db_status = "unknown"
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        conn.close()
        db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"

    # Check Redis
    redis_status = "unknown"
    try:
        r = redis.from_url(os.getenv("REDIS_URL", "redis://redis:6379/0"))
        r.ping()
        redis_status = "connected"
    except Exception as e:
        redis_status = f"error: {str(e)}"

    return {
        "status": "healthy",
        "database": db_status,
        "redis": redis_status
    }
