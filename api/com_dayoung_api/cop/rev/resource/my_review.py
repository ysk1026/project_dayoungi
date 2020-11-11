from flask_restful import Resource, reqparse
from flask import request
import json
from flask import jsonify
from com_dayoung_api.cop.rev.model.review_dao import ReviewDao

class MyReview(Resource):
    
    '''
    리뷰 게시판에서 내가 작성한 리뷰들만을 관리하는 클래스 
    '''
    
    def get(self, user_id):
        print("나의 리뷰 찾기 진입!")
        print(f"User ID : {user_id}의 리뷰들를 불러오는 중 . . .")
        review = ReviewDao.find_review_by_user_id(user_id) # 받아온 User id에 해당하는 Row 전체를 불러온다.
        print(f"Review : {review}")
        print(f"Review type : {type(review)}")
        return review