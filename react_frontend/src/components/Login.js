import React, { Component } from 'react'

export default class Login extends Component {
    render() {
        return (
                <div className="textCenter">
                    <form onSubmit={this.props.handleLogin.bind(this)}>
                        <h1 id="loginTitle">Login</h1>
                        <div className="accountDetailsContainer">
                        <label htmlFor="username">Username:</label>
                        <input type="text" name="username" placeholder="username" onChange={this.props.handleUsername} required></input>
                        <br/>
                        <label htmlFor="password">Password:</label>
                        <input type="password" name="password" placeholder="password" onChange={this.props.handlePassword} required></input>
                        <br/>
                        <input className="button" type="submit" value="Login" />
                        </div>
                    </form>
                <p id="loginMsg" className="textCenter">{this.props.logInMessage !== null ? this.props.logInMessage : null}</p>
                <p id="registerPrompt" className="textCenter">Dont have an account? Create one <a href='/register'>here</a></p>
                </div>
        )
    }
}
