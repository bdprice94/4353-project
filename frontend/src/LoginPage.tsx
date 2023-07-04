import React, { useState } from 'react';
import RegisterForm from './RegisterForm';
import LoginForm from './LoginForm';

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
