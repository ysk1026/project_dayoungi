from flask_restful import Resource, reqparse
from flask import request
import json
from flask import jsonify
from com_dayoung_api.cop.rev.model.review_dao import ReviewDao

class ReviewSearch(Resource):
    
    '''
    리뷰 리스트내에서 검색 기능을 수행,
    특정 영화 제목을 입력하면 해당 영화에 대한 리뷰들만 보여준다.
    '''
    
    def get(self, movie_title):
        print("SEARCH 진입")
        print(f'제목 : {movie_title}') # 입력된 영화 제목        
        review = ReviewDao.find_by_movie_title(movie_title) # 데이터베이스 내에서 해당 영화 제목을 가지고 있는 모든 Row를 받아옴   
        return review
