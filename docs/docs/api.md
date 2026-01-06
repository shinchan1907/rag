# API Reference

The backend exposes a RESTful API documented via OpenAPI (Swagger).

## Endpoints

### WhatsApp Webhook

*   `GET /api/whatsapp/webhook`: Verify webhook (Meta challenge).
*   `POST /api/whatsapp/webhook`: Receive messages.

### Chat

*   `POST /api/chat/`: Direct chat interface.

### Ingestion

*   `POST /api/ingest/`: Ingest documents into Vector DB.

## Swagger UI

Access the interactive Swagger UI at [/docs](/docs).
