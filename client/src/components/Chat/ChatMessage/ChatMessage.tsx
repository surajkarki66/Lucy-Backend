import "./ChatMessage.css";
import Logo from "../../../assets/images/logo.png";

type PropsType = { message: string };

const ChatMessage: React.FC<PropsType> = ({ message }) => {
  return (
    <div className="chat--message-container">
      <div className="chat--sent--message">
        <p> {message}</p>
      </div>
      <span>
        <img className="chat--logo" src={Logo} alt="Lucy" />
      </span>
    </div>
  );
};
export default ChatMessage;
