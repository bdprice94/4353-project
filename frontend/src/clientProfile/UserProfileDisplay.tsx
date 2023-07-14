import React from "react";
import { useNavigate } from "react-router-dom";

import styles from "./UserProfileDisplay.module.css";
import Navbar from "../Navbar/Navbar";

const UserProfileDisplay:React.FC = () =>  {
    const navigate = useNavigate();

  const handleEdit = () => {
    navigate("/user-profile-form");
  };

  return (
    <>
    <Navbar/>
    <div className={styles.userprofiledisplay}>
      <h2>User Profile</h2>
      <p>Full Name: </p>
      <p>Address 1: </p>
      <p>Address 2: </p>
      <p>City: </p>
      <p>State: </p>
      <p>Zipcode: </p>
      <button onClick={handleEdit}>Edit</button>
    </div>
    </>
  );
};

export default UserProfileDisplay;
