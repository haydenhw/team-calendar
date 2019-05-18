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
    state = {
        open: false,
    };

    togglePopup = () => {
        const { open } = this.state;

        const logState = () => console.log(this.state);

        this.setState({ open: !open });
    };

  render() {
    const { id } = this.props;
      return (
        <div key={id} onClick={this.togglePopup}>
          {
              this.state.open
                ? <div style={styles.popup}/>
                : <div/>
          }
          <img src={chargeMarkerImg}/>;
        </div>
    );
  }
}
 
export default Marker;