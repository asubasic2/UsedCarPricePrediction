import React, { Component } from 'react';
import PrijavaForm from './PrijavaForm';
import NavBar from '../NavBar/NavBar';

import './PrijavaPage.css';

class PrijavaPage extends Component {
  render() {
    return (
     
      <div className="LoginPage">
        
        <NavBar />
        
        <div className="naslov"> Prijava </div>
        
        <div className="body">

          <PrijavaForm />

        </div>
        

      </div>
      
    );
  }
}

export default PrijavaPage;
