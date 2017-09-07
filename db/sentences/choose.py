
from datetime import datetime



import bson
import random
import pymongo
from mongoengine import *


from db.config import _MongoengineConnect,_MongoUrl

connect(_MongoengineConnect)

class ChooseSentences(Document):
    '''
    集合： 显示在列表页的内容，句子，平假名，类型（video，song，text）
    '''
    belongsto_ntext = ListField()#,dbref=True

    jp = StringField(required=True)
    cn = StringField()
    # N1~N5;others
    sentence_Nx = StringField()

    words_list = ListField(DictField())
    tags = ListField(StringField(max_length=20))


    add_date = DateTimeField(default=datetime.now, required=True) #datetime.utcnow  datetime.now()

    # todo
    # belongsto_user = ReferenceField((Users), required=True,dbref=True)#,dbref=True

    def __str__(self):
        return self.jp

###############################################################################
# solve func
# c = ChooseSentences()
# c.jp = 'sdad'
# c.save()

class MgChoose:
    def __init__(self):
        self.client = pymongo.MongoClient(_MongoUrl,27017)
        self.db = self.client[_MongoengineConnect]
        # self.coll = self.db['flow']
        self.coll_s = self.db['choose_sentences']

        # self.coll_w = self.db['words']


    def a_sentence(self,sentence_id):
        a_s = self.coll_s.find_one({'_id': bson.objectid.ObjectId(sentence_id)})
        print(a_s)
        def trans_id(data):
            data['_id'] = str(data['_id'])
            data['belongsto_ntext'] = [str(x) for x in data['belongsto_ntext']]
            last = []
            for x in data['words_list']:
                x['word_id'] = str(x['word_id'])
                last.append(x)
            data['words_list'] = last
            return data
        return trans_id(a_s)



# MgChoose().a_sentence('59ae70b9d9f0920e1313ffcf')





