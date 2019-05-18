import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';
import locations from '../config/locations'; 

import UserMarker from '../components/UserMarker';
import DrainMarker  from '../components/DrainMarker';

const serverLocation = 'http://www.google.com';

const hackathonLocation = { lat: 37.8039001, lng: -122.272983 };
const testLocation = locations[0].coordinates;

class SimpleMap extends Component {
  static defaultProps = {
    center: hackathonLocation,
    zoom: 14, 
  };
 
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
          <UserMarker location={hackathonLocation}  />
          <DrainMarker location={testLocation}  />
        </GoogleMapReact>
      </div>
    );
  }
}
 
export default SimpleMap;