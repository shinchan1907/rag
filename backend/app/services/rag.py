import chromadb
from chromadb.utils import embedding_functions
from ..config import settings
import uuid

# Use OpenAI embeddings
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=settings.OPENAI_API_KEY,
    model_name="text-embedding-3-small"
)

client = chromadb.PersistentClient(path=settings.CHROMA_DB_PATH)
collection = client.get_or_create_collection(
    name="jyoti_ai_memory",
    embedding_function=openai_ef
)

def add_to_memory(text: str, metadata: dict = None):
    collection.add(
        documents=[text],
        metadatas=[metadata or {}],
        ids=[str(uuid.uuid4())]
    )

def query_memory(query_text: str, n_results: int = 5):
    results = collection.query(
        query_texts=[query_text],
        n_results=n_results
    )
    return results["documents"][0] if results["documents"] else []
