import React, { useState } from "react";
import RegisterForm from "./LoginSignup";
import LoginForm from "./LoginSignin";

const LoginPage: React.FunctionComponent = () => {
  const [needsLogin, setNeedsLogin] = useState(false);

  const changeLoginOrRegister = () => {
    setNeedsLogin(!needsLogin);
  };

  const FormToRender: React.FunctionComponent<{}> = needsLogin
    ? LoginForm
    : RegisterForm;

  return (
    <div style={{ justifyContent: "center" }}>
      <FormToRender />
      <br />
      <button
        id="register_or_login"
        onClick={changeLoginOrRegister}
        style={{
          border: "1px solid #26474e",
          borderRadius: "5px",
          padding: "10px",
          margin: "10px",
          position: "absolute",
          top: "80%",
          right: "600px",
          transform: "translateY(-50%)",
        }}
      >
        {needsLogin
          ? "Don't have an account yet? Click to Register"
          : "Already have an account? Sign in here!"}
      </button>
    </div>
  );
};

export default LoginPage;
