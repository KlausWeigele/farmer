# Epics & erste Stories (mit AK)

Quelle: Konsolidiert aus den gelieferten Plänen.

## EP1: Schläge & Karte
- Import GeoJSON; Zeichnen; Flächenberechnung; Snap‑to‑Boundary; CRS‑Tests (ETRS89/UTM32/33)
- AK:
  - AK-EP1-001-a: Nutzer importiert/zeichnet 10 Schläge in <5 min
  - AK-EP1-001-b: Flächenabweichung <0,5 %, EPSG korrekt erkannt

## EP2: Wetter‑Fenster
- DWD Pull; Metrik‑Normalisierung; Ampel‑Heuristik; UI‑Badge „Heute/48 h“
- AK:
  - AK-EP2-001-a: 48 h Ansicht mit Ampel; Schwellen konfigurierbar
  - AK-EP2-001-b: „Grün“ wenn kum. RR < X mm, Wind < Y m/s, LF > Z % (pro Maßnahme)

## EP3: Maßnahmen/Tasks
- CRUD + Vorlagen; Schlagauswahl in 2 Taps; Bulk‑Planung; Push
- AK:
  - AK-EP3-001-a: Task anlegen in ≤2 Taps nach Schlagwahl
  - AK-EP3-001-b: Push‑Reminder (Web‑Push) für fällige Tasks

## EP4: Schlagkartei/PDF
- Datenschema; Filter/Export; Branding; numerische Validierungen
- AK:
  - AK-EP4-001-a: PDF „Jahresübersicht pro Schlag“ <10 s generiert
  - AK-EP4-001-b: Hash/Signatur im Footer zur Revisionssicherheit

## EP5: NDVI
- Sentinel‑Fetcher; Cloud‑Mask; Resampling; Timeseries‑Chart; Kachelcache
- AK:
  - AK-EP5-001-a: NDVI‑Zeitreihe pro Schlag; Detail in <2 s bei 4G
  - AK-EP5-001-b: Wöchentliche Komposite automatisch aktualisiert

## EP6: Offline/PWA
- Service Worker; IndexedDB; Sync‑Queue; Konfliktlösung
- AK:
  - AK-EP6-001-a: Flugmodus‑Test: Task+Foto speicherbar
  - AK-EP6-001-b: Sync <30 s nach Netzrückkehr

## EP7: KI‑Copilot
- RAG auf Hofdaten; Prompt‑Safeguards; Antwort‑Vorlagen; Log‑Redaktion
- AK:
  - AK-EP7-001-a: „Fasse meine Woche zusammen“ liefert korrekte, zitierte Datenquellen
  - AK-EP7-001-b: Strikte Disclaimer und keine PSM‑Empfehlungen

