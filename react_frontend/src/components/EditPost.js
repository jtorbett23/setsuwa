import React, { Component } from 'react'
import axios from 'axios';
import { Redirect } from 'react-router-dom';

export default class EditPost extends Component {
    state = {
        user_id: this.props.user_id,
        post_id: this.props.id,
        title: null,
        content: null,
        tag: null,
        retreived: false,
        response: null,
        updated: false,
    }

    handleTitle (e) {
        this.setState({title: e.target.value})
    }
    handleBlog (e) {
        this.setState({content: e.target.value})
    }
    handleTags (e) {
        this.setState({tag: e.target.value})
    }

    getPost() {
        axios.get(`http://localhost:5000/db/post?post_id=${this.state.post_id}`)
          .then(res => {
            this.setState({title: res.data.title, content: res.data.content, tag: res.data.tag, response: res, retreived: true})
          })
    }

    updateThenRedirect(e) {
        e.preventDefault()
        axios.put(`http://localhost:5000/db/post?post_id=${this.state.post_id}&title=${this.state.title}&content=${this.state.content}&tag=${this.state.tag}`)
          .then(res => {
            this.setState({updated: true})
          })
    }

    componentDidMount() {
        this.getPost()
    }

    render() {
        return (
            <div>
                {this.state.retreived === true && this.state.response.data.user_id === this.state.user_id ? 
                <div>
                    
                    <form onSubmit={this.updateThenRedirect.bind(this)}>

                    <div className="createContainer">
                        <label htmlFor="title">Title:</label>
                        <input type="text" name="title" onChange={this.handleTitle.bind(this)} value={this.state.title} required></input>
                        <label htmlFor="blog">Content:</label>
                        <textarea wrap="hard" id="blog" name="blog" onChange={this.handleBlog.bind(this)} placeholder="What's on your mind..." required value={this.state.content}></textarea>
                        <label htmlFor="tags">Tag:</label>

                        <input type="text" name="tags" onChange={this.handleTags.bind(this)} value={this.state.tag} required></input>
                        <input type="submit" className="button" value="Update"></input>
                        </div>
                    </form>
                </div> : null}
                {this.state.updated === true ? <Redirect push to={`/post/${this.state.post_id}`}/> : null}
            </div>
        )
    }
}
