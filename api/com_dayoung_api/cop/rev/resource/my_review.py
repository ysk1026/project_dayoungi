from flask_restful import Resource, reqparse
from flask import request
import json
from flask import jsonify
from com_dayoung_api.cop.rev.model.review_dao import ReviewDao

class MyReview(Resource):
    
    def get(self, user_id):
        print("마이 리뷰 찾기 진입!")
        print(f"User ID : {user_id}의 리뷰들를 불러오는 중 . . .")
        review = ReviewDao.find_review_by_user_id(user_id)
        print(f"Review : {review}")
        print(f"Review type : {type(review)}")
        return review