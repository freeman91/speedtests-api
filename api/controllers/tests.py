import time
import json
from bson import json_util
from flask import request, Blueprint

from api.db import database as db

tests = Blueprint("tests", __name__)


@tests.route("/tests/past-day")
def get_test_data():
    now = time.time()
    print(db)

    test_data = db.tests.find(
        {
            "timestamp": {
                "$gt": now - 86400,
                "$lte": now,
            }
        }
    )

    json_docs = [json.dumps(doc, default=json_util.default) for doc in test_data]

    return {"resp": json_docs}, 200
