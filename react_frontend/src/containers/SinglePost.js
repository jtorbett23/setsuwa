import React, { Component } from 'react'
import axios from 'axios';

export default class SinglePost extends Component {
    state = {
        post: null
    }

    getPost() {
        axios.get(`http://localhost:5000/db/post?post_id=${this.props.id}`)
          .then(res => {
            this.setState({post: res.data})
          })
      }

    componentDidMount() {
        this.getPost()
    }

    render() {
        return (
            <div>
                {this.state.post !== null ? 
                <div>
                <h3>{this.state.post.title}</h3>
                <p>{this.state.post.content}</p>
                <p>{this.state.post.tag}</p>
                </div> 
                : null}
            </div>
        )
    }
}
