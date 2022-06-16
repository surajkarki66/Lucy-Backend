import { Link } from "react-router-dom";

import "./Home.css";
import ai from "../../assets/videos/ai.mp4";

const Home: React.FC = () => {
  return (
    <section className="wrapper">
      <div className="video-wrap">
        <video src={ai} playsInline autoPlay muted loop></video>
      </div>
      <div className="overlay"></div>
      <div className="landing-text">
        <h1>Welcome Everyone</h1>
        <h3>
          If you want to know anything about Nepal Engineering College, Please
          chat with Lucy
        </h3>
        <Link to="/chat" style={{ textDecoration: "none" }}>
          <div className="btn">Start Here</div>
        </Link>
      </div>
    </section>
  );
};

export default Home;
