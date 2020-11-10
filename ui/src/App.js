import React, {useState} from 'react'
import { Nav } from './components/cmm'
import { BrowserRouter as Router, Route, Switch} from 'react-router-dom'
import { Home, User, Actor, Movie, Rating } from './templates'
import { UserLogin, UserRegister, UserList, UserSearch, UserProfile } from './containers/usr'
import { ActorQuiz, ActorQuizSingle } from './containers/act'
import { RatingDetail, RatingList, RatingModify, RatingRegister, RatingRemove } from './containers/rat'
import { MovieDetail, MovieList, MovieModify, MovieRegister, MovieRemove } from './containers/mov'
import { ReviewContainer, ReviewListContainer, MyReview, ReviewWrite, ReviewEdit } from './containers/rev'
import { Chatbot } from './containers/cht'

// react -> redux -> thunk -> saga -> Mobx
export default function App(){
  const [loggedIn, setLoggedIn] = useState(sessionStorage.getItem('sessionUser'))
  return (<>
  <Router>
    <Nav isAuth = {loggedIn}/>
    <Switch>
      <Route path='/home'component= {Home}/>
      <Route path='/user'component= {User}/>
      <Route path='/actor'component= {Actor}/>
      <Route path ='/userlogin' component={UserLogin}/>
      <Route path ='/userregister' component={UserRegister}/>
      <Route path='/userlist' component={UserList}/>
      <Route path='/usersearch' component={UserSearch}/>
      <Route path ='/actorquiz' component={ActorQuiz}/>
      <Route path ='/actorquizsingle' component={ActorQuizSingle}/>
      <Route path ='/userprofile' component={UserProfile}/>
      <Route path ='/chatbot' component={Chatbot}/>
      <Route path='/rating' component={Rating}/>
      <Route path='/rating-detail' component={RatingDetail}/>
      <Route path='/rating-register' component={RatingRegister}/>
      <Route path='/rating-list' component={RatingList}/>
      <Route path='/rating-modify' component={RatingModify}/>
      <Route path='/rating-remove' component={RatingRemove}/>                
      <Route path='/movie' component={Movie}/>
      <Route exact path='/' component={MovieDetail}/>
      <Route path='/movie-register' component={MovieRegister}/>
      <Route path='/movie-list' component={MovieList}/>
      <Route path='/movie-modify' component={MovieModify}/>
      <Route path='/movie-remove' component={MovieRemove}/>
      <Route path='/review-container' component={ReviewContainer}/>
      <Route path ='/review-list' component={ReviewListContainer}/>
      <Route path ='/my-review' component={MyReview}/>
      <Route path ='/write-review' component={ReviewWrite}/>
      <Route path ='/edit-review' component={ReviewEdit}/>
    </Switch>

  </Router>

</>)}