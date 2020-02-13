import React, { Component } from 'react'
import axios from 'axios';
import Post from '../components/Post'
import Comments from './Comments'

export default class Posts extends Component {
    state = {
        hook: parseInt(this.props.hook),
        user_id: this.props.user_id,
        posts: [],
        tags: null,
        comments: null,
        category: null
    }

    getPosts() {
        axios.get(`http://localhost:5000/db/posts`)
          .then(res => {
            this.setState({posts: res.data})
          })
    }

    getTags() {
      axios.get(`http://localhost:5000/db/posts/tags`)
        .then(res => {
          this.setState({tags: res.data})
        })
    }

    getPostsWithFilter(category) {
        axios.get(`http://localhost:5000/db/posts?filter=${category}`)
          .then(res => {
            this.setState({posts: res.data})
          })
    }

    getPostsWithTag(tag) {
        axios.get(`http://localhost:5000/db/posts?tag=${tag}`)
          .then(res => {
            this.setState({posts: res.data})
          })
    }

    getUserPosts() {
        axios.get(`http://localhost:5000/db/posts?user_id=${this.state.hook}`)
          .then(res => {
            this.setState({posts: res.data})
          })
    }
    
    handleCategory (e) {
      this.getPostsWithFilter(e.target.value)
    }

    handleTag (e) {
      this.getPostsWithTag(e.target.value)
    }

    componentDidMount() {
        if(this.state.hook !== undefined && this.state.hook === this.state.user_id) {
            this.getUserPosts()
        } else {
            this.getPosts()
        }
        this.getTags()
    }

    render() {
        return (
            <div>
                <p>Posts page</p>
                
                <p>Search a Category</p>
                  <select onChange={this.handleCategory.bind(this)}>
                    <option value="pop">Popular</option>
                    <option value="unpop">Unpopular</option>
                    <option value="new">New</option>
                    <option value="old">Old</option>
                  </select>

                <p>Search a Category</p>
                {this.state.tags !== null ? 
                <select onChange={this.handleTag.bind(this)}>
                  <option value="">All</option>
                {this.state.tags.map((tag, index) => (
                    <option key={index} value={tag}>{tag}</option>
                ))}
                </select>
                : <p>loading categories...</p>}

                {this.state.posts.map((post, index) => (
                    <Post key={index} post={post} />
                ))}
                {/* <Comments /> */}
            </div>
        )
    }
}
