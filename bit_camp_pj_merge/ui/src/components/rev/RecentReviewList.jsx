import React, {useEffect, useState} from 'react';
import Link from '@material-ui/core/Link';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Title from './Title';
import axios from 'axios';
import './rev.style.css'
import {Emoji} from '../cmm'

const useStyles = makeStyles((theme) => ({
  seeMore: {
    marginTop: theme.spacing(3),
  },
}));

export default function RecentReviewList() {
  const classes = useStyles();
  const [data, setData] = useState([])
  useEffect(() => {
    axios.get('http://localhost:8080/api/reviews')
    .then(res=> {
      // console.log('loaded')
      setData(res.data.slice(-5))
    })
    .catch(e => {
      alert('Failed')
      throw(e)
    })
},[])
return (
  <React.Fragment>
    <Title>Recent Reviews</Title>
    <Table size="small" className = "tbsize">
      <TableHead>
        <TableRow>
          
          {/* <TableCell>ID</TableCell> */}
          <TableCell>영화</TableCell>
          <TableCell>리뷰 제목</TableCell>
          <TableCell align="right">평가</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {data.map((i, index) => (
          <TableRow key={index}>
            {/* <TableCell>{i.user_id}</TableCell> */}
            <TableCell>{i.movie_id}</TableCell>
            <TableCell>{i.title}</TableCell>
            <TableCell align="right">{((i.label == 1) ? <Emoji symbol="⭐️"/> : <Emoji symbol="❌"/>)}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
    <div className={classes.seeMore}>
      <Link className = "writereview" color="primary" href ="/write-review">
        리뷰 작성
      </Link>
      <Link className = "writereview" color="primary" href="/review-list">
        전체 리뷰 보기
      </Link>
    </div>
  </React.Fragment>
  );
}