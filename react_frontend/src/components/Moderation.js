import React, { Component } from 'react'
import { Redirect } from 'react-router-dom';
import axios from 'axios'

export default class Moderation extends Component {
    state = {
        user: this.props.user,
        flaggedPosts: [],
        reponded: false,
    }

    getFlagedPosts() {
        axios.get("http://localhost:5000/db/flag")
          .then(res => {
            this.setState({flaggedPosts: res.data})
          })
    }

    flagPost(e) {
        axios.put(`http://localhost:5000/db/flag?post_id=${e.target.id}`)
          .then(res => {
            this.getFlagedPosts()
          })
    }

    deletePost(e) {
        axios.delete(`http://localhost:5000/db/post?post_id=${e.target.id}`)
        .then(res => {
            this.getFlagedPosts()
        })
    }

    componentDidMount() {
        this.getFlagedPosts()
    }

    render() {
        return (
            <div>
            {this.state.user !== null ? <div>
            {(this.state.user.moderator === true) ?
                this.state.flaggedPosts.length > 0 ? this.state.flaggedPosts.map((post, index) => (
                    <div key={index}>
                        <h3>{post.title}</h3>
                        <p>{post.content}</p>
                        <p>{post.tag}</p>
                        <button id={post.post_id} onClick={this.flagPost.bind(this)}>Approve</button>
                        <button id={post.post_id} onClick={this.deletePost.bind(this)}>Delete post</button>
                    </div>
                )) : <p>No posts to moderate :P</p>
            : null}
            {this.state.reponded === true && <Redirect push to={`/moderation`} />}
            </div> : <p>You cannot access this page</p>}
            </div>
        )
    }
}
