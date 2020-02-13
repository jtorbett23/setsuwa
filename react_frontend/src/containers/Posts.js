import React, { Component } from 'react'
import axios from 'axios';
import Post from '../components/Post'

export default class Posts extends Component {
    state = {
        hook: parseInt(this.props.hook),
        user_id: this.props.user_id,
        posts: [],
        tags: null,
        tag: '',
        category: 'pop',
        comments: null,
    }

    getPosts(category, tag) {
        axios.get(`http://localhost:5000/db/posts?filter=${category}&tag=${tag}`)
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

    getUserPosts() {
        axios.get(`http://localhost:5000/db/posts?user_id=${this.state.hook}`)
          .then(res => {
            this.setState({posts: res.data})
          })
    }
    
    handleCategory (e) {
      this.setState({category: e.target.value})
      this.getPosts(e.target.value, this.state.tag)
    }

    handleTag (e) {
      this.setState({tag: e.target.value})
      this.getPosts(this.state.category, e.target.value)
    }

    handleTagetory (e) {
      console.log(e.target.value)
    }

    componentDidMount() {
        if(this.state.hook !== undefined && this.state.hook === this.state.user_id) {
            this.getUserPosts()
        } else {
            this.getPosts(this.state.category, this.state.tag)
            this.getTags()
        }
    }

    render() {
        return (
            <div>
                <p>{this.state.hook === this.state.user_id ? 'Your posts' : 'Posts'}</p>
                
                {this.state.hook !== undefined && this.state.hook === this.state.user_id ? null :
                <div>
                <p>Search a Category</p>
                  <select onChange={this.handleCategory.bind(this)}>
                    <option value="pop">Popular</option>
                    <option value="unpop">Unpopular</option>
                    <option value="new">New</option>
                    <option value="old">Old</option>
                  </select>

                <p>Search a Tag</p>
                {this.state.tags !== null ? 
                <select onChange={this.handleTag.bind(this)}>
                  <option value="">All</option>
                {this.state.tags.map((tag, index) => (
                    <option key={index} value={tag}>{tag}</option>
                ))}
                </select>
                : <p>loading categories...</p>}
                </div>}

                {this.state.posts.map((post, index) => (
                    <Post key={index} post={post} />
                ))}
            </div>
        )
    }
}
