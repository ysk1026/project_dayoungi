import React, {useState} from 'react'
import axios from 'axios'
import { Rating } from '../../templates'

const RatingRegister = () => {
    const [usr_id, setUsrid] = useState('')
    const [mov_id, setMovid] = useState('')
    const [rating, setRating] = useState('')

    const register = () => {
        axios.post(`http://127.0.0.1:8080/api/rating`,{
        'usr_id': usr_id,
        'mov_id': mov_id, 
        'rating': rating})
        .then(res => {
            alert(`REGISTER SUCCESS`)
        })
        .catch(e => {
            alert(`REGISTER FAIL${e}`)    
        })

    }

    
    return (<Rating>
        <h1>RatingRegister</h1>
        <form>
            <table className='tab_layer'>
                <tr>
                    <td>USERID</td>
                    <td><input type="text" onChange={e => setUsrid(e.target.value)}/></td>
                </tr>
                <tr>
                    <td>MOVIEID</td>
                    <td><input type="text" onChange={e => setMovid(e.target.value)}/></td>
                </tr>
                <tr>
                    <td>RATING</td>
                    <td><input type="text" onChange={e => setRating(e.target.value)}/></td>
                </tr>
                <tr>
                    <td colspan={2}>
                        <button type="button" class="btn btn-sm btn-primary" id="btnSave" onClick={register}>REGISTER</button>
                        <button>CANCEL</button>
                    </td>
                </tr>
            </table>
        </form>
    </Rating>)
}

export default RatingRegister