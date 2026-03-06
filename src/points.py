from qdrant_client import QdrantClient, models

def upsert_data(client: QdrantClient, collection_name: str, points_data: list):
    return client.upsert(
        collection_name=collection_name,
        points=points_data
    )

def search_vectors(client: QdrantClient, collection_name: str, query_vector: list, limit: int = 1):
    return client.query_points(
        collection_name=collection_name,
        query=query_vector,
        limit=limit
    )