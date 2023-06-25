import React, { useEffect, useState } from 'react';
import axios from 'axios';
import RegisterForm from './RegisterForm';
import LoginForm from './LoginForm';

const backendurl = "http://localhost:8000"; // will need to read from env if we need to host this

const LoginPage: React.FunctionComponent = () => {
    const [needsLogin, setNeedsLogin] = useState(false)

    const changeLoginOrRegister = () => {
        setNeedsLogin(!needsLogin)
    }

    const FormToRender: React.FunctionComponent<{}> = needsLogin ? LoginForm : RegisterForm;

    return (
        <div>
            <FormToRender/>
            <br/>
            <button id="register_or_login" onClick={changeLoginOrRegister}>
                {needsLogin ? "Register" : "Login"}
            </button>
        </div>
    )
};

export default LoginPage;
