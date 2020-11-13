from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
# pip install sklearn
# conda install python-graphviz
import pydotplus  # pip install pydotplus
from IPython.core.display import Image
from IPython.display import display
# pip install Ipython
# conda install -c anaconda ipython
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn import metrics
from six import StringIO 
import os, sys

class ActorAi(object):
    def __init__(self):
        self._n_nodes = None
        # left tree, right tree 따로 Preorder 로 읽음
        self._children_left = None
        self._children_right = None
        self._feature = None
        self._threshold = None

    def train_actors(self, data):
        data.append("1") # state 1, 화면에 보이는 배우들.
        path = os.path.abspath('')
        fname = "\\com_dayoung_api\\cop\\act\\model\\data\\actors2.csv"
        df = pd.read_csv(path + fname)
        df = df.drop('photo_url',1)  # 0 means to drop rows, 1 means drop columns
        df = df.drop('act_id',1) 
        print("bring dfo 완료")
        df = df[df['state'] == 1] # 현재 보이는 배우들만 확인
        # df = df.head()
        # print(df)
        #         age       name       real_name              religion         agency                 spouse    children        debut_year   gender  state
        #     0   50        이병헌      no real name           불교             BH엔터테인먼트          이민정      이준후(아들)    1991         m       1
        #     1   39        전지현      왕지현(王智賢)          no religion      문화창고               최준혁       2남            1997        f        1
        #     2   38        손예진      손언진                  no religion     엠에스팀엔터테인먼트     no spouse   no child       1999        f        1
        #     3   28        안소희      no real name           불교             BH엔터테인먼트          no spouse   no child       2004        f        1 
        #     4   39        강동원      no real name           무신론[1]        YG 엔터테인먼트         no spouse   no child       2003        m        1

        # print(df.columns.values.tolist())
        # ['age', 'name', 'real_name', 'religion', 'agency', 'spouse', 'children','debut_year', 'gender', 'state']

        # 총 9개의 column 이지만 8개의 질문만 하면 됨
        # 처음부터 state 는 1인걸 알고 있음
        # 1st Question: 남자 입니까?
        # 2nd Question: 자녀가 있습니까?
        # 3rd Question: 배우자가 있습니까?
        # 4th Question: 소속사가 관련 ->  
        # 5th Question: 종교 관련 -> 
        # 6th Question: 본명으로 활동 하나요?
        # 7th Question: 나이가 어떻게 됩니까?
        # 8th Question: 데뷔년도가 어떻게 됩니까?
        # x = df['age', 'real_name', 'religion', 'agency', 'spouse', 'children','debut_year', 'gender', 'state']
        # print(x)
        y_train = df.filter(["name"])  # 구할 것 Output
        X_train = df.filter(['age', 'real_name', 'religion', 'agency', 'spouse', 'children','debut_year', 'gender', 'state'])
        # print(y_train)
        # print(X_train)
        y_test = y_train
        # 모르는 것을 예측 하는 것이 아니기 때문에 pred 에 train_set 과 같은 value
        # 예상 100퍼 맞춤
        
        print("-----------------------------------------------------------------------")
        for set_max_depth in range(1,2):
            set_random_state = 0
            set_max_depth = 8
            clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=set_max_depth, random_state=set_random_state)
            clf.fit(X_train,y_train)
            y_pred = clf.predict(X_train)
            # print("Accuracy :", metrics.accuracy_score(y_test, y_pred))
            # print("raondom state: ", set_random_state)
            # print("Max Depth: ", set_max_depth)
        # 28,0,1,1,0,0,2004,0,1
        # print(clf.predict([[28,0,1,1,0,0,2004,0,1]])) # 안소희
        name = clf.predict([data]) # 받은 데이터 값으로 배우를 예측한다
        return name[0]
        # -------------------------여기는 분석 자료 프린트 ------------------------------------
        # dot_data = StringIO()
        # tree.export_graphviz(clf, out_file=dot_data)
        # graph = pydotplus.graph_from_dot_data(dot_data.getvalue()) 
        # Image(graph.write_png("max_depth{}.png".format(set_max_depth)))  # png file 생성

        # ------------------- 더 효율적이게 하기 ----------------
        # Tree에 관해 Node 뿌려주기.
        # print(df[eval(rules[3])])
        # self._n_nodes = clf.tree_.node_count
        # self._children_left = clf.tree_.children_left
        # self._children_right = clf.tree_.children_right
        # self._feature = clf.tree_.feature
        # self._threshold = clf.tree_.threshold

        # X_test = X_train
        # leave_id = clf.apply(X_test)
        # paths ={}
        # for leaf in np.unique(leave_id):
        #     path_leaf = []
        #     self.find_path(0, path_leaf, leaf)
        #     paths[leaf] = np.unique(np.sort(path_leaf))
        # rules = {}
        # for key in paths:
        #     rules[key] = self.get_rule(paths[key], X_train.columns)
        
        # print("n_nodes: ", self._n_nodes)
        # print("children_left: ", self._children_left)
        # print("children_right: ", self._children_right)
        # print("Feature: ", self._feature)
        # print("Threshold: ", self._threshold)
        # 

        
    def find_path(self, node_numb, path, x):
        """
        Recursive functions.
        Find the path from the tree's root to create a specific node
        (all the leaves in our case).
        """
        path.append(node_numb)
        if node_numb == x:
            return True
        left = False
        right = False
        if (self._children_left[node_numb] !=-1):
            left = self.find_path(self._children_left[node_numb], path, x)
        if (self._children_right[node_numb] !=-1):
            right = self.find_path(self._children_right[node_numb], path, x)
        if left or right :
            return True
        path.remove(node_numb)
        return False

    def get_rule(self, path, column_names):
        """
        Write the specific rules used to create a node using its creation path :
        """
        mask = ''
        for index, node in enumerate(path):
            #We check if we are not in the leaf
            if index!=len(path)-1:
                # Do we go under or over the threshold ?
                if (self._children_left[node] == path[index+1]):
                    mask += "(df['{}']<= {}) \t ".format(column_names[self._feature[node]], self._threshold[node])
                else:
                    mask += "(df['{}']> {}) \t ".format(column_names[self._feature[node]], self._threshold[node])
        # We insert the & at the right places
        mask = mask.replace("\t", "&", mask.count("\t") - 1)
        mask = mask.replace("\t", "")
        return mask


if __name__ == "__main__":
    ai = ActorAi()
    ai.train_actors()