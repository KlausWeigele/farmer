---
id: PRD-FENSTER-AMP-001
status: draft
owners: product, eng
tags: [MVP, DIFF, DE]
---

# PRD — Fenster‑Ampel (48 h)

## Ziel & Problem
Schnelle, rechtssichere Einschätzung: „Kann ich in den nächsten 48 h spritzen/düngen/ernten/mähen?“ Heute verteilt auf viele Apps/Erfahrungswerte → Zeitverlust, Risiko.

## Personas / Nutzer
Betriebsleiter, Feldmitarbeiter. Mobil draußen, teilweise schlechtes Netz → Offline‑Fallback nötig.

## Scope
In: 48‑h Prognose pro Schlag; Ampel (grün/gelb/rot) je Maßnahme; Begründung (Wind, ΔT, Blattnässe, Bodenbefahrbarkeit).
Out: Mittel‑/PSM‑Empfehlungen, Langfrist‑Planung >72 h.

## User Flows
Home → „Heute auf dem Hof“ → Ampel‑Karte + Schlagliste → Klick auf Schlag → Begründung + Schnellaktion „Task anlegen“.

## Akzeptanzkriterien
- AK-PRD-AMP-001: 48 h Ansicht mit Ampel; Schwellenwerte pro Maßnahme konfigurierbar.
- AK-PRD-AMP-002: „Grün“ wenn kum. RR < X mm, Wind < Y m/s (Böen), LF > Z %, ΔT innerhalb Grenzwert; Parameter pro Maßnahme.
- AK-PRD-AMP-003: Antwortzeit <1 s für Liste; <2 s für Details bei 4G.

## Risiken & Guardrails
Keine PSM‑Empfehlungen; klare Disclaimer. Datenquellen klar attribuieren (DWD). Offline: letzte Prognose markieren.

## Analytics/KPIs
„Grüne Fenster genutzt“/Woche; Klickrate „Task aus Ampel“; WAU Home‑Besuche.

## Abhängigkeiten
DWD‑Adapter, Felder/Geometrien, Task‑Modul, Telemetrie.

