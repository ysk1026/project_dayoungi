import React, {useEffect, useCallback, useState} from 'react'
import {useHistory } from "react-router-dom"
import { context as c } from '../../context'
import axios from 'axios'
import Avatar from '@material-ui/core/Avatar'
import Button from '@material-ui/core/Button'
import CssBaseline from '@material-ui/core/CssBaseline'
import TextField from '@material-ui/core/TextField'
// import FormControlLabel from '@material-ui/core/FormControlLabel'
// import Checkbox from '@material-ui/core/Checkbox'
import Link from '@material-ui/core/Link'
import Grid from '@material-ui/core/Grid'
import Box from '@material-ui/core/Box'
// import LockOutlinedIcon from '@material-ui/icons/LockOutlined'
import Typography from '@material-ui/core/Typography'
import { makeStyles } from '@material-ui/core/styles'
import Container from '@material-ui/core/Container'
  
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
    marginTop: theme.spacing(3),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}))


const UserProfile = () => {
  /*
  유저 정보를 보여주고 수정 할 수 있다.
  */
  const classes = useStyles()
  const [password, setPassword] = useState()
  const [fname, setFname] = useState()
  const [lname, setLname] = useState()
  const [age, setAge] = useState()
  const [gender, setGender] = useState()
  const edit = (id) => {
    // 수정을 가능 하게 만들어 준다.
    document.getElementById(id).disabled = false
  }

const [data, setData] = useState([])
const fetchOneUser = () => {
  /*
  로그인 된 유저 정보를 불러온다. 
  */
  const u_id = sessionStorage.getItem('sessionUser')
  axios.get(`http://localhost:8080/api/user/${u_id}`)
    .then(res=>{
      setFname(res.data['fname'])
      setAge(res.data['age'])
      setPassword(res.data['password'])
      setLname(res.data['lname'])
      // setEmail(res.data['email'])
      setAge(res.data['age'])
      setGender(res.data['gender'])
      setData(res.data)
    })
    .catch( e => {alert(`Search failed`) 
    }
  )
}

  useEffect(() => {fetchOneUser()},[])

  const editConfirm = e => {
    // 유저 정보를 수정한다
    e.preventDefault()
    const u_id = sessionStorage.getItem('sessionUser')
    axios.put(`http://localhost:8080/api/user/${u_id}`, {
        'user_id':u_id, 'password':password,  'gender':gender,  'lname':lname, 'fname':fname, 'age':age, 'email':u_id
    })
    .then(res=>{
        alert(`아이디 업데이트`)
        setData(res.data)
        // console.log('Sign up Success 아이디가 생성 되셨습니다.')
    })
    .catch( e=> {
        alert(`아이디 업데이트 실패`)
        // console.log('Sign up Fail 아이디가 생성 되지 않았습니다.')
        throw(e)
    })
}
  const history = useHistory()
  const deleteConfirm = useCallback(async () => {
    // 해당 유저를 삭제 한다
    const u_id = sessionStorage.getItem('sessionUser')
    try {
      const req = {
        method: c.post,
        url: `${c.url}/api/delete/${u_id}`,
        auth: c.auth
      }
      axios(req) 
      history.push('/')

    } catch (error) {
      console.log(`Error ${error}`) 
      alert('회원 탈퇴 실패')
    }
  })
  
  return (<>
    <Container component="main" >

      <CssBaseline />
      <div className={classes.paper}>
        <Avatar className={classes.avatar}>
          
        </Avatar>
        <Typography component="h1" variant="h5">
          회원정보
        </Typography>
        <form className={classes.form} noValidate>
          <Grid container spacing={3}>
          <Grid item xs={12} sm={5} >
            <h1>Last Name</h1>
          </Grid>
          <Grid item xs={12} sm={5}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="lastName"
                label={(data['lname'])}
                name="lastName"
                autoComplete="lname"
                onChange={e => {setLname(`${e.target.value}`)}}
                defaultValue = {(data['lname'])}
                disabled
              />
            </Grid>
            <Grid item xs={2}> 
              <Button variant="contained" color="primary" onClick = {e => edit("lastName")}>
                Edit
              </Button>
            </Grid>
              
            <Grid item xs={5}>
              <h1>First Name</h1>
            </Grid>
            <Grid item xs={5}>
              <TextField
                autoComplete="fname"
                name="firstName"
                variant="outlined"
                required
                fullWidth
                id="firstName"
                label= {data['fname']}
                autoFocus
                Defaultvalue = {(data['fname'])}
                onChange={e => {setFname(`${e.target.value}`)}}
                disabled
              />
            </Grid>
            <Grid item xs={2}> 
              <Button variant="contained" color="primary" onClick = {e => edit("firstName")}>
                Edit
              </Button>
            </Grid>
            <Grid item xs={12} sm ={5}>
              <h1>Email/ID</h1>
            </Grid>
            <Grid item xs={12} sm ={5}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="email"
                label={data['user_id']}
                name="email"
                autoComplete="email"
                // onChange={e => {setEmail(`${e.target.value}`)}}
                defaultValue = {(data['user_id'])}
                disabled
              />
            </Grid>
            <Grid item xs={2}> 
              <Button variant="contained" color="primary" onClick = {e => alert("You cannot change Email Address")}>
                Edit
              </Button>
            </Grid>

            <Grid item xs={12} sm ={5}>
              <h1>Password</h1>
            </Grid>

            <Grid item xs={12} sm ={5}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="password"
                label="Password"
                name="password"
                autoComplete="password"
                onChange={e => {setPassword(`${e.target.value}`)}}
                defaultValue = {data['password']}
                disabled
              />
            </Grid>
            <Grid item xs={2}> 
              <Button variant="contained" color="primary" onClick = {e => edit("password")}>
                Edit
              </Button>
            </Grid>

            <Grid item xs={5}>
              <h1>Gender</h1>
            </Grid>
            
            <Grid item xs={5}>
              <TextField
                variant="outlined"
                required
                fullWidth
                name="gender"
                label={(data['gender'])}
                type="gender"
                id="gender"
                autoComplete="current-gender"
                onChange={e => {setGender(`${e.target.value}`)}}
                DefaultValue = {(data['gender'])}
                disabled
              />
            </Grid>
            <Grid item xs={2}> 
              <Button variant="contained" color="primary" onClick = {e => edit("gender")}>
                Edit
              </Button>
            </Grid>

            <Grid item xs={5} >
              <h1>Age</h1>
            </Grid>
            <Grid item xs={5}>
              <TextField
                variant="outlined"
                required
                fullWidth
                name="age"
                label={(data['age'])}
                type="age"
                id="age"
                autoComplete="current-age"
                DefaultValue = {(data['age'])}
                onChange={e => {setAge(`${e.target.value}`)}}
                disabled
              />
            </Grid>
            <Grid item xs={2}> 
              <Button variant="contained" color="primary" onClick = {e => edit("age")}>
                Edit
              </Button>
            </Grid>
          </Grid>
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
            onClick ={editConfirm}
          >
            회원정보 수정
          </Button>
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
            onClick ={deleteConfirm}
          >
            회원 탈퇴
          </Button>
          <Grid container justify="flex-end">
            <Grid item>
              <Link href="/" variant="body2">
                Go back to Home
              </Link>
            </Grid>
          </Grid>
        </form>
      </div>
      <Box mt={5}>
      </Box>
    </Container>
  </>)
}
export default UserProfile