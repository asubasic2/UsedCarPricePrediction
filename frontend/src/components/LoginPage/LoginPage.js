import React, { Component } from 'react';
import LoginForm from './LoginForm';
import NavBar from '../NavBar/NavBar';

import './LoginPage.css';

class LoginPage extends Component {
  render() {
    return (
     
      <div className="LoginPage">
        
        <NavBar />
        
        <div className="naslov"> Login </div>
        
        <div className="body">

          <LoginForm />

        </div>
        

      </div>
      
    );
  }
}

export default LoginPage;
