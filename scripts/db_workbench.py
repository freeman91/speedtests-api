import os, sys
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

USERNAME = os.getenv("MONGO_INITDB_ROOT_USERNAME")
PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD")


def connect() -> MongoClient:
    client = None
    try:
        client = MongoClient(
            host=["192.168.0.42:27017"],
            username=USERNAME,
            password=PASSWORD,
        )
        return client["tests"]
    except:
        print("Error")


def insert_speedtest(values):
    # TODO: input validation
    db = connect()
    insert_doc = {
        "timestamp": values["timestamp"],
        "ping": values["ping"],
        "download": values["download"],
        "upload": values["upload"],
        "server_name": values["server_name"],
        "server_lat": values["server_lat"],
        "server_long": values["server_long"],
    }
    try:
        db.tests.insert_one(insert_doc)
        print(f"{values['timestamp']}: speedtest inserted")
    except:
        print(f"Error inserting data: {insert_doc}")


if __name__ == "__main__":
    db = connect()
