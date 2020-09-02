import React, { Component } from 'react';
import { Form} from 'react-bootstrap';
import {Redirect} from 'react-router-dom'

import "./LoginPage.css"



class LoginForm extends Component {

  
  constructor(props) {
    super(props);

      this.state = {
        redirect: false,
        username:'',
        password:'',
      };
      this.onLogin = this.onLogin.bind(this)
  }

    
  onLogin() {
    
  
    var data = new FormData();
    data.append("username",this.state.username)
    data.append("password",this.state.password)
    fetch('/user',{
      method: "OPTIONS",
      body: data

    }).then((response) => response.json())
    .then(
      (responseJson) => {
        if(responseJson.message==="No value present"){
          alert("pogresan username ili password")
        }
        else{
          global.role=responseJson.role.role;
            localStorage.setItem('username',this.state.username);
            localStorage.setItem('password',this.state.password);
            localStorage.setItem('id',responseJson.id);
            localStorage.setItem('prijavljen',true);
            localStorage.setItem('role',responseJson.role.role);
            this.setState(
              ()=>({
                redirect:true,
              })
            ) 
        }
      }
    )
   
  }

componentDidMount(){
  localStorage.setItem('username','');
  localStorage.setItem('password','');
  localStorage.setItem('id','');
  localStorage.setItem('prijavljen',false);
  localStorage.setItem('role','odjavljen');
}

  render() {

    if(this.state.redirect === true){
      if(global.role==="user"){
        return <Redirect to="/pregledusluga"></Redirect>
      }
      if(global.role==="uposleni"){
        return <Redirect to="/uposleni"></Redirect>
      }
      return <Redirect to="/incidentmanageradmin"></Redirect>
    }

    return (
     
      <div>

      <Form >
          <Form.Group>
            
            <Form.Control type="username" placeholder="Username" value={this.state.username} onChange={(e)=>{
              this.setState({
                username:e.target.value
              })
            }}/>
          </Form.Group>

          <Form.Group controlId="formBasicPassword">

            <Form.Control type="password" placeholder="Password" value={this.state.password} onChange={(e)=>{
              this.setState({
                password:e.target.value
              })
            }}/>
          </Form.Group>
          
          
          
      </Form>
      <button className="submit" onClick={this.onLogin} >
      Login
      </button>
      </div>
    )
  }
}

export default LoginForm;
