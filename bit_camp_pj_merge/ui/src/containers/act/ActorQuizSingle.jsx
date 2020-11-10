import React, {useEffect, useState} from 'react'
import axios from 'axios'
import {useHistory} from "react-router-dom"

import AppBar from '@material-ui/core/AppBar'
import Button from '@material-ui/core/Button'
import CameraIcon from '@material-ui/icons/PhotoCamera'
import Card from '@material-ui/core/Card'
import CardActions from '@material-ui/core/CardActions'
import CardContent from '@material-ui/core/CardContent'
import CardMedia from '@material-ui/core/CardMedia'
import CssBaseline from '@material-ui/core/CssBaseline'
import Grid from '@material-ui/core/Grid'
import Toolbar from '@material-ui/core/Toolbar'
import Typography from '@material-ui/core/Typography'
import { makeStyles } from '@material-ui/core/styles'
import Container from '@material-ui/core/Container'
import Link from '@material-ui/core/Link'
// import Link from 'react-router-dom'
import Chatbot from '../cht/Chatbot'

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
  )
}

const useStyles = makeStyles((theme) => ({
  icon: {
    marginRight: theme.spacing(2),
  },
  heroContent: {
    backgroundColor: theme.palette.background.paper,
    padding: theme.spacing(8, 0, 6),
  },
  heroButtons: {
    marginTop: theme.spacing(4),
  },
  cardGrid: {
    paddingTop: theme.spacing(8),
    paddingBottom: theme.spacing(8),
  },
  card: {
    height: '100%',
    display: 'flex',
    flexDirection: 'column',
  },
  cardMedia: {
    paddingTop: '150%', // 16:9
    
  },
  cardContent: {
    flexGrow: 1,
    height:"250px",
    width:"223px"
  },
  footer: {
    backgroundColor: theme.palette.background.paper,
    padding: theme.spacing(6),
  },
}))


export default function ActorQuizSingle() {
  /*
  선택한 배우의 스무고개를 시작한다.
  */
  const history = useHistory()
  const backToList = () => {
    // 기존의 모든 배우를 볼 수 있는 화면으로 돌아간다
    history.push("./actorquiz")
  }
  const classes = useStyles()
  const [data, setData] = useState([])
  
  useEffect(() => {showActor()},[])
  const showActor = () => {
    /*
    스무고개를 시작할 배우를 보여준다.
    */
    const one_id = localStorage.getItem('act_id')
    axios.get(`http://localhost:8080/api/actor/${one_id}`)
    .then(res=>{
        setData(res.data)
    })
    .catch(e =>{
        alert(`list Fail`)
        throw(e)
    } )
  } 

  return (
    <React.Fragment>
      <CssBaseline />
      <AppBar position="relative">
        <Toolbar>
          <CameraIcon className={classes.icon} />
          <Typography variant="h6" color="inherit" noWrap>
            스무고개
          </Typography>
        </Toolbar>
      </AppBar>
      <main>
        {/* Hero unit */}
        <div className={classes.heroContent}>
          <Container maxWidth="sm">
            <Typography component="h1" variant="h2" align="center" color="textPrimary" gutterBottom>
              배우 스무고개
            </Typography>  
          </Container>
        </div>
        <Container className={classes.cardGrid} maxWidth="md"> 
          {/* End hero unit */}
          
          <Grid className = "helloooooooooooooooooooooo" container spacing={5}>
              <Grid item xs={12} sm={4}>
                <Card className="아무거나" >
                  <Link href= '/'>
                  <CardMedia
                    className={classes.cardMedia}
                    image= {data['photo_url']}
                    title= {data['name']}
                  />
                </Link>
                  <CardContent className={classes.cardContent}>
                    <Typography gutterBottom variant="h5" component="h2">
                      {data['name']}
                    </Typography>
                    <Typography>
                      나이 {data['age']}
                    </Typography>
                    <Typography>
                      본명 {data['real_name']}
                    </Typography>
                    <Typography>
                      종교 {data['religion']}
                    </Typography>
                    <Typography>
                      소속사 {data['agency']}
                    </Typography>
                    <Typography>
                      자녀 {data['children']}
                    </Typography>
                    <Typography>
                      데뷔년도 {data['debut_year']}
                    </Typography>
                  </CardContent>
                  
                  <CardActions>
                    <Button size="small" color="primary">
                      게임 시작
                    </Button>
                    <Button size="small" color="primary" onClick={backToList}>
                      돌아가기
                    </Button>
                  </CardActions>
                </Card>
              </Grid>
              <Grid item xs={12} sm={8}  > 
                {/* style={{"border": "1px solid black"}} */}
                {/* 여기 chatbot 들어갈 거임 */}
                <Chatbot/>
                {/* <Chatbot/> */}
              </Grid>
          </Grid>


        </Container>
      </main>
      {/* Footer */}
      <footer className={classes.footer}>
        <Typography variant="h6" align="center" gutterBottom>
          Footer
        </Typography>
        <Typography variant="subtitle1" align="center" color="textSecondary" component="p">
          Something here to give the footer a purpose!
        </Typography>
        <Copyright />
      </footer>
      {/* End footer */}
    </React.Fragment>
  )
}