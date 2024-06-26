import React, { useState, useEffect } from "react";
import SafeZoneComponent from "./SafeZone";
import DangerZoneComponent from "./DangerZone";
import DrawingControl from "./control/Draw";

const ZonesComponent = ({ mode, setMode }) => {
  const [zones, setZones] = useState([]);

  useEffect(() => {
    fetchZones();
  }, []);

  const fetchZones = async () => {
    try {
      const response = await fetch("http://localhost:5000/api/polygons");
      if (!response.ok) {
        throw new Error("Failed to fetch zones");
      }
      const data = await response.json();
      setZones(data);
    } catch (error) {
      console.error("Error fetching zones:", error);
    }
  };

  const addZone = async (newZone) => {
    try {
      const response = await fetch("http://localhost:5000/api/polygons", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(newZone),
      });
      if (!response.ok) {
        throw new Error("Failed to add zone");
      }
      const data = await response.json();
      setZones([...zones, data]);
    } catch (error) {
      console.error("Error adding zone:", error);
    }
  };

  const handleZoneCreated = (e) => {
    console.log(e.editing.latlngs[0]);
    const  layer  = e.editing.latlngs[0];
    const newZone = {
      type: mode,
      coordinates: layer[0].map((latlng) => [latlng.lat, latlng.lng]),
    };

    addZone(newZone);
  };

  return (
    <>
      <SafeZoneComponent zones={zones} />
      <DangerZoneComponent zones={zones} />
      <DrawingControl onCreated={handleZoneCreated} />
    </>
  );
};

export default ZonesComponent;
