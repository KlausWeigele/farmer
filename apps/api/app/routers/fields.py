import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy import text
from uuid import UUID

from ..db import engine

router = APIRouter()


class FieldIn(BaseModel):
    name: str
    geom: dict  # GeoJSON geometry in EPSG:4326


@router.post("")
def create_field(field: FieldIn):
    try:
        with engine.begin() as conn:
            conn.execute(text("CREATE EXTENSION IF NOT EXISTS postgis"))
            conn.execute(text("CREATE EXTENSION IF NOT EXISTS pgcrypto"))
            res = conn.execute(
                text(
                    """
                    insert into field (id, farm_id, name, area_ha, crs, geom, created_at, updated_at)
                    values (
                        gen_random_uuid(),
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
                        'EPSG:25832',
                        ST_Transform(
                          ST_Multi(
                            ST_SetSRID(
                              ST_GeomFromGeoJSON(:gjson::json), 4326
                            )
                          ), 25832
                        ),
                        now(), now()
                    )
                    returning id, name, area_ha
                    """
                ),
                {"name": field.name, "gjson": json.dumps(field.geom)},
            )
            row = res.fetchone()
            return {"id": str(row[0]), "name": row[1], "area_ha": float(row[2])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("")
def list_fields():
    with engine.connect() as conn:
        res = conn.execute(text("select id, name, area_ha from field order by created_at desc limit 100"))
        rows = [
            {"id": str(r[0]), "name": r[1], "area_ha": float(r[2]) if r[2] is not None else None}
            for r in res
        ]
        return rows


class FieldUpdate(BaseModel):
    name: str | None = None
    geom: dict | None = None  # GeoJSON geometry in EPSG:4326


@router.put("/{field_id}")
def update_field(field_id: UUID, payload: FieldUpdate):
    setters = ["updated_at = now()"]
    params: dict[str, object] = {"id": str(field_id)}
    if payload.name is not None:
        setters.append("name = :name")
        params["name"] = payload.name
    if payload.geom is not None:
        setters.append(
            "geom = ST_Transform(ST_Multi(ST_SetSRID(ST_GeomFromGeoJSON(:gjson::json),4326)),25832)"
        )
        setters.append(
            "area_ha = ST_Area(ST_Transform(ST_Multi(ST_SetSRID(ST_GeomFromGeoJSON(:gjson::json),4326)),25832))/10000.0"
        )
        params["gjson"] = json.dumps(payload.geom)
    if len(setters) == 1:
        raise HTTPException(status_code=400, detail="nothing to update")
    sql = f"update field set {', '.join(setters)} where id = :id returning id, name, area_ha"
    with engine.begin() as conn:
        res = conn.execute(text(sql), params)
        row = res.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="not found")
        return {"id": str(row[0]), "name": row[1], "area_ha": float(row[2]) if row[2] is not None else None}


@router.delete("/{field_id}")
def delete_field(field_id: UUID):
    with engine.begin() as conn:
        res = conn.execute(text("delete from field where id = :id returning 1"), {"id": str(field_id)})
        if res.fetchone() is None:
            raise HTTPException(status_code=404, detail="not found")
    return {"ok": True}
