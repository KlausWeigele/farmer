# ADR-0002 — Auth (Keycloak vs. SaaS)

Status: accepted
Datum: 2025-09-14

## Kontext
Mehrmandanten‑Setup mit Rollen/RLS, EU‑Hosting, DSGVO/AVV, Offline‑taugliche Tokenflüsse. Schnelle Pilotfähigkeit ohne Vendor‑Lock‑in.

## Optionen
- A) Keycloak (self‑host, EU) — volle Kontrolle, OIDC/OAuth 2.1, RBAC, Gruppen/Mandanten, Audit.
- B) SaaS (Clerk/Auth0) — schneller Start, aber Datenhaltung/Preis/Lock‑in‑Risiko.

## Entscheidung
A) Keycloak self‑hosted für MVP/Piloten. Spätere SaaS‑Integration optional pro Kunde.

## Konsequenzen
- Pro: Datenhoheit, flexible Policies, AVV einfach. Contra: eigener Betrieb/Updates.

