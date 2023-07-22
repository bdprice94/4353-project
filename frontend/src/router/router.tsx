import { useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import LoginPage from "../components/LoginPage";
import UserProfileForm from "../components/UserProfileForm";
import UserProfileDisplay from "../components/UserProfileDisplay";
import FuelQuoteForm from "../components/FuelQuoteForm";
import FuelQuoteHistory from "../components/FuelQuoteHistory";
import { getCookie } from "../authentication";

const doesCookieExist = () => {
  const username = getCookie("username");
  return username !== undefined;
};

const Routing = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const shouldNavigateToLogin =
      !doesCookieExist() && window.location.pathname !== "/";
    if (shouldNavigateToLogin) {
      navigate("/");
    }
  }, [navigate]);

  return (
    <Routes>
      <Route path="/" element={<LoginPage />} />
      <Route path="/user-profile-form" element={<UserProfileForm />} />
      <Route path="/user-profile-display" element={<UserProfileDisplay />} />
      <Route path="/fuel-quote-form" element={<FuelQuoteForm />} />
      <Route path="/fuel-quote-history" element={<FuelQuoteHistory />} />
    </Routes>
  );
};

export default Routing;
