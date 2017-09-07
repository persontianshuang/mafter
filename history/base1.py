from mongoengine import *
from datetime import datetime


from db import config

connect(config._MongoengineConnect)


class Sentences(Document):
    '''
    集合： 显示在列表页的内容，句子，平假名，类型（video，song，text）
    '''
    meta = {'allow_inheritance': True}
    # belongsto_user = ReferenceField((Users), required=True,dbref=True)#,dbref=True

    sentence_jp = StringField(required=True)  # sentence_to_hiragana = StringField()  #mecab分词来说不需要  goo 的api需要
    sentence_cn = StringField()
    sentence_Nx = StringField()

    words_list = ListField(DictField())
    tags = ListField(StringField(max_length=20))
    # STATUS
    marked = IntField(default=0)
    learned = IntField(default=0)



    date = DateTimeField(default=datetime.now, required=True) #datetime.utcnow  datetime.now()
    def __str__(self):
        return self.sentence_jp

# s = Sentences(sentence_jp = 'dsads')
# s.save()
# print(s)
###############################################################################
# solve func


class Solve():
    def __init__(self,sentence):
        self.sentence = sentence

    def delete(self):
        # 删除Sentences里的句子文档
        self.sentence.delete()

    def update(self,db_word):
        # 更新句子文档
        self.sentence.words_list.append({
            'word_db': db_word,
            'word_mecab': db_word.mecab,
        })
        self.sentence.save()

