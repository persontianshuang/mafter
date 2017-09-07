from datetime import datetime
import bson

from mongoengine import *
import pymongo
from bson.objectid import ObjectId
from bson.dbref import DBRef

from db.config import _MongoengineConnect,_MongoUrl

connect(_MongoengineConnect)

class Words(Document):
    '''
    sgk and n级 原生词汇 共47250左右
    '''
    # 1.
    # raw 原生; sub 派生; yours 自定义
    type = StringField()
    Nx = StringField(default='',max_length=30)
    meaning = StringField(default='')   #可修改

    # mecab  复合主键 数组
    mecab = ListField()
    # tags = ListField(StringField(max_length=20))
    # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
    # 表層形
    raw = StringField()
    # 品詞
    sorted1 = StringField()
    sorted2 = StringField()
    sorted3 = StringField()
    sorted4 = StringField()
    # 活用形
    the_best_shape = StringField()
    # 活用型
    flexible_type = StringField()
    # 原形
    original_shape = StringField()
    # 読み-片假名
    read = StringField()
    # 発音-片假名
    speak = StringField()
    # mecab 结束____________________________________

    # 読み-平假名
    read_hiragana = StringField()
    # 発音-平假名
    speak_hiragana = StringField()

    # 句子相关
    in_sentences = ListField(DictField())
    in_sentences_num = IntField(default=0)
    # 能力考选项
    in_choose = ListField(DictField())
    in_choose_num = IntField(default=0)

    # STATUS
    marked = IntField(default=0)
    learned = IntField(default=0)
    # 创建时间
    add_date = DateTimeField(default=datetime.now(), required=True)
    # todo
    # en_meaning = StringField(default='',max_length=1000)
    # en_cn_meaning = StringField(max_length=1000)

    # meta = {'allow_inheritance': True}
    # belongsto_user = ReferenceField((Users), required=True,dbref=True)#,dbref=True
# Words().save()


class MgWord:
    def __init__(self):
        self.client = pymongo.MongoClient(_MongoUrl,27017)
        self.db = self.client[_MongoengineConnect]
        # self.coll = self.db['flow']
        self.coll_s = self.db['sentences']
        self.coll_w = self.db['words']


    def a_word_meaning(self,word_id):
        word = self.coll_w.find_one({'_id':ObjectId(word_id)})
        data = {
            'tag': '/'.join([x for x in word['mecab'][1:7] if x!='*']),
            'meaning': word['meaning'],
            'Nx': word['Nx'],
            'raw_word': word['mecab'][7],
            'speak': word['mecab'][-1],
            'this_word': word['mecab'][0],
            # 'sentences': [x['sentence_jp'] for x in word['in_sentences']],
            'sentences': [
                {'id': str(x['sentence_db']['_ref'].id),'content': x['sentence_jp']}
                for x in word['in_sentences']],
        }

        # print(data)
        # a_w = self.coll_w.find_one({'_id': bson.objectid.ObjectId(word_id)},{'_id':0})
        # print(a_w)
        return data

# MgWord().a_word("59833989d9f09209e7ef6981")
