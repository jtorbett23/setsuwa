import React, { Component } from 'react'
import { Redirect } from 'react-router-dom';
import axios from 'axios';

export default class SinglePost extends Component {
    state = {
        post: null,
        user_id: this.props.user_id,
        deleted: false,
        edit: false,
        flagged: false
    }

    getPost() {
        axios.get(`http://localhost:5000/db/post?post_id=${this.props.id}`)
          .then(res => {
            this.setState({post: res.data})
          })
    }

    deletePost() {
        axios.delete(`http://localhost:5000/db/post?post_id=${this.props.id}`)
        .then(res => {
            this.setState({deleted: true})
        })
    }

    editPost() {
        this.setState({edit: true})
    }

    flagPost() {
        axios.put(`http://localhost:5000/db/flag?post_id=${this.props.id}`)
          .then(res => {
            this.setState({flagged: true})
          })
    }

    componentDidMount() {
        this.getPost()
    }

    render() {
        return (
            <div>
                {this.state.post !== null ? 
                !this.state.deleted ?
                <div>
                <h3>{this.state.post.title}</h3>
                <p>{this.state.post.content}</p>
                <p>{this.state.post.tag}</p>
                {this.state.user_id === this.state.post.user_id ? 
                <div>
                    <button onClick={this.deletePost.bind(this)}>Delete post</button>
                    <button onClick={this.editPost.bind(this)}>Edit post</button>
                </div> 
                : null}
                <button onClick={this.flagPost.bind(this)}>Flag</button>
                </div> : <p>Post deleted</p>
                : <p>This post does not exist :L</p>}
                {this.state.deleted === true || this.state.flagged === true ? <Redirect push to="/"/> : null}
                {this.state.edit === true ? <Redirect push to={`/editpost/${this.state.post.post_id}`}/> : null}
            </div>
        )
    }
}
