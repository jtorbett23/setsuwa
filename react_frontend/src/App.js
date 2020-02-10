import React, { Component } from 'react'
import Posts from './containers/posts'
import './static/css/App.css';

export default class App extends Component {
  state = {
    food: 'chicken'
  }
  render() {
    return (
      <div className="App">
        <h1>The app container</h1>
        <Posts food={this.state.food} />
      </div>
    )
  }
}
