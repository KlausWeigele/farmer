# ADR-0004 — Hosting (Hetzner+Vercel vs. AWS only)

Status: accepted
Datum: 2025-09-14

## Kontext
Kostenbewusster Start in EU, schnelles FE‑Deployment, klare Datenlokation.

## Optionen
- A) FE auf Vercel; API/DB/Storage auf Hetzner (DE) — Kosten/Performance gut, EU‑Standort.
- B) AWS only (eu‑central‑1) — einheitlich, aber höherer Preis.

## Entscheidung
A) Hetzner (API/DB/MinIO) + Vercel (FE) für MVP. Evaluierung AWS bei Skalierung/Enterprise.

## Konsequenzen
- Pro: geringe Kosten, EU‑Datenstandort; Contra: Multi‑Provider‑Management.

