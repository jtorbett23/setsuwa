import React, { Component } from 'react'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import axios from 'axios';
import Posts from './containers/Posts'
import Login from './components/Login'
import './static/css/App.css';

export default class App extends Component {
  state = {
    loggedIn: false,
    food: 'rice',
    username: null,
    password: null,
    user_id: null,
    loggedInMessage: false,
    registerMessage: false
  }

  handleUsername (e) {
    this.setState({username: e.target.value})
  }
  handlePassword (e) {
    this.setState({password: e.target.value})
  }

  getID() {
    let headers = {
      "Access-Control-Allow-Origin": "http://localhost:5000/",
      "Access-Control-Allow-Methods": "GET, POST",
      "Access-Control-Allow-Credentials": "true",
      "Access-Control-Allow-Headers": "Access-Control-Allow-Origin, Access-Control-Allow-Origin"
    }

    axios.post(`http://localhost:5000/auth/login?username=${this.state.username}&password=${this.state.password}`)
      .then(res => {
        if(res.data.user_id) {
          this.setState({user_id: res.data.user_id})
          this.setState({loggedInMessage: "Logged in"})
        }
        if(res.data.message) {
          this.setState({loggedInMessage: res.data.message})
        }
        console.log(res.data)
      })
  }
  
  createUser() {
    let headers = {
      "Access-Control-Allow-Origin": "http://localhost:5000/",
      "Access-Control-Allow-Methods": "GET, POST",
      "Access-Control-Allow-Credentials": "true",
      "Access-Control-Allow-Headers": "Access-Control-Allow-Origin, Access-Control-Allow-Origin"
    }

    axios.post(`http://localhost:5000/auth/register?username=${this.state.username}&password=${this.state.password}`)
      .then(res => {
        this.setState({registerMessage: res.data.message})
        // this.setState({user_id: res.data.user_id})
      })
  }

  handleLogin(e) {
    e.preventDefault();
    this.getID()
  }
  handleRegister(e) {
    e.preventDefault();
    this.createUser()
  }

  componentDidUpdate() {
    console.log("woop")
    console.log(this.state.user_id)
  }

  render() {
    return (
      <Router>
        <div className="App">
          <nav>
              <ul>
                  <li>
                      <Link to="/">Home</Link>
                  </li>
                  <p>Search a tag</p>
                  <select>
                    <option value="Sports">Sports</option>
                    <option value="Movies">Movies</option>
                    <option value="Food">Food</option>
                  </select>
                  {this.state.loggedIn &&
                    <div>
                      <li>
                          <Link to="/createpost">Create post</Link>
                      </li>
                      <li>
                          <Link to="/friends">Friends</Link>
                      </li>
                      <li>
                          <Link to="/useracount">User account</Link>
                      </li>
                      <li>
                          <Link to="/">Logout</Link>
                      </li>
                    </div>
                  }
                  {!this.state.loggedIn &&
                    <li>
                        <Link to="/login">Login/Register</Link>
                    </li>
                  }
              </ul>
          </nav>

          <h1>Setsuwa</h1>

          <Switch>
              <Route path="/login">
                  <Login handleUsername={this.handleUsername.bind(this)} handlePassword={this.handlePassword.bind(this)} handleLogin={this.handleLogin.bind(this)} handleRegister={this.handleRegister.bind(this)} loggedInMessage={this.state.loggedInMessage} registerMessage={this.state.registerMessage}/>
              </Route>
              <Route path="/users">
                  {/* <Users /> */}
              </Route>
              <Route path="/">
                  <Posts food={this.state.food} />
              </Route>
          </Switch>
        </div>
      </Router>
    )
  }
}

