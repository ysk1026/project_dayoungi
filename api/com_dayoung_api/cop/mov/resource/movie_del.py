from flask import request, jsonify
from flask_restful import Resource, reqparse

from com_dayoung_api.cop.mov.model.movie_dao import MovieDao
from com_dayoung_api.cop.mov.model.movie_dto import MovieDto
from com_dayoung_api.cop.mov.model.movie_dfo import MovieDf

class MovieDel(Resource):
    
    @staticmethod
    def post():
        print('*****')
        parser = reqparse.RequestParser()
        parser.add_argument('mov_id', type=str, required=True, help='This field should be a movieid')     
        args = parser.parse_args()
        print('*********')
        print(f'{args}')
        print('*********')
        movieid = args['mov_id']
        print(movieid)

        try:
            MovieDao.delete_movie(movieid)
            return{'code':0, 'message':'SUCCESS'}, 200
        except:
            return {'message':'An error occured registering the movie'}, 500