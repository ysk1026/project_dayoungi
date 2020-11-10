import React, {useState} from 'react'
import axios from 'axios'
import { Movie } from '../../templates'
// movieid,movie_l_title,movie_l_org_title,movie_l_genres,movie_l_year,movie_l_rating,movie_l_rating_count
const MovieRegister = () => {
    const [title_kor, setTitle_kor] = useState('')
    const [title_naver_eng, setTitle_naver_eng] = useState('')
    const [genres_kor, setGenres_kor] = useState('')
    const [keyword_kor, setKeyword_kor] = useState('')
    const [running_time_kor, setRunning_time_kor] = useState('')
    const [year_kor, setYear_kor] = useState('')
    const [director_naver_kor, setDirector_naver_kor] = useState('')
    const [actor_naver_kor, setActor_naver_kor] = useState('')
    const [movie_l_rating, setMovie_l_rating] = useState('')
    const [movie_l_rating_count, setMovie_l_rating_count] = useState('')
    const [movie_l_popularity, setMovie_l_popularity] = useState('')
    const [link_naver, setLink_naver] = useState('')
    const [image_naver, setImage_naver] = useState('')

    const register = () => {
        axios.post(`http://127.0.0.1:8080/api/movie`,{
        'title_kor': title_kor, 
        'title_naver_eng': title_naver_eng, 
        'genres_kor': genres_kor, 
        'keyword_kor': keyword_kor, 
        'running_time_kor': running_time_kor, 
        'year_kor': year_kor, 
        'director_naver_kor': director_naver_kor, 
        'actor_naver_kor': actor_naver_kor, 
        'movie_l_rating': movie_l_rating, 
        'movie_l_rating_count': movie_l_rating_count, 
        'movie_l_popularity': movie_l_popularity, 
        'link_naver': link_naver, 
        'image_naver': image_naver})
        .then(res => {
            alert(`REGISTER SUCCESS`)
        })
        .catch(e => {
            alert(`REGISTER FAIL${e}`)    
        })

    }


    return (<Movie>
        <h1>MovieRegister</h1>
        <form>
            <table className='tab_layer'>
                <tr>
                    <td>TITLE</td>
                    <td><input type="text" onChange={e => setTitle_kor(e.target.value)}/></td>
                </tr>
                <tr>
                    <td>TITLE_ENG</td>
                    <td><input type="text" onChange={e => setTitle_naver_eng(e.target.value)}/></td>
                </tr>
                <tr>
                    <td>GENRES</td>
                    <td><input type="text" onChange={e => setGenres_kor(e.target.value)}/></td>
                </tr>
                <tr>
                    <td>KEYWORD</td>
                    <td><input type="text" onChange={e => setKeyword_kor(e.target.value)}/></td>
                </tr>
                <tr>
                    <td>RUNNIG TIME</td>
                    <td><input type="text" onChange={e => setRunning_time_kor(e.target.value)}/></td>
                </tr>
                <tr>
                    <td>YEAR</td>
                    <td><input type="text" onChange={e => setYear_kor(e.target.value)}/></td>
                </tr>
                <tr>
                    <td>DIRECTOR</td>
                    <td><input type="text" onChange={e => setDirector_naver_kor(e.target.value)}/></td>
                </tr>
                <tr>
                    <td>ACTOR</td>
                    <td><input type="text" onChange={e => setActor_naver_kor(e.target.value)}/></td>
                </tr>
                <tr>
                    <td>RATING</td>
                    <td><input type="text" onChange={e => setMovie_l_rating(e.target.value)}/></td>
                </tr>
                <tr>
                    <td>RATING COUNT</td>
                    <td><input type="text" onChange={e => setMovie_l_rating_count(e.target.value)}/></td>
                </tr>
                <tr>
                    <td>POPULARITY</td>
                    <td><input type="text" onChange={e => setMovie_l_popularity(e.target.value)}/></td>
                </tr>
                <tr>
                    <td>NAVER URL</td>
                    <td><input type="text" onChange={e => setLink_naver(e.target.value)}/></td>
                </tr>
                <tr>
                    <td>IMAGE URL</td>
                    <td><input type="text" onChange={e => setImage_naver(e.target.value)}/></td>
                </tr>
                
                <tr>
                    <td colspan={2}>
                        <button type="button" class="btn btn-sm btn-primary" id="btnSave" onClick={register}>REGISTER</button>
                        <button>CANCEL</button>
                    </td>
                </tr>
            </table>
        </form>
    </Movie>)
}

export default MovieRegister