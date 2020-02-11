import React, { Component } from 'react'

export default class Register extends Component {
    render() {
        return (
            <div className="Register">
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

            <p id="RegisterMsg">{this.props.registerPayload !== null ? (this.props.registerPayload.status === 200 ? <a href='/login'>Login</a> : this.props.registerPayload.data.message) : null}</p>

        {/* {this.props.registerPayload.status && <p id="RegisterMsg">{this.props.registerPayload.data.message}</p>}  */}
        {/* {(this.props.registerPayload && this.props.registerPayload.status === 200) && } */}
        {}
        </div>
        )
    }
}
