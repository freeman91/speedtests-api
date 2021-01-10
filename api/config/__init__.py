import logging
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)


class Config(object):
    LOG_LEVEL = logging.INFO


class DevelopmentConfig(Config):
    ENV = "dev"
    LOG_LEVEL = logging.DEBUG
    DEBUG = True
    SECRET_KEY = "secr3t"
    APP_FQDN = "localhost:9000"
    DATABASE_HOST = os.getenv("MONGO_IP", "localhost")
    DATABASE_PORT = os.getenv("MONGO_PORT", 27017)


class TestConfig(Config):
    ENV = "test"
    LOG_LEVEL = logging.DEBUG
    SECRET_KEY = "test"
    APP_FQDN = "localhost:9000"
    DATABASE_HOST = os.getenv("MONGO_IP", "localhost")
    DATABASE_PORT = os.getenv("MONGO_PORT", 27018)


class ProductionConfig(Config):
    ENV = "production"
    LOG_LEVEL = logging.DEBUG
    DEBUG = True
    SECRET_KEY = ""
    APP_FQDN = ""
    DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT = os.getenv("DATABASE_PORT", 27017)


def get_config():
    env = os.environ.get("ENV", "dev").lower()
    if env == "dev":
        return DevelopmentConfig
    elif env == "test":
        return TestConfig
    elif env == "production":
        return ProductionConfig
    else:
        return Config


app_config = get_config()
