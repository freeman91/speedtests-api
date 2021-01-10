from flask import request, Blueprint

from api.db import database as db

users = Blueprint("users", __name__)


@users.route("/users")
def user_add():
    user = db.users.find_one()
    user["_id"] = str(user["_id"])
    return {"resp": user}, 200
