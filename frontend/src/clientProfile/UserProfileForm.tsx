import React, { useState } from "react";

import styles from "./UserProfileForm.module.css";
import Navbar from "../Navbar/Navbar";

const states = [
    { code: "AL" },
    { code: "AK" },
    { code: "AZ" },
    { code: "AR" },
    { code: "CA" },
    { code: "CO" },
    { code: "CT" },
    { code: "DE" },
    { code: "FL" },
    { code: "GA" },
    { code: "HI" },
    { code: "ID" },
    { code: "IL" },
    { code: "IN" },
    { code: "IA" },
    { code: "KS" },
    { code: "KY" },
    { code: "LA" },
    { code: "ME" },
    { code: "MD" },
    { code: "MA" },
    { code: "MI" },
    { code: "MN" },
    { code: "MS" },
    { code: "MO" },
    { code: "MT" },
    { code: "NE" },
    { code: "NV" },
    { code: "NH" },
    { code: "NJ" },
    { code: "NM" },
    { code: "NY" },
    { code: "NC" },
    { code: "ND" },
    { code: "OH" },
    { code: "OK" },
    { code: "OR" },
    { code: "PA" },
    { code: "RI" },
    { code: "SC" },
    { code: "SD" },
    { code: "TN" },
    { code: "TX" },
    { code: "UT" },
    { code: "VT" },
    { code: "VA" },
    { code: "WA" },
    { code: "WV" },
    { code: "WI" },
    { code: "WY" }
  
];

const UserProfileForm: React.FC = () => {
  const [fullName, setFullName] = useState( "");
  const [address1, setAddress1] = useState( "");
  const [address2, setAddress2] = useState( "");
  const [city, setCity] = useState( "");
  const [state, setState] = useState("");
  const [zipCode, setZipCode] = useState("");

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    
  //backend stuff here blah blah will add later slay
  };

  return (
    <>
    <div className={styles.body}>
    <Navbar />

    <form className={styles.userprofileform} onSubmit={handleSubmit}>
      <div className="form-group">
        <label htmlFor="fullName">Full Name:</label>
        <input
          id="fullName"
          type="text"
          value={fullName}
          onChange={(e) => setFullName(e.target.value)}
          maxLength={50}
          required />
      </div>
      <div className={styles.formgroup}>
        <label htmlFor="address1">Address 1:</label>
        <input
          id="address1"
          type="text"
          value={address1}
          onChange={(e) => setAddress1(e.target.value)}
          maxLength={100}
          required />
      </div>
      <div className={styles.formgroup}>
        <label htmlFor="address2">Address 2:</label>
        <input
          id="address2"
          type="text"
          value={address2}
          onChange={(e) => setAddress2(e.target.value)}
          maxLength={100} />
      </div>
      <div className={styles.formgroup}>
        <label htmlFor="city">City:</label>
        <input
          id="city"
          type="text"
          value={city}
          onChange={(e) => setCity(e.target.value)}
          maxLength={100}
          required />
      </div>
      <div className={styles.formgroup}>
        <label htmlFor="state">State:</label>
        <select
          id="state"
          value={state}
          onChange={(e) => setState(e.target.value)}
          required
        >
          <option value="">Select a state</option>
          {states.map((s) => (
            <option key={s.code} value={s.code}>
              {s.code}
            </option>
          ))}
        </select>
      </div>
      <div className={styles.formgroup}>
        <label htmlFor="zipCode">Zipcode:</label>
        <input
          id="zipCode"
          type="text"
          value={zipCode}
          onChange={(e) => setZipCode(e.target.value)}
          minLength={5}
          maxLength={9}
          required />
      </div>
      <button type="submit">Submit</button>
    </form>
    </div>
    </>
  );
};

export default UserProfileForm;
