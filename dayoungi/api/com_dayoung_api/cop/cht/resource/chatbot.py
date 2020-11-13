from flask_restful import Resource, reqparse
from flask import request
from com_dayoung_api.cop.act.model.actor_ai import ActorAi
import json
class Chatbot(Resource):
    @staticmethod
    def post():
        print("들어옴")
        ai = ActorAi()
        args = request.get_json()
        print(args)
        args = [args[i]['value'] for i in args.keys()]
        print(args)
        name = ai.train_actors(args)
        print(name)
        return name