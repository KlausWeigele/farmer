"use client";
import { useEffect, useRef } from "react";
import maplibregl from "maplibre-gl";
import MapboxDraw from "@mapbox/mapbox-gl-draw";
import "maplibre-gl/dist/maplibre-gl.css";
import "@mapbox/mapbox-gl-draw/dist/mapbox-gl-draw.css";

export default function MapPage() {
  const mapRef = useRef<maplibregl.Map | null>(null);
  const containerRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    if (containerRef.current && !mapRef.current) {
      const map = new maplibregl.Map({
        container: containerRef.current,
        style: "https://demotiles.maplibre.org/style.json",
        center: [9.0, 51.2], // Mitte DE
        zoom: 5.2,
      });
      const draw = new MapboxDraw({ displayControlsDefault: false, controls: { polygon: true, trash: true } });
      map.addControl(new maplibregl.NavigationControl(), "top-right");
      // @ts-ignore
      map.addControl(draw, "top-left");

      // Beispiel: Ausgabe der Geometrie in die Konsole
      map.on("draw.create", () => {
        const fc = draw.getAll();
        // eslint-disable-next-line no-console
        console.log("Drawn GeoJSON:", JSON.stringify(fc));
      });

      mapRef.current = map;
    }
    return () => {
      mapRef.current?.remove();
      mapRef.current = null;
    };
  }, []);

  return (
    <main style={{ height: "100vh" }}>
      <div style={{ padding: 12 }}>
        <h2>Schläge zeichnen (EP1 Demo)</h2>
        <p>Nutze das Polygon‑Tool. Geometrien erscheinen in der Browser‑Konsole.</p>
      </div>
      <div ref={containerRef} style={{ height: "calc(100vh - 80px)" }} />
    </main>
  );
}

