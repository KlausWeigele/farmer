import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.engine import create_engine

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"postgresql+psycopg://{os.getenv('POSTGRES_USER','farm')}:{os.getenv('POSTGRES_PASSWORD','farm123')}@{os.getenv('POSTGRES_HOST','localhost')}:{os.getenv('POSTGRES_PORT','5432')}/{os.getenv('POSTGRES_DB','farm')}",
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

app = FastAPI(title="Farmer API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        db_ok = True
    except Exception as e:
        db_ok = False
    return JSONResponse({"ok": True, "db": db_ok})


class FieldIn(BaseModel):
    name: str
    geom: dict  # GeoJSON geometry in EPSG:4326


@app.post("/fields")
def create_field(field: FieldIn):
    try:
        with engine.begin() as conn:
            # Ensure PostGIS
            try:
                conn.execute(text("CREATE EXTENSION IF NOT EXISTS postgis"))
            except Exception:
                pass
            # Insert geometry (transform to EPSG:25832 and enforce MultiPolygon)
            res = conn.execute(
                text(
                    """
                    insert into field (farm_id, name, area_ha, geom)
                    values (
                        NULL,
                        :name,
                        ST_Area(
                          ST_Transform(
                            ST_Multi(
                              ST_SetSRID(
                                ST_GeomFromGeoJSON(:gjson::json), 4326
                              )
                            ), 25832
                          )
                        )/10000.0,
                        ST_Transform(
                          ST_Multi(
                            ST_SetSRID(
                              ST_GeomFromGeoJSON(:gjson::json), 4326
                            )
                          ), 25832
                        )
                    )
                    returning id, name, area_ha
                    """
                ),
                {"name": field.name, "gjson": field.geom},
            )
            row = res.fetchone()
            return {"id": str(row[0]), "name": row[1], "area_ha": float(row[2])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/fields")
def list_fields():
    try:
        with engine.connect() as conn:
            res = conn.execute(text("select id, name, area_ha from field order by created_at desc limit 100"))
            rows = [
                {"id": str(r[0]), "name": r[1], "area_ha": float(r[2]) if r[2] is not None else None}
                for r in res
            ]
            return rows
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
