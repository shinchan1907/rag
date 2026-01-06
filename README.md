# Jyoti AI - Advanced Personal Assistant Agent

Jyoti AI is a robust, containerized Personal Assistant (PA) system designed to run on a VPS (AWS Lightsail). It acts as a "Second Brain," integrating with WhatsApp for interaction, storing context in a Vector Database (ChromaDB), and performing background tasks like email summarization and document ingestion.

## 🌟 Features

*   **Dual Persona System**:
    *   **"Donna"**: A polite, proactive, and personal assistant for the Owner.
    *   **"Professional PA"**: A formal assistant for handling guest queries.
*   **WhatsApp Integration**: Full 2-way communication via WhatsApp Business API (WABA).
*   **RAG (Retrieval-Augmented Generation)**: Ingests documents and chats into a Vector DB for long-term memory and context-aware responses.
*   **Background Tasks**:
    *   **Email Monitoring**: Periodically checks Gmail for important emails and summarizes them.
    *   **Document Ingestion**: Asynchronous processing of documents for the knowledge base.
*   **Observability**:
    *   **Prometheus**: Metrics collection.
    *   **Grafana**: Visual dashboards for system health and performance.
*   **Security**:
    *   **Traefik Edge Router**: Automatic SSL (Let's Encrypt) and reverse proxying.
    *   **Role-Based Access**: Owner-only access to sensitive data.

## 🏗️ Tech Stack

*   **Core**: Python 3.11, FastAPI
*   **Task Queue**: Celery, Redis
*   **Database**: PostgreSQL (Relational), ChromaDB (Vector)
*   **Infrastructure**: Docker, Docker Compose
*   **Routing**: Traefik v3
*   **Monitoring**: Prometheus, Grafana

## 🚀 Quick Start

### Prerequisites

*   Docker & Docker Compose installed on the host.
*   A domain name pointed to your server IP (e.g., `ai.bytenex.io`).
*   WhatsApp Business Account (WABA) credentials.

### Installation

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/shinchan1907/rag.git
    cd rag
    ```

2.  **Configure Environment**:
    Create a `.env` file (or use the provided one) with your credentials:
    ```bash
    # Domain & SSL
    DOMAIN=ai.bytenex.io
    SSL_EMAIL=your-email@example.com

    # Secrets
    POSTGRES_PASSWORD=secure_password
    OPENAI_API_KEY=sk-proj-...
    WHATSAPP_ACCESS_TOKEN=...
    
    # Owner Config
    OWNER_NUMBERS=+919872944859,+917087215463
    ```

3.  **Deploy**:
    Run the deployment script to build and start all services:
    ```bash
    bash deploy.sh
    ```

4.  **Verify**:
    *   **Documentation**: [https://ai.bytenex.io/](https://ai.bytenex.io/)
    *   **API Health**: [https://ai.bytenex.io/api/health](https://ai.bytenex.io/api/health)
    *   **Grafana**: [https://ai.bytenex.io/grafana/](https://ai.bytenex.io/grafana/) (Default: `admin` / `Account102@@`)

## 📂 Project Structure

```
.
├── backend/                # FastAPI Application
│   ├── app/
│   │   ├── api/            # API Routes (WhatsApp, Chat, Ingest)
│   │   ├── core/           # Config & Settings
│   │   ├── worker.py       # Celery Tasks
│   │   └── main.py         # App Entrypoint
│   └── Dockerfile
├── docs/                   # MkDocs Documentation
├── monitoring/             # Prometheus Config
├── docker-compose.yml      # Service Orchestration
├── deploy.sh               # Deployment Script
└── .env                    # Environment Variables
```

## 🔌 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/whatsapp/webhook` | Verifies the webhook with Meta. |
| `POST` | `/api/whatsapp/webhook` | Receives incoming WhatsApp messages. |
| `POST` | `/api/chat/` | Direct chat interface for testing. |
| `POST` | `/api/ingest/` | Ingests text/files into the Vector DB. |

## 🛠️ Development

To run locally for development:

1.  **Install Dependencies**:
    ```bash
    cd backend
    pip install -r requirements.txt
    ```

2.  **Run Backend**:
    ```bash
    uvicorn app.main:app --reload
    ```

3.  **Run Worker**:
    ```bash
    celery -A app.worker worker --loglevel=info
    ```

## 📝 License

Private & Confidential - Property of Sunny Gupta.
