from flask_restful import Resource, reqparse
from flask import request
import json
from flask import jsonify
import pandas as pd
import numpy as np
import os
from com_dayoung_api.cop.rev.model.review_dfo import ReviewDfo 
from com_dayoung_api.cop.rev.model.review_dto import ReviewDto
from com_dayoung_api.cop.mov.model.movie_dao import MovieDao
from com_dayoung_api.cop.mov.model.movie_dto import MovieDto, MovieVo
from com_dayoung_api.usr.model.user_dto import UserDto
from com_dayoung_api.ext.db import db, openSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import func

class ReviewDao(ReviewDto):
    
    '''
    Review Database내의 데이터에 접근하여 관리하는 클래스
    데이터들에 대한 조작을 담당함
    '''
    
    @classmethod
    def count(cls):
        Session = openSession()
        session = Session()
        return session.query(func.count(ReviewDto.rev_id)).one() # 테이블내의 총 Row 개수 반환
    
    @classmethod
    def group_by(cls):
        Session = openSession()
        session = Session()
        print("그룹 바이 진입!!!")
        titles = session.query(cls, MovieDto.title_kor).filter(cls.mov_id.like(MovieDto.mov_id)).all()
        titledict = {} # 타이틀 뽑아 왔음
        for title in titles:
            print('왜 안돼?', titledict[title-2])
            if title[-1] not in titledict:
                titledict[title[-1]] = 1
            else:
                titledict[title[-1]] += 1
            if title[-2] == 1:
                titledict[title[-1]] += 1
        session.close()
        titledict = {k: v for k, v in sorted(titledict.items(), key=lambda item: item[1])}
        print(f'Sorting 이후 : {titledict}')
        # max_key = max(titledict, key=titledict. get)
        # print(f'Max key : {max_key}')
        return titledict
    
    @classmethod
    def group_by_for_top(cls):
        Session = openSession()
        session = Session()
        print("그룹 바이 for top 진입!!!")
        titles = session.query(cls, MovieDto.title_kor).filter(cls.mov_id.like(MovieDto.mov_id)).all()
        titledict = {} # 타이틀 뽑아 왔음
        for title in titles:
            if title[-1] not in titledict:
                titledict[title[-1]] = 1
            else:
                titledict[title[-1]] += 1
            if title[-2] == 1:
                titledict[title[-1]] += 1
        session.close()
        titledict = {k: v for k, v in sorted(titledict.items(), key=lambda item: item[1])}
        print(f'Sorting 이후 : {titledict}')
        # max_key = max(titledict, key=titledict. get)
        # print(f'Max key : {max_key}')
        return titledict
                
    @classmethod
    def find_all(cls):
        Session = openSession()
        session = Session()
        newtables = session.query(ReviewDto, MovieDto.title_kor, UserDto.fname).filter(UserDto.usr_id.like(ReviewDto.usr_id))\
            .filter(ReviewDto.mov_id.like(MovieDto.mov_id))
        df = pd.read_sql(newtables.statement, newtables.session.bind)
        print(df)
        return json.loads(df.to_json(orient='records'))
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name == name)
    
    @classmethod
    def find_by_id(cls, id):
        Session = openSession()
        session = Session()
        print("FIND BY ID method 진입!")
        print(f'ID : {id}')

        return session.query(ReviewDto).filter(ReviewDto.rev_id.like(id)).one()
    
    @classmethod
    def find_review_by_user_id(cls, user_id):
        Session = openSession()
        session = Session()
        print("FIND BY USER ID METHOD 진입!")
        print ("성공")

        # 기존 Reviews table에 movies.title_kor / UserDto.fname을 조인해서 SQLAlchemy 자체로 가져옴
        newtables = session.query(ReviewDto, MovieDto.title_kor, UserDto.fname).filter(ReviewDto.usr_id.like(user_id))\
            .filter(ReviewDto.usr_id.like(UserDto.usr_id)).filter(ReviewDto.mov_id.like(MovieDto.mov_id))
        # 해당 Query를 DataFrame으로 전환
        df = pd.read_sql(newtables.statement, newtables.session.bind)
        print(df)
        return json.loads(df.to_json(orient='records'))

    
    @classmethod
    def find_by_movie_title(cls, movie_title):
        print("FIND BY MOVIE TITLE 진입 !")
        Session = openSession()
        session = Session()
        mov_id = MovieDao.find_by_title_return_id(movie_title)
        newtables = session.query(cls, MovieDto.title_kor, UserDto.fname).filter(MovieDto.mov_id.like(mov_id))\
            .filter(cls.mov_id.like(mov_id)).filter(cls.usr_id.like(UserDto.usr_id))
        df = pd.read_sql(newtables.statement, newtables.session.bind)
        print(df)
        return json.loads(df.to_json(orient='records'))
        # return session.query(ReviewDto).filter(ReviewDto.title.like(title)).all()
    
    @staticmethod
    def save(review):
        Session = openSession()
        session = Session()
        print('SAVE 진입')
        print(f'REVIEW: {review}')
        print(f'Rev id : {review.rev_id} / Movie_id :{review.mov_id}/\
            User_id: {review.usr_id}/ Title: {review.title}/ Content: {review.content} / Label: {review.label}')
        print('1 clear')
        session.add(review)
        print('2 clear')
        session.commit()
        print('3 clear')
        session.close()
        print('4 clear')
    
    @staticmethod
    def update(review, id):
        Session = openSession()
        session = Session()
        print('진입')
        print(f'Rev id : {review.rev_id} / Movie_id :{review.mov_id}/\
            User_id: {review.usr_id}/ Title: {review.title}/ Content: {review.content} / Label: {review.label}')
        print('update 1 clear')
        print(f'************ID : {id} **************** ')
        print('update 2 clear')
        session.query(ReviewDto).filter(ReviewDto.rev_id == review.rev_id).update({ReviewDto.usr_id:review.usr_id,
                                                                                   ReviewDto.mov_id:review.mov_id,
                                                                                   ReviewDto.title:review.title,
                                                                                   ReviewDto.content:review.content,
                                                                                   ReviewDto.label:review.label
                                                                                   })
        print('update 3 clear')
        session.commit()
        session.close()
        print('update 4 clear')
    
    @staticmethod   
    def insert_many():
        service = ReviewDfo()
        Session = openSession()
        session = Session()
        df = service.hook()
        print(df.head())
        session.bulk_insert_mappings(ReviewDto, df.to_dict(orient="records"))
        session.commit()
        session.close()          
        
    @classmethod
    def delete(cls,rev_id):
        print('##### review data delete #####')
        print(rev_id)
        data = cls.query.get(rev_id)
        print(f'###### review data: {data}')
        db.session.delete(data)
        print("Delete in progress")
        db.session.commit()
        print('##### review data delete complete #####')