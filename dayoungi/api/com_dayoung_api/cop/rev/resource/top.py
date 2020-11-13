from flask_restful import Resource, reqparse
from flask import request
import json
from flask import jsonify
from com_dayoung_api.cop.rev.model.review_dao import ReviewDao
from com_dayoung_api.cop.mov.model.movie_dao import MovieDao


class ReviewTop(Resource):
    
    '''
    영화들을 리뷰 등록 갯수, 긍정 부정 점수로 평가하여
    가장 높은 점수를 보유한 영화 정보를 Return 한다.
    '''
     
    @staticmethod
    def get():
        print("Top Movie 진입")
        rank = ReviewDao.group_by_for_top() # 영화 = Key, 점수 = Value로 분류한 Dict를 받아옴.
        movie_top_by_review = max(rank, key=rank. get) # Dict내 Value 점수가 가장 높은 영화 찾기.
        print(movie_top_by_review)
        top_movie_info = MovieDao.find_by_title(movie_top_by_review) # 해당 영화의 정보를 받아옴
        print('# * 30')
        return top_movie_info[0].json() # 해당 정보가 리스트에 담겨 있어 인덱싱으로 꺼내온 후 json화하여 리턴한다.
        