import os
from sqlalchemy import create_engine

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"postgresql+psycopg://{os.getenv('POSTGRES_USER','farm')}:{os.getenv('POSTGRES_PASSWORD','farm123')}@{os.getenv('POSTGRES_HOST','postgres')}:{os.getenv('POSTGRES_PORT','5432')}/{os.getenv('POSTGRES_DB','farm')}",
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

