import React, { Component } from 'react';
import ChargeMarkerImg from '../markers/charge-marker.png';

const ChargeMarker = ({ text }) => <img src={ChargeMarkerImg}></img>;

class Marker extends Component {
  render() {
    const { location } = this.props;
    console.log(location);
    return (
          <ChargeMarker 
            lat={location.lat}
            lng={location.lng}
          />
    );
  }
}
 
export default Marker;