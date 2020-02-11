import React, { Component } from 'react'

export default class MakePost extends Component {
    render() {
        return (
            <div>
                <label htmlFor="title">Title</label>
                <input type="text" name="title" onChange={this.props.handleTitle} placeholder="type here..."></input>
                <label htmlFor="blog">Blog</label>
                <input type="text" name="blog" onChange={this.props.handleBlog} placeholder="Whatsonn your mind..."></input>
                <label htmlFor="tags">Tag</label>
                <input type="text" name="tags" onChange={this.props.handleTags} placeholder="tag"></input>
                <button onClick={this.props.createPost}>Post</button>
            </div>
        )
    }
}
