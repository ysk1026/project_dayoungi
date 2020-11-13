from flask import request, jsonify
from flask_restful import Resource, reqparse

import pandas as pd

from com_dayoung_api.cop.mov.model.movie_dao import MovieDao
from com_dayoung_api.cop.mov.model.movie_dto import MovieDto
from com_dayoung_api.cop.mov.model.movie_ai import MovieAi


class MovieRecommendation(Resource):
    def __init__(self):
        self.movieai =  MovieAi()

    # def hook(self):
    #     ai = self.movieai
    #     recommendation_df = ai.hook()
    #     print(recommendation_df)
    #     recommendation_titles = recommendation_df['title']
    #     print(recommendation_titles)
    #     recommendation_mov_id = recommendation_df['id']
    #     print(recommendation_mov_id)

    def get(self, title_naver_eng):
        print("영화 추천")
        print(f'ID : {title_naver_eng}')

        ai = self.movieai
        recommendation_df = ai.hook(title_naver_eng)
        print(recommendation_df)
        recommendation_mov_id = recommendation_df['id']
        print(recommendation_mov_id)
        mov_id_list = recommendation_df['id'].tolist()
        print(mov_id_list)


        # a = MovieDao.find_by_id(mov_id_list[0])
        # print(a)
        # print(a.json())
        movie_list = []
        for i in mov_id_list:
            print(i)
            try:
                movie = MovieDao.find_by_id(i)
                movie_list.append(movie)
            except:
                print('없는 영화')
            if len(movie_list) >= 6:
                break

        movie_json_list = []
        for d in movie_list:
            movie_json_list.append(d.json())
        
        print('***** end *****')
        print(movie_json_list)

        return movie_json_list

# if __name__ == "__main__":
#     t = MovieRecommendation()
#     t.hook()