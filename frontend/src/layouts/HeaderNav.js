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

<Sidebar />
    <div style={styles.main}>
        <Navbar />
    </div>