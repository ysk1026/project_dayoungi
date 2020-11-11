from flask_restful import Resource, reqparse
from flask import request
import json
from flask import jsonify
from com_dayoung_api.cop.rev.model.review_dto import ReviewDto
from com_dayoung_api.cop.rev.model.review_dao import ReviewDao
from com_dayoung_api.cop.rev.model.review_ai import ReviewAi

class Review(Resource):
    
    '''
    리뷰 게시판의 가장 기본이 되는 CRUD 기능 구현 클래스
    RESTful 방식으로 POST / GET / PUT / DELETE 을 처리한다.  
    '''
    
    @staticmethod
    def post():
        print('Post 진입')

        # UI에서 전달된 정보들을 등록함
        parser = reqparse.RequestParser()
        parser.add_argument('usr_id', type =str, required =False, help ='This field cannot be left blank')
        parser.add_argument('mov_id', type =int, required =False, help ='This field cannot be left blank')
        parser.add_argument('title', type =str, required =False, help ='This field cannot be left blank')
        parser.add_argument('content', type =str, required =False, help ='This field cannot be left blank')
        args = parser.parse_args()

        # 학습된 모델을 통해 리뷰의 content의 긍정/부정 여부를 평가한다.
        ai = ReviewAi()
        if ai.predict_review(args.content) > 0.5:
            label = 1
        else:
            label = 0
        
        # 위 정보들을 통합하여 새롭게 등록할 리뷰 정보를 완성한다.     
        review = ReviewDto(args.title, args.content, label, args.usr_id, args.mov_id)
        print(f"Review: {review}")
        print('=======3======')

        try: 
            ReviewDao.save(review) # 리뷰를 데이터베이스에 저장
            return {'code' : 0, 'message' : 'SUCCESS'}, 200    
        except:
            return {'message': 'An error occured inserting the article'}, 500
    

    def get(self, id):
        print("Get 진입")
        print(id)
        review = ReviewDao.find_by_id(id) # 리뷰 데이터베이스의 Primary Key를 통해 해당 리뷰의 Row를 가져옴.
        print("Review 가져옴!")
        print(f'리뷰 정보: \n {review}')
        print(f'리뷰 타입 {type(review)}')
        print(f'제이슨 변환 이후: {review.json()}')
        
        return review.json()
        
    
    def put(self, id):
        print('Put 진입')
        
        # Update시 수정되는 title, content 정보를 받아와 등록함.
        parser = reqparse.RequestParser()
        parser.add_argument('title', type =str, required =False, help ='This field cannot be left blank')
        parser.add_argument('content', type =str, required =False, help ='This field cannot be left blank')
        args = parser.parse_args()
        print(args)
        
        # 바뀐 content 내용에 대한 긍정/부정 여부 재평가.
        ai = ReviewAi()
        if ai.predict_review(args.content) > 0.5:
            label = 1
        else:
            label = 0
            
        review = ReviewDao.find_by_id(id) # Primary Key로 수정하려는 리뷰의 Row를 불러옴.
        
        # 업데이트 된 title, content, label 등록
        review.title = args['title']
        review.content = args['content']
        review.label = label
        
        print('업데이트 된 리뷰', review)
        
        try: 
            ReviewDao.update(review, id) # 해당 리뷰를 데이터베이스에 업데이트
            return {'code' : 0, 'message' : 'SUCCESS'}, 200    
        except:
            return {'message': 'An error occured inserting the article'}, 500
    
    def delete(self, id):
        print('Delete 진입')
        review = ReviewDao.find_by_id(id) # Primary Key로 삭제하려는 리뷰의 Row를 불러옴.
        
        print('리뷰 아이디', review.rev_id)
        print('전체 리뷰', review)
        print('리뷰 타입', type(review))
        
        try:
            ReviewDao.delete(review.rev_id) # 해당 리뷰를 데이터베이스에서 삭제
            return{'code':0, 'message':'SUCCESS'}, 200
        except:
            return {'message':'An error occured registering the movie'}, 500

class Reviews(Resource):
    
    '''
    하나의 특정한 리뷰가 아닌 다수의 리뷰들을 관리 할 때 사용하는 클래스
    '''
    
    def get(self):    
        data = ReviewDao.find_all() # Review 데이터베이스에 저장된 전체 Rows를 불러들인다.
        return data, 200