import React, { Component } from 'react';
import {Container,Form, Button, Col, Row} from 'react-bootstrap';
import NavBar from '../NavBar/NavBar';
import './HomePage.css'



class HomePage extends Component {


  constructor(props) {
    super(props);
    this.state = {
      Proizvodjac: [],
      ProizvodjacModel: [],
      Modeli: [],
      Godiste: 2000,
      kubika : 1.0,
      Proiz: "",
      Model: "",
      Kilometraza: -1,
      Mjenjac: "Manuelni",
      BrojVrata: "",
      Emisija: "",
      Gorivo: "Benzin",
      kilovata: 40,
      Pogon: "Prednji",
      tip: "Caddy",
      Cijena: 0


    }
  }

  componentDidMount(){
    fetch("/api/Proizvodjaci").then((response) => response.json())
                .then((responseJson) => {
                    var json = JSON.parse(responseJson)
                    var o=Object.keys(json).length
                    var l=[]
                    for(var i=0; i<o; i++){
                      l.push(json[i].Proizvodjac)
                    }
                    this.setState({
                      Proizvodjac: l,
                      ProizvodjacModel: json
                    })
                })
  }

modeli(auto){
    this.setState({
      Proiz: auto
    })
    var o=Object.keys(this.state.ProizvodjacModel).length
    for(var i=0; i<o; i++){
      if(this.state.ProizvodjacModel[i].Proizvodjac === auto){
        this.setState({
          Modeli: this.state.ProizvodjacModel[i].Model
        })
      }
    }

}

getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

procijeni(){
  const csrftoken = this.getCookie('csrftoken');
  fetch('/api/procijeni', {
    method: 'POST',
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({
      Proizvodjac: this.state.Proiz,
      Model: this.state.Model,
      Godiste: parseInt(this.state.Godiste),
      Kilometara: parseInt(this.state.Kilometraza),
      Gorivo: this.state.Gorivo,
      Kubika: parseFloat(this.state.kubika),
      BrojVrata: this.state.BrojVrata,
      Kilovata: parseInt(this.state.kilovata),
      Cijena: 0,
      Tip: this.state.tip,
      Pogon: this.state.Pogon,
      Mjenjac: this.state.Mjenjac,
      Emisija: this.state.Emisija,
    })
  }).then((response) => response.json()).
  then((responseJson) => {
        this.setState({
          Cijena: responseJson.Cijena
        })
  })
}

  render() {
    const Proizvodjaci = this.state.Proizvodjac.map((Auto) => {
      return (
        <option>{Auto}</option>
      )
    });
    const Modeli = this.state.Modeli.map((Mod) => {
      return (
        <option>{Mod}</option>
      )
    })
    return (
      <div className='HomePage'>
        <NavBar></NavBar>
       

        <div className="body">

        <Container>
          <Form>
            <Row>
            <Col sm>
            <Form.Group controlId="osnovno">
              <div className="naslov">Osnovni podaci</div>
              <Form.Label className="text">Proizvođač</Form.Label>
              <Form.Control as="select" onChange={(e)=>{this.modeli(e.target.value)}}> 
                <option>Odaberite proizvođača...</option>
                {Proizvodjaci}
              </Form.Control>
              <Form.Label className="text">Model</Form.Label>
              <Form.Control as="select" onChange={(e)=>this.setState({Model: e.target.value})}>
                <option>Odaberite model...</option>
                {Modeli}
              </Form.Control>
              <Form.Label className="text" >Godište</Form.Label>
              <Form.Control as="select" onChange={(e)=>this.setState({Godiste: e.target.value})}>
                <option>2000</option>
                <option>2001</option>
                <option>2002</option>
                <option>2003</option>
                <option>2004</option>
                <option>2005</option>
                <option>2006</option>
                <option>2007</option>
                <option>2008</option>
                <option>2009</option>
                <option>2010</option>
                <option>2011</option>
                <option>2012</option>
                <option>2013</option>
                <option>2014</option>
                <option>2015</option>
                <option>2016</option>
                <option>2017</option>
                <option>2018</option>
                <option>2019</option>
                <option>2020</option>
              </Form.Control>
            <Form.Label className="text">Kilometraža</Form.Label>
            <Form.Control id="kilometri" type="number" min="0" step="5000" onChange={(e)=>this.setState({Kilometraza: e.target.value})}></Form.Control>
            </Form.Group>
            </Col>
            <Col sm>
            <Form.Group controlId="motor">
              <div className="naslov">Podaci o motoru</div>
              <Form.Label className="text">Gorivo</Form.Label>
              <Form.Control as="select"  onChange={(e)=>this.setState({Gorivo: e.target.value})}> 
                <option>Benzin</option>
                <option>Dizel</option>
                <option>Plin</option>
                <option>Hibrid</option>
              </Form.Control>
              <Form.Label className="text">Kubika</Form.Label>
              <Form.Control id="neki" type="number" min="1.0" max="5.0" step=".1"  onChange={(e)=>this.setState({kubika: e.target.value})}></Form.Control>
              <Form.Label className="text">Kilovata</Form.Label>
              <Form.Control id="neki2" type="number" min="40" max="400" step="1"  onChange={(e)=>this.setState({kilovata: e.target.value})}></Form.Control>
              <Form.Label as="legend" className="lab">
                Mjenjač
              </Form.Label>
              <Form.Control as="select"  onChange={(e)=>this.setState({Mjenjac: e.target.value})}>
                <option>Manuelni</option>
                <option>Automatik</option>
                <option>Polu-automatik</option>
              </Form.Control>
              </Form.Group>
              </Col>
            </Row>
            <Row>
              <Col sm>
                <Form.Group controlId="ostalo">
                <div className="naslov">Ostali podaci</div>
                    <Form.Label as="legend" className="lab">
                      Vrsta vozila
                    </Form.Label>
                    <Form.Control as="select"  onChange={(e)=>this.setState({tip: e.target.value})}>
                      <option>Caddy</option>
                      <option>Kabriolet</option>
                      <option>Karavan</option>
                      <option>Kombi</option>
                      <option>Limuzina</option>
                      <option>Malo auto</option>
                      <option>Monovolumen</option>
                      <option>Off-road</option>
                      <option>Pick-up</option>
                      <option>Sportski/kupe</option>
                      <option>Terenac</option>
                    </Form.Control>
                    <Form.Label as="legend" className="lab">
                      Pogon
                    </Form.Label>
                    <Form.Control as="select"  onChange={(e)=>this.setState({Pogon: e.target.value})}>
                      <option>Prednji</option>
                      <option>Sva četiri</option>
                      <option>Zadnji</option>
                    </Form.Control>
                  <Form.Label as="legend" className="lab" >
                      Broj vrata
                  </Form.Label>
                  <Form.Control as="select"  onChange={(e)=>this.setState({BrojVrata: e.target.value})}>
                    <option>2/3</option>
                    <option>4/5</option>
                  </Form.Control>
                  <Form.Label className="text" >Emisija</Form.Label>
                    <Form.Control as="select"  onChange={(e)=>this.setState({Emisija: e.target.value})}>
                      <option>Euro 0</option>
                      <option>Euro 1</option>
                      <option>Euro 2</option>
                      <option>Euro 3</option>
                      <option>Euro 4</option>
                      <option>Euro 5</option>
                      <option>Euro 6</option>
                    </Form.Control>
                </Form.Group>
              </Col>
            </Row>
            <Row>
              <Col sm><button type="button" class="button button1" onClick={() => {this.procijeni()}}>Procijeni!</button></Col>
              <Col sm><p className="naslov">{this.state.Cijena} KM</p></Col>
            </Row>
            </Form>
        </Container>   
        </div>
        

      </div>
    );
  }
}

export default HomePage;