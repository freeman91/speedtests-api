import os, time, logging

from flask import Flask, jsonify, request
from flask_meter import FlaskMeter
from flask_cors import CORS

from api.controllers.tests import tests
from api.config import app_config
from api.db import database

flask_meter = FlaskMeter()


def create_app():
    app = Flask(__name__)
    cors = CORS(app)

    logger = logging.getLogger()
    logger.setLevel(app_config.LOG_LEVEL)

    app.config.from_object(app_config)

    flask_meter.init_app(app)

    app.register_blueprint(tests)

    @app.route("/health")
    def index():
        check = database.tests.find_one()
        health = "DB connected" if check else "No DB connection"
        payload = {"health": "healthy", "DB connection": health}
        return jsonify(payload)

    @app.route("/last24hours")
    def last_24():
        utc_24_hours_ago = round(time.time()) - 86400
        res = database.tests.find({"timestamp": {"$gt": utc_24_hours_ago}}, {"_id": 0})
        return jsonify({"result": "success", "payload": list(res)})

    return app
