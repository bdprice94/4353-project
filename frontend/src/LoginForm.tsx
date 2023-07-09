import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { backendurl, setCookie } from './utils';
import styles from "./LoginForm.module.css";



const backendurl_users = `${backendurl}/users`; // will need to read from env if we need to host this
 
export interface UserLoginForm {
    username: { value: string },
    password:  { value: string },
}

export interface UserLogin {
    username: string,
    password: string,
}

export interface UserLoginResponse {
    username: string,
    id:       number,
}

const convertFormToModel = (form: UserLoginForm) => {
    return {
        username: form.username.value,
        password: form.password.value,
    }
}

const registerFormSubmit: React.FormEventHandler<HTMLFormElement> = (e: React.SyntheticEvent) => {
    e.preventDefault();
    const target = e.target as typeof e.target & UserLoginForm;
    const userLoginForm = {
        username: {value: target.username.value},
        password: {value: target.password.value},
    };
    const userLogin = convertFormToModel(userLoginForm);
    axios.post(`${backendurl_users}/login`, userLogin)
        .then(response => {
            console.log(response)
            const data = response.data as UserLoginResponse
            alert(`Successfully logged in ${data.username}!`);
            setCookie('username', data.username);
            setCookie('userid', data.id.toString())
        })
        .catch(e => {
            if ('response' in e && e.response.status === 422) {
                const errString = e.response.data.detail
                    .map((err: any) => err.msg)
                    .join('\n');
                alert(errString)
            }
            else {
                console.log(e)
            }
        });
}

const LoginForm: React.FunctionComponent = () => {
    return (
        <form  className={styles.form} onSubmit={registerFormSubmit}>
            <label className={styles.label}>
                Username: <input type='text' id='username' className={styles.input}></input>
            </label>
            <br/>
            <label className={styles.label}>
                Password: <input type='password' id='password' className={styles.input}></input>
            </label>
            <br/>
            <input type='submit' id ='submit' ></input>
        </form>
    )
}

export default LoginForm
