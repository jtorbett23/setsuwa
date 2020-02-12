import React from 'react'
import {useParams} from 'react-router'
import Posts from '../containers/Posts'

export default function PostsHookContainer(props) {
    const {id} = useParams();
    let query = id;
    return (
        <div className="Search">
                <div> <Posts hook={query} user_id={props.user_id}/> </div>
        </div>
    )
}