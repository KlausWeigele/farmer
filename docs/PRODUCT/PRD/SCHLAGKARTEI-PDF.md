---
id: PRD-SCHLAGKARTEI-001
status: draft
owners: product, eng
tags: [MVP, DE]
---

# PRD — Schlagkartei + PDF

## Ziel & Problem
Minimaler, schneller Nachweisfluss mit sauberem PDF‑Export je Schlag/Jahr, revisionssicher.

## Personas
Betriebsleiter, Berater. Desktop und mobil.

## Scope
In: Erfassung (Datum, Maßnahme, Produkt, Menge/ha, Gesamtmenge, Wetter, Notizen, Fotos); Filter; PDF je Schlag/Jahr.
Out: Vollständige DüV/Stoffstrom‑Abbildungen (separate Features).

## Flows
Schlag → „Neue Maßnahme“ → Formular (validiert) → Speichern → Export → PDF (Hash im Footer).

## AK
- AK-SCH-001: PDF „Jahresübersicht pro Schlag“ <10 s generiert.
- AK-SCH-002: Validierungen (Einheiten, realistische Mengen/ha) schlagen an.
- AK-SCH-003: Offline Eingaben möglich; Sync <30 s nach Netz.

## Risiken/Guardrails
Haftungs‑Disclaimer, Datenintegrität (Audit‑Trail), DSGVO (Fotos/PersDaten).

## KPIs
Anzahl Exporte/Monat, Fehlerquote Validierungen <2 %.

