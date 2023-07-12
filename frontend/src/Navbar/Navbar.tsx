import React from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";






const Navbar: React.FunctionComponent = () => {
  
  return (
   
    <nav className="navbar">
      <div className="navbar__logo">
        <Link to="/">
          <h1>Team 8</h1>
        </Link>
      </div>
      <ul className="navbar__links">
        <li>
          <Link to="/fuel-quote-form">
            
            Fuel Quote
          </Link>
        </li>
        <li>
          <Link to="/fuel-quote-history">
            
            History
          </Link>
        </li>
        <li>
          <Link to="/user-profile-display">
            
            Profile
          </Link>
        </li>
        <li>
          <Link to="/">
            
            Sign out
          </Link>
        </li>
      </ul>
    </nav>
  );
};

// Export the Navbar component as a default export
export  default Navbar;
