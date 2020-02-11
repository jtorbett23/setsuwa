import React, { Component } from 'react'
import Post from '../components/Post'
import Comments from './Comments'

export default class Posts extends Component {
    state = {
        posts: this.props.posts,
        comments: null
    }
    render() {
        return (
            <div>
                <p>Posts page</p>
                {/* map through all the posts pass through */}
                <Post post={this.props.post} />
                <Comments />
            </div>
        )
    }
}
