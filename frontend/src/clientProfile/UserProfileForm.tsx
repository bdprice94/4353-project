import React, { useState } from "react";
<<<<<<< Updated upstream
import "./UserProfileForm.css";
=======
import styles from "./UserProfileForm.module.css";
import Navbar from "../Navbar/Navbar";
import axios, {AxiosError} from 'axios';
import {getCookie,backendurl} from "../utils"
>>>>>>> Stashed changes


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

const backendurl_users = `${backendurl}/users`;


export interface ProfileForm{
  full_name: { value: string },
  address_1: { value: string },
  address_2: { value: string },
  city: { value: string },
  state: { value: string },
  zipcode: { value: number },
}
export interface UserProfile {
  full_name: string,
  address_1: string,
  address_2: string,
  city: string,
  state: string,
  zipcode: number
}

const convertFormToModel = (form: UserProfile) => {
  return {
    full_name: form.full_name,
    address_1: form.address_1,
    address_2: form.address_2,
    city: form.city,
    state: form.state,
    zipcode: form.zipcode
      
     }
}


const UserProfileForm: React.FC = () => {
  const [fullName, setFullName] = useState( "");
  const [address1, setAddress1] = useState( "");
  const [address2, setAddress2] = useState( "");
  const [city, setCity] = useState( "");
  const [state, setState] = useState("");
  const [zipCode, setZipCode] = useState("");

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    const backendurl_profile = `${backendurl}/profile`;
 
  e.preventDefault();
  
  const target = e.target as typeof e.target & ProfileForm;
  
  const profile = {
    full_name: target.full_name?.value,
    address_1: target.address_1?.value,
    address_2: target.address_2?.value,
    city: target.city?.value,
    state: target.state?.value,
    zipcode: target.zipcode?.value
  };
  console.log(profile);
  const userprofile = convertFormToModel(profile);
  const username = getCookie("username"); 
  console.log(username);
  axios.post(`${backendurl_users}/user_profile/${username}`, userprofile, )
    .then(response => {
     alert(`LETS FREAKNG GO!!! ${username} your profile has just been created!`);
    })
    .catch((e: AxiosError) => {
      
      let errString = "Sorry, we don't know what happened. Please verify information is correct";
      if ('response' in e && e.response !== undefined) {
        if (e.response.status === 422) {
          const data = e.response.data as { detail: Array<string> };
          errString = data.detail
            .map((err: any) => err.msg)
            .join('\n');
        }
        else if (e.response.status === 404) {
          const data = e.response.data as { detail: string };
          errString = data.detail;
        }
        else {
          console.log(e.response.data);
        }
      }
      else {
        console.log(e);
      }
      alert(errString);
    });
  };

  return (
<<<<<<< Updated upstream
    <form className="user-profile-form" onSubmit={handleSubmit}>
=======
    <>
    
    <div className={styles.body}>
    <Navbar />

    <form className={styles.userprofileform} onSubmit={handleSubmit}>
>>>>>>> Stashed changes
      <div className="form-group">
        <label htmlFor="full_name">Full Name:</label>
        <input
          id="full_name"
          type="text"
          value={fullName}
          onChange={(e) => setFullName(e.target.value)}
          maxLength={50}
<<<<<<< Updated upstream
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="address1">Address 1:</label>
=======
          />
      </div>
      <div className={styles.formgroup}>
        <label htmlFor="address_1">Address 1:</label>
>>>>>>> Stashed changes
        <input
          id="address_1"
          type="text"
          value={address1}
          onChange={(e) => setAddress1(e.target.value)}
          maxLength={100}
<<<<<<< Updated upstream
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="address2">Address 2:</label>
=======
          />
      </div>
      <div className={styles.formgroup}>
        <label htmlFor="address_2">Address 2:</label>
>>>>>>> Stashed changes
        <input
          id="address_2"
          type="text"
          value={address2}
          onChange={(e) => setAddress2(e.target.value)}
          maxLength={100}
        />
      </div>
      <div className="form-group">
        <label htmlFor="city">City:</label>
        <input
          id="city"
          type="text"
          value={city}
          onChange={(e) => setCity(e.target.value)}
          maxLength={100}
<<<<<<< Updated upstream
          required
        />
=======
           />
>>>>>>> Stashed changes
      </div>
      <div className="form-group">
        <label htmlFor="state">State:</label>
        <select
          id="state"
          value={state}
          onChange={(e) => setState(e.target.value)}
          
        >
          <option value="">Select a state</option>
          {states.map((s) => (
            <option key={s.code} value={s.code}>
              {s.code}
            </option>
          ))}
        </select>
      </div>
<<<<<<< Updated upstream
      <div className="form-group">
        <label htmlFor="zipCode">Zipcode:</label>
=======
      <div className={styles.formgroup}>
        <label htmlFor="zipcode">Zipcode:</label>
>>>>>>> Stashed changes
        <input
          id="zipcode"
          type="text"
          value={zipCode}
          onChange={(e) => setZipCode(e.target.value)}
          minLength={5}
          maxLength={9}
<<<<<<< Updated upstream
          required
        />
=======
           />
>>>>>>> Stashed changes
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};

export default UserProfileForm;
