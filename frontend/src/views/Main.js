import React, { Component } from 'react';
import axios from 'axios';
import GoogleMapReact from 'google-map-react';
import locations from '../config/locations';


import ChargeMarker from '../components/ChargeMarker';
import userMarkerImg from '../markers/user-marker.png';
import chargeMarkerImg from '../markers/charge-marker.png';

const styles = {
  popup: {
    position: "abosolute",
    width: "100px",
    height: "100px",
    backgroundColor: "lightgrey",
  }
}

// const ChargeMarker = ({ popupActive, handleClick }) => (
//   <div onClick={handleClick}>
//     {
//      popupActive
//       ? <div style={styles.popup}/>
//       : <div/>
//     }
//     <img src={chargeMarkerImg}/>;
//   </div>
// );

const UserMarker = ({ text }) => <img src={userMarkerImg}></img>;


const hackathonLocation = { lat: 37.8039001, lng: -122.272983 };

class SimpleMap extends Component {
  state = {
    open: false,
  }

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
    // fetchData();
  }

  renderChargeMarkers () {
    var chargeMarkers = locations.map((location, i) => {

      return (
        <ChargeMarker
          key={location.coordinates.lat}
          handleClick={this.togglePopup}
          popupActive={this.state.open}
          lat={location.coordinates.lat}
          lng={location.coordinates.lng}
        />
      );
  });

    return chargeMarkers;
  }

togglePopup = () => {
  const { open } = this.state;

  const logState = () => console.log(this.state);

  this.setState({ open: !open }, logState);
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
        hoverDistance={100 / 2}

      >
        {/* <UserMarker lat={hackathonLocation.lat} lng={hackathonLocation.lng} /> */}
        {/* <HoverMarker lat={hackathonLocation.lat} lng={hackathonLocation.lng} /> */}
        {this.renderChargeMarkers()}
      </GoogleMapReact>
    </div>
  );
}
}

export default SimpleMap;