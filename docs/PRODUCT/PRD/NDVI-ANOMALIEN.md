---
id: PRD-NDVI-ANOM-001
status: draft
owners: product, eng
tags: [PRO]
---

# PRD — NDVI‑Anomalien

## Ziel
Schneller Überblick über Felder/Zonen mit ungewöhnlichen Veränderungen; Priorisierung fürs Scouting.

## Scope
Wöchentliche Komposite (S2, cloud‑mask), Outlier‑Detektion vs. Feld‑Historie/Cluster.

## AK
- AK-NDVI-001: Liste „Auffällige Schläge/Zonen“ mit Δ‑Wert und Zeitfenster.
- AK-NDVI-002: Detailansicht <2 s bei 4G, Kacheln aus Cache/COG.

## Risiken
Wolken/Lücken → Unsicherheiten anzeigen; Fehlalarme minimieren.

## KPIs
Anzahl bestätigter Befunde/Scouting‑Fotos je Alarm; Reduktion Blind‑Fahrten.

