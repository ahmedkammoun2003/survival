import React, { useState, useEffect } from "react";
import { MapContainer, TileLayer } from "react-leaflet";
import ZonesComponent from "./Zone";
import DrawingControl from "./control/Draw";
import MarkerComponent from "./Marker";
import "leaflet/dist/leaflet.css";
import "leaflet-draw/dist/leaflet.draw.css";

const MapComponent = () => {
  const [mode, setMode] = useState("safe");

  return (
    <div style={{ minHeight: "500px", minWidth: "500px", position: "relative" }}>
      <MapContainer
        center={[51.505, -0.09]}
        zoom={13}
        style={{ minHeight: "500px", minWidth: "500px", height: "100%", width: "100%" }}
      >
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        <MarkerComponent />
        <ZonesComponent mode={mode} setMode={setMode} />
      </MapContainer>
      <div>
        <button onClick={() => document.dispatchEvent(new Event('addMarker'))}>Add Marker</button>
        <button onClick={() => setMode("safe")}>Add Safe Zone</button>
        <button onClick={() => setMode("danger")}>Add Danger Zone</button>
      </div>
    </div>
  );
};

export default MapComponent;
