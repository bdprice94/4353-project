import logo from './logo.svg';
import styles from './App.module.css'; // import as a module
import BackendSample from './BackendSample';
import LoginPage from './LoginPage';
import UserProfileForm from './clientProfile/UserProfileForm';
import UserProfileDisplay from './clientProfile/UserProfileDisplay';
import FuelQuoteForm from './clientfuelquote/components/FuelQuoteForm';
import FuelQuoteHistory from './clientfuelquote/components/FuelQuoteHistory';
import { BrowserRouter, Route, Routes } from "react-router-dom";

function App() {

  return (
<BrowserRouter>
      <div className={styles.App}> 
        <header className={styles.Appheader}>
          {/* Route for the LoginPage */}
          <Routes>
          <Route path="/" element={<LoginPage />} />
          <Route path="/backend-sample" element={<BackendSample />} />
          <Route path="/user-profile-form" element={<UserProfileForm/>} />
          <Route path="/user-profile-display" element={<UserProfileDisplay/>} />
          <Route path="/fuel-quote-form" element={<FuelQuoteForm/>} />
          <Route path="/fuel-quote-history" element={<FuelQuoteHistory/>} />
          </Routes>
        </header>
      </div>
    </BrowserRouter>
  );
}
          
          
          
          
          
         
         
       

export default App;
