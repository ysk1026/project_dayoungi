import React, {useState} from 'react'
import {Rating} from '../../templates'
import axios from 'axios'
export default function RatingDetail() {
    const detail = e => {
        e.preventDefault()
        axios.get(`http:127.0.0.1:8080/movie/detail`)
        .then(

        )
        .error(
            
        )

    }
    return (<Rating>
        <h1>MovieDetail</h1>
        <form>
        <table className='tab_layer'>
            
                <tr>
                    <td>ID</td>
                    <td><input type="text"/></td>
                </tr>
                <tr>
                    <td>PASSWORD</td>
                    <td><input type="text"/></td>
                </tr>
                <tr>
                    <td>NAME</td>
                    <td><input type="text" /></td>
                </tr>
                <tr>
                    <td>PCLASS</td>
                    <td><input type="text"/></td>
                </tr>
                <tr>
                    <td>GENDER</td>
                    <td><input type="text" /></td>
                </tr>
                <tr>
                    <td>BIRTH YEAR</td>
                    <td><input type="text" /></td>
                </tr>
                <tr>
                    <td>EMBARKED</td>
                    <td><input type="text" /></td>
                </tr>
                <tr>
                    <td>RANK</td>
                    <td><input type="text" /></td>
                </tr>
                <tr>
                    <td colspan={2}><button onClick={detail}>Update Info</button>
                    <button>취소</button></td>
                </tr>
        </table></form>
    </Rating>)
}
