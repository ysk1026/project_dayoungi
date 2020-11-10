from flask_restful import Resource, reqparse
from flask import request
import json
from flask import jsonify
from com_dayoung_api.cop.rev.model.review_dao import ReviewDao
from com_dayoung_api.cop.mov.model.movie_dao import MovieDao

class ReviewTop(Resource):
    
    @staticmethod
    def get():
        print("Top Movie 진입")
        rank = ReviewDao.group_by_for_top()
        movie_top_by_review = max(rank, key=rank. get)
        print(movie_top_by_review)
        top_movie_info = MovieDao.find_by_title(movie_top_by_review)
        print('# * 30')
        return top_movie_info[0].json()
        