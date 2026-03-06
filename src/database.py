from qdrant_client import QdrantClient, models
from .config import QDRANT_URL, QDRANT_API_KEY

def get_client():
    return QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

def init_collection(client: QdrantClient, name: str, size: int):
    if not client.collection_exists(name):
        client.create_collection(
            collection_name=name,
            vectors_config=models.VectorParams(
                size=size, 
                distance=models.Distance.COSINE
            )
        )
        return f"Created {name}"
    return f"{name} already exists"