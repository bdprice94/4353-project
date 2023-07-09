import React from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";


// Define the props type for the Navbar component
type NavbarProps = {
  // You can add any props you want here
};

// Define the Navbar component using a function expression
const Navbar: React.FC<NavbarProps> = (props) => {
  // You can use any state or effect hooks here
  return (
    // Use JSX syntax to render the navbar element
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
