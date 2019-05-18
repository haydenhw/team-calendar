import React, { Component } from 'react';

import chargeMarkerImg from '../markers/charge-marker.png';

const styles = {
        popup: {
            position: "abosolute",
            width: "100px",
            height: "100px",
            backgroundColor: "lightgrey",
        }
    };

class Marker extends Component {

  render() {
    const { handleClick, popupActive, id } = this.props;
      return (
        <div key={id} onClick={handleClick}>
          {
            popupActive
                ? <div style={styles.popup}/>
                : <div/>
          }
          <img src={chargeMarkerImg}/>;
        </div>
    );
  }
}
 
export default Marker;