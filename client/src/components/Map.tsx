import { MapContainer, TileLayer } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import type { ReactNode } from "react";
import styles from "./Map.module.css";
import Legend from "./Legend";

interface MapProps {
  children: ReactNode;
}

function Map({ children }: MapProps) {

  return (
    <div className={styles.mapWrapper}>
      <MapContainer center={[20, 0]} zoom={2} className={styles.map}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; OpenStreetMap contributors'
        />
        {children}
        <Legend position="bottomright" />
      </MapContainer>
    </div>

  );}

export default Map;
