import React, { Component } from 'react'

export default class Login extends Component {
    render() {
        return (
            <div>
                <div className="login">
                    <form onSubmit={this.props.handleLogin}>
                        <h4>Login</h4>
                        <label for="username">Username</label>
                        <input type="text" name="username" placeholder="username" onChange={this.props.handleUsername}></input>
                        <br/>
                        <label for="password">Password</label>
                        <input type="text" name="password" placeholder="password" onChange={this.props.handlePassword}></input>
                        <br/>
                        <input type="submit" value="Login" />
                    </form>
                </div>

                <p id="loginMsg">{this.props.loggedInMessage !== false ? this.props.loggedInMessage : null}</p>

                <div className="Register">
                    <form onSubmit={this.props.handleRegister}>
                        <h4>Register</h4>
                        <label for="username">Username</label>
                        <input type="text" name="username" placeholder="username" onChange={this.props.handleUsername}></input>
                        <br/>
                        <label for="password">Password</label>
                        <input type="text" name="password" placeholder="password" onChange={this.props.handlePassword}></input>
                        <br/>
                        <input type="submit" value="Register" />
                    </form>
                </div>

                <p id="RegisterMsg">{this.props.registerMessage !== false ? this.props.registerMessage : null}</p>
                
            </div>
        )
    }
}
