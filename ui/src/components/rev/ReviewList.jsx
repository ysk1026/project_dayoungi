import React, {useEffect, useState, useCallback} from 'react';
import {Link} from 'react-router-dom';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Title from './Title';
import axios from 'axios';
import {context as c} from '../../context'
import './rev.style.css'
import {Emoji} from '../cmm'

const useStyles = makeStyles((theme) => ({
  seeMore: {
    marginTop: theme.spacing(3),
  },
}));

export default function EntireList() {
  const classes = useStyles();
  const [data, setData] = useState([])
  useEffect(() => {
    axios.get('http://localhost:8080/api/reviews')
    .then(res=> {
      // console.log('loaded')
      setData(res.data)
    })
    .catch(e => {
      alert('Failed')
      throw(e)
    })
},[])

const fetchSomeReview = useCallback(async e=> {
  alert("진입")
  const title = document.querySelector('#movieTitle').value
  alert(title)
  try {
      const req = {
          method: c.get,
          url: `${c.url}/api/reviewsearch${title}`,
          // data: {params: title},
          auth: c.auth

      }
      const res = await axios(req)
      alert(res.rev_id)
      setData(res.data)
  } catch (error){
      alert(`fetchSomeReviews failure ${error}`)
  }
},[])

const userId = e => {
  // const revId = e.target.getAttribute('rev-id')
  // console.log(revId)
  localStorage.setItem("user_id", '10');
  // alert()
}
  return (
    <React.Fragment>
      <Title>Reviews</Title>
      <div>
      <input type="text" id='movieTitle' placeholder ="Type Movie"/> 
            <button onClick={fetchSomeReview}>Search</button>

            <Link className ="myList" color="primary" to="/my-review" onClick={userId}>
            나의 리뷰 모음
            </Link>

            </div>      
      <Table size="small" className = "tbsize">
        <TableHead>
          <TableRow>
            
            <TableCell>ID</TableCell>
            <TableCell>영화</TableCell>
            <TableCell>리뷰 제목</TableCell>
            <TableCell>리뷰 내용</TableCell>
            <TableCell>평가</TableCell>

          </TableRow>
        </TableHead>
        <TableBody>
          {data.map((i, index) => (
            <TableRow key={index}>
              <TableCell>{i.usr_id}</TableCell>
              <TableCell>{i.mov_id}</TableCell>
              <TableCell>{i.title}</TableCell>
              <TableCell>{i.content}</TableCell>
              <TableCell>{((i.label == 1) ? <Emoji symbol="⭐️"/> : <Emoji symbol="❌"/>)}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      <div className={classes.seeMore}>
        <Link className = "writereview" color="primary" to="/write-review">
          리뷰 작성
        </Link>
      </div>
    </React.Fragment>
  );
}