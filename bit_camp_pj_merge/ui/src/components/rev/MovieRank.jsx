import React, {useState, useEffect} from 'react';
import './rev.style.css'
import axios from 'axios';

export default function MovieRank() {
  const [data, setData] = useState([])
  useEffect(() => {
    axios.get('http://localhost:8080/api/reviewscore')
    .then (res => {
      // alert(res.data['Avengers'])
      const newarray = Object.keys(res.data)
      setData(newarray)
      console.log(newarray[newarray.length - 1])
    })
    .catch(e => {
      alert("Failed")
      throw(e)
    })
  }, [])
  return (
    <table className="size">
      <thead className = "spacing">
      <tr>
        <th>순위</th>
        <th className ="movietitle">영화명</th>
      </tr>
    </thead>
      <tr>
        <td><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r01.gif" alt="01" width="14" height="13"/></td>
        <td>{data[data.length - 1]}</td>
      </tr>
      <tr>
        <td><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r02.gif" alt="02" width="14" height="13"/></td>
        <td>{data[data.length - 2]}</td>
      </tr>
      <tr>
        <td><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r03.gif" alt="03" width="14" height="13"/></td>
        <td>{data[data.length - 3]}</td>
      </tr>
      <tr>
        <td><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r04.gif" alt="04" width="14" height="13"/></td>
        <td>{data[data.length - 4]}</td>
      </tr>
      <tr>
        <td><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r05.gif" alt="05" width="14" height="13"/></td>
        <td>{data[data.length - 5]}</td>
      </tr>
    </table>
  );
}