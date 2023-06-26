import logo from './logo.svg';
import './App.css';
import BackendSample from './BackendSample';

function App() {

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Hello, this is a main page. Below you can see a list of all the current users.
        </p>
        <BackendSample />
      </header>
    </div>
  );
}

export default App;
