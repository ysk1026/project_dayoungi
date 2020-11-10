import React , {useCallback, useEffect, useState} from 'react'
import axios from 'axios'
import {Rating} from '../../templates'
import {context as c} from '../../context'
import {useHistory} from 'react-router-dom'

export default function RatingList(){
    const history = useHistory()
    
    const [data, setData] = useState([])
    useEffect(() => {
        axios.get(`http://127.0.0.1:8080/api/ratings`)
        .then(res=>{
            setData(res.data)
        })
        .catch(e=>{
            alert(`List Failure`)
            throw(e)
        })

    },[])

    const fetchSomeRating = useCallback(async e=> {
        const ratingid = document.querySelector('#Ratingid').value
        alert(ratingid)
        try {
            const req = {
                method: c.get,
                url: `${c.url}/api/rating-search/${ratingid}`,
                auth: c.auth
            }
            const res = await axios(req)
            setData(res.data)
        } catch (error){
            alert(`The value could not be found. ${error}`)
        }
    },[])

    return (<Rating>

        <table>
          Search : <input type="text" id='Ratingid'/> 
          <button onClick={fetchSomeRating}>Search</button>

            <h1>Rating List</h1>
            <tr>
                <th>ratingid</th>
                <th>userid</th>
                <th>movieid</th>
                <th>rating</th>
            </tr>
            {data.map((i, index)=>(
                <tr key={index}>
                <td>{i.rat_id}</td>
                <td>{i.usr_id}</td>
                <td>{i.mov_id}</td>
                <td>{i.rating}</td>
            </tr>
            ))}
            
        </table>

    </Rating>)
}
