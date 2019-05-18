import React, { Component } from 'react';
import drainMarkerImg from '../markers/charge-marker.png';

const DrainMarker = ({ text }) => <img src={drainMarkerImg}></img>;

class Marker extends Component {
  render() {
    const { location } = this.props;
    return (
          <DrainMarker 
            lat={location.lat}
            lng={location.lng}
          />
    );
  }
}
 
export default Marker;