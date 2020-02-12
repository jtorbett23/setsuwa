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
import SinglePostHookContainer from './containers/SinglePostHookContainer'
// import Posts from './containers/Posts'
import './static/css/App.css';

export default class App extends Component {
  state = {
    loggedIn: true,
    username: null,
    password: null,
    user_id: 1,
    loggedInMessage: false,
    logInMessage: false,
    registerPayload: null,
    // title: null,
    // blog: null,
    // tags: null,
    post: null,
    posts: null,
  }

  handleUsername (e) {
    this.setState({username: e.target.value})
  }
  handlePassword (e) {
    this.setState({password: e.target.value})
  }
  // handleTitle (e) {
  //   this.setState({title: e.target.value})
  // }
  // handleBlog (e) {
  //   this.setState({blog: e.target.value})
  // }
  // handleTags (e) {
  //   this.setState({tags: e.target.value})
  // }

  getID() {
    axios.post(`http://localhost:5000/auth/login?username=${this.state.username}&password=${this.state.password}`)
      .then(res => {
        if(res.data.user_id) {
          this.setState({user_id: res.data.user_id})
          this.setState({loggedInMessage: "Logged in"})
          this.setState({loggedIn: true})
        }
        if(res.data.message) {
          this.setState({logInMessage: res.data.message})
          this.setState({loggedIn: false})
        }
      })
    }
    
    createUser() {
      axios.post(`http://localhost:5000/auth/register?username=${this.state.username}&password=${this.state.password}`)
      .then(res => {
        this.setState({registerPayload: res})
      })
      .catch(err => {
        this.setState({registerPayload: err.response})
      })
    }
    
    // createPost() {
    //   axios.post(`http://localhost:5000/db/post?user_id=${this.state.user_id}&title=${this.state.title}&content=${this.state.blog}&tag=${this.state.tags}`)
    //   .then(res => {
    //     if(res.status === 200) {
    //         this.setState({post: res.data.post_id})
    //         console.log(res.data.post_id)
    //     }
    //     if(res.status === 500) {
    //       console.log('didnt work') // need to alter this
    //     }
    //   })
    // }

    handleLogin(e) {
      e.preventDefault();
      this.getID()
    }
    handleRegister(e) {
      e.preventDefault();
      this.createUser()
    }
    
    logout() {
      window.location.reload(false);
    }

  componentDidUpdate() {
    console.log("woop")
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
                  <Register
                  handleUsername={this.handleUsername.bind(this)} 
                  handlePassword={this.handlePassword.bind(this)}
                  handleRegister={this.handleRegister.bind(this)} 
                  registerPayload={this.state.registerPayload}/>
              </Route>
              <Route path="/users">
                  {/* <Users /> */}
              </Route>
              <Route path="/createpost">
                  {this.state.post !== null ? <Redirect to={`/post/${this.state.post}`} /> :
                  <MakePost 
                  user_id={this.state.user_id}
                  // handleTitle={this.handleTitle.bind(this)}
                  // handleBlog={this.handleBlog.bind(this)}
                  // handleTags={this.handleTags.bind(this)}
                  // createPost={this.createPost.bind(this)}
                  />}
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

