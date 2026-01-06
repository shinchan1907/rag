from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from .routers import whatsapp, knowledge, activity
from .config import settings

from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(
    title="Jyoti AI API",
    description="Backend for Jyoti AI - Personal RAG-powered AI Companion",
    version="1.0.0",
)

# Prometheus Instrumentation
Instrumentator().instrument(app).expose(app)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(whatsapp.router, prefix="/webhook", tags=["whatsapp"])
app.include_router(knowledge.router, prefix="/api/knowledge", tags=["knowledge"])
app.include_router(activity.router, prefix="/api/activity", tags=["activity"])

@app.get("/")
async def root():
    return {"message": "Jyoti AI is online and keeping things in order. - Donna"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
