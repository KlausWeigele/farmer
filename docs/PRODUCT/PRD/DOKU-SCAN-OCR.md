---
id: PRD-DOKU-OCR-001
status: draft
owners: product, eng
tags: [MVP]
---

# PRD — Doku‑Scan (OCR)

## Ziel & Problem
Wiegescheine/Rechnungen schnell erfassen, Schlag/Task zuordnen; Offline‑Upload → späterer Sync.

## Scope
In: Kamera‑Capture, Zuschneiden, OCR, Felderkennung (Datum, Menge, Produkt), Confidence‑Score, manuelle Bestätigung.
Out: Vollständige Beleg‑Workflow‑Automatisierung (später PRO).

## AK
- AK-OCR-001: OCR extrahiert Datum/Menge mit >90 % Trefferquote bei Standardbelegen.
- AK-OCR-002: Offline‑Upload mit späterem Sync; Konfliktlösung vorhanden.
- AK-OCR-003: Zuordnung zu Schlag/Task in ≤2 Taps.

## Risiken
Belegvielfalt → Template‑Fallback; Datenschutz (personenbezogene Daten maskieren/anonymisieren).

## KPIs
Zeit bis erfasster Beleg <30 s; Anteil Belege ohne manuelle Korrektur >70 %.

