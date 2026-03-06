from qdrant_client import models
from src.database import get_client, init_collection


def main():
    client = get_client()
    collection = "my_first_collection"

    result = init_collection(client, collection, size=384)
    print(result)

    print(client.get_collections())


if __name__ == "__main__":
    main()