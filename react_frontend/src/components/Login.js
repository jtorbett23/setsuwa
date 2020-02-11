import React, { Component } from 'react'

export default class Login extends Component {
    render() {
        return (
            <div>
                <div className="login">
                    <form onSubmit={this.props.handleLogin}>
                        <h4>Login</h4>
                        <label htmlFor="username">Username</label>
                        <input type="text" name="username" placeholder="username" onChange={this.props.handleUsername}></input>
                        <br/>
                        <label htmlFor="password">Password</label>
                        <input type="password" name="password" placeholder="password" onChange={this.props.handlePassword}></input>
                        <br/>
                        <input type="submit" value="Login" />
                    </form>
                <p id="loginMsg">{this.props.logInMessage !== false ? this.props.logInMessage : null}</p>
                </div>

                <p>Dont have an account? Create one <a href='/register'>here</a></p>

                {/* <div className="Register">
                    <form onSubmit={this.props.handleRegister}>
                        <h4>Register</h4>
                        <label htmlFor="username">Username</label>
                        <input type="text" name="username" placeholder="username" onChange={this.props.handleUsername}></input>
                        <br/>
                        <label htmlFor="password">Password</label>
                        <input type="password" name="password" placeholder="password" onChange={this.props.handlePassword}></input>
                        <br/>
                        <input type="submit" value="Register" />
                    </form>
                {this.props.registerPayload.status === 200 ? this.show() : <p id="RegisterMsg">{this.props.registerPayload.data.message}</p>} 
                </div> */}
                
            </div>
        )
    }
}
