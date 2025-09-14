# Feature‑Katalog (mit Tags)

Hinweis zu Tags: siehe `docs/LEGEND.md`.

## Home („Heute auf dem Hof“)
- Tagescockpit mit Maßnahmen‑Fenstern (Spritzen/Düngen/Ernte/Mähen) inkl. Ampel und Begründung (Wind, ΔT, Blattnässe, Bodenbefahrbarkeit). [MVP][DIFF]
- „Was hat sich seit gestern geändert?“ – differenzierte Abweichungen pro Schlag (Wetter, NDVI, Sensoren, Maschinenstatus). [PRO][DIFF]
- 1‑Minuten‑Zusammenfassung als Text, Audio & WhatsApp‑Share. [MVP]
- Schnellaktionen (⌘K / Voice): „Task anlegen“, „Beleg scannen“, „Export erstellen“. [MVP][DIFF]

## Karte, Schläge & Geodaten
- Schlagverwaltung: Zeichnen, Import (GeoJSON, Shape, KML), ETRS89/UTM 32/33 sauber, PostGIS‑Genauigkeit, Vorgewende, Pufferzonen. [MVP]
- Layer‑Suite: OSM/Orthofoto, NDVI/NDRE/EVI/LAI, Sentinel‑1 (SAR) Bodenfeuchte, Hangneigung/Exposition, Topographic Wetness Index, Bodenkarten (BGR), Schutzgebiete. [MVP→PRO]
- Zonierung & Managementzonen aus Zeitreihen + Boden → speichern/teilen. [PRO]
- AB‑Linien/Spurverwaltung (Import/Export, Autosteering‑kompatibel). [PRO]
- Offline‑Karten (PWA) mit gerasterten Vektor‑Tiles & lokaler Kachel‑Cache. [MVP]
- Time‑Slider (Phänologie/Vegetation) + Change‑Detection Heatmap. [PRO][DIFF]

## Wetter & Mikroklima
- DWD + Nowcast (Niederschlag, Wind in Böen, ΔT, Blattnässe, Luftfeuchte, Strahlung). [MVP]
- Feldspezifische Mikromodelle (Relief/Leeseite/Bewuchs) zur Arbeitsfenster‑Prognose. [PRO][DIFF]
- Spezialwarnungen: Frost, Inversionslage (Abdrift), Hagel, Sturm, Hitze‑Stress, Spritzfenster‑Alarm. [MVP→PRO]
- Befahrbarkeits‑Score (Niederschlags‑Historie + Bodenart + Hang + SAR‑Feuchte). [PRO][DIFF]

## Planung, Aufgaben & Workflows
- Task‑Vorlagen (Säen, Pflanzenschutz, Düngen, Mähen, Ernten, Kalken, Walzen) inkl. Abhängigkeiten (Wetter, Boden, Wartezeiten). [MVP]
- Routen-/Reihenfolge‑Optimierung für Schläge (Wegzeiten, Hang, Bodenzustand). [PRO]
- Freigabe an Lohnunternehmer mit geofenced Arbeitsfenster & Checklisten. [PRO]
- Wiederkehrende Aufgaben (Weidezaun‑Kontrolle, Stallklima‑Check). [MVP]
- Bulk‑Planung (mehrere Schläge, ein Vorgang, differenzierte Mengen). [MVP]

## Schlagkartei & Dokumentation
- Minimal‑Erfassung: Datum, Maßnahme, Produkt/Mittel, Menge/ha, Gesamtmenge, Wetter, Notizen, Fotos. [MVP]
- Pflanzenschutz‑Journal mit Wartezeiten‑Kontrolle, Pufferzonen, Abstandsauflagen, Wasser-/Naturschutz. [DE][PRO]
- Dünger‑Dokumentation: Mineraldünger, Gülle, Gärrest, Mist, Kalk (Nährstoffgehalte, Transport). [MVP→PRO]
- PDF‑Exporte (Schlag/Jahr/Betrieb), digitale Signatur/Hash (Revisionssicherheit). [MVP→PRO]
- „Evidence Pack“ (Fotos, Wetter, GPS, Zeiten) als Nachweis‑Bundle für Amt/Versicherung. [PRO][DIFF]

## Nährstoff‑ & Umweltmanagement
- Feld‑ und Betriebsbilanz N/P/K/S inkl. organischer Dünger, N‑Saldo. [PRO]
- Düngeverordnung (DüV)‑Checks: rote/gelbe Gebiete, Sperrfristen, Obergrenzen, Lagerkapazität. [DE][PRO]
- Stoffstrombilanz (Import/Export, Tierplätze, Futtermittel). [DE][ENTERPRISE]
- Applikationskarten (VRA) aus Zonen + Bodenproben + Zielertrag. [PRO]
- Erosion/Schlagrisiko (USLE‑ähnlich) + Maßnahmen‑Checklisten. [PRO]

## Remote Sensing & Analytics
- Cloud‑maskierte Sentinel‑2‑Pipeline (10 m), wöchentliche Komposite, Outlier‑Detektion. [MVP→PRO]
- NDVI/NDRE → Biomasse/Stickstoff‑Proxy mit Kalibrations‑Assistent (Bodenprobe/Ertrag). [PRO]
- Sentinel‑1 (C‑Band SAR) für Bodenfeuchte/Erntbarkeit bei Bewölkung. [PRO][DIFF]
- Ertragskarten‑Import (ISOXML/Shape) + Deckungsbeitrags‑Karten. [PRO]
- Anomalie‑Feed: „Schlag X: Einbruch in Nord‑Ost‑Zone“. [PRO]

## Maschinen, ISOBUS & Telematik
- ISO 11783/ISOXML Import/Export (Taskdata, Boundary, Guidance). [PRO]
- Agrirouter‑Connector (CLAAS, CNH, AGCO, JD via Connectoren) – Auftragserteilung, Log‑Rücklauf. [PRO][ENTERPRISE]
- Telemetrie‑Live (Position, Kraftstoff, Drehzahl), Geofencing & Diebstahlalarm. [PRO]
- Wartung & Ersatzteile: Intervalle, Checklisten, Öl/Filter‑Historie, Teilelager. [MVP→PRO]
- Maschinenkosten‑Monitor (€/h, €/ha, Kraftstoff/AdBlue, Abschreibung). [PRO]

## Ernte, Logistik & Wiegescheine
- Ernte‑Koordination (Mähdrescher ↔ Abfahrer) mit Funkstille‑Offline‑Fallback (Token/QR). [PRO][DIFF]
- Routenplanung (Feld ↔ Lager ↔ Trocknung) inkl. Straßen‑Sperren/Brückenlast. [PRO]
- Wiegeschein‑Erfassung (OCR), Feuchte‑/Mängelabzug, Los-/Silo‑Tracking. [MVP→PRO]
- Ballen‑Mapping (Zählung/GPS) & Abfuhrlisten. [PRO]

## Tierhaltung & Futter (optional)
- Herde/Kälber/Abferkelung: Ereignisse, Medikamente, Wartezeiten, Leistungsdaten. [PRO]
- Futterrationen & Silomanagement (Schichten, TS‑Verluste), Futterkosten/Tag. [PRO]
- Stallklima & Sensoren (Temp, NH₃, CO₂) mit Alerts & Ventilations‑Checklisten. [PRO]
- QS/ITW/Öko‑Dokumentation mit Export. [DE][ENTERPRISE]

## Spezialkulturen (Packs)
- Grünland/Heu/Silage: Schnittfenster (Wetter + Zuwachs), Narbenschutz, Weidemanagement. [MVP→PRO]
- Obst/Wein/Hopfen: GDD/Chill‑Hours, Krankheits‑Risiko‑Checklisten, Reife‑Tracking, Leseplanung. [PRO]
- Kartoffel/Rübe/Mais: Reihen‑Plan, Spezifika, Rodetermine, Lagerreporting. [PRO]

## Dokumente, OCR & e‑Akte
- Dokumenten‑Scanner (mobil, offline‑Queue), OCR mit Feld/Task‑Auto‑Zuordnung. [MVP]
- Rechnung → Kostenstelle/Schlag (Netto/Brutto, Skonto, USt‑Satz) via ML‑Extraktion. [PRO]
- Sicherheitsdatenblätter (SDB)‑Verwaltung, Gefahrstoff‑Symbole, PPE‑Checkliste. [PRO]
- Durchsuchbare e‑Akte (Volltext, Tags, Versionierung, Aufbewahrungsfristen). [PRO]

## Compliance, Förderungen & Behörden
- GAP‑Antrag (eAntrag)‑Vorbereitung: Flächen, Nutzungen, Öko‑Regeln, Konflikterkennung (Natura 2000, Gewässerabstände). [DE][PRO][DIFF]
- Pflanzenschutzrecht: Mittelverzeichnis‑Abgleich, Wartezeit/BBCH‑Checks, Abstandsauflagen, Drift‑Risiko. [DE][PRO]
- DüV/Stoffstrom: Regeln je Bundesland, rote Gebiete, Sperrfristen‑Kalender. [DE][PRO]
- Zertifizierungen: Bio (EU, Bioland, Demeter), GlobalG.A.P., QS – Audit‑Checklisten & Export. [DE][PRO]
- Arbeits-/Betriebssicherheit: Unterweisung, Gefährdungsbeurteilung, Unfall‑Dokumentation. [PRO]

