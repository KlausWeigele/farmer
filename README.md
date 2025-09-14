# Farmer — Produkt, Architektur & Skeleton

Willkommen! Dieses Repository enthält die Produkt‑, Architektur‑ und Compliance‑Dokumentation für die geplante Software für Landwirte in Deutschland.

- Start: siehe `docs/INDEX.md`
- Vision und Nutzen: `docs/VISION.md`
- Feature‑Katalog mit Tags ([MVP]/[PRO]/[DE]/[DIFF]/…): `docs/PRODUCT/FEATURES.md`
- Roadmap (90 Tage, Phasen, 12–18 Monate): `docs/PRODUCT/ROADMAP.md`
- Epics mit Akzeptanzkriterien: `docs/PRODUCT/EPICS.md`
- Architektur & Datenmodell: `docs/ARCHITECTURE/ARCHITECTURE.md`, `docs/ARCHITECTURE/DATA-MODEL.md`
- Integrationen (DWD, Sentinel, ISOXML, Agrirouter, …): `docs/ARCHITECTURE/INTEGRATIONS.md`
- DSGVO & Recht: `docs/SECURITY-COMPLIANCE.md`

Konventionen, Vorlagen und Decision Records (ADR) findest du in `docs/LEGEND.md`, `docs/TEMPLATES/`, `docs/DECISIONS/`.

## Lokal starten (Hinweis)
- `.env` in `infra/` von `.env.example` ableiten.
- Docker Compose: `cd infra && docker compose --env-file .env up -d`
- API (Stub): `apps/api` enthält FastAPI; Health unter `/health`.
- Web (Stub): `apps/web` Next.js 14 App Router.

Hinweis: Dieses Skeleton enthält noch keine vollständige Build‑/CI‑Konfiguration.
