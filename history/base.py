from mongoengine import *
from datetime import datetime


from db import config

connect(config._MongoengineConnect)



class Item(EmbeddedDocument):
    '''
   流： 视频流，音乐流  句子的集合
   '''
# belongsto_user = ReferenceField((Users), required=True,dbref=True)#,dbref=True
    meta = {'allow_inheritance': True}
    sentence_jp = StringField(required=True)
    Nx = StringField()
    tags = ListField(StringField(max_length=20))


    def __str__(self):
        return self.sentence_jp


class SubFlow(Document):
    meta = {'allow_inheritance': True}
    name = StringField()
    items = EmbeddedDocumentListField(Item)
    date = DateTimeField(default=datetime.now, required=True) #datetime.utcnow  datetime.now()






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

