#! /usr/bin/env python3

import time
from datetime import datetime
from speedtest import Speedtest
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

from db_workbench import insert_speedtest


def run_speedtest():
    try:
        s = Speedtest()
        s.get_best_server()
        s.download()
        s.upload()
        s.results.share()
        return {"msg": "SUCCESS", **s.results.dict()}
    except:
        return {
            "msg": "FAILED",
            "timestamp": int(time.time()),
            "ping": 0,
            "download": 0,
            "upload": 0,
            "server": {
                "name": None,
                "lat": None,
                "lon": None,
            },
        }


# move this function to db workbench
def main():
    speedtest_vals = run_speedtest()
    if speedtest_vals["msg"] == "SUCCESS":
        speedtest_vals["timestamp"] = (
            int(
                time.mktime(
                    datetime.strptime(
                        speedtest_vals["timestamp"][
                            0 : speedtest_vals["timestamp"].find(".")
                        ],
                        "%Y-%m-%dT%H:%M:%S",
                    ).timetuple()
                )
            )
            - 18000
        )

    ret = {
        "timestamp": speedtest_vals["timestamp"],
        "ping": round(speedtest_vals["ping"], 1),
        "download": round(speedtest_vals["download"] / 10 ** 6, 1),
        "upload": round(speedtest_vals["upload"] / 10 ** 6, 1),
        "server_name": speedtest_vals["server"]["name"],
        "server_lat": speedtest_vals["server"]["lat"],
        "server_long": speedtest_vals["server"]["lon"],
    }
    insert_speedtest(ret)


if __name__ == "__main__":
    main()
