import React, {useEffect, useCallback, useState} from 'react'
import axios from 'axios'
import {User} from '../../templates'
import {useHistory } from "react-router-dom"
import { context as c } from '../../context'
const UserSearch = () => {
    const history = useHistory()
    const backToList = () => {
        history.push("./userlist")
    }

    const [data, setData] = useState([])
    
    const fetchOneUser = useCallback(async () => {
        const u_id = localStorage.getItem('user_id')
        try {
            console.log(`Search Id is ${u_id}`) 
            const req = {
                method: c.get,
                url: `${c.url}/api/user/${u_id}`,
                auth: c.auth
            }
            const res = await axios(req)  
            setData(res.data)
        } catch (error) {
            console.log(`Error ${error}`) 
            alert('failed')
        }
    }) // 혹시 안되면 ) 전에 [] 더할것
    useEffect(() => {fetchOneUser()},[])

    // useEffect(() => {
    //     axios.get(`http://localhost:8080/api/user/${u_id}`)
    //     .then(res=>{
    //         console.log(typeof(res.Data))
    //         setData(res.data) // database 안에 있는 데이터 res.data['lname'] 이런식으로 뽑을 수 있음
    //     })
    //     .catch( e => {alert(`Search failed`) })
    // },[])
    
    const search = e => {
        const u_id = document.getElementById('search').value
        localStorage.setItem("user_id", u_id)
        fetchOneUser()
        
    }
        

    return (<User>
        Search ID : <input type="text" id='search'/> 
        
        <button onClick={search}>search</button>
        <button onClick={backToList}>Show whole List</button>
        <table>
            <tr>
                <th>User ID</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Age</th>
                <th>Gender (M or F)</th>
            </tr>
            <tr>
                <th>{data['user_id']}</th>
                <th>{data['lname']}</th>
                <th>{data['fname']}</th>
                <th>{data['age']}</th>
                <th>{data['gender']}</th>
                
            </tr>
            
        </table>
    </User>)
}

export default UserSearch