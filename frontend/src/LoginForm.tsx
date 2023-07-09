import React from 'react';
import axios, {AxiosError} from 'axios';
import { backendurl, setCookie } from './utils';

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

const loginFormSubmit: React.FormEventHandler<HTMLFormElement> = (e: React.SyntheticEvent) => {
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
                    errString = data.detail
                }
                else {
                    console.log(e.response.data)
                }
            }
            else {
                console.log(e)
            }
            alert(errString)
        });
}

const LoginForm: React.FunctionComponent = () => {
    return (
        <form onSubmit={loginFormSubmit}>
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
