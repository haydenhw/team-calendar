import React, { Component } from 'react';
import axios from 'axios';
import GoogleMapReact from 'google-map-react';
import locations from '../config/locations';
import userMarkerImg from '../markers/user-marker.png';


import ChargeMarker from '../components/ChargeMarker';

const styles = {
  popup: {
    position: "abosolute",
    width: "100px",
    height: "100px",
    backgroundColor: "lightgrey",
  }
}

const UserMarker = ({ text }) => <img src={userMarkerImg}></img>;


const hackathonLocation = { lat: 37.8039001, lng: -122.272983 };

class SimpleMap extends Component {

  static defaultProps = {
    center: hackathonLocation,
    zoom: 16,
  };

  state = {
    locations: [],
  };

  async componentDidMount () {
    const fetchData = async () => {
      const url = 'http://localhost:8080/rest/v1/sink';
      const { data } = await axios(url);
      return data;
    };

    const locations = await fetchData();
    this.setState({locations});
  }

  renderChargeMarkers () {
    const { locations } = this.state;
    console.log(locations);

    if (!locations.length) {
      return null;
    }

    var chargeMarkers = locations.map((location, i) => {
      return (
        <ChargeMarker
          key={location.coordinates.lat}
          lat={location.coordinates.lat}
          lng={location.coordinates.lng}
        />
      );
  });

    return chargeMarkers;
  }


render() {
  return (
    <div style={{ height: '100vh', width: '100%' }}>
      <a href="http://www.google.com">Link to Today</a>
      <GoogleMapReact
        bootstrapURLKeys={{ key: 'AIzaSyAvPFEDTIhHF19n9qSU9XOLQoUOlwJrAbE' }}
        defaultCenter={this.props.center}
        defaultZoom={this.props.zoom}
        hoverDistance={100 / 2}

      >
         <UserMarker lat={hackathonLocation.lat} lng={hackathonLocation.lng} />
        {this.renderChargeMarkers()}
      </GoogleMapReact>
    </div>
  );
}
}

export default SimpleMap;