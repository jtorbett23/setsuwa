import React, { Component } from 'react'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect
} from "react-router-dom";
import axios from 'axios';
import Login from './components/Login'
import Register from './components/Register'
import MakePost from './components/MakePost'
import EditPostHookContainer from './containers/EditPostHookContainer'
import SinglePostHookContainer from './containers/SinglePostHookContainer'
import UserPage from './containers/UserPage'
import Posts from './containers/Posts'
import Moderation from './components/Moderation'
import './static/css/App.css';
import logo from './static/logoSmall.png';

export default class App extends Component {
  state = {
    loggedIn: false,
    username: null,
    password: null,
    user: null,
    user_id: null,
    moderator: false,
    loggedInMessage: false,
    logInMessage: false,
    posts: null,
  }

  handleUsername (e) {
    this.setState({username: e.target.value, logInMessage: false})
  }
  handlePassword (e) {
    this.setState({password: e.target.value, logInMessage: false})
  }

  getID() {
    axios.post(`http://localhost:5000/auth/login?username=${this.state.username}&password=${this.state.password}`)
      .then(res => {
          this.setState({user: res.data})
          this.setState({user_id: res.data.user_id})
          this.setState({moderator: res.data.moderator})
          this.setState({loggedInMessage: "Logged in"})
          this.setState({loggedIn: true})
      })
      .catch(err => {
          this.setState({logInMessage: err.response.data.message})
          this.setState({loggedIn: false})   
      })
  }

  handleLogin(e) {
    e.preventDefault();
    this.getID()
  }
    
  logout() {
    window.location.reload(false);
  }

  render() {
    return (
      <Router>
        <div className="App">
          <nav>
              <ul>
                  <li>
                  <Link to="/"> <img id="logo" src={logo} alt="Logo"/></Link>
                  </li>
                  <li>
                      <Link to="/">Home</Link>
                  </li>
                  {this.state.loggedIn &&
                    <div id="loggedInNav">
                      <li>
                          <Link to="/createpost">Create post</Link>
                      </li>
                      <li>
                          <Link to={`/user/${this.state.user_id}`}>User account</Link>
                      </li>
                      {this.state.moderator &&
                        <li>
                          <Link to="/moderation">Moderate</Link>
                        </li>}
                      <li>
                          <Link onClick={this.logout} id="logout" to="/">Logout</Link>
                      </li>
                    </div>
                  }
                  {!this.state.loggedIn &&
                    <li>
                        <Link id="login" to="/login">Login / Register</Link>
                    </li>
                  }
              </ul>
          </nav>
          <section id ="page">
          <Switch>
              <Route path="/post/:id">
                   <SinglePostHookContainer user_id={this.state.user_id} />
              </Route>
              <Route path="/login">
               {this.state.loggedIn ? <Redirect to="/" /> :
                    <Login 
                  handleUsername={this.handleUsername.bind(this)} 
                  handlePassword={this.handlePassword.bind(this)} 
                  handleLogin={this.handleLogin.bind(this)} 
                  logInMessage={this.state.logInMessage} />}
                  </Route>
                  <Route path="/register">
                  <Register />
              </Route>
              <Route path="/moderation">
                  <Moderation user={this.state.user}/>
              </Route>
              <Route path="/createpost">
                  <MakePost user_id={this.state.user_id} />
              </Route>
              <Route path="/editpost/:id">
                  <EditPostHookContainer user_id={this.state.user_id} />
              </Route>
              <Route path="/user/:id">
                  <UserPage user_id={this.state.user_id} />
              </Route>
              <Route path="/">
                  <Posts user_id={this.state.user_id} />
              </Route>
          </Switch>
          </section>
        </div>
      </Router>
    )
  }
}

