import React, { Component } from 'react'

export default class Posts extends Component {
    render() {
        return (
            <div>
                <p>Posts page</p>
                <p>{this.props.food}</p>

            </div>
        )
    }
}
