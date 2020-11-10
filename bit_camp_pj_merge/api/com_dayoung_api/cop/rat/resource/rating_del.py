from com_dayoung_api.cop.rat.model.rating_dao import RatingDao
from com_dayoung_api.cop.rat.model.rating_dto import RatingDto
from flask import request, jsonify
from flask_restful import Resource, reqparse

class RatingDel(Resource):
    
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('ratingid', type=int, required=True, help='This field should be a ratingid')
        args = parser.parse_args()
        print('*********')
        print(args)
        ratingid = args['ratingid']

        try:
            RatingDao.delete_rating(ratingid)
            return{'code':0, 'message':'SUCCESS'}, 200
        except:
            return {'message':'An error occured registering the movie'}, 500