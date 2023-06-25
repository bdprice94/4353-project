import React, { useEffect, useState } from 'react';
import axios from 'axios';

const backendurl = "http://localhost:8000"; // will need to read from env if we need to host this

export interface UserRegisterForm {
    username: { value: string },
    password:  { value: string },
    password2:  { value: string },
}

export interface UserRegister {
    username: string,
    password: string,
    password2: string,
}

export interface UserRegisterResponse {
    status: { value: boolean },
    text: {value: string},
}

const convertFormToModel = (form: UserRegisterForm) => {
    return {
        username: form.username.value,
        password: form.password.value,
        password2: form.password2.value,
    }
}

const stringContainsOneOf = (str: string, set: string) => {
    const chars = [...set];
    for (const char in chars) {
        if (str.includes(char)) {
            return true;
        }
    }
    return false;
}

const validateUserRegister = (userRegister: UserRegister) => {
    const username = userRegister.username;
    const password = userRegister.password;
    const password2 = userRegister.password2;
    const validSet =  '!@#$%^&*()<>,.;:"\'[]{}=-0987654321' ;
    const passwordRequirements = "Please enter a password of at least 8 characters with one special character " + 
        "in the set " + validSet;
    if (password !== password2) {
        alert("Please ensure that your passwords match!");
        return false;
    }
    if (username.length < 1) {
        alert("Please enter a username");
        return false;
    }
    if (password.length < 8 || !stringContainsOneOf(password, validSet)) {
        alert(passwordRequirements);
        return false;
    }
    return true;
}

const registerFormSubmit: React.FormEventHandler<HTMLFormElement> = (e: React.SyntheticEvent) => {
    e.preventDefault();
    const target = e.target as typeof e.target & UserRegisterForm;
    const userRegisterForm = {
        username: {value: target.username.value},
        password: {value: target.password.value},
        password2: {value: target.password2.value},
    };
    const userRegister = convertFormToModel(userRegisterForm);

    if (!validateUserRegister(userRegister)) {
        return;
    }
    axios.post(`${backendurl}/create_user`, userRegister)
        .then(response => {
            const data = response.data as UserRegisterResponse
            if (!data.status) {
                alert(data.text);
            }
            else {
                alert('Successfully created a user!');
            }
        })
        .catch(e => console.log(e));
}

const LoginPage: React.FunctionComponent = () => {

    return(
        <form onSubmit={registerFormSubmit}>
            <label>
                Username: <input type='text' id='username'></input>
            </label>
            <br/>
            <label>
                Password: <input type='password' id='password'></input>
            </label>
            <br/>
            <label>
                Confirm Password: <input type='password' id='password2'></input>
            </label>
            <br/>
            <input type='submit' id ='submit'></input>
        </form>
    )
};

export default LoginPage;
