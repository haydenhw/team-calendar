import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';
import locations from '../config/locations'; 

// import UserMarker from '../components/UserMarker';
// import ChargeMarker  from '../components/ChargeMarker';

import userMarkerImg from '../markers/user-marker.png';
import chargeMarkerImg from '../markers/charge-marker.png';

const ChargeMarker = ({ text }) => <img src={chargeMarkerImg}></img>;
const UserMarker = ({ text }) => <img src={userMarkerImg}></img>;

const serverLocation = 'http://www.google.com';

const hackathonLocation = { lat: 37.8039001, lng: -122.272983 };
const testLocation = locations[0].coordinates;
const testLocation2 = locations[1].coordinates;

class SimpleMap extends Component {
  static defaultProps = {
    center: hackathonLocation,
    zoom: 14, 
  };

  renderChargeMarkers() {
    var chargeMarkers = locations.map((location, i) => {
      
      return (
          <ChargeMarker key={i} lat={location.coordinates.lat} lng={location.coordinates.lng} />
      );
    });

    return chargeMarkers;
  }
 
  render() {
    return (
      // Important! Always set the container height explicitly
      <div style={{ height: '100vh', width: '100%' }}>
        <a href="http://www.google.com">Link to Today</a>
        <GoogleMapReact
          bootstrapURLKeys={{ key: 'AIzaSyAvPFEDTIhHF19n9qSU9XOLQoUOlwJrAbE' }}
          defaultCenter={this.props.center}
          defaultZoom={this.props.zoom}
        >
          <UserMarker lat={hackathonLocation.lat} lng={hackathonLocation.lng} />
          { this.renderChargeMarkers() }
        </GoogleMapReact>
      </div>
    );
  }
}
 
export default SimpleMap;