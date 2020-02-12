import React from 'react'
import {useParams} from 'react-router'
import SinglePost from './SinglePost'

export default function SinglePostHookContainer(props) {
    const {id} = useParams();
    let query = id;
    return (
        <div className="Search">
                <div> <SinglePost id={query} user_id={props.user_id}/> </div>
        </div>
    )
}