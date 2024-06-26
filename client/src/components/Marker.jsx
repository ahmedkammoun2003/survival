import React, { useState, useEffect } from "react";
import { Marker, Popup, useMap } from "react-leaflet";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

const createCustomIcon = (iconUrl) => {
  return new L.Icon({
    iconUrl,
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
  });
};

const MarkerComponent = () => {
  const [markers, setMarkers] = useState([]);
  const [newMarker, setNewMarker] = useState(null);
  const map = useMap();

  useEffect(() => {
    fetchMarkers();
    const handleAddMarker = () => handleMarkerAdd();
    document.addEventListener('addMarker', handleAddMarker);
    return () => {
      document.removeEventListener('addMarker', handleAddMarker);
    };
  }, []);

  const fetchMarkers = async () => {
    try {
      const response = await fetch("http://localhost:5000/api/markers");
      if (!response.ok) {
        throw new Error("Failed to fetch markers");
      }
      const data = await response.json();
      setMarkers(data);
    } catch (error) {
      console.error("Error fetching markers:", error);
    }
  };

  const handleMarkerAdd = () => {
    const comment = prompt("Comment:");
    if (map) {
      const center = map.getCenter();
      setNewMarker({
        comments: comment,
        iconUrl: "", // Set your icon URL logic here
        latlng: center, // Set initial position to map center
      });
    }
  };

  const handleMarkerSubmit = async () => {
    try {
      if (!newMarker || !newMarker.comments) {
        throw new Error("Comments are required for the marker.");
      }
      const response = await fetch("http://localhost:5000/api/markers", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(newMarker),
      });
      if (!response.ok) {
        throw new Error("Failed to add marker");
      }
      const data = await response.json();
      setMarkers([...markers, data]);
      setNewMarker(null);
    } catch (error) {
      console.error("Error adding marker:", error);
    }
  };

  const handleCommentChange = (e) => {
    setNewMarker({
      ...newMarker,
      comments: e.target.value,
    });
  };

  const handleMarkerDrag = (latlng) => {
    // Update the position of the new marker being dragged
    setNewMarker({
      ...newMarker,
      latlng,
    });
  };

  return (
    <>
      {markers.map((marker) => (
        <Marker
          key={marker._id}
          position={[marker.latlng.coordinates[0], marker.latlng.coordinates[1]]}
          draggable={true}
          onDragEnd={(e) => handleMarkerDrag(e.target.getLatLng())}
          icon={createCustomIcon(marker.iconUrl || "http://localhost:5173/node_modules/leaflet/dist/images/marker-icon-2x.png")}
        >
          <Popup>
            <textarea style={{ width: "200px", minHeight: "100px" }} readOnly value={marker.comments} />
          </Popup>
        </Marker>
      ))}
      {newMarker && newMarker.latlng && (
        <Marker
          position={newMarker.latlng}
          draggable={true}
          onDragEnd={(e) => handleMarkerDrag(e.target.getLatLng())}
        >
          <Popup>
            <textarea
              placeholder="Enter comments..."
              style={{ width: "200px", minHeight: "100px" }}
              value={newMarker.comments}
              onChange={handleCommentChange}
            />
            <br />
            <button onClick={handleMarkerSubmit}>Submit</button>
          </Popup>
        </Marker>
      )}
    </>
  );
};

export default MarkerComponent;
