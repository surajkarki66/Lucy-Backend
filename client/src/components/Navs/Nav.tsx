import "./Nav.css";

const Nav: React.FC = () => {
  return (
    <div className="nav--container">
      <div className="home">HOME</div>
      <li className="navigation">
        <ul>About</ul>
        <ul>Contact</ul>
        <ul>Feedback</ul>
      </li>
    </div>
  );
};

export default Nav;
