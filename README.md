## Setup

1. Install Docker
2. create .env file with contents
```sh
ENV=dev
FRONTEND_IP=http://localhost:9000
MONGO_INITDB_DATABASE=
MONGO_INITDB_ROOT_USERNAME=
MONGO_INITDB_ROOT_PASSWORD=
MONGO_IP=172.19.199.3
MONGO_PORT=27017
SECRET_KEY=
```
3. build docker containers `docker-compose up -d`
4. To use db_workbench/exec_speedtest install the following requirements locally 

```sh
python3.8 -m pip install speedtest-cli pymongo python-dotenv
script/db_workbench.py

script/exec_speedtest
```

5. add cronjob
```sh
crontab -e
# ----------
*/5 * * * * cd ~/repos/speedtests-api && python3 scripts/exec_speedtest.py >> cronlogs/stdout 2>> cronlogs/errors
# ----------
```
