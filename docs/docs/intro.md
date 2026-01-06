# Jyoti AI Documentation

Welcome to the documentation for Jyoti AI.

## Project Vision
Jyoti AI is designed to be more than just a chatbot. She is a Personal Assistant with a character—Donna.

## Core Features
1. **WhatsApp Integration**: Treat owners differently from outsiders.
2. **Gmail/Calendar Access**: Summary and notifications.
3. **RAG Memory**: Persistent context from every chat.
4. **PC Activity Monitoring**: Efficiency tracking via API.

## API Reference
### WhatsApp Webhook
- `GET /webhook/whatsapp`: Verification.
- `POST /webhook/whatsapp`: Handle messages.

### Knowledge Management
- `POST /api/knowledge/ingest`: Ingest data.
- `GET /api/knowledge/query`: Search memory.

### Activity Monitoring
- `POST /api/activity/log`: Send PC details.
