import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.engine import create_engine

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"postgresql+psycopg://{os.getenv('POSTGRES_USER','farm')}:{os.getenv('POSTGRES_PASSWORD','farm123')}@{os.getenv('POSTGRES_HOST','localhost')}:{os.getenv('POSTGRES_PORT','5432')}/{os.getenv('POSTGRES_DB','farm')}",
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

app = FastAPI(title="Farmer API", version="0.1.0")


@app.get("/health")
def health():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        db_ok = True
    except Exception as e:
        db_ok = False
    return JSONResponse({"ok": True, "db": db_ok})

