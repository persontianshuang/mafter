import bson

import pymongo
from mongoengine import *
from datetime import datetime



from db.config import _MongoengineConnect,_MongoUrl

connect(_MongoengineConnect)


class Flow(Document):

    '''
    流
    '''
    # 公共
    name = StringField()
    num = IntField()
    # 类型: 视频 音频 长文本
    type = StringField()
    tag = ListField(StringField(max_length=20))

    # music video 公用
    img = StringField()
    mp3_url = StringField()
    # video 独占
    mp4_url = StringField()
    srt_from = StringField()
    # music 独占
    wy_song_id = StringField()
    songer = StringField()

class MgFlow:
    def __init__(self):
        self.client = pymongo.MongoClient(_MongoUrl,27017)
        self.db = self.client[_MongoengineConnect]
        self.coll = self.db['flow']
        self.coll_s = self.db['sentences']
        self.coll_w = self.db['words']

    def all_videos(self):
        def id(data):
            data['_id'] = str(data['_id'])
            return data
        # .sort('_id',-1)
        return [id(x) for x in list(self.coll.find({}))]

    def a_video(self,flow_id):
        vs = self.coll.find_one({'_id': bson.objectid.ObjectId(flow_id)},{'_id':0})
        print(vs)
        return vs



    def a_video_sentences(self,flow_id):
        # the_video = self.coll.find_one({'_id': bson.objectid.ObjectId(flow_id)})
        vs = self.coll_s.find({'belongsto_flow': bson.objectid.ObjectId(flow_id)},{'_id':0})
        vs_list = list(vs)
        def trans_id(data):
            data['belongsto_flow'] = str(data['belongsto_flow'])
            last = []
            for x in data['words_list']:
                x['word_id'] = str(x['word_id'])
                last.append(x)
            data['words_list'] = last
            return data
        return [trans_id(x) for x in vs_list]




# m = MgFlow().all_videos()
# print(m)
