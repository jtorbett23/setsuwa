import React, { Component } from 'react'

export default class Post extends Component {
    render() {
        return (
            <div>
                <h3><a href={`/post/${this.props.post.post_id}`}>{this.props.post.title}</a></h3>
                <h5>{this.props.post.content}</h5>
                <p>Tags: {this.props.post.tag}</p>
            </div>
        )
    }
}
