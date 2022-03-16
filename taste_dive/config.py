import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    SECRET_KEY = os.getenv("SECRET_KEY")
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_ENV = os.getenv("FLASK_ENV")
    API_KEY = os.getenv("API_KEY")
    MONGODB_SETTINGS = {"host": os.getenv("MONGODB_SETTINGS")}


class TestConfig(Config):
    SECRET_KEY = "112233445566998877"
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_ENV = "testing"
    TESTING = True
    DEBUG = True
    MONGODB_SETTINGS = {"host": os.getenv("MONGODB_SETTINGS")}
