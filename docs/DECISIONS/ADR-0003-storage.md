# ADR-0003 — Storage (S3/MinIO vs. DB-LO)

Status: accepted
Datum: 2025-09-14

## Kontext
Dokumente, Fotos, Kacheln, COGs; große Dateien, Signierte Downloads, Lifecycle/Archivierung.

## Optionen
- A) S3‑kompatibel (MinIO dev; S3 eu‑central‑1 prod)
- B) Postgres Large Objects (nur MVP)

## Entscheidung
A) S3‑kompatibel ab Start (MinIO lokal/Dev), Metadaten in DB.

## Konsequenzen
- Pro: skaliert, günstig, Signaturen; Contra: zusätzliche Abhängigkeit/Infra.

