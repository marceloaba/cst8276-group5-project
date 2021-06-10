import React from "react";

import { MapContainer, Marker, TileLayer, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import L from "leaflet";

delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  iconRetinaUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.3.1/images/marker-icon.png",
  iconUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.3.1/images/marker-icon.png",
  shadowUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.3.1/images/marker-shadow.png",
});

const marker = { lat: 45.34610952669544, lng: -75.74572456050461 }; //These will come from the API get request

const interactionOptions = {
  zoomControl: true,
  doubleClickZoom: true,
  closePopupOnClick: false,
  dragging: true,
  zoomSnap: true,
  zoomDelta: true,
  trackResize: true,
  touchZoom: true,
  scrollWheelZoom: false,
};

const StaticMap = () => {
  return (
        <div className="map">
          <h2></h2>
            <MapContainer
              center={marker}
              zoom={13}
              className="static-map"
              {...interactionOptions}
            >
              <TileLayer
                attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              />
              <Marker position={[marker.lat, marker.lng]}>
                <Popup>
                  Apo's Place
                </Popup>
              </Marker>
            </MapContainer>
        </div>
  );
};

export default StaticMap;