import React from 'react';
import { BrowserRouter as Router, Route } from "react-router-dom";

// views
import Main from "./views/Main";
import Signup from "./views/Signup";

// layout components
import Sidebar from "./components/Sidebar";
import Navbar from "./components/Navbar";

const styles = {
    appWrapper: {
        display: "flex",
    },
    main: {
        width: "100%",
    },
    view: {
        padding: "20px",
    }
};

const Test = () => (<h1>This is a test view</h1>)

const App = () => {
    return (
        <Router>
            <div style={styles.appWrapper}>
                <Sidebar />
                <div style={styles.main}>
                    <Navbar />
                    <div style={styles.view}>
                        <Route exact path="/" component={Main} />
                        <Route path="/signup" component={Signup} />
                        <Route path="/test" component={Test} />
                    </div>
                </div>
            </div>
        </Router>
    );
}

export default App;