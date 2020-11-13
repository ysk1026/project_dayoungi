import React from 'react'
import {Link} from 'react-router-dom'
import dayoungi from './dayoungi.png'
import axios from 'axios'
import Button from '@material-ui/core/Button';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
    container: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        marginTop: theme.spacing(3)
    },

    link: {
        fontsize: '1 rem',
        fontWeight: 'bold',
        textDecoration: 'none',
        color: 'white'
      },

    button: {
        backgroundColor: 'Transparent',
        border: 'none',
        cursor:'pointer'
    },

    imges: {
        display: 'block',
        height: '350px',
    }
  }));

export default function Home(){ 
    const classes = useStyles()
    
    return(<>
            {/* <div style={{width: '100%', height: '100%'}}> */}
           <div className={classes.container} style = {{marginTop: '210px'}}>
            <button className={classes.button}>
                <Link to="/movie-detail">
            <img className={classes.imges} src={dayoungi} alt="dayoungi"/>      
                </Link>
            </button>
            </div>  
            <div className={classes.container} style={{marginTop: '60px'}}>
            <Button variant="contained" color="secondary" style={{marginRight: '15px'}}>
          <Link to="/userregister" className={classes.link}>Sign up</Link>
        </Button>
        <Button variant="contained" color="secondary" style={{marginLeft: '15px'}}>
          <Link to="/userlogin" className={classes.link}>Sign in</Link>
        </Button>
            {/* <h1>다영이</h1> */}
            </div>
            {/* </div> */}
                    </>)
            
}
