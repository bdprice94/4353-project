import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { backendurl } from './utils';

const backendurl_users = `${backendurl}/users`

export interface UserRegisterForm {
    username:  { value: string },
    password:  { value: string },
    password2: { value: string },
}

export interface UserRegister {
    username:  string,
    password:  string,
    password2: string,
}

const convertFormToModel = (form: UserRegisterForm) => {
    return {
        username:  form.username.value,
        password:  form.password.value,
        password2: form.password2.value,
    }
}

const registerFormSubmit: React.FormEventHandler<HTMLFormElement> = (e: React.SyntheticEvent) => {
    e.preventDefault();
    const target = e.target as typeof e.target & UserRegisterForm;
    const userRegisterForm = {
        username:  {value: target.username.value},
        password:  {value: target.password.value},
        password2: {value: target.password2.value},
    };
    const userRegister = convertFormToModel(userRegisterForm);
    axios.post(`${backendurl_users}/create_user`, userRegister)
        .then(response => {
            alert('Successfully created a user!');
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

const RegisterForm: React.FunctionComponent = () => {
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
            <label>
                Confirm Password: <input type='password' id='password2'></input>
            </label>
            <br/>
            <input type='submit' id ='submit'></input>
        </form>
    )
}

export default RegisterForm
