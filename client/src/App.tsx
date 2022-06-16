import { Route, Routes } from "react-router-dom";

import Nav from "./components/Navs/Nav";
import Home from "./pages/Home/Home";
import ChatPage from "./pages/ChatPage";

const App: React.FC = () => {
  const routes = (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/chat" element={<ChatPage />} />
    </Routes>
  );
  return (
    <div>
      <Nav />
      {routes}
    </div>
  );
};

export default App;
