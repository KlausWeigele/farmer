# ADR-0001 — Backend-Stack (FastAPI vs. NestJS)

Status: proposed
Datum: 2025-09-14

## Kontext
Backend soll Geo‑/RS‑Pipelines, OCR/Exporte und klassische CRUD/APIs bedienen. Team möchte schnelle Iteration für MVP, starke Geo‑Bibliotheken und klare DSGVO‑Story.

## Optionen
- A) FastAPI (Python) + Uvicorn; Stärken: Geo/ML‑Ökosystem (rasterio, rio‑cogeo, numpy/xarray), einfache Worker‑Integration (Celery/Arq), schnelles Prototyping.
- B) NestJS (TypeScript); Stärken: Einsprachiger Stack (mit Frontend), gutes Modul‑/DI‑System, starke Tooling‑Ökologie.

## Entscheidung (Vorschlag)
Tendenz zu A) FastAPI für MVP‑Phase wegen Geo/ML‑Nähe und bereits geplanten Python‑Pipelines. NestJS bleibt Option für spätere Services.

## Konsequenzen
- Pro: schnellere RS/Geo‑Implementierung, vorhandene Libs; klare Pfade für Worker
- Contra: Polyglott (TS+Py); zusätzliche Schnittstelle/Contracts zwischen FE/BE/Worker

