import React, { useEffect, useState } from 'react';
import axios from 'axios';

const backendurl = "http://localhost:8000"; // will need to read from env if we need to host this
 
export interface UserLoginForm {
    username: { value: string },
    password:  { value: string },
}

export interface UserLogin {
    username: string,
    password: string,
}

export interface UserLoginResponse {
    status: { value: boolean },
    text: {value: string},
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
    axios.post(`${backendurl}/login`, userLogin)
        .then(response => {
            const data = response.data as UserLoginResponse
            if (!data.status) {
                alert(data.text);
            }
            else {
                alert('Successfully logged in!');
            }
        })
        .catch(e => {
            if (e.response.status === 422) {
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
        <form onSubmit={registerFormSubmit}>
            <label>
                Username: <input type='text' id='username'></input>
            </label>
            <br/>
            <label>
                Password: <input type='password' id='password'></input>
            </label>
            <br/>
            <input type='submit' id ='submit'></input>
        </form>
    )
}

export default LoginForm
