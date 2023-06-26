import React from "react";
import { useNavigate } from "react-router-dom";
import "./UserProfileDisplay.css";



const UserProfileDisplay:React.FC = () =>  {
    const navigate = useNavigate();

  const handleEdit = () => {
    navigate("/edit");
  };

  return (
    <div className="user-profile-display">
      <h2>User Profile</h2>
      <p>Full Name: </p>
      <p>Address 1: </p>
      <p>Address 2: </p>
      <p>City: </p>
      <p>State: </p>
      <p>Zipcode: </p>
      <button onClick={handleEdit}>Edit</button>
    </div>
  );
};

export default UserProfileDisplay;
