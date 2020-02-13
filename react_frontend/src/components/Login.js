import React, { Component } from 'react'

export default class Login extends Component {
    render() {
        return (
                <div className="login">
                    <form onSubmit={this.props.handleLogin.bind(this)}>
                        <h4>Login</h4>
                        <label htmlFor="username">Username</label>
                        <input type="text" name="username" placeholder="username" onChange={this.props.handleUsername} required></input>
                        <br/>
                        <label htmlFor="password">Password</label>
                        <input type="password" name="password" placeholder="password" onChange={this.props.handlePassword} required></input>
                        <br/>
                        <input type="submit" value="Login" />
                    </form>
                <p id="loginMsg">{this.props.logInMessage !== null ? this.props.logInMessage : null}</p>
                <p>Dont have an account? Create one <a href='/register'>here</a></p>
                </div>
        )
    }
}
