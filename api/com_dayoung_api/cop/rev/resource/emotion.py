from flask_restful import Resource, reqparse
from flask import request
import json
from flask import jsonify
from com_dayoung_api.cop.rev.model.review_dto import ReviewDto
from com_dayoung_api.cop.rev.model.review_dao import ReviewDao
from com_dayoung_api.cop.rev.model.review_ai import ReviewAi

class ReviewEmotion(Resource):
    
    '''
    리뷰 내용을 학습된 모델을 통해 분석하여 긍정 / 부정 여부를 평가한다.
    '''
    def get(self, content):
        print("감정 분석 진입!")
        print(f"리뷰 내용 : {content}")
        ai = ReviewAi()
        score = ai.predict_review(content) # 분석된 리뷰의 긍정 점수를 score로 받아옴.
        return score