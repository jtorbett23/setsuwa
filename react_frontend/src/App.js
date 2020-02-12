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
import './static/css/App.css';

export default class App extends Component {
  state = {
    loggedIn: false,
    username: null,
    password: null,
    user_id: null,
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
          this.setState({user_id: res.data.user_id})
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
                          <Link to="/useraccount">User account</Link>
                      </li>
                      <li>
                          <Link onClick={this.logout} id="logout" to="/">Logout</Link>
                      </li>
                    </div>
                  }
                  {!this.state.loggedIn &&
                    <li>
                        <Link id="login" to="/login">Login/Register</Link>
                    </li>
                  }
              </ul>
              <p id="loginMsg">{this.state.loggedInMessage !== false ? this.state.loggedInMessage : 'Logged out'}</p>
          </nav>

          <h1>Setsuwa</h1>

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
              <Route path="/users">
                  {/* <Users /> */}
              </Route>
              <Route path="/createpost">
                  <MakePost user_id={this.state.user_id} />
              </Route>
              <Route path="/editpost/:id">
                  <EditPostHookContainer user_id={this.state.user_id} />
              </Route>
              <Route path="/">
                  {/* <Posts post={this.state.post} /> */}
                  <p>This is the home page that will display "Posts"</p>
              </Route>
          </Switch>
        </div>
      </Router>
    )
  }
}

