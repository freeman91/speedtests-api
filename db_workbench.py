import os, sys
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

USERNAME = os.getenv("MONGO_INITDB_ROOT_USERNAME")
PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
MONGO_URI = os.getenv("MONGO_URI")
ENV = sys.argv[1]


def connect() -> MongoClient:
    client = None
    if ENV == "dev":
        client = MongoClient(
            host=["localhost:27017"],
            username=USERNAME,
            password=PASSWORD,
        )
    elif ENV == "prod":
        client = MongoClient(MONGO_URI)

    return client["database"]


if __name__ == "__main__":
    db = connect()
