# Architektur (Gesamt)

## Frontend
- Framework: Next.js (App Router) — Svelte/SvelteKit wird explizit nicht verwendet (siehe ADR‑0006)
- PWA, i18n (de/en), TanStack Query/React Query, Zustand/Signals
- Karte: MapLibre GL JS, Draw‑Tools, Vector‑Tiles

## Backend
- Option A (Empfehlung): FastAPI + Uvicorn, Python‑Ökosystem für Geo/ML Nähe
- Option B: NestJS (TypeScript) für Single‑Language‑Stack
- Postgres 16 + PostGIS, Redis (Queues/Cache), Objekt‑Storage (S3‑kompatibel, z. B. MinIO)
- Async Jobs: Celery/Arq/RQ für NDVI‑Pipelines, OCR, Exporte

## Geo/Remote Sensing
- Raster: rasterio, rio‑cogeo, NumPy; Speicherung als COG/MBTiles
- CRS: ETRS89/UTM32 & 33; pyproj‑Transform; Auto‑Detect beim Import

## Sicherheit & Datenschutz
- OAuth 2.1/OIDC (z. B. Keycloak), MFA optional (TOTP)
- Verschlüsselung in Transit/at Rest; Audit‑Log (OpenTelemetry)
- Mandantentrennung + Row Level Security; Backups (PITR)

## DevOps & Hosting
- Monorepo (Turborepo), CI/CD (GitHub Actions), IaC (Terraform)
- FE auf Vercel; BE/DB/Storage auf Hetzner oder AWS (eu‑central‑1)
- Observability: Sentry, Grafana/Prometheus, strukturiertes Logging (JSON)

## Kostenkontrolle
- Open‑Source Kartenstack (MapLibre/OMT), On‑Demand NDVI, Storage Lifecycle/Archivierung
