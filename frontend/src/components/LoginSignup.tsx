import React from "react";
import axios, { AxiosError } from "axios";
import { backendurl } from "../authentication";
import styles from "./LoginPage.module.css";

const backendurl_users = `${backendurl}/users`;

export interface UserRegisterForm {
  username: { value: string };
  password: { value: string };
  password2: { value: string };
}

export interface UserRegister {
  username: string;
  password: string;
  password2: string;
}

const convertFormToModel = (form: UserRegisterForm) => {
  return {
    username: form.username.value,
    password: form.password.value,
    password2: form.password2.value,
  };
};

const registerFormSubmit: React.FormEventHandler<HTMLFormElement> = (
  e: React.SyntheticEvent,
) => {
  e.preventDefault();
  const target = e.target as typeof e.target & UserRegisterForm;
  const userRegisterForm = {
    username: { value: target.username.value },
    password: { value: target.password.value },
    password2: { value: target.password2.value },
  };
  const userRegister = convertFormToModel(userRegisterForm);
  axios
    .post(`${backendurl_users}/create_user`, userRegister)
    .then(() => {
      alert("Successfully created a user!");
    })
    .catch((e: AxiosError) => {
      let errString =
        "Sorry, we don't know what happened. Please verify information is correct";
      if ("response" in e && e.response !== undefined) {
        console.log(e.response.data);
        const data = e.response.data as { detail: string | Array<string> };
        if (Array.isArray(data.detail)) {
          errString = (data.detail as Array<string>)
            .map((err: any) => err.msg)
            .join("\n");
        } else if (e.response.status === 422 || e.response.status === 400) {
          errString = data.detail as string;
        } else {
          console.log(data);
        }
      } else {
        console.log(e);
      }
      alert(errString);
    });
};

const RegisterForm: React.FunctionComponent = () => {
  return (
    <form className={styles.form} onSubmit={registerFormSubmit}>
      <label className={styles.label}>
        Username: <input className={styles.input} type="text" id="username"></input>
      </label>
      <br />
      <label className={styles.label}>
        Password: <input className={styles.input} type="password" id="password"></input>
      </label>
      <br />
      <label className={styles.label}>
        Confirm Password: <input className={styles.input} type="password" id="password2"></input>
      </label>
      <br />
      <input type="submit" id="submit"></input>
    </form>
  );
};

export default RegisterForm;
