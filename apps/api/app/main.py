import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import health, fields, tasks, documents, weather


def get_cors_origins() -> list[str]:
    origins = os.getenv("CORS_ORIGINS", "*")
    if origins.strip() == "*":
        return ["*"]
    return [o.strip() for o in origins.split(",") if o.strip()]


app = FastAPI(title="Farmer API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_cors_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health.router)
app.include_router(fields.router, prefix="/fields", tags=["fields"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
app.include_router(documents.router, prefix="/documents", tags=["documents"])
app.include_router(weather.router, prefix="/weather", tags=["weather"])
