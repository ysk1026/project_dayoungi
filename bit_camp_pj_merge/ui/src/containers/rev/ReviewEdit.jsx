import React, {useState, useEffect} from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import {Link} from 'react-router-dom'
import AppBar from '@material-ui/core/AppBar';
import Box from '@material-ui/core/Box';
import axios from 'axios';
import {Nav} from '../../components/cmm'
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import BorderColorIcon from '@material-ui/icons/BorderColor';
import {useHistory} from 'react-router-dom'

function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {'Copyright © '}
      <Link color="inherit" href="https://material-ui.com/">
        Your Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: '100%', // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

export default function ReviewEdit() {
 
  const [data, setData] = useState([])
  const [title, setTitle] = useState('')
  const [content, setContent] = useState('')
  const revId = localStorage.getItem("rev_id")
  const history = useHistory()
  
  useEffect(() => {
    alert("진입!")
    axios.get(`http://localhost:8080/api/review/${revId}`)
    .then(res => {
        setData(res.data)
        console.log(res.data)
    })
    .catch(e => {
        throw(e)
    })
  },[]) 

  const modify = () => {
    // alert(`Title: ${title}, UserId: ${userId}, Content: ${content}, ItemId: ${movieId}`)
    alert(`Title: ${title}, Content: ${content}`)
    axios.put(`http://localhost:8080/api/review/${revId}`,{'title':title, 'content': content})
    .then(res => {
        alert(`Update SUCCESS`)
    })
    .catch(
        e => {
            alert(`Writing ${e}`)
        }
    )

}

const del = () => {
    alert(`Review ID: ${revId}`)
    axios.delete(`http://localhost:8080/api/review/${revId}`, {'rev_id' : revId})
    .then(res => {
        alert('Delete SUCCESS')
    })
    .catch(err => {
        throw(err)
    })
}


  const classes = useStyles();
  
  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <AppBar position="absolute">
        <Nav></Nav>
      </AppBar>
      <div className={classes.paper} style={{margin:'100px 0'}}>
        <Avatar className={classes.avatar}>
          <BorderColorIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          리뷰 수정
        </Typography>
        <form className={classes.form} noValidate>
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            label={data['title']}
            onChange= {e => setTitle(e.target.value)}
          />
          <TextField
          id="outlined-multiline-static"
          label={data['content']}
          multiline
          required
          fullWidth
          rows={4}
          variant="outlined"
          onChange= {e => setContent(e.target.value)}
          />
        <div style={{display:'flex' , justifyContent: "center"}}>
          <div style={{display: 'inline-block', margin: '0 40px'}}>
          {/* <Button type="submit"
            variant="contained"
            color="primary"
            className={classes.submit}
            onClick={modify}
            href="review-list"> */}

                           {/* SAVE <Link href="review-list" class="btn btn-sm btn-primary" id="btnSave" onClick={modify}>Save</Link> */}
                  {/* </Button> */}
                  <button type="button">
                            <Link to="/review-list" class="btn btn-sm btn-primary" id="btnSave" onClick={modify}>Save</Link>
                        </button>
                  </div>
        <div style={{display: 'inline-block', margin: '0 40px'}}>
        {/* <Button
            type="submit"
            variant="contained"
            color="primary"
            className={classes.submit}
            onClick={del}
            href="review-list" */}
          {/* > */}
            {/* <Link href="review-list" class="btn btn-sm btn-primary" id="btnSave" onClick={del}>Delete</Link> */}
            {/* Delete
          </Button> */}
                                  <button type="button">
                            <Link to="/review-list" class="btn btn-sm btn-primary" id="btnSave" onClick={del}>Delete</Link>
                        </button>
        </div>
        </div>
        </form>
      </div>
      <Box mt={8}>
        <Copyright />
      </Box>
    </Container>
  );
}


