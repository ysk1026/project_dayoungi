from typing import List
import json
import pandas as pd
import os
import sys
import urllib.request
import csv
import ast
import time
from pandas import DataFrame
from pathlib import Path
from com_dayoung_api.cmm.util.file_helper import FileReader, FileChecker

class MovieDfo:
    '''
    kmdb_naver_search\saved_data\naver_movie_search_merge.csv
    resources\data\movie_lens\movies_metadata.csv
                             \credits.csv
                             \keyword.csv
    위 의 파일 불러와 합치기
    movielens.csv = movies_metadata.csv - credits.csv - keyword.csv => id 기준으로 합치기 (나머지 드랍)
    movielens_kmdb.csv = movielens.csv - naver_movie_search_merge.csv => title - eng_title 기준으로 합치기 ?

    데이터 처리 한것 들 적기!!!
    -. naver_movie_search_merge.csv
    >
    >
    >

    -. keyword.csv
    >
    >
    >

    '''

    def __init__(self):
        self.fileReader = FileReader()
        self.filechecker = FileChecker()
        self.path = os.path.abspath("")

    def hook(self):
        print('***** 무비 렌즈 UI용 DF가공 시작 *****')

        movie_lens_meta_df = self.read_movie_lens_meta_csv()
        kmdb_naver_df = self.read_kmdb_naver_csv()

        arrange_movie_lens_meta_df = self.arrange_movie_lens_meta_df(movie_lens_meta_df)
        arrange_kmdb_naver_df = self.arrange_kmdb_naver_df(kmdb_naver_df)

        merge_movie_lens_kmdb_naver_df = self.merge_movie_lens_kmdb_naver_df(arrange_movie_lens_meta_df, arrange_kmdb_naver_df)
        
        print('***** 무비 렌즈 UI용 DF가공 완료 *****')

        return merge_movie_lens_kmdb_naver_df

    def read_movie_lens_meta_csv(self):
        print('***** 무비렌즈 메타 데이터 읽기*****')
        path = os.path.abspath('')
        fname = '\com_dayoung_api\cop\mov\model\data\movies_metadata.csv'
        # path = os.path.abspath("")
        # fname = '\data\movie_lens\movies_metadata.csv'
        movie_lens_meta_df = pd.read_csv(path + fname, encoding='utf-8')
        print('***** 무비렌즈 메타 데이터 읽기 완료*****')
        return movie_lens_meta_df

    def read_kmdb_naver_csv(self):
        print('***** kmdb 네이버 데이터 읽기*****')
        path = os.path.abspath("")
        fname = '\com_dayoung_api\cop\mov\model\data\kmdb_naver_merge.csv'
        # path = os.path.abspath("")
        # fname = '\data\\kmdb_naver_merge.csv' 
        kmdb_naver_df = pd.read_csv(path + fname, encoding='utf-8')
        print('***** kmdb 네이버 데이터 읽기 완료*****')
        return kmdb_naver_df

    def arrange_movie_lens_meta_df(self, movie_lens_meta_df):
        print('***** 무비렌즈 메타 데이터 가공 *****')
        fchecker = self.filechecker


        '''
        [original columns]
        adult,
        belongs_to_collection,
        budget,
        genres,
        homepage,
        id,
        imdb_id,
        original_language,
        original_title,
        overview,
        popularity,
        poster_path,
        production_companies,
        production_countries,
        release_date,
        revenue,
        runtime,
        spoken_languages,
        status,
        tagline,
        title,
        video,
        vote_average,
        vote_count
        '''
        ##### 필요없는 column 삭제 #####
        '''
        [drop columns]
        genres,
        id,
        original_title,
        overview,
        popularity,
        release_date,
        tagline,
        title,
        vote_average,
        vote_count

        [한글 열 샘플]
        type                org_columns         한글 열                   sample - by toystory

        str(list in dict)   genres,             장르                      [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
        str                 id,                 아이디                    862
        str                 original_title,     원문 제목(각 나라 언어)    Toy Story
        str                 overview,           줄거리                    Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.
        str                 popularity,         인기도                    21.946943
        str                 release_date,       날짜                      1995-10-30
        str                 tagline,            한 줄 카피                Roll the dice and unleash the excitement! (주만지 꺼 토이스토리는 없음)
        str                 title,              영어 제목                 Toy Story
        float               vote_average,       별점 평균                 7.7
        int                 vote_count          별점 투표 갯수            5415
        '''
        drop_df = movie_lens_meta_df.drop(['adult',
                                    'belongs_to_collection',
                                    'budget',
                                    'homepage',
                                    'imdb_id',
                                    'original_language',
                                    'poster_path',
                                    'production_companies',
                                    'production_countries',
                                    'revenue',
                                    'runtime',
                                    'spoken_languages',
                                    'status',
                                    'video'], axis=1)
        # print(drop_df.columns)
        # print(drop_df)
        ##### 필요없는 column 삭제 #####

        ##### null 값 대체 #####

        # filechecker.df_null_check(drop_df)
        '''
        genres                    : null count =      0
        id                        : null count =      0
        original_title            : null count =      0
        overview                  : null count =    954 -> null_vlaue 대체
        popularity                : null count =      5 -> null_vlaue 대체
        release_date              : null count =     87 -> colums     드랍
        tagline                   : null count =  25054 -> null_value 대체
        title                     : null count =      6 -> colums     드랍
        vote_average              : null count =      6 -> 0.0        대체
        vote_count                : null count =      6 -> 0          대체
        '''

        genres_fill_na = drop_df['genres']
        id_fill_na = drop_df['id']
        original_title_fill_na = drop_df['original_title']
        overview_fill_na = drop_df['overview'].fillna('null_value')
        popularity_fill_na = drop_df['popularity'].fillna('null_value')
        release_date_fill_na = drop_df['release_date'].fillna('0000')
        tagline_fill_na = drop_df['tagline'].fillna('null_value')
        title_fill_na = drop_df['title'].fillna('null_value')
        vote_average_fill_na = drop_df['vote_average'].fillna('0.0')
        vote_count_fill_na = drop_df['vote_count'].fillna('0')

        genres_fill_na = pd.Series.to_frame(genres_fill_na, 'genres')
        id_fill_na = pd.Series.to_frame(id_fill_na, 'id')
        original_title_fill_na = pd.Series.to_frame(original_title_fill_na, 'original_title')
        overview_fill_na = pd.Series.to_frame(overview_fill_na, 'overview')
        popularity_fill_na = pd.Series.to_frame(popularity_fill_na, 'popularity')
        release_date_fill_na = pd.Series.to_frame(release_date_fill_na, 'release_date')
        tagline_fill_na = pd.Series.to_frame(tagline_fill_na, 'tagline')
        title_fill_na = pd.Series.to_frame(title_fill_na, 'title')
        vote_average_fill_na = pd.Series.to_frame(vote_average_fill_na, 'vote_average')
        vote_count_fill_na = pd.Series.to_frame(vote_count_fill_na, 'vote_count')
        
        fill_na_df = pd.concat([genres_fill_na, 
                                id_fill_na, 
                                original_title_fill_na,
                                overview_fill_na, 
                                popularity_fill_na, 
                                release_date_fill_na, 
                                tagline_fill_na, 
                                title_fill_na, 
                                vote_average_fill_na, 
                                vote_count_fill_na],
                                axis=1)    
        # fill_na_df = fill_na_df.dropna()
        ##### null 값 대체 #####

        ##### 데이터 축소 #####
        '''
        year : 1995-10-30 -> 1995
        genres : [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
                -> ['Animation', 'Comedy', 'Family']
        '''
        
        fill_na_df['release_date'] = fill_na_df['release_date'].str.slice(stop=4)   # 년도 4자리 따오기
        
        new_genres_list = pd.Series.to_list(fill_na_df['genres'])   # 장르 축소

        mylist = []
        
        for d in range(0, len(new_genres_list)):
            eval_str = ast.literal_eval(new_genres_list[d])
            temp_list = []
            for i in range(0, len(eval_str)):
                temp_list.append(eval_str[i]['name'])
            mylist.append(str(temp_list))
       
        new_genres = pd.DataFrame(mylist, columns=['new_genres'])

        reduction_df = fill_na_df.drop(['genres'], axis=1)
        reduction_df = pd.concat([reduction_df, new_genres], axis=1)

        ##### 데이터 축소 #####

        ##### movie lens와 비교 컬럼 생성 #####
        '''
        title + release_date 
        ex) Gone To Earth/1950
        '''
        sub_title_list = pd.Series.to_list(reduction_df['title'])
        year_list = pd.Series.to_list(reduction_df['release_date'])
        mylist = []
        for d in range(0, len(sub_title_list)):
            compare_data = str(sub_title_list[d]) + '/' + str(year_list[d])
            mylist.append(compare_data)
        compare_column = pd.DataFrame(mylist, columns=['compare_column'])
        compare_df = pd.concat([reduction_df, compare_column], axis=1)
        ##### movie lens와 비교 컬럼 생성 #####

        ##### column 정렬 및 이름 변경 #####
        column_sort_df = compare_df[['id',
                            'title',
                            'original_title',
                            'new_genres',
                            'release_date',
                            'vote_average',
                            'vote_count',
                            'popularity',
                            'overview',
                            'tagline',
                            'compare_column']]

        mycolumns = {
            'id':'movieid',
            'title':'movie_l_title',
            'original_title':'movie_l_org_title',
            'new_genres':'movie_l_genres',
            'release_date':'movie_l_year',
            'vote_average':'movie_l_rating',
            'vote_count':'movie_l_rating_count',
            'popularity':'movie_l_popularity',
            'overview':'movie_l_overview',
            'tagline':'movie_l_tagline',
            'compare_column':'compare_column'
        }

        sort_df = column_sort_df.rename(columns=mycolumns)
        ##### column 정렬 및 이름 변경 #####
        
        ##### id 기준 중복 값 제거 #####
        print('중복 ID 제거 전 : ', sort_df.duplicated(['movieid']).sum())
        drop_duplicates_df = sort_df.drop_duplicates(subset='movieid', keep='first', inplace=False)
        print('중복 ID 제거 후 : ', drop_duplicates_df.duplicated(['movieid']).sum())
        ##### id 기준 중복 값 제거 #####

        final_movie_lens_meta_df = drop_duplicates_df
        return final_movie_lens_meta_df
        print('***** 무비렌즈 메타 데이터 가공 완료 *****')

    def arrange_kmdb_naver_df(self, kmdb_naver_df):
        print('***** kmdb naver 데이터 가공 *****')
        fchecker = self.filechecker

        '''
        [original columns]
        'Unnamed: 0',
        'title',
        'eng_title',
        'org_title',
        'genre',
        'country',
        'year',
        'company',
        'director',
        'actor',
        'date',
        'running_time',
        'keyword',
        'plot',
        'Unnamed: 0.1',
        'title_naver',
        'link_naver',
        'image_naver',
        'subtitle_naver',
        'pubdate_naver',
        'director_naver',
        'actor_naver',
        'userrating_naver',
        'id'
        '''

        ##### 필요없는 column 삭제 #####
        '''
        [drop columns]
        'title',
        'subtitle_naver',
        'genre',
        'pubdate_naver',
        'keyword',
        'running_time',
        'link_naver',
        'image_naver',
        'director_naver',
        'actor_naver'
        '''
        drop_df = kmdb_naver_df.drop(['Unnamed: 0',
                                    'eng_title',
                                    'org_title',
                                    'country',
                                    'year',
                                    'company',
                                    'director',
                                    'actor',
                                    'date',
                                    'plot',
                                    'Unnamed: 0.1',
                                    'title_naver',
                                    'userrating_naver',
                                    'id'], axis=1)
        ##### 필요없는 column 삭제 #####

        ##### null 값 대체 #####
        '''
        title                     : null count =      0
        genre                     : null count =      0
        running_time              : null count =   3818 -> 0 대체
        keyword                   : null count =  22111 -> null_vlaue 대체
        link_naver                : null count =      0
        image_naver               : null count =      0
        subtitle_naver            : null count =   5410 -> null_vlaue 대체
        pubdate_naver             : null count =      0
        director_naver            : null count =    463 -> null_vlaue 대체
        actor_naver               : null count =   4433 -> null_vlaue 대체
        '''
        title_fill_na = drop_df['title']
        genre_fill_na = drop_df['genre']
        running_time_fill_na = drop_df['running_time'].fillna('0')
        keyword_fill_na = drop_df['keyword'].fillna('null_vlaue')
        link_naver_fill_na = drop_df['link_naver']
        image_naver_fill_na = drop_df['image_naver']
        subtitle_naver_fill_na = drop_df['subtitle_naver'].fillna('null_vlaue')
        pubdate_naver_fill_na = drop_df['pubdate_naver']
        director_naver_fill_na = drop_df['director_naver'].fillna('null_vlaue')
        actor_naver_fill_na = drop_df['actor_naver'].fillna('null_vlaue')

        title_fill_na = pd.Series.to_frame(title_fill_na, 'title')
        genre_fill_na = pd.Series.to_frame(genre_fill_na, 'genre')
        running_time_fill_na = pd.Series.to_frame(running_time_fill_na, 'running_time')
        keyword_fill_na = pd.Series.to_frame(keyword_fill_na, 'keyword')
        link_naver_fill_na = pd.Series.to_frame(link_naver_fill_na, 'link_naver')
        image_naver_fill_na = pd.Series.to_frame(image_naver_fill_na, 'image_naver')
        subtitle_naver_fill_na = pd.Series.to_frame(subtitle_naver_fill_na, 'subtitle_naver')
        pubdate_naver_fill_na = pd.Series.to_frame(pubdate_naver_fill_na, 'pubdate_naver')
        director_naver_fill_na = pd.Series.to_frame(director_naver_fill_na, 'director_naver')
        actor_naver_fill_na = pd.Series.to_frame(actor_naver_fill_na, 'actor_naver')
        
        fill_na_df = pd.concat([title_fill_na, 
                                genre_fill_na, 
                                running_time_fill_na,
                                keyword_fill_na, 
                                link_naver_fill_na, 
                                image_naver_fill_na, 
                                subtitle_naver_fill_na, 
                                pubdate_naver_fill_na, 
                                director_naver_fill_na, 
                                actor_naver_fill_na],
                                axis=1)
        ##### null 값 대체 #####

        ##### 데이터 축소 #####
        '''
        subtitle_naver : Iron Man <b>2</b> -> Iron Man 2
        director_naver : 상위 3명만 추출
        actor_naver : 상위 3명만 추출
        '''
        sub_title_list = pd.Series.to_list(fill_na_df['subtitle_naver'])
        mylist1 = []
        for d in range(0, len(sub_title_list)):
            new_eng_title = sub_title_list[d]
            new_eng_title = new_eng_title.replace('<b>','').replace('</b>', '')
            mylist1.append(new_eng_title)
        new_subtitle_naver = pd.DataFrame(mylist1, columns=['new_subtitle_naver'])

        director_list = pd.Series.to_list(fill_na_df['director_naver'])
        mylist2 = []
        for d in range(0, len(director_list)):
            new_director = director_list[d]
            new_director = new_director.replace('<b>','').replace('</b>', '')
            drop_last_r = new_director.rstrip('|')
            split_new_director = drop_last_r.split('|')
            mylist2.append(str(split_new_director[:3]))
        new_director_df = pd.DataFrame(mylist2, columns=['new_director_naver'])
        new_director_df = new_director_df['new_director_naver'].str.replace(pat=r'[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9\,\ ]', repl='', regex=True)

        actor_list = pd.Series.to_list(fill_na_df['actor_naver'])
        mylist3 = []
        for d in range(0, len(actor_list)):
            new_actor = actor_list[d]
            new_actor = new_actor.replace('<b>','').replace('</b>', '')
            drop_last_r = new_actor.rstrip('|')
            split_new_actor = drop_last_r.split('|')
            mylist3.append(str(split_new_actor[:3]))
        new_actor_df = pd.DataFrame(mylist3, columns=['new_actor_naver'])
        new_actor_df = new_actor_df['new_actor_naver'].str.replace(pat=r'[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9\,\ ]', repl='', regex=True)

        reduction_df = fill_na_df.drop(['subtitle_naver', 'director_naver', 'actor_naver'], axis=1)
        reduction_df = pd.concat([reduction_df, new_subtitle_naver, new_director_df, new_actor_df], axis=1)
        ##### 데이터 축소 #####

        ##### movie lens와 비교 컬럼 생성 #####
        '''
        title_naver_eng + year_kor 
        ex) Gone To Earth/1950
        '''
        sub_title_list = pd.Series.to_list(reduction_df['new_subtitle_naver'])
        year_list = pd.Series.to_list(reduction_df['pubdate_naver'])
        mylist = []
        for d in range(0, len(sub_title_list)):
            compare_data = str(sub_title_list[d]) + '/' + str(year_list[d])
            mylist.append(compare_data)
        compare_column = pd.DataFrame(mylist, columns=['compare_column'])
        compare_df = pd.concat([reduction_df, compare_column], axis=1)
        ##### movie lens와 비교 컬럼 생성 #####
        

        #### column 정렬 및 이름 변경 #####
        column_sort_df = compare_df[['title',
                            'new_subtitle_naver',
                            'genre',
                            'keyword',
                            'running_time',
                            'pubdate_naver',
                            'new_director_naver',
                            'new_actor_naver',
                            'link_naver',
                            'image_naver',
                            'compare_column']]

        mycolumns = {
            'title':'title_kor',
            'new_subtitle_naver':'title_naver_eng',
            'genre':'genres_kor',
            'keyword':'keyword_kor',
            'running_time':'running_time_kor',
            'pubdate_naver':'year_kor',
            'new_director_naver':'director_naver_kor',
            'new_actor_naver':'actor_naver_kor',
            'link_naver':'link_naver',
            'image_naver':'image_naver',
            'compare_column':'compare_column'
        }

        sort_df = column_sort_df.rename(columns=mycolumns)
        ##### column 정렬 및 이름 변경 #####

        ##### compare_column 기준 중복 값 제거 #####
        print('중복 ID 제거 전 : ', sort_df.duplicated(['compare_column']).sum())
        drop_duplicates_df = sort_df.drop_duplicates(subset='compare_column', keep='first', inplace=False)
        print('중복 ID 제거 후 : ', drop_duplicates_df.duplicated(['compare_column']).sum())
        ##### compare_column 기준 중복 값 제거 #####

        final_kmdb_naver_df = drop_duplicates_df
        print('***** kmdb naver 데이터 가공 완료 *****')
        return final_kmdb_naver_df

    def merge_movie_lens_kmdb_naver_df(self, arrange_movie_lens_meta_df, arrange_kmdb_naver_df):
        print('***** 무비렌즈 KMDB NAVER MERGE 및 가공 *****')
        fchecker = self.filechecker
        merge_df = pd.merge(arrange_movie_lens_meta_df, arrange_kmdb_naver_df, on='compare_column')
        '''
        movieid                   : null count =      0
        movie_l_title             : null count =      0 -> drop
        movie_l_org_title         : null count =      0 -> drop
        movie_l_genres            : null count =      0 -> drop
        movie_l_year              : null count =      0 -> drop
        movie_l_rating            : null count =      0
        movie_l_rating_count      : null count =      0
        movie_l_popularity        : null count =      0
        movie_l_overview          : null count =      0 -> drop
        movie_l_tagline           : null count =      0 -> drop
        compare_column            : null count =      0 -> drop
        title_kor                 : null count =      0
        title_naver_eng           : null count =      0
        genres_kor                : null count =      0
        keyword_kor               : null count =      0
        running_time_kor          : null count =      0
        year_kor                  : null count =      0
        director_naver_kor        : null count =      0
        actor_naver_kor           : null count =      0
        link_naver                : null count =      0
        image_naver               : null count =      0
        '''
        drop_df = merge_df.drop([
        'movie_l_title', 
        'movie_l_org_title', 
        'movie_l_genres',
        'movie_l_year', 
        'movie_l_overview', 
        'movie_l_tagline',
        'compare_column'], axis=1)

        sort_df = drop_df[['movieid', 
        'title_kor', 
        'title_naver_eng', 
        'genres_kor',
        'keyword_kor', 
        'running_time_kor', 
        'year_kor', 
        'director_naver_kor',
        'actor_naver_kor',
        'movie_l_rating', 
        'movie_l_rating_count',
        'movie_l_popularity', 
        'link_naver', 
        'image_naver']]
        
        mycolumns = {
            'movieid':'mov_id'
        }
        sort_df = sort_df.rename(columns=mycolumns)


        final_merge_df = sort_df
        print('***** 무비렌즈 KMDB NAVER MERGE 및 가공 완료 *****')
        return final_merge_df

# if __name__ == "__main__":
#     service = MovieDfo()
#     service.hook()

    print('***** 무비 렌즈 서비스 완료 *****')

