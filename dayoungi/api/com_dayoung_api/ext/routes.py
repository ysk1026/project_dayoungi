import logging
from flask import Blueprint
from flask_restful import Api
from com_dayoung_api.usr.resource.user import User, Users, Delete
from com_dayoung_api.usr.resource.auth import Auth
from com_dayoung_api.usr.resource.access import Access

from com_dayoung_api.cop.act.resource.actor import Actor, Actors, AddActor

from com_dayoung_api.cop.cht.resource.chatbot import Chatbot

from com_dayoung_api.cop.mov.resource.movie import Movie, Movies
from com_dayoung_api.cop.mov.resource.search import MovieSearch
from com_dayoung_api.cop.mov.resource.movie_del import MovieDel
from com_dayoung_api.cop.mov.resource.recommendation import MovieRecommendation

from com_dayoung_api.cop.rev.resource.review import Review, Reviews
from com_dayoung_api.cop.rev.resource.my_review import MyReview
from com_dayoung_api.cop.rev.resource.score import ReviewScore
from com_dayoung_api.cop.rev.resource.search import ReviewSearch
from com_dayoung_api.cop.rev.resource.emotion import ReviewEmotion
from com_dayoung_api.cop.rev.resource.top import ReviewTop

############################## HOME ##############################
from com_dayoung_api.cop.hom.resource.home import Home
home = Blueprint('home', __name__, url_prefix='/api')
api = Api(home)
api.add_resource(Home, '/api')
############################## HOME ##############################

############################## USER ##############################
user = Blueprint('user', __name__, url_prefix='/api/user')
users = Blueprint('users', __name__, url_prefix='/api/users')
auth = Blueprint('auth', __name__, url_prefix='/api/auth')
access = Blueprint('access', __name__, url_prefix='/api/access')

api = Api(user)
api = Api(users)
api = Api(auth)
api = Api(access)
############################## USER ##############################

############################## ACTOR ##############################
actor = Blueprint('actor', __name__, url_prefix='/api/actor')
actors = Blueprint('actors', __name__, url_prefix='/api/actors')
delete = Blueprint('delete', __name__, url_prefix='/api/delete')
addActor = Blueprint('addActor', __name__, url_prefix='/api/addActor')

api = Api(actor)
api = Api(actors)
api = Api(delete)
api = Api(addActor)
############################## ACTOR ##############################

############################## CHATBOT ##############################
chatbot = Blueprint('chatbot', __name__, url_prefix='/api/chatbot')

api = Api(chatbot)
############################## CHATBOT ##############################

############################## MOVIE ##############################
movie = Blueprint('movie', __name__, url_prefix='/api/movie')
movies = Blueprint('movies', __name__, url_prefix='/api/movies')
movie_search = Blueprint('movie_search', __name__, url_prefix='/api/movie-search')
movie_del = Blueprint('movie_del', __name__, url_prefix='/api/movie-del')
movie_recommendation = Blueprint('movie_recommendation', __name__, url_prefix='/api/movie-recommendation')

api = Api(movie)
api = Api(movies)
api = Api(movie_search)
api = Api(movie_del)
api = Api(movie_recommendation)
############################## MOVIE ##############################

############################## REVIEW ##############################
review = Blueprint('review', __name__, url_prefix='/api/review')
reviews = Blueprint('reviews', __name__, url_prefix='/api/reviews')
myreview = Blueprint('myreview', __name__, url_prefix='/api/myreview')
reviewscore = Blueprint('reviewscore', __name__, url_prefix='/api/reviewscore')
reviewsearch = Blueprint('reviewsearch', __name__, url_prefix='/api/reviewsearch')
reviewemotion = Blueprint('reviewemotion', __name__, url_prefix='/api/reviewemotion')
reviewtop = Blueprint('reviewtop', __name__, url_prefix='/api/reviewtop')

api = Api(review)
api = Api(reviews)
api = Api(myreview)
api = Api(reviewscore)
api = Api(reviewsearch)
api = Api(reviewemotion)
api = Api(reviewtop)
############################## REVIEW ##############################

def initialize_routes(api):
    api.add_resource(Home, '/api')

############################## USER ##############################
    api.add_resource(User, '/api/user/<string:id>')
    api.add_resource(Users, '/api/users')
    api.add_resource(Auth, '/api/auth')
    api.add_resource(Access, '/api/access')
############################## USER ##############################

############################## ACTOR ##############################
    api.add_resource(Actor, '/api/actor/<string:id>')
    api.add_resource(AddActor, '/api/addActor/<string:name>')
    api.add_resource(Delete, '/api/delete/<string:id>')
    api.add_resource(Actors, '/api/actors')    
############################## ACTOR ##############################

############################## CHATBOT ############################
    api.add_resource(Chatbot, '/api/chatbot') 
############################## CHATBOT ############################

############################## MOVIE ##############################
    api.add_resource(Movie, '/api/movie','/api/movie/<string:title>') #  '/api/movie/<string:mov_id>', 
    api.add_resource(Movies, '/api/movies')
    api.add_resource(MovieSearch, '/api/movie-search/<string:title>')
    api.add_resource(MovieDel, '/api/movie-del')
    api.add_resource(MovieRecommendation, '/api/movie-recommendation/<string:title_naver_eng>')
############################## MOVIE ##############################

############################## REVIEW ##############################
    api.add_resource(Review, '/api/review', '/api/review/<string:id>')
    api.add_resource(Reviews, '/api/reviews')
    api.add_resource(MyReview, '/api/myreview/<string:user_id>')
    api.add_resource(ReviewScore, '/api/reviewscore')
    api.add_resource(ReviewSearch, '/api/reviewsearch/<string:movie_title>')
    api.add_resource(ReviewEmotion, '/api/reviewemotion/<string:content>')
    api.add_resource(ReviewTop, '/api/reviewtop')
############################## REVIEW ##############################