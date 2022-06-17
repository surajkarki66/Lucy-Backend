import "./ChatMessage.css";
import Logo from "../../../assets/images/logo.png";
// import { useRef } from "react";

type PropsType = { message: string };

const ChatMessage: React.FC<PropsType> = ({ message }) => {
  // const scroll = useRef();
  return (
    <div>
      <div className="msgs">
        <div>
          <div className="msg received">
            <img src={Logo} alt="" />
            <p>{message}</p>
          </div>
        </div>
      </div>
      <div>
        <form>
          <div className="sendMsg">
            <input
              className="input-message"
              placeholder="Ask anything to Lucy !"
              type="text"
            />
            <button className="btn-send" type="submit">
              Send
            </button>
          </div>
        </form>
      </div>
      {/* <div ref={scroll}></div> */}
    </div>
  );
};
export default ChatMessage;
