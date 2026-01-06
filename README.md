# Jyoti AI: Personal RAG-powered AI Companion

Developed by Sunny Gupta

🌌 **Overview**
Jyoti AI is a low-latency, multi-persona AI ecosystem built for Sunny.

- **Bilingual**: Speaks natural Hinglish and English.
- **Donna-Inspired**: Resourceful, witty, and always two steps ahead.
- **Deep Memory**: Uses RAG to recall history with perfect accuracy.

🚀 **Tech Stack**
- **Frontend/Backend**: FastAPI (Python)
- **Vector DB**: ChromaDB
- **Message Broker**: Redis
- **Database**: PostgreSQL
- **Orchestration**: Docker Compose
- **Proxy**: Traefik + SSL (Cloudflare)

## 🛠 Setup & Deployment

1. **Clone the Repo**
   ```bash
   git clone https://github.com/shinchan1907/rag-project.git
   cd rag-project
   ```

2. **Configure Environment**
   ```bash
   cp .env.example .env
   # Fill in your OPENAI_API_KEY, WABA details, and Cloudflare credentials
   ```

3. **Launch with Docker**
   ```bash
   docker compose up -d --build
   ```

## 🧠 Personal Knowledge (RAG)
You can ingest your chat history or documents via the API:
- `POST /api/knowledge/ingest`: Send JSON or upload .txt files.

## 📱 Integration
- **Owner Mode**: +919872944859, +917087215463 triggers the "Donna" persona.
- **Security Mode**: Other numbers get a professional PA response.

Created with ❤️ by Sunny Gupta.
