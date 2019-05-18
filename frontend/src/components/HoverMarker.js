
import React, { Component } from 'react';
import shouldPureComponentUpdate from 'react-pure-render/function';


import {
  greatPlaceStyle,
  greatPlaceCircleStyle, greatPlaceCircleStyleHover,
  greatPlaceStickStyle, greatPlaceStickStyleHover, greatPlaceStickStyleShadow} from './HoverMarkerStyles';


import chargeMarkerImg from '../markers/charge-marker.png';
import {Visibility} from '@material-ui/icons'
const ChargeMarker = ({ text }) => <img src={chargeMarkerImg}></img>;

//   console.log( { greatPlaceStyle,
//   greatPlaceCircleStyle, greatPlaceCircleStyleHover,
//   greatPlaceStickStyle, greatPlaceStickStyleHover, greatPlaceStickStyleShadow});

export default class MyGreatPlaceWithStick extends Component {
  static defaultProps = {};

  shouldComponentUpdate = shouldPureComponentUpdate;

  render() {
    const {text, zIndex} = this.props;

    const style = {
      ...greatPlaceStyle,
      zIndex: this.props.$hover ? 1000 : zIndex
    };

    const styles = {
        popup: {
            width: "100px",
            height: "100px",
            backgroundColor: "lightgrey",
        }
    }

    const circleStyle = this.props.$hover ? greatPlaceCircleStyleHover : greatPlaceCircleStyle;
    const stickStyle = this.props.$hover ? greatPlaceStickStyleHover : greatPlaceStickStyle;
    // const isVisible = { visibility: "hidden" };
    // const isVisible = this.props.$hover ? { visibility: "visible" } : { visibility: "hidden" };
    const isVisible = false ? { visibility: "visible" } : { visibility: "hidden" };
    const popupStyle = { ...isVisible, ...styles.popup };

    console.log(this.props.$hover);

    return (
       <div style={style} onClick={console.log('hello')}>
          <div style={popupStyle}></div>
          <div>
              { <ChargeMarker /> }
          </div>
       </div>
    );
  }
}