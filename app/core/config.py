import os

from starlette.datastructures import CommaSeparatedStrings

PROJECT_NAME = os.getenv("PROJECT_NAME", "FastAPI-SQLAlchemy")
LOG_LEVEL = os.getenv("LOG_LEVEL")
DEBUG = os.getenv("LOG_LEVEL", "").strip().lower() == "debug"
API_VERSION = os.getenv("API_VERSION", "v1")
ROOT_PATH = os.getenv("ROOT_PATH", "")
API_KEY = os.getenv("API_KEY")
API_KEY_NAME = "X-API-KEY"
ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv("ALLOWED_HOSTS", "*"))
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB = os.getenv("POSTGRES_DB")

    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}"
