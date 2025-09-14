from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy import text

from ..db import engine

router = APIRouter(tags=["health"])


@router.get("/health")
def health():
    return JSONResponse({"ok": True})


@router.get("/ready")
def ready():
    db_ok = False
    try:
        with engine.connect() as conn:
            conn.execute(text("select 1"))
        db_ok = True
    except Exception:
        db_ok = False
    return JSONResponse({"ok": db_ok, "db": db_ok})

