import { useMap } from "react-leaflet";
import { useEffect } from "react";
import L from "leaflet";
import "leaflet-draw/dist/leaflet.draw.css";
import "leaflet-draw";

const DrawingControl = ({ onCreated }) => {
  const map = useMap();

  useEffect(() => {
    if (!map) return;
    const drawControl = new L.Control.Draw({
      draw: {
        polygon: true,
        rectangle: true,
        circle: true,
        marker: true,
        polyline: true,
        circlemarker: true,
      },
    });

    map.addControl(drawControl);

    map.on(L.Draw.Event.CREATED, (event) => {
      const layer = event.layer;
      drawnItems.addLayer(layer);
      onCreated(layer);
    });

    return () => {
      map.removeControl(drawControl);
    };
  }, [map, onCreated]);

  return null;
};

export default DrawingControl;

