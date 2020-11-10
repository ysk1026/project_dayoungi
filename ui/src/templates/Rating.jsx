import React from 'react'
import {RatingMenu as Menu} from '../components/cmm'
import './table.style.css'

const Rating = ({children}) => (<>
    <h1>Movie</h1>
    <Menu/>
    {children}
</>)

export default Rating


