from fastapi import APIRouter

router = APIRouter()


@router.get("/window")
def weather_window(field_id: str | None = None):
    # EP1 stub
    return {"status": "yellow", "reasons": ["stub"], "metrics": {}}