## Finanzen, Einkauf & Märkte
- Kosten je Schlag/Maßnahme (Input, Diesel, Arbeitszeit, Lohnarbeit). [MVP→PRO]
- Deckungsbeiträge & Break‑even mit Sensitivität (Ertrag/Preis/Kosten). [PRO]
- DATEV‑Export, Umsatz-/Einkaufsreports, Kassenbuch light. [DE][PRO]
- Input‑Preisvergleich (Saat, Dünger, PSM) + Sammelbestellungen/Gruppenkäufe. [PRO][DIFF]
- Vermarktung: Silos/Chargen, Kontrakte, Liefertermine, Euronext/MATIF‑Ticker & Basis‑Preisalarme. [PRO]
- Risiko‑Management: Hail/Frost‑Schadendossier, Index‑Wetter‑Trigger (Belegdokumentation). [PRO]

## Sensoren, IoT & Wetterstationen
- LoRaWAN/Modbus/MQTT‑Connector, The Things Network‑Integration. [PRO]
- Bodenfeuchte-/Tensiometer, Sonden‑Kalibration, Bewässerungs‑Checklisten. [PRO]
- Wetterstation (Davis, Pessl/Metos, Sencrop): Auto‑Ingestion + Qualitätsprüfung. [PRO]
- Silo-/Getreidelager‑Sensorik (Temp/Feuchte), Schimmel‑Alarm. [PRO]

## KI‑Copilot & Automatisierung
- „Ask my Farm“ – natürlichsprachige Abfragen über Hofdaten. [PRO][DIFF]
- Woche planen: Copilot erstellt Tasks + Reihenfolge + Ressourcen inkl. Compliance‑Checks. [PRO][DIFF]
- Agenten/Flows: „Wenn Fenster grün & Maschine verfügbar → Auftrag an Lohnunternehmer“ (mit Bestätigung). [PRO][DIFF]
- OCR‑Autoposting: neuer Wiegeschein → Los/Silo aktualisieren + DB/Kosten. [PRO]
- On‑Device‑Modelle (Edge) für Bildklassifikation ohne Cloud. [LABS][DIFF]
- Guardrails: klare Grenzen (keine Wirkstoff-/Mittel‑Empfehlungen), Quellen/Unsicherheiten transparent. [MVP]

## Team, Zusammenarbeit & Kommunikation
- Rollen & Rechte (Eigentümer, Mitarbeiter, Berater, Lohnunternehmer) mit Row‑Level‑Security. [MVP]
- Freigaben per Link (zeitlich begrenzt), Kommentarthreads auf Schlag/Task/Beleg. [MVP→PRO]
- In‑App‑Chat & Sprachnachrichten, Transkription + Auto‑Zusammenfassung. [PRO]
- Zeiterfassung & Schichteinteilung, Akkord/Zeit‑Reports. [PRO]
- Kalender‑Sync (Google/Microsoft/Apple) für Feldtermine & Sperrfristen. [PRO]

## Sicherheit, Arbeitsschutz & Compliance vor Ort
- Gefahrenzonen‑Geofences (Gruben, Stromleitungen, Steillagen) + Warnungen. [PRO]
- PPE‑Checklisten pro Maßnahme, SDB‑Zugriff offline, Erste‑Hilfe‑Karten. [MVP→PRO]
- Notfall‑„Buddy“‑Modus: Allein‑arbeiten → Inaktivitäts‑Alarm/Standort‑Ping. [PRO][DIFF]

## Mobile‑Erlebnis (PWA → Native Wrapper)
- Offline‑First: Daten/Medien‑Queue, Konfliktlösung, Airplane‑Test bestanden. [MVP]
- Kamera‑Tools: Beleg‑Scan, Fotopins, AR‑Messband (Längen/Flächen), Pflanzen‑Makro‑Guide. [MVP→PRO]
- Glove‑Mode (große Touch‑Ziele), Sonnenlicht‑Kontrast, Sprach‑zu‑Task. [MVP]
- Hintergrund‑Sync (Capacitor/React Native), GPS‑Trails für Arbeiten. [PRO]

## Nachhaltigkeit, Klima & Zertifikate
- CO₂/CH₄/N₂O‑Inventar (IPCC‑nahe), Humus‑Monitoring (Bodenprobentrends). [PRO]
- Öko‑Regelungen (GAP 2023+) Assistent: Zwischenfrucht, Untersaat, Stilllegung – Fristen & Nachweise. [DE][PRO]
- Biodiversitäts‑Indikatoren (Blühstreifen, Hecken), Pufferzonen‑Heatmap. [PRO]
- Traceability/Chargen bis Kunden/Lieferant (QR‑Codes, Rückrufe). [ENTERPRISE]

## Marktplatz & Community (Optional)
- Einkauf: Kataloge, Verfügbarkeit, Gruppenrabatte, Hof‑zu‑Hof‑Tausch (Stroh, Mist, Gärrest). [PRO]
- Dienstleistungs‑Börse (Lohnarbeiten, Druschfenster, Transport). [PRO]
- Community‑Karten (opt‑in, anonymisiert) für Krankheits-/Schädlingsdruck‑Signale. [LABS][DIFF]

