import React from 'react'
import {Link} from 'react-router-dom'

export const UserMenu = () => <nav>
    <ol>
        <li><Link to ='/userlogin'>User Login</Link></li>
        <li><Link to ='/userregister'>User register</Link></li>
        <li><Link to ='/userremove'>User remove</Link></li>
        <li><Link to ='/userupdate'>User update</Link></li>
        <li><Link to ='/userlist'>User List</Link></li>
        <li><Link to ='/usersearch'>User Search</Link></li>
        <li><Link to ='/userprofile'>User Profile</Link></li>

    </ol>
    
</nav>

export const RatingMenu = () => (<nav>
    <ol>
        <li><Link to='/rating-detail'>Movie Rating</Link></li>
        <li><Link to='/rating-register'>Movie Rating Register</Link></li>
        <li><Link to='/rating-list'>Movie Rating List</Link></li>
        <li><Link to='/rating-modify'>Movie Rating Modify</Link></li>
        <li><Link to='/rating-remove'>Movie Rating Remove</Link></li>
    </ol>
</nav>)

export const ActorMenu = () => <nav>
    <ol>
        <li><Link to = '/actorquiz'>Actor Quiz</Link></li>
        <li><Link to = '/actorquizsingle'>Actor Quiz Single</Link></li>

    </ol>

</nav>

export const MovieMenu = () => (<nav>
    <ol>
        <li><Link to='/movie-detail'>Movie</Link></li>
        <li><Link to='/movie-register'>Movie Register</Link></li>
        <li><Link to='/movie-list'>Movie List</Link></li>
        <li><Link to='/movie-modify'>Movie Modify</Link></li>
        <li><Link to='/movie-remove'>Movie Remove</Link></li>
    </ol>
</nav>)

export const ArticleMenu = () =>(<nav>
    <ol>
        <li><Link to='/article-write-form'>Writing Article Form</Link></li> 
        <li><Link to='/article-list'>Article List</Link></li> 
        <li><Link to='/edit-article'>Update Article Form</Link></li> 
        <li><Link to='/delete-article'>Delete Article Form</Link></li> 
    </ol>
</nav>)

export const ItemMenu = () => (<nav>
    <ol>
        <li><Link to='/item-list'>Item List</Link></li>
        <li><Link to='/register-item'>Register Item</Link></li>
        <li><Link to='/modify-item'>Modify Item</Link></li>
        <li><Link to='/remove-item'>Remove Item</Link></li>
    </ol>
</nav>)

export const AuthMenu = () => (<nav>
    <ol>
        <li><Link to='/signup-form'>Siginup Form</Link></li>
        <li><Link to='/signin-form'>Signin Form</Link></li>
    </ol>
</nav>)



