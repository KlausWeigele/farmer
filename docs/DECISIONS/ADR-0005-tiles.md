# ADR-0005 — Tiles (OMT/MapTiler vs. eigener Server)

Status: accepted
Datum: 2025-09-14

## Kontext
Kartenbasis für MVP ohne hohe Fixkosten; Offline‑Raster/Cache geplant.

## Optionen
- A) OpenMapTiles/MapTiler Basic für Start; später optional eigener Tile‑Server.
- B) Eigener Vector‑Tile‑Stack ab Tag 1.

## Entscheidung
A) OMT/MapTiler für MVP; eigener Tile‑Server bei Skalierung/Bedarf an vollständiger Kontrolle.

## Konsequenzen
- Pro: schnell, zuverlässig; Contra: externer Dienst/Limitierungen im Free/Basic‑Plan.

