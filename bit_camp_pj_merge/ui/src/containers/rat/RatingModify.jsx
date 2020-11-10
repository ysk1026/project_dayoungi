import React, {useState} from 'react'
import {Rating} from '../../templates'
import axios from 'axios'

// movieid,title,subtitle,description,imageurl,year,rating
const RatingModify = () => {
    const [rat_id, setRatid] = useState('')
    const [rating, setRating] = useState('')

    const modify = () => {
        axios.put(`http://127.0.0.1:8080/api/rating`,{
        'rat_id': rat_id,
        'rating': rating})
        .then(res => {
            alert(`MODIFY SUCCESS`)
        })
        .catch(e => {
            alert(`MODIFY FAIL${e}`)    
        })

    }
    return (<Rating>
        <h1>RatingModify</h1>
        <form>
            <table className='tab_layer'>
                <tr>
                    <td>RATINGID</td>
                    <td><input type="text" onChange={e => setRatid(e.target.value)}/></td>
                </tr>
                <tr>
                    <td>RATING</td>
                    <td><input type="text" onChange={e => setRating(e.target.value)}/></td>
                </tr>
                <tr colspan={2}>
                    <button type="button" class="btn btn-sm btn-primary" id="btnModify" onClick={modify}>MODIFY</button>
                    <button>cancel</button>
                </tr>
           
            </table>
        </form>
    </Rating>)
}

export default RatingModify