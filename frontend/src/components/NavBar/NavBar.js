import React, { Component } from 'react';
import {Navbar,Nav} from 'react-bootstrap';
import './NavBar.css'

class NavBar extends Component {

render(){
    return(
     <div className="navbar"> 
      <Navbar  expand="lg">
      <Navbar.Brand href="/" style={{color:'#f8ea23'}}><h3>Procijeni Moje Auto!</h3></Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav"  style={{color: '#f8bf23'}} />
      <Navbar.Collapse id="basic-navbar-nav" style={{color: '#f8bf23'}}>
       <Nav className="mr-auto"></Nav>
      
        <Nav.Link href="/"><p className="textlink">Pregled usluga</p> </Nav.Link>
        <Nav.Link href="/login"><p className="textlink">Login</p> </Nav.Link>
        <Nav.Link href="/prijava"><p className="textlink">Prijava</p> </Nav.Link>
       
      </Navbar.Collapse>
      </Navbar>
    </div>  
    );
}

}

export default NavBar;