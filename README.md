```
docker-compose up -d

python -m venv venv
source venv/bin/activate
pip3 install -r requirements.text
pip3 install -r requirements.dev.text
script/db_workbench.py dev
```


.env file
```
ENV=dev

FRONTEND_IP=http://localhost:9000

MONGO_URI=
MONGO_INITDB_DATABASE=database
MONGO_INITDB_ROOT_USERNAME=admin
MONGO_INITDB_ROOT_PASSWORD=password
MONGO_IP=172.19.199.3
MONGO_PORT=27017
SECRET_KEY=
```