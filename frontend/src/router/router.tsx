import LoginPage from "../components/LoginPage";
import UserProfileForm from "../components/UserProfileForm";
import UserProfileDisplay from "../components/UserProfileDisplay";
import FuelQuoteForm from "../components/FuelQuoteForm";
import FuelQuoteHistory from "../components/FuelQuoteHistory";
import { BrowserRouter, Route, Routes } from "react-router-dom";

const Routing = () => (
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<LoginPage />} />
      <Route path="/user-profile-form" element={<UserProfileForm />} />
      <Route path="/user-profile-display" element={<UserProfileDisplay />} />
      <Route path="/fuel-quote-form" element={<FuelQuoteForm />} />
      <Route path="/fuel-quote-history" element={<FuelQuoteHistory />} />
    </Routes>
  </BrowserRouter>
);

export default Routing;
