import React, { Component } from 'react';
import userMarkerImg from '../markers/user-marker.png';

const UserMarker = ({ text }) => <img src={userMarkerImg}></img>;

class Marker extends Component {
  
  render() {
    const { location } = this.props;

    return (
          <UserMarker
            lat={location.lat}
            lng={location.lng}
          />
    );
  }
}
 
export default Marker;