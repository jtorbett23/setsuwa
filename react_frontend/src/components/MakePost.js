import React, { Component } from 'react'
import axios from 'axios';
import { Redirect } from 'react-router-dom';

export default class MakePost extends Component {
    state = {
        user_id: this.props.user_id,
        title: null,
        blog: null,
        tags: null,
        post_id: null,
        made: false,
        errorMSG: null
    }

    handleTitle (e) {
        this.setState({title: e.target.value})
    }
    handleBlog (e) {
        this.setState({blog: e.target.value})
    }
    handleTags (e) {
        this.setState({tags: e.target.value})
    }

    createPost() {
        axios.post(`http://localhost:5000/db/post?user_id=${this.state.user_id}&title=${this.state.title}&content=${this.state.blog}&tag=${this.state.tags}`)
        .then(res => {
            if(res.status === 200) {
                this.setState({post_id: res.data.post_id})
                console.log(res.data.post_id)
                this.setState({made: true})
            }   
            if(res.status === 500) {
                this.setState({errorMSG: "create post failed"})
                console.log('didnt work') // need to alter this
            }
        })
    }

    createThenRedirect(e) {
        e.preventDefault()
        this.createPost()
    }

    render() {
        return (
            <div>
                <form onSubmit={this.createThenRedirect.bind(this)}>
                    <div className="createContainer">
                    <label htmlFor="title">Title:</label>
                    <input type="text" name="title" onChange={this.handleTitle.bind(this)} placeholder="type here..." required></input>
                    <label htmlFor="blog">Content:</label>
                    <textarea wrap="hard" id="blog" name="blog" onChange={this.handleBlog.bind(this)} placeholder="What's on your mind..." required></textarea>
                    <label htmlFor="tags">Tag:</label>
                    <input type="text" name="tags" onChange={this.handleTags.bind(this)} placeholder="tag" required></input>
                    <input className="button" type="submit" value="Post"></input>
                    </div>
                </form>
                {this.state.errorMSG !== null ? <p>{this.state.errorMSG}</p> : null}
                {this.state.made === true ? <Redirect push to={`/post/${this.state.post_id}`}/> : null}
            </div>
        )
    }
}
