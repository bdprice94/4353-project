import React from "react";
import ReactDOM from "react-dom/client";
import Routing from "./router/router";
import axios from "axios";
import { BrowserRouter } from "react-router-dom";

axios.defaults.withCredentials = true;

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement,
);
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routing />
    </BrowserRouter>
  </React.StrictMode>,
);
