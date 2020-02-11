import React from 'react'
import {useParams} from 'react-router'
import SinglePost from './SinglePost'

export default function SinglePostHookContainer() {
    const {id} = useParams();
    let query = id;
    return (
        <div className="Search">
                <div> <SinglePost id={query} /> </div>
        </div>
    )
}