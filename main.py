from qdrant_client import models
from src.database import get_client, init_collection
from src.points import upsert_data, search_vectors

def main():
    client = get_client()
    collection = "my_first_collection"

    result = init_collection(client, collection, size=4)
    print(result)

    print(client.get_collections())

    sample_points = [
        models.PointStruct(id=1, vector=[0.1, 0.2, 0.3, 0.4], payload={"tag": "step6"})
    ]
    upsert_data(client, collection, sample_points)

    results = search_vectors(client, collection, [0.1, 0.2, 0.3, 0.4])
    print(f"Search result: {results.points[0].payload}")

if __name__ == "__main__":
    main()