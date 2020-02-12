import React, { Component } from 'react'
import axios from 'axios';
import { Redirect } from 'react-router-dom';

export default class Register extends Component {
    state = {
        username: null,
        password: null,
        registerPayload: null,
    }

    handleUsername (e) {
        this.setState({username: e.target.value, registerPayload: null})
    }
    handlePassword (e) {
        this.setState({password: e.target.value, registerPayload: null})
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
      
    handleRegister(e) {
        e.preventDefault();
        this.createUser()
    }

    render() {
        return (
            <div className="Register">
            <form onSubmit={this.handleRegister.bind(this)}>
                <h4>Register</h4>
                <label htmlFor="username">Username</label>
                <input type="text" name="username" placeholder="username" onChange={this.handleUsername.bind(this)} required></input>
                <br/>
                <label htmlFor="password">Password</label>
                <input type="password" name="password" placeholder="password" onChange={this.handlePassword.bind(this)} required></input>
                <br/>
                <input type="submit" value="Register" />
            </form>

            {this.state.registerPayload !== null ? this.state.registerPayload.status === 200 ? <Redirect push to="/login"/> : <p id="RegisterMsg">{this.state.registerPayload.data.message}</p> : null}
        </div>
        )
    }
}
