import React, {useEffect, useState} from 'react';
import axios from 'axios'
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Title from './Title';

const useStyles = makeStyles({

  background: '#B2BABB'   

  ,
  depositContext: {
    flex: 1,
  },
  
  poster: {
    width: '300px',
    height: '120px',
    borderRadius: '4px'
  }
});

export default function TopMovie() {
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
    <React.Fragment>
      <Title>Top Movie</Title>
      <Typography component="p" variant="h4">
        {/* <img className={classes.poster} src="https://images8.alphacoders.com/110/1106852.jpg" alt="img"/> */}
          <p>{data[data.length - 1]}</p>
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