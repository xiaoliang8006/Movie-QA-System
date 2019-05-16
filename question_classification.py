#-*- coding: UTF-8 -*-
#对问题进行分类

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import jieba


class Question_classify():
    def __init__(self):
        # 读取训练数据
        self.train_x,self.train_y=self.read_train_data()
        # 训练模型
        self.model=self.train_model_NB()
    # 获取训练数据
    def read_train_data(self):
        train_x=[]
        train_y=[]
        # 读取文件内容
        with(open("./questions/label.txt", "r", encoding="utf-8")) as fr:
            lines = fr.readlines()
            for one_line in lines:
                temp = one_line.split('    ')
                #print(temp)
                word_list=list(jieba.cut(str(temp[1]).strip()))
                # 将这一行加入结果集
                train_x.append(" ".join(word_list))
                train_y.append(temp[0])
        return train_x,train_y

    # 训练并测试模型-NB
    def train_model_NB(self):
        X_train, y_train = self.train_x, self.train_y
        self.tv = TfidfVectorizer()

        train_data = self.tv.fit_transform(X_train).toarray()
        clf = MultinomialNB(alpha=0.01)
        clf.fit(train_data, y_train)
        return clf

    # 预测
    def predict(self,question):
        question=[" ".join(list(jieba.cut(question)))]
        test_data=self.tv.transform(question).toarray()
        y_predict = self.model.predict(test_data)[0]
        print("questions type:",y_predict)
        return int(y_predict)

if __name__ == '__main__':
    qc=Question_classify()
    qc.predict("暗道上映时间")
