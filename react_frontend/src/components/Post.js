import React, { Component } from 'react'
import { Redirect } from 'react-router-dom';

export default class Post extends Component {
    state = {
        clicked: false
    }

    clicker() {
        this.setState({clicked: true})
    }

    render() {
        return (
            <div className="postContainer">
                <h3 style={{color: "blue", textDecoration: "underline"}} onClick={this.clicker.bind(this)}>{this.props.post.title}</h3>
                <h5>{this.props.post.content}</h5>
                <p>Tags: {this.props.post.tag} </p>
                <p>Created: {this.props.post.created}</p>
                {this.state.clicked === true ? <Redirect push to={`/post/${this.props.post.post_id}`} /> : null}
            </div>
        )
    }
}
