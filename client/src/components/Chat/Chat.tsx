import "./Chat.css";
import Logo from "../../assets/images/logo.png";

import ChatMessage from "./ChatMessage/ChatMessage";

const Chat: React.FC = () => {
  return (
    <div className="Chat--container">
      <div className="side--panel">
        <div className="title">Nepal Engineering College (NEC)</div>
      </div>
      <div className="main--panel">
        <div className="chat--head">
          <img className="chat--logo" src={Logo} alt="Lucy" />
          <div className="chat--head--title">LUCY</div>
        </div>

        <ChatMessage message="Hello! This is Lucy, NEC chatbot" />
        <div className="chat--message">
          <div className="chat--message-box">
            <input type="text" placeholder="Write your Message" />
          </div>
          <div className="chat--message-enter">Send</div>
        </div>
      </div>
    </div>
  );
};

export default Chat;
