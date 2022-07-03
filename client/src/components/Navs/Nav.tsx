import "./Nav.css";

import { Link } from "react-router-dom";

const Nav: React.FC = () => {
  return (
    <div className="nav--container">
      <Link to="/" style={{ textDecoration: "none", color: "white" }}>
        <div className="home">HOME </div>
      </Link>

      <li className="navigation">
        <Link to="/chat" style={{ textDecoration: "none", color: "white" }}>
          <ul> Chat</ul>
        </Link>
        <Link to="/aboutUs" style={{ textDecoration: "none", color: "white" }}>
          <ul> About</ul>
        </Link>
        <Link to="/feedback" style={{ textDecoration: "none", color: "white" }}>
          <ul> Feedback</ul>
        </Link>
      </li>
    </div>
  );
};

export default Nav;
