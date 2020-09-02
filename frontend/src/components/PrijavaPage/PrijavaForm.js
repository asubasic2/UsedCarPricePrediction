import React, { Component } from 'react';
import { Form } from 'react-bootstrap';
import {Redirect} from 'react-router-dom'
import "./PrijavaPage.css"



class PrijavaForm extends Component {

  constructor(props) {
    super(props);

      this.state = {
        redirect: false,
        ime:'',
        prezime:'',
        username:'',
        password:'',
        repeatpassword:''
      };
      this.onLogin = this.onLogin.bind(this)
  }

    
  onLogin() {
    var korisnik = {
      first_name:this.state.ime,
      last_name:this.state.prezime,
      username:this.state.username,
      password:this.state.password,
      role:{
        id:2,
        role:"user"
      }
    };
   
   
    fetch('/user',{
      method: "POST",
      body: JSON.stringify(korisnik),  
      headers:{
        'Content-Type': 'application/json'
       }

    }).then((response) => response.json())
    .then(
      (responseJson) => {
        if(responseJson.id>0){
          alert("uspješno ste prijavljeni")
          this.setState({
            redirect:true
          })
        }
        else{
          alert("pogrešno uneseni podaci")
        }
      })
  }

  render() {

    if(this.state.redirect === true){
      return <Redirect to="/incidentmanageradmin"></Redirect>
    }



    return (
      <div>
      <Form>
  <Form.Group>   
    <Form.Control type="username" placeholder="Ime" value={this.state.ime} onChange={(e)=>{
              this.setState({
                ime:e.target.value
              })
            }}/>
  </Form.Group>

  <Form.Group>   
    <Form.Control type="username" placeholder="Prezime" value={this.state.prezime} onChange={(e)=>{
              this.setState({
                prezime:e.target.value
              })
            }}/>
  </Form.Group>

  <Form.Group>   
    <Form.Control type="username" placeholder="username" value={this.state.username} onChange={(e)=>{
              this.setState({
                username:e.target.value
              })
            }}/>
  </Form.Group>

  <Form.Group controlId="formBasicPassword">

    <Form.Control type="password" placeholder="Šifra" value={this.state.password} onChange={(e)=>{
              this.setState({
                password:e.target.value
              })
            }}/>
  </Form.Group>

  <Form.Group controlId="formBasicPassword">

    <Form.Control type="password" placeholder="Ponovite šifru" value={this.state.repeatpassword} onChange={(e)=>{
              this.setState({
                repeatpassword:e.target.value
              })
            }}/>
  </Form.Group>

</Form>
<button className="submit" onClick={this.onLogin}>
    Prijavi se
  </button>
  </div>
    )
  }
}

export default PrijavaForm;
