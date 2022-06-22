import React from "react";

import "./AboutUs.css";
import About from "../../assets/images/about.png";

const AboutUs: React.FC = () => {
  return (
    <div className="section">
      <div className="container">
        <div className="title">
          <h1>About Us</h1>
        </div>
        <div className="content">
          <div className="article">
            <h3>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua.
              Iaculis urna id volutpat lacus laoreet non curabitur gravida. Dui
              nunc mattis enim ut tellus elementum sagittis vitae. Amet purus
              gravida quis blandit turpis cursus. Est placerat in egestas erat
              imperdiet. Eget lorem dolor sed viverra ipsum nunc. Ultricies
              tristique nulla aliquet enim tortor at auctor urna nunc.
            </h3>
            <p>
              Posuere ac ut consequat semper viverra nam libero justo laoreet.
              Dolor sed viverra ipsum nunc aliquet. Quis ipsum suspendisse
              ultrices gravida dictum fusce. Quam quisque id diam vel quam
              elementum. Nisi lacus sed viverra tellus in hac habitasse platea
              dictumst.
            </p>{" "}
            <div className="button">
              <a href="https://nec.edu.np/" target="_blank" rel="noreferrer">
                Know More
              </a>
            </div>
          </div>
        </div>
        <div className="image-section">
          <img src={About} alt="About Us" />
        </div>
      </div>
    </div>
  );
};

export default AboutUs;
