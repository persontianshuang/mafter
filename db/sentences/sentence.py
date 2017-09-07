
from datetime import datetime


from db.subFlow.flow import Flow
import bson
import random
import pymongo
from mongoengine import *


from db.config import _MongoengineConnect,_MongoUrl

connect(_MongoengineConnect)

class Sentences(Document):
    '''
    集合： 显示在列表页的内容，句子，平假名，类型（video，song，text）
    '''
    belongsto_flow = ReferenceField((Flow))#,dbref=True
    flow_id = IntField(default=0)#,dbref=True
    flow_name = StringField()

    jp = StringField(required=True)
    cn = StringField()
    # N1~N5;others
    sentence_Nx = StringField()

    words_list = ListField(DictField())
    tags = ListField(StringField(max_length=20))

    # (('text','纯文本'),('music','音乐'),('video','视频'))
    type = StringField()
    start_seconds = StringField()
    end_seconds = StringField()

    split_mp3_url = StringField()
    split_mp4_url = StringField()


    # STATUS
    marked = IntField(default=0)
    learned = IntField(default=0)

    add_date = DateTimeField(default=datetime.now, required=True) #datetime.utcnow  datetime.now()

    # todo
    # belongsto_user = ReferenceField((Users), required=True,dbref=True)#,dbref=True

    def __str__(self):
        return self.jp

###############################################################################
# solve func


class MgSentence:
    def __init__(self):
        self.client = pymongo.MongoClient(_MongoUrl,27017)
        self.db = self.client[_MongoengineConnect]
        # self.coll = self.db['flow']
        self.coll_s = self.db['sentences']
        self.coll_comments = self.db['comments']
        # self.coll_w = self.db['words']


    def a_sentence(self,sentence_id):
        a_s = self.coll_s.find_one({'_id': bson.objectid.ObjectId(sentence_id)})

        def trans_id(data):
            data['_id'] = str(data['_id'])
            data['belongsto_flow'] = str(data['belongsto_flow'])
            last = []
            for x in data['words_list']:
                x['word_id'] = str(x['word_id'])
                last.append(x)
            data['words_list'] = last
            return data
        return trans_id(a_s)


    def a_video_sentence_one(self,flow_id,sentense_index):
        print(flow_id,sentense_index)
        this_sentense = Sentences.objects(belongsto_flow=flow_id,flow_id=sentense_index).first()
        print(this_sentense.id)
        return {'sentence_id': str(this_sentense.id)}

    def a_sentence_comments(self,sentence_id):
        a_s_c = self.coll_comments.find\
            ({'belongsto_sentence': bson.objectid.ObjectId(sentence_id)},{'_id':0}).sort('add_date',-1)
        # .sort({'add_date':-1})
        print(a_s_c)
        return [x['content'] for x in list(a_s_c)]



    def random(self,Nx=None):
        if Nx:
            r_s_all = list(self.coll_s.find({'sentence_Nx':{'$in':Nx}}))
            # print(len(r_s_all))
            r_num = random.choice(range(len(r_s_all)))
            # print(r_s_all[r_num])
            r_s = r_s_all[r_num]['_id']

        else:
            # print('all')
            r_s_all = list(self.coll_s.find({}))
            r_num = random.choice(range(len(r_s_all)))
            # print(r_s_all[r_num])
            r_s = r_s_all[r_num]['_id']

        return self.a_sentence(r_s)

