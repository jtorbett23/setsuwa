import React from 'react'
import {useParams} from 'react-router'
import EditPost from '../components/EditPost'

export default function EditPostHookContainer(props) {
    const {id} = useParams();
    let query = id;
    return (
        <div className="Search">
                <div> <EditPost id={query} user_id={props.user_id}/> </div>
        </div>
    )
}