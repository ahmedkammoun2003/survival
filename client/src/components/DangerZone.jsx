import { Polygon } from "react-leaflet";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

const DangerZoneComponent = ({ zones }) => {
  const dangerZones = zones.filter((zone) => zone.type === "danger");

  return (
    <>
      {dangerZones.map((zone) => (
        <Polygon
          key={zone._id}
          positions={zone.coordinates.map((coord) => [coord[1], coord[0]])}
          color="red"
        >
        </Polygon>
      ))}
    </>
  );
};

export default DangerZoneComponent;
