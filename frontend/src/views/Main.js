import React, { Component } from 'react';
import axios from 'axios';
import GoogleMapReact from 'google-map-react';
import locations from '../config/locations';

import HoverMarker from '../components/HoverMarker';
import {K_CIRCLE_SIZE, K_STICK_SIZE} from '../components/HoverMarkerStyles';
import userMarkerImg from '../markers/user-marker.png';
import chargeMarkerImg from '../markers/charge-marker.png';
import InfoCard from '../components/InfoCard';

const ChargeMarker = ({ text }) => <img src={chargeMarkerImg}></img>;
const UserMarker = ({ text }) => <img src={userMarkerImg}></img>;


const hackathonLocation = { lat: 37.8039001, lng: -122.272983 };
const testLocation = locations[0].coordinates;
const testLocation2 = locations[1].coordinates;



class SimpleMap extends Component {
  static defaultProps = {
    center: hackathonLocation,
    zoom: 14,
  };

  componentDidMount () {
    const fetchData = async () => {
      const url = 'http://localhost:8080/rest/v1/sink';
      const { data } = await axios(url);
      console.log(data);
    }
    fetchData();
  }

  renderChargeMarkers () {
    var chargeMarkers = locations.map((location, i) => {

      return (
        <ChargeMarker key={i} lat={location.coordinates.lat} lng={location.coordinates.lng} />
      );
    });

    return chargeMarkers;
  }

  render () {
    return (
      // Important! Always set the container height explicitly
      <div style={{ height: '100vh', width: '100%' }}>
        <a href="http://www.google.com">Link to Today</a>
        <GoogleMapReact
          bootstrapURLKeys={{ key: 'AIzaSyAvPFEDTIhHF19n9qSU9XOLQoUOlwJrAbE' }}
          defaultCenter={this.props.center}
          defaultZoom={this.props.zoom}
          hoverDistance={100 / 2}

        >
          <InfoCard foo="bar"></InfoCard>
          {/* <UserMarker lat={hackathonLocation.lat} lng={hackathonLocation.lng} /> */}
          <HoverMarker lat={hackathonLocation.lat} lng={hackathonLocation.lng} />
          
          {/* {this.renderChargeMarkers()} */}
        </GoogleMapReact>
      </div>
    );
  }
}

export default SimpleMap;