import time
import json
from bson import json_util
from flask import request, Blueprint
from flask_cors import cross_origin

from api.db import database as db

tests = Blueprint("tests", __name__)


@tests.route("/tests/past-day", methods=["GET"])
@cross_origin()
def get_test_data():
    now = time.time()
    print(db)

    test_data = db.tests.find(
        {
            "timestamp": {
                "$gt": now - 86400,
                "$lte": now,
            }
        },
        {
            "_id": 0,
        }
    )

    json_docs = [json.dumps(doc, default=json_util.default) for doc in test_data]

    return {"payload": json_docs}, 200
