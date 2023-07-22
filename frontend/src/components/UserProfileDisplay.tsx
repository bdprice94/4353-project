import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

import styles from "./UserProfileDisplay.module.css";
import Navbar from "./Navbar";
import { getCookie, backendurl } from "../authentication";
import { UserProfile } from "./UserProfileForm";

const UserProfileDisplay: React.FC = () => {
  const navigate = useNavigate();
  const backendurl_profile = `${backendurl}/profile`;

  const [userProfile, setUserProfile] = useState<UserProfile | null>(null);
  const handleEdit = () => {
    navigate("/user-profile-form");
  };
  const fetchUserProfile = async () => {
    const username = getCookie("username");
    try {
      const response = await axios.get(
        `${backendurl_profile}/${username}`,
      );
      setUserProfile(response.data);
    } catch (error) {
      console.error(error);
    }
  };
  useEffect(() => {
    fetchUserProfile();
  }, []);

  return (
    <>
      <Navbar />
      <div className={styles.userprofiledisplay}>
        <h2>User Profile</h2>
        <p>Full Name: {userProfile?.full_name}</p>
        <p>Address 1: {userProfile?.address_1}</p>
        <p>Address 2: {userProfile?.address_2}</p>
        <p>City: {userProfile?.city}</p>
        <p>State: {userProfile?.state}</p>
        <p>Zipcode: {userProfile?.zipcode}</p>
        <button onClick={handleEdit}>Edit</button>
      </div>
    </>
  );
};

export default UserProfileDisplay;
