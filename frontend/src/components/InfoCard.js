import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';

const styles = {
  card: {
    minWidth: 275,
  },
  bullet: {
    display: 'inline-block',
    margin: '0 2px',
    transform: 'scale(0.8)',
  },
  title: {
    fontSize: 14,
  },
  pos: {
    marginBottom: 12,
  },
};

function InfoCard(props) {
    console.log(props.bar);
//   const { classes } = props;
//   const bull = <span className={classes.bullet}>•</span>;

  return (
    // <Card className={props.locationName}>
    <Card styles={styles.card}>
      <CardContent>
        {/* <Typography className={classes.title} color="textSecondary" gutterBottom>
          Word of the Day
        </Typography> */}
        <Typography className={props.locationName} variant="h5" component="h2">
          {/* be
          {bull}
          nev
          {bull}o{bull}
          lent */}
          {props.locationName}
        </Typography>
        <Typography color="textSecondary">
          $5
        </Typography>
        <Typography component="p">
          {/* well meaning and kindly.
          <br /> */}
          {"5 miles away"}
        </Typography>
      </CardContent>
      <CardActions>
        <Button style={{ background: '#449938' }} size="small">Accept</Button>
      </CardActions>
    </Card>
  );
}

// InfoCard.propTypes = {
//   classes: PropTypes.object.isRequired,
// };

function Parent(props){
    return withStyles(styles)(<InfoCard foo={props.foo}/>);
}

export default Parent;

//withStyles(styles)(InfoCard);

