from flask_restful import Resource, reqparse
from flask import request
import json
from flask import jsonify
from com_dayoung_api.cop.rev.model.review_dao import ReviewDao

class ReviewScore(Resource):
    
    '''
    영화들을 리뷰 등록 갯수, 긍정 부정 점수로 평가하여
    상위 5개 영화를 보여준다.
    '''
    
    @staticmethod
    def get():
        print("진입")
        top_movies = ReviewDao.group_by() # 영화 = Key, 점수 = Value로 분류한 Dict를 받아옴.
        return top_movies