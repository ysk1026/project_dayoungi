import React , {useCallback ,useEffect, useState} from 'react'
import axios from 'axios'
import {Movie} from '../../templates'
import {context as c} from '../../context'

export default function MovieList(){
    const [data, setData] = useState([])
    useEffect(() => {
        axios.get(`http://127.0.0.1:8080/api/movies`)
        .then(res=>{
            alert(`List Success`)
            setData(res.data)
        })
        .catch(e=>{
            alert(`List Failure`)
            throw(e)
        })

    },[])

    const fetchSomeMovie = useCallback(async e=> {
        const title = document.querySelector('#Title').value
        alert(title)
        try {
            const req = {
                method: c.get,
                url: `${c.url}/api/movie-search/${title}`,
                // data: {params: title},
                auth: c.auth


            }
            const res = await axios(req)
            setData(res.data)
        } catch (error){
            alert(`The value could not be found. ${error}`)
        }
    },[])

    return (<Movie>
  
        <table>
            <h1>Movie List</h1>
            제목 검색 : <input type="text" id='Title'/> 
            <button onClick={fetchSomeMovie}>Search</button>
            <tr>
                <th>movieid</th>
                <th>title_kor</th>
                <th>title_naver_eng</th>
                <th>genres_kor</th>
                <th>keyword_kor</th>
                <th>running_time_kor</th>
                <th>year_kor</th>
                <th>director_naver_kor</th>
                <th>actor_naver_kor</th>
                <th>movie_l_rating</th>
                <th>movie_l_rating_count</th>
                <th>movie_l_popularity</th>
                <th>link_naver</th>
                <th>image_naver</th>
            </tr>
            {data.map((i, index)=>(
                <tr key={index}>
                <td>{i.mov_id}</td>
                <td>{i.title_kor}</td>
                <td>{i.title_naver_eng}</td>
                <td>{i.genres_kor}</td>
                <td>{i.keyword_kor}</td>
                <td>{i.running_time_kor}</td>
                <td>{i.year_kor}</td>
                <td>{i.director_naver_kor}</td>
                <td>{i.actor_naver_kor}</td>
                <td>{i.movie_l_rating}</td>
                <td>{i.movie_l_rating_count}</td>
                <td>{i.movie_l_popularity}</td>
                <td>{i.link_naver}</td>
                <td>{i.image_naver}</td>
            </tr>
            ))}
            
        </table>

    </Movie>)
}
