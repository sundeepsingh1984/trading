from databases import DatabaseURL
from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

PROJECT_NAME = "Trading-app"
VERSION = "1.0.0"
API_PREFIX = "/api"

SECRET_KEY = config("SECRET_KEY", cast=Secret, default="CHANGEME")

POSTGRES_USER = config("DB_USER", cast=str)
POSTGRES_PASSWORD = config("postgres", cast=Secret)
POSTGRES_SERVER = config("DB_HOST", cast=str, default="db")
POSTGRES_PORT = config("DB_PORT", cast=str, default="5432")
POSTGRES_DB = config("DB_NAME", cast=str)

DATABASE_URL = config(
  "DB_URL",
  cast=DatabaseURL,
  default=f"postgresql:asyncpg//{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
)
