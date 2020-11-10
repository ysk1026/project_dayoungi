
import os
import pandas as pd
import numpy as np
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
from surprise import Reader, Dataset, SVD, accuracy

from com_dayoung_api.cmm.util.file_helper import FileReader, FileChecker

class MovieAi:
    def __init__(self):
        self.fileReader = FileReader()
        self.filechecker = FileChecker()
        self.path = os.path.abspath("")

        self.md = object
        self.qualified = object
        self.min_vote = int
        self.movie_ave = int
        self.smd = object
        self.indices = object
        self.cosine_sim = object
        self.titles = object
        self.links_small = object
        self.keyword_frequency = object

    # def hook(self):

        # x = qualified
        # qualified['wr'] = qualified.apply(self.weighted_rating, axis=1)
        # qualified = qualified.sort_values('wr', ascending=False).head(250)


    def preprocess(self):
        '''
        adult                     : null count =      0
        belongs_to_collection     : null count =  40972
        budget                    : null count =      0
        genres                    : null count =      0 -> id제거 & 장르만 list화 / 
        homepage                  : null count =  37684
        id                        : null count =      0
        imdb_id                   : null count =     17
        original_language         : null count =     11
        original_title            : null count =      0
        overview                  : null count =    954
        popularity                : null count =      5
        poster_path               : null count =    386
        production_companies      : null count =      3
        production_countries      : null count =      3
        release_date              : null count =     87
        revenue                   : null count =      6
        runtime                   : null count =    263
        spoken_languages          : null count =      6
        status                    : null count =     87
        tagline                   : null count =  25054
        title                     : null count =      6
        video                     : null count =      6
        vote_average              : null count =      6 -> string > ing
        vote_count                : null count =      6 -> string > ing
        year                      : null count =      0 -> 년도만 표기
        '''
        
        
        fchecker = self.filechecker

        path = os.path.abspath('')
        fname = '\data\movies_metadata.csv'
        md = pd.read_csv(path + fname, encoding='utf-8')
        
        md['genres'] = md['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])
        md['year'] = pd.to_datetime(md['release_date'], errors='coerce').apply(lambda x: str(x).split('-')[0] if x != np.nan else np.nan)
        md = md.drop([19730, 29503, 35587])

        vote_counts = md[md['vote_count'].notnull()]['vote_count'].astype('int')
        vote_averages = md[md['vote_average'].notnull()]['vote_average'].astype('int')
        movie_ave = vote_averages.mean()
        
        min_vote = vote_counts.quantile(0.95)

        self.md = md
        self.movie_ave = movie_ave
        self.min_vote = min_vote

        return md

    def create_qualified(self):
        '''
        adult                     : null count =      0 -> drop
        belongs_to_collection     : null count =  40972 -> drop
        budget                    : null count =      0 -> drop
        genres                    : null count =      0
        homepage                  : null count =  37684 -> drop
        id                        : null count =      0 -> drop
        imdb_id                   : null count =     17 -> drop
        original_language         : null count =     11 -> drop
        original_title            : null count =      0 -> drop
        overview                  : null count =    954 -> drop
        popularity                : null count =      5
        poster_path               : null count =    386 -> drop
        production_companies      : null count =      3 -> drop
        production_countries      : null count =      3 -> drop
        release_date              : null count =     87 -> drop
        revenue                   : null count =      6 -> drop
        runtime                   : null count =    263 -> drop
        spoken_languages          : null count =      6 -> drop
        status                    : null count =     87 -> drop
        tagline                   : null count =  25054 -> drop
        title                     : null count =      6
        video                     : null count =      6 -> drop
        vote_average              : null count =      6
        vote_count                : null count =      6
        year                      : null count =      0
        '''
        fchecker = self.filechecker
        md = self.md
        min_vote = self.min_vote

        qualified = md[(md['vote_count'] >= min_vote) & (md['vote_count'].notnull()) & (md['vote_average'].notnull())][['title', 'year', 'vote_count', 'vote_average', 'popularity', 'genres']]
        qualified['vote_count'] = qualified['vote_count'].astype('int')
        qualified['vote_average'] = qualified['vote_average'].astype('int')
        self.qualified = qualified


        print(qualified)
        fchecker.df_null_check(qualified)

        '''
        ['title', 'year', 'vote_count', 'vote_average', 'popularity', 'genres']
        title                     : null count =      0
        year                      : null count =      0
        vote_count                : null count =      0
        vote_average              : null count =      0
        popularity                : null count =      0
        genres                    : null count =      0
        '''

        return qualified

    def weighted_rating(self, x):
        min_vote = self.min_vote
        movie_ave = self.movie_ave

        v = x['vote_count']
        R = x['vote_average']
        return (v/(v+min_vote) * R) + (min_vote/(min_vote+v) * movie_ave)

    def emb_proc(self):
        md = self.md
        emb = md.apply(lambda x: pd.Series(x['genres']), axis=1).stack().reset_index(level=1, drop=True)
        emb.name = 'genre'
        print(emb.head(10))

        gen_md = md.drop('genres', axis=1).join(emb)
        print(gen_md.head(10))


    def create_smd(self):
        md = self.md
        smd = self.smd
        links_small = self.links_small

        path = os.path.abspath('')
        fname = '\data\links_small.csv'
        links_small = pd.read_csv(path + fname, encoding='utf-8')
        links_small = links_small[links_small['tmdbId'].notnull()]['tmdbId'].astype('int')
        
        md['id'] = md['id'].astype('int')
        smd = md[md['id'].isin(links_small)]
        smd.shape
        smd = md[md['id'].isin(links_small)]
        smd['tagline'] = smd['tagline'].fillna('')
        smd['description'] = smd['overview'] + smd['tagline']
        smd['description'] = smd['description'].fillna('')
        self.links_small = links_small
        self.smd = smd

        return smd

    def creat_tfidf_matrix(self):
        smd = self.smd
        indices = self.indices
        cosine_sim = self.cosine_sim
        titles = self.titles

        tf_idf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df=0, stop_words='english')
        tfidf_matrix = tf_idf.fit_transform(smd['description'])
        tfidf_matrix.shape
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        cosine_sim[0]
        print(cosine_sim[0])
        smd = smd.reset_index()
        titles = smd['title']
        indices = pd.Series(smd.index, index=smd['title'])

        self.indices = indices
        self.cosine_sim = cosine_sim
        self.titles = titles


    def create_similarity_degree(self):
        pass

    def get_recommendations_with_tfidf(self):
        pass

    def get_recommendations_with_tfidf(self, title):
        indices = self.indices
        cosine_sim = self.cosine_sim
        titles = self.titles

        idx = indices[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:31]
        movie_indices = [i[0] for i in sim_scores]
        return titles.iloc[movie_indices]

    def create_count_vectorizer_matrix(self):
        smd = self.smd
        indices = self.indices
        cosine_sim = self.cosine_sim
        titles = self.titles
        md = self.md
        links_small = self.links_small
        keyword_frequency = self.keyword_frequency

        path = os.path.abspath('')
        fname = '\data\credits.csv'
        credits = pd.read_csv(path + fname, encoding='utf-8')
        fname = '\data\keywords.csv'
        keywords = pd.read_csv(path + fname, encoding='utf-8')

        credits['crew'][0]

        keywords['id'] = keywords['id'].astype('int')
        credits['id'] = credits['id'].astype('int')

        md['id'] = md['id'].astype('int')

        md.shape

        md = md.merge(credits, on='id')
        md = md.merge(keywords, on='id')

        smd = md[md['id'].isin(links_small)]
        smd.shape

        smd['cast'] = smd['cast'].apply(literal_eval)
        smd['crew'] = smd['crew'].apply(literal_eval)
        smd['keywords'] = smd['keywords'].apply(literal_eval)
        smd['cast_size'] = smd['cast'].apply(lambda x: len(x))
        smd['crew_size'] = smd['crew'].apply(lambda x: len(x))

        smd['director'] = smd['crew'].apply(self.get_director)

        # 출연진 중 상위에 노출되는 3명만 추출
        smd['cast'] = smd['cast'].apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])
        smd['cast'] = smd['cast'].apply(lambda x: x[:3] if len(x) >= 3 else x)

        # 출연진의 이름에서 공백 삭제
        smd['keywords'] = smd['keywords'].apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])

        # 감독의 이름에서 공백 삭제 및 3번 언급
        smd['director'] = smd['director'].astype('str').apply(lambda x: str.lower(x.replace(" ", "")))
        smd['director'] = smd['director'].apply(lambda x: [x, x, x])

        # 키워드 빈도수
        keyword_frequency = smd.apply(lambda x: pd.Series(x['keywords']), axis=1).stack().reset_index(level=1, drop=True)
        keyword_frequency.name = 'keyword'

        keyword_frequency = keyword_frequency.value_counts()
        keyword_frequency[:5]

        # 2번 이상 등장한 키워드만 추출
        keyword_frequency = keyword_frequency[keyword_frequency > 1]

        # 어근 추출을 통해 동일 의미&다른 형태의 단어(dogs&dog, imaging&image 등)를 동일한 단어로 인식
        stemmer = SnowballStemmer('english')

        self.keyword_frequency = keyword_frequency

        # 키워드의 어근을 찾아서 공백 제거 후 세팅
        smd['keywords'] = smd['keywords'].apply(self.filter_keywords)
        smd['keywords'] = smd['keywords'].apply(lambda x: [stemmer.stem(i) for i in x])
        smd['keywords'] = smd['keywords'].apply(lambda x: [str.lower(i.replace(" ", "")) for i in x])

        smd['soup'] = smd['keywords'] + smd['cast'] + smd['director'] + smd['genres']
        smd['soup'] = smd['soup'].apply(lambda x: ' '.join(x))

        count = CountVectorizer(analyzer='word', ngram_range=(1,2), min_df=0, stop_words='english')
        count_matrix = count.fit_transform(smd['soup'])

        cosine_sim = cosine_similarity(count_matrix, count_matrix)
        smd = smd.reset_index()
        titles = smd['title']
        indices = pd.Series(smd.index, index=smd['title'])

        # a = self.get_recommendations_with_tfidf('The Godfather').head(10)
        # b = self.get_recommendations_with_tfidf('Inception').head(10)
        # print(a)
        # print(b)

        self.indices = indices
        self.cosine_sim = cosine_sim
        self.titles = titles        
        self.smd = smd

    def get_recommendations_with_count_vectorizer(self, title):
        indices = self.indices
        cosine_sim = self.cosine_sim
        titles = self.titles

        idx = indices[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:31]
        movie_indices = [i[0] for i in sim_scores]
        return titles.iloc[movie_indices]

    @staticmethod
    def get_director(x):
        for i in x:
            if i['job'] == 'Director':
                return i['name']
        return np.nan

    def filter_keywords(self, x):
        keyword_frequency = self.keyword_frequency
        words = []
        for i in x:
            if i in keyword_frequency:
                words.append(i)
        return words

    def craete_personal_value(self):
        # surprise 라이브러리의 Reader
        reader = Reader()
        path = os.path.abspath('')
        fname = '\data\\ratings_small.csv'
        ratings = pd.read_csv(path + fname, encoding='utf-8')
        data = Dataset.load_from_df(ratings[['userId', 'movieId','rating']], reader)
        trainset = data.build_full_trainset()
        testset = trainset.build_testset()
        svd = SVD()
        svd.fit(trainset)
        predictions = svd.test(testset)
        accuracy.rmse(predictions)
        ratings[ratings['userId'] == 1]
        svd.predict(1, 302, 3)
        print(svd)
        return(svd)

    @staticmethod
    def convert_int(x):
        try:
            return int(x)
        except:
            return np.nan

    def hybrid(self, userId, title):
        indices = self.indices
        cosine_sim = self.cosine_sim
        
        svd = self.craete_personal_value()
        print(svd)
        path = os.path.abspath('')
        fname = '\data\links_small.csv'
        id_map = pd.read_csv(path + fname, encoding='utf-8')[['movieId', 'tmdbId']]
        id_map['tmdbId'] = id_map['tmdbId'].apply(self.convert_int)
        id_map.columns = ['movieId', 'id']
        id_map = id_map.merge(smd[['title', 'id']], on='id').set_index('title')
        indices_map = id_map.set_index('id')

        idx = indices[title]
        tmdbId = id_map.loc[title]['id']
        movie_id = id_map.loc[title]['movieId']
        
        sim_scores = list(enumerate(cosine_sim[int(idx)]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:26]
        movie_indices = [i[0] for i in sim_scores]
        
        movies = smd.iloc[movie_indices][['title','vote_count','vote_average','year','id']]
        movies['est'] = movies['id'].apply(lambda x: svd.predict(userId, indices_map.loc[x]['movieId']).est)
        print(movies['est'])
        movies = movies.sort_values('est', ascending=False)
        return movies.head(10)


if __name__ == "__main__":
    ai = MovieAi()
    print('***** START *****')

    md = ai.preprocess()
    print(f'메타 데이터 전처리 완료 : {md.head()}')

    qualified = ai.create_qualified()
    print(f'별점 상위 5% 데이터 : {qualified.head()}')

    x = qualified
    qualified['wr'] = qualified.apply(ai.weighted_rating, axis=1)
    qualified = qualified.sort_values('wr', ascending=False).head(250)
    print(f' Vote 상위 5% 값 : {qualified.head(15)}')

    emb_proc = ai.emb_proc()
    print(f' 장르 EMBEDING : {emb_proc}')

    smd = ai.create_smd()
    # description = overview + tagline
    print(f' SMALL 메타 데이터 (약1만개) : {qualified.head()}')

    tfidf_matrix = ai.creat_tfidf_matrix()
    # TEST 줄거리(tfidf) 기반 추천
    print(ai.get_recommendations_with_tfidf('The Godfather').head(10)) # 대부1
    '''
    973      The Godfather: Part II
    8387                 The Family
    3509                       Made
    4196         Johnny Dangerously
    29               Shanghai Triad
    5667                       Fury
    2412             American Movie
    
    1582    The Godfather: Part III
    4221                    8 Women
    2159              Summer of Sam
    '''
    print(ai.get_recommendations_with_tfidf('Inception').head(10)) # 인셉션
    '''
    5239                              Cypher
    141                                Crumb
    6398                         Renaissance
    653                            Lone Star
    1703                               House
    4739                    The Pink Panther
    319                                 Cobb
    2828    What Ever Happened to Baby Jane?
    8867                     Pitch Perfect 2
    979          Once Upon a Time in America
    '''
    # TEST 줄거리(tfidf) 기반 추천

    cv_matrix = ai.create_count_vectorizer_matrix()
    # TEST 감독(가중치*3), 배우(가중치*1), 키워드(가중치*1) (CountVectorizer)기반 추천
    print(ai.get_recommendations_with_count_vectorizer('The Godfather').head(10)) # 대부1
    '''
    994            The Godfather: Part II
    3300                 Gardens of Stone
    3616    Tucker: The Man and His Dream
    1346                    The Rainmaker
    1602          The Godfather: Part III
    3705                  The Cotton Club
    4518               One from the Heart
    981                    Apocalypse Now
    2998                 The Conversation
    5867                      Rumble Fish
    '''
    print(ai.get_recommendations_with_count_vectorizer('Inception').head(10)) # 인셉션
    '''
    6623                             The Prestige
    3381                                  Memento
    4145                                 Insomnia
    2085                                Following
    8031                    The Dark Knight Rises
    8613                             Interstellar
    6981                          The Dark Knight
    6218                            Batman Begins
    8207                                   Looper
    5638    Sky Captain and the World of Tomorrow
    '''
    # TEST 감독(가중치*3), 배우(가중치*1), 키워드(가중치*1) (CountVectorizer)기반 추천
    print('구분구분구분')


    print(ai.hybrid(1, 'Avatar'))
    print(ai.hybrid(500, 'Avatar'))

    print('***** END *****')

