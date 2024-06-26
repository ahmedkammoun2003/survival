import { Polygon } from "react-leaflet";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

const SafeZoneComponent = ({ zones }) => {
  const safeZones = zones.filter((zone) => zone.type === "safe");

  return (
    <>
      {safeZones.map((zone) => (
        <Polygon
          key={zone._id}
          positions={zone.coordinates.map((coord) => [coord[0], coord[1]])}
          color="green"
        >
        </Polygon>
      ))}
    </>
  );
};

export default SafeZoneComponent;
