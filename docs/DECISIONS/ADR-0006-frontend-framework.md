# ADR-0006 — Frontend-Framework (Next.js vs. Alternativen)

Status: accepted
Datum: 2025-09-14

## Kontext
Frontend-Stack für Web/PWA muss offline-first können, starkes Ökosystem (Karten/MapLibre, PWA, i18n), schnelle Iteration, und Vercel-Deployment unterstützen. Vorgabe des Product Owners: Kein Svelte/SvelteKit; bevorzugt React/Next.js.

## Optionen
- A) Next.js (App Router, React 18)
- B) SvelteKit (ausdrücklich ausgeschlossen)
- C) Remix / reine React SPA

## Entscheidung
A) Next.js als verbindliches Frontend-Framework. Svelte/SvelteKit wird nicht verwendet.

## Konsequenzen
- Pro: Reifes Ökosystem, starke PWA-/SSR-/ISR-Fähigkeiten, gute DX, nahtlose Vercel-Integration, breite Library-Unterstützung (MapLibre, TanStack, i18n).
- Contra: React-Komplexität (Server/Client Components), Build-Größe; aber akzeptabel für Ziel.