## Integrationen & Standards (Übersicht)
- Agrirouter, John Deere, CLAAS, CNH, AGCO (wo API verfügbar). [PRO][ENTERPRISE]
- DATEV, ETL/CSV für Buchhaltung/WaWi. [DE][PRO]
- ADAPT (AgGateway) Datenmodell, ISOXML, GeoTIFF/COG/MBTiles, WMS/WFS. [PRO]
- Webhook-/REST‑API, Zapier/n8n‑Flows, MQTT. [PRO][DIFF]

## Suche, Filter & Command Palette
- Global‑Suche (Schläge, Tasks, Dokumente, Maschinen, Kontakte) mit Operatoren. [MVP]
- Command Palette (⌘K) inkl. Voice – „Lege für Schlag Acker 3 morgen 150 kg/ha KAS an“. [PRO][DIFF]
- Smart‑Filter: „Schläge mit Hang>8 %, Sandboden, Niederschlag>20 mm in 48 h“. [PRO]

## Datenqualität, Governance & Datenschutz
- EU‑Hosting, AVV, Rollen/RLS, Audit‑Log (immutabel), Backups (PITR). [MVP]
- Datenportabilität (GeoJSON/CSV/PDF/ISOXML) – Export jederzeit, kein Datenverkauf. [MVP][DIFF]
- Fehlerdetektion (z. B. unrealistische Mengen/ha), Einheiten‑/CRS‑Wächter. [MVP→PRO]
- Freigabe‑Protokolle (wer sah was, wann), Attributions-/Quellen‑Transparenz. [PRO]

## Performance, Zuverlässigkeit & Offline‑Robustheit
- Kachel‑Preloading für anstehende Schläge, COG‑Streaming (Raster). [MVP→PRO]
- Graceful Degradation (schlanke Liste statt Karte offline), Retry-/Sync‑Strategie. [MVP]
- SLA‑Monitoring, Sentry/Telemetry, Edge‑Caching. [PRO]

## Onboarding, Hilfe & Training
- 5‑Min‑Setup: 10 Schläge importieren/zeichnen, erste Aufgabe, erster Export. [MVP]
- Interaktive Touren, kontextsensitive Hilfe, Mikro‑Videos offline. [MVP→PRO]
- Berater‑Modus: Read‑only‑Zugang mit Kommentaren/Checklisten. [PRO]

## Internationalisierung & Mehrbetriebs‑Fähigkeit
- Mehrsprachigkeit (DE/EN…), Einheiten (metrisch/imperial). [MVP]
- Mehr‑Betriebs‑Mandanten (Hofgruppen, Betriebszweige getrennt). [ENTERPRISE]
- Regionale Regelmodule (EU‑CAP, CH, AT, FR, UK, US – modular ladbar). [ENTERPRISE]

## Qualität‑des‑Lebens (QoL)
- Dunkel-/Kontrastmodus, große Schrift, Traktor‑Vibrations‑Toleranz (Tap‑Debounce). [MVP]
- „Letzte Aktion wiederholen“ (Batch‑Erfassung bei Feld‑Tour). [MVP]
- Schnapp‑Memos (2‑Sek‑Audio → Text → Task). [PRO]
- QR‑Codes an Tanks/Silos/Feld‑Einfahrten → Schnellerfassungen. [PRO]

## Produkt‑Moat (explizit)
- Farm‑Graph (Wissensmodell) für präzise Antworten. [DIFF]
- Window Engine (regel‑ & datengetrieben) – Herz zwischen Wetter, Boden, Compliance, Ressourcen. [DIFF]
- Edge‑KI + Offline: nutzbare Intelligenz ohne Netz, Datenschutz by design. [DIFF]
- Ökosystem‑/Plugin‑Store für regionale/branchenspezifische Erweiterungen. [DIFF]
- Radikale Exportierbarkeit + keine Datenmonetarisierung = Vertrauen & virale Weiterempfehlung. [DIFF]

## „Wir sind besser“ (Beispiele)
- Ein‑Blick‑Entscheidungen statt 5 Menüs (Fenster‑Ampel + Begründung + Klick zur Maßnahme). [DIFF]
- Behörden‑„Evidence Packs“ inkl. Signatur & Audit‑Trail. [DIFF]
- SAR‑gestützte Befahrbarkeit & Ernte‑Readiness bei Wolken. [DIFF]
- Command Palette + Voice → 2‑Sekunden‑Erfassung während der Fahrt. [DIFF]
- Lohnunternehmer‑Freigaben mit geofenced Arbeitsfenstern & Rücklaufdaten. [DIFF]

