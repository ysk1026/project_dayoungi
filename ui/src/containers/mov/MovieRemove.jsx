import React, {useState} from 'react'
import axios from 'axios'
import { Movie } from '../../templates'

const MovieRemove = () => {
    const [mov_id, setMovid] = useState('')


    const del = () => {
        alert(`DELETE MOVIE ID : ${mov_id}`)
        axios.post(`http://127.0.0.1:8080/api/movie-del`,{'mov_id':mov_id})
        .then(res => {
            alert(`DELETE SUCCESS`)
        })
        .catch(e => {
            alert(`DELETE FAIL ${e}`)
        })
    }

    return (<Movie>
        <h1>MovieRemove</h1>
        <form>
            <table className='tab_layer'>
                <tr>
                    <td>MOVIEID</td>
                    <td><input type="text" onChange={e => setMovid(e.target.value)}/></td>
                </tr>
                <tr>
                    <td colspan={2}>
                        <button type="button" class="btn btn-sm btn-primary" id="btnDelete" onClick={del}>DELETE</button>
                        <button>CANCEL</button>
                    </td>
                </tr>
            </table>
        </form>
    </Movie>)
}

export default MovieRemove