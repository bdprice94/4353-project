import React, { useEffect, useState } from 'react';
import axios from 'axios';

const backendurl = "http://localhost:8000" // will need to read from env if we need to host this

export interface UserProfile {
  "username": string,
  "password":  string,
}

const construct_register_form: React.FunctionComponent = () => {
    
}

const LoginPage: React.FunctionComponent = () => {

    const [text, setText] = useState<UserProfile>()
    useEffect(() => {
        async function getText() {
            const response = await axios.get(backendurl);
            const payload: UserProfile = response.data;
            setText(payload)
        }

        // react components will re-render every time set state functions (like setText) are called
        // this prevents an infinite render loop but obv not good practice, just setting up quick
        // prototype
        if (!text.message) {
            getText();
        }
    });

    return(
        <div>
            <p>{text.message}</p>
        </div>
    )
};

export default LoginPage;
