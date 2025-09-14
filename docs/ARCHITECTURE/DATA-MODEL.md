# Datenmodell (Skizze)

Entitäten (erste Iteration):
- farm, user, membership (Rollen)
- field (geom, fläche, bodeninfos)
- crop_cycle (kultur, jahr, sorte)
- task (typ, status, field_id, fenster)
- operation (durchgeführt, mengen/ha, gesamtmenge, wetter)
- weather_observation (field_id, t/wind/rr)
- ndvi_snapshot (field_id, datum, wert/verteilung)
- document (ocr_json, verknüpfung)
- notification, audit_event

Hinweise:
- CRS: Standard ETRS89/UTM32/33
- RLS: Row‑Level‑Security pro `farm_id`
- Medien: Objekt‑Storage (S3) mit signierten URLs; Metadaten in `document`

