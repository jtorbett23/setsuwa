import React, { Component } from 'react'
import axios from 'axios';
import Post from '../components/Post'
import Comments from './Comments'

export default class Posts extends Component {
    state = {
        hook: parseInt(this.props.hook),
        user_id: this.props.user_id,
        posts: [],
        comments: null,
        category: null
    }

    getPosts() {
        axios.get(`http://localhost:5000/db/posts`)
          .then(res => {
            this.setState({posts: res.data})
          })
    }

    getPostsWithFilter() {
        axios.get(`http://localhost:5000/db/posts?filter=${this.state.category}`)
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
        this.setState({category: e.target.value})
      }

    componentDidMount() {
        if(this.state.hook !== undefined && this.state.hook === this.state.user_id) {
            this.getUserPosts()
        } else {
            this.getPosts()
        }
    }
    componentDidUpdate() {
        this.getPostsWithFilter()
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
                {/* map through all the posts pass through */}
                {this.state.posts.map((post, index) => (
                    <Post key={index} post={post} />
                ))}
                {/* <Comments /> */}
            </div>
        )
    }
}
