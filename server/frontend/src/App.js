import Dealers from './components/Dealers/Dealers';
import Dealer from "./components/Dealers/Dealer";
import PostReview from "./components/Dealers/PostReview";

import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register";

import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      
      {/* Authentication Routes */}
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<Register />} />

      {/* Dealers List */}
      <Route path="/dealers" element={<Dealers />} />

      {/* Dealer Details */}
      <Route path="/dealer/:id" element={<Dealer />} />

      {/* Post Review Page */}
      <Route path="/postreview/:id" element={<PostReview />} />

    </Routes>
  );
}

export default App;