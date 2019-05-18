import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import List from '@material-ui/core/List';
import Divider from '@material-ui/core/Divider';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import HomeIcon from '@material-ui/icons/Home';
import BuildIcon from '@material-ui/icons/Build';

import { withRouter } from 'react-router-dom'

const drawerWidth = 240;

const styles = () => ({
    drawer: {
        width: drawerWidth,
    },
    drawerPaper: {
        width: drawerWidth,
    },
});

function PermanentDrawerLeft (props) {
    const { classes, history } = props;

    return (
        <div>
            <Drawer
                className={classes.drawer}
                variant="permanent"
                classes={{
                    paper: classes.drawerPaper,
                }}
                anchor="left"
            >
                <div className={classes.toolbar} />
                <Divider />
                <List>
                    <ListItem button key={1} onClick={() => history.push('/')}>
                        <ListItemIcon>
                            <HomeIcon/>
                        </ListItemIcon>
                        <ListItemText primary="App" />
                    </ListItem>
                    <ListItem button key={2} onClick={() => history.push('/test')} >
                        <ListItemIcon>
                            <BuildIcon/>
                          </ListItemIcon>
                        <ListItemText primary="Test" />
                    </ListItem>
                </List>
                <Divider />
            </Drawer>
        </div>
    );
}

PermanentDrawerLeft.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withRouter(withStyles(styles)(PermanentDrawerLeft));
