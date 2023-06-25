import React, { useEffect, useState } from 'react';
import axios from 'axios';
import RegisterForm from './RegisterForm';

const backendurl = "http://localhost:8000"; // will need to read from env if we need to host this

const LoginPage: React.FunctionComponent = () => {
    return (
        <RegisterForm/>
    )
};

export default LoginPage;
