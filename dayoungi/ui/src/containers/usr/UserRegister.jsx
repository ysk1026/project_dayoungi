import React, {useState} from 'react'
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


const Copyright = () => {
    return (
      <Typography variant="body2" color="textSecondary" align="center">
        {'Copyright © '}
        <Link color="inherit" href="https://material-ui.com/">
          Your Website
        </Link>{' '}
        {new Date().getFullYear()}
        {'.'}
      </Typography>
    )
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
      marginTop: theme.spacing(3),
    },
    submit: {
      margin: theme.spacing(3, 0, 2),
    },
  }))
 

const UserRegister = () => {
    // const [userid, setUserid] = useState()
    const [password, setPassword] = useState()
    const [fname, setFname] = useState()
    const [lname, setLname] = useState()
    const [email, setEmail] = useState()
    const [age, setAge] = useState()
    const [gender, setGender] = useState()
    
    const classes = useStyles()

    const Register = e => {
        
        e.preventDefault()
        axios.post(`http://localhost:8080/api/auth`, {
            'usr_id':email, 'password':password,  'gender':gender, 'email':email, 'lname':lname, 'fname':fname, 'age':age,
        })
        .then(res=>{
            alert(`아이디 생성`)
            //setData(res.data)
            // console.log('Sign up Success 아이디가 생성 되셨습니다.')
        })
        .catch( e=> {
            alert(`아이디 생성 실패`)
            // console.log('Sign up Fail 아이디가 생성 되지 않았습니다.')
            throw(e)
        })
  }

    // const SignupButton = (e) => {
    //   e.preventDefault()
    //   alert(`fname: ${fname} lname: ${lname} email : ${email} age :${age} gender: ${gender}  password : ${password}`)
    // }
    // alert('회원가입 완료')
    return <>
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Avatar className={classes.avatar}>
          
        </Avatar>
        <Typography component="h1" variant="h5">
          Sign up
        </Typography>
        <form className={classes.form} noValidate>
          <Grid container spacing={2}>
          <Grid item xs={12} sm={6}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="lastName"
                label="Last Name"
                name="lastName"
                autoComplete="lname"
                onChange={e => {setLname(`${e.target.value}`)}}
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                autoComplete="fname"
                name="firstName"
                variant="outlined"
                required
                fullWidth
                id="firstName"
                label="First Name"
                autoFocus
                onChange={e => {setFname(`${e.target.value}`)}}
              />
            </Grid>

            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="email"
                label="Email"
                name="email"
                autoComplete="email"
                onChange={e => {setEmail(`${e.target.value}`)}}
              />
            </Grid>

            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                name="password"
                label="Password"
                type="password"
                id="password"
                autoComplete="current-password"
                onChange={e => {setPassword(`${e.target.value}`)}}
              />
            </Grid>

            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                name="gender"
                label="Gender" // 이게 화면에 보이는거임
                type="gender"
                id="gender"
                autoComplete="current-gender"
                onChange={e => {setGender(`${e.target.value}`)}}
              />
            </Grid>

            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                name="age"
                label="Age"
                type="age"
                id="age"
                autoComplete="current-age"
                onChange={e => {setAge(`${e.target.value}`)}}
              />
            </Grid>

            {/* <Grid item xs={12}>
              <FormControlLabel
                control={<Checkbox value="allowExtraEmails" color="primary" />}
                label="I want to receive inspiration, marketing promotions and updates via email."
              />
            </Grid> */}
          </Grid>
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
            onClick ={Register}
          >
            Sign Up Here
          </Button>
          <Grid container justify="flex-end">
            <Grid item>
              <Link href="UserLogin" variant="body2">
                Already have an account? Sign in
              </Link>
            </Grid>
          </Grid>
        </form>
      </div>
      <Box mt={5}>
        <Copyright />
      </Box>
    </Container>
    </>
}
export default UserRegister