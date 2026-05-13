import { CircleMarker, Popup } from "react-leaflet";
import { useEffect, useState } from "react";
import { getEarthquakes } from "../services/api";
import Map from "../components/Map";

interface Earthquake {
    id: number;
    latitude: number;
    longitude: number;
    magnitude: number;
    depth: number;
    isTsunami: boolean;
    year: number;
    month: number;
}

const getMonthName = (month: number): string => {
  const months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
  ];
  return months[month - 1];
};

function EarthquakeMap() {
    const [earthquakes, setEarthquakes] = useState<Earthquake[]>([]);

    useEffect(() => {
        getEarthquakes().then((data) => {
            setEarthquakes(data);
        });
    }, []);

  return (
    <Map>
      {earthquakes.map((eq) => (
        <CircleMarker 
        key={eq.id} 
        center={[eq.latitude, eq.longitude]} 
        radius={eq.magnitude * 1} 
        fillOpacity={0.2} 
        color={eq.isTsunami ? "#f97316" : "#0d9488"}>
            <Popup>
                <strong>Magnitude:</strong> {eq.magnitude} <br />
                <strong>Depth:</strong> {eq.depth} km <br />    
                <strong>Date:</strong> {getMonthName(eq.month)} {eq.year} <br />
                <strong>Tsunami:</strong> {eq.isTsunami ? "Yes" : "No"}
            </Popup>
        </CircleMarker>
      ))}
    </Map>
  );}

export default EarthquakeMap;
