import React, {useEffect,useCallback, useState} from 'react'
import axios from 'axios'
import {User} from '../../templates'
import {useHistory } from "react-router-dom"
import { context as c } from '../../context'


// useEffect 시작하면 바로 시작됨
const UserList = () => {
    const fetchAllUsers = useCallback(async () => {
        try{
            const req = {
                method: c.get, 
                url: `${c.url}/api/users`
            }
            const res = await axios(req)   
            setData(res.data)
        }catch(error){
            alert(`fetchAllUsers failure`)
            throw(error)
        }
    }) // 혹시 안되면 ) 전에 [] 더할것
    
    const [data, setData] = useState([])
    const history = useHistory()
    useEffect(() => {fetchAllUsers()},[]) 
    // useEffect(() => {
    //     axios.get('http://localhost:8080/api/users')
    //     .then(res=>{
    //         // alert(`list Success`)
    //         console.log(typeof(res.Data))
    //         setData(res.data) // database 안에 있는 데이터 res.data['lname'] 이런식으로 뽑을 수 있음
    //     })
    //     .catch(e =>{
    //         alert(`list Fail`)
    //         throw(e)
    //     } )
    // },[])
    const search = e => {
        const u_id = document.getElementById('search').value
        localStorage.setItem("user_id", u_id)
        history.push('/usersearch')
    }

    return (<User>
        Search ID : <input type="text" id='search'/> 
            <button onClick={search}>Search</button>
        <table>
            <tr>
                <th>User ID</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Age</th>
                <th>Gender (M or F)</th>
            </tr>
            {data.map((i, index)=>(
                <tr key={index}>
                    <td>{i.user_id}</td>
                    <td>{i.fname}</td>
                    <td>{i.lname}</td>
                    <td>{i.age}</td>
                    <td>{i.gender}</td>
                </tr>
            ))}
            
        </table>
    </User>)
}

export default UserList