import React, {useEffect, useState} from 'react';
import axios from 'axios'
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Title from './Title';
import {context as c} from '../../context'

const useStyles = makeStyles({

  background: '#B2BABB'   

  ,
  depositContext: {
    flex: 1,
  },
  
  poster: {
    width: '155px',
    height: '100px',
    borderRadius: '4px'
  },

  text: {
    fontSize: '18px'
  }
});

export default function TopMovie() {
  const classes = useStyles();
  const [data, setData] = useState([])
  useEffect(() => {
    axios.get('http://localhost:8080/api/reviewtop')
    .then (res => {
      // alert(res.data['Avengers'])
      // const newarray = Object.keys(res.data)
      setData(res.data)
      // console.log(newarray[newarray.length - 1])
    })
    .catch(e => {
      alert("Failed")
      throw(e)
    })
  }, [])

  return (
    <React.Fragment>
      <div style={{textAlign: "center"}}>  
      <Title>Top Movie</Title>
      </div>
      <Typography component="p" variant="h4" align="center">
        <img className={classes.poster} src={data['image_naver']} alt="img"/>
          <p className={classes.text}>{data['title_kor']}</p>
      </Typography>
      
      {/* <Typography color="textSecondary" className={classes.depositContext}>
        on 19 Oct, 2020
      </Typography> */}
      {/* <div> */}
        {/* <Link color="primary" href="#" onClick={preventDefault}>
          View all
        </Link> */}
      {/* </div> */}
    </React.Fragment>
  );
}