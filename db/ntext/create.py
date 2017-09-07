from datetime import datetime


import bson
import random
import pymongo
from mongoengine import *

from db.subFlow.flow import Flow
from db.sentences.sentence import Sentences,MgSentence
from db.sentences.choose import ChooseSentences,MgChoose

from db.words.word import Words

from db.config import _MongoengineConnect,_MongoUrl

from db.config import _Db

from db.actions import ws

from tool.toolJp import aboutMecab

from bson.objectid import ObjectId

connect(_MongoengineConnect)

class Ntext(Document):
    '''
    填空 选择  句子 索引  空白单词或者假名  4个选项 单词索引  正确的是
    '''

    from_sentence = ReferenceField((Sentences))#,dbref=True
    sentence_text = StringField(min_length=1,max_length=1000)



    # 前端数据
    text_num = StringField(min_length=1,max_length=100000)
    text_value1 = StringField(min_length=1,max_length=1000)
    text_value2 = StringField(min_length=1,max_length=1000)

    sentence_cn = StringField(min_length=1,max_length=1000)  #text_value3

    choose_value1 = StringField(min_length=1,max_length=100)
    choose_value2 = StringField(min_length=1,max_length=100)
    choose_value3 = StringField(min_length=1,max_length=100)
    choose_value4 = StringField(min_length=1,max_length=100)
    right_answer = StringField(min_length=1)  # 1 2 3 4
    nx = StringField(min_length=1,max_length=100)
    #前端数据结束

    choose_value1_ref = ReferenceField((ChooseSentences))
    choose_value2_ref = ReferenceField((ChooseSentences))
    choose_value3_ref = ReferenceField((ChooseSentences))
    choose_value4_ref = ReferenceField((ChooseSentences))



def deal_with_sentence(q,flow):
    s = Sentences()
    s.belongsto_flow = flow
    s.type = 'text'
    s.flow_id = q.text_num
    s.flow_name = flow.name
    s.jp = q['sentence_text']
    s.cn = q['sentence_cn']
    s.save()
    ws.word_sentence(s)
    q.from_sentence = s
    q.save()

# ws.get_word
def deal_with_word(q):
    for x in range(1,5):
        target = 'choose_value'+str(x)
        target_ref = 'choose_value'+str(x)+'_ref'
        s = ChooseSentences()
        print(q['choose_value1'])
        s.jp = q[target]
        s.belongsto_ntext.append(q)
        ws.word_choose_sentence(s)
        q[target_ref] = s
        q.save()

class NewNtext:
    def __init__(self,rep):
        self.rep = rep
        self.rep_keys =  ['choose_value2','text_value2','choose_value4','choose_value3','right_answer','choose_value1','nx','text_value1','text_num']
        self.coll_ntext = _Db['ntext']

    def show_all(self):
        this_ntexts = list(self.coll_ntext.find({},{'_id':1,'text_num':1,'text_value1':1}).sort('_id',-1))
        def str_id(x):
            x['_id']=str(x['_id'])
            # 忘了return
            return x
        after_ntexts = [str_id(xx) for xx in this_ntexts]
        return after_ntexts


    def show_ntext(self,ntext_id):
        this_ntext = self.coll_ntext.find_one({'_id': ObjectId(ntext_id)})
        # print()
        this_ntext_keys = list(this_ntext.keys())
        for x in this_ntext_keys:
            exec("this_ntext[x] = str(this_ntext[x])")

        if this_ntext['text_value2']=="$":
            this_ntext['text_value1'] = this_ntext['text_value1'].replace('$',"<u> ___ </u>")
            "<u> ___ </u>"
        else:
            this_ntext['text_value1'] = this_ntext['text_value1'].replace('$',"<u>{}</u>".format(this_ntext['text_value2']))

        return this_ntext

    def show_ntext_dtails(self,ntext_id):
        # 展现所有分词  ref 展现数据
        this_ntext = self.coll_ntext.find_one({'_id': ObjectId(ntext_id)})
        this_ntext_keys = list(this_ntext.keys())
        for x in this_ntext_keys:
            exec("this_ntext[x] = str(this_ntext[x])")


        if this_ntext['text_value2']=="$":
            this_ntext['text_value1'] = this_ntext['text_value1'].replace('$',"<u> ___ </u>")
            "<u> ___ </u>"
        else:
            this_ntext['text_value1'] = this_ntext['text_value1'].replace('$',"<u>{}</u>".format(this_ntext['text_value2']))

        # 原句
        this_ntext['from_sentence'] = MgSentence().a_sentence(this_ntext['from_sentence'])

        # 选项
        for x in range(1,5):
            target = 'choose_value'+str(x)
            target_ref = 'choose_value'+str(x)+'_ref'
            this_ntext[target_ref] = MgChoose().a_sentence(this_ntext[target_ref])

        return this_ntext

    def save_from_rep(self):
        print(self.rep_keys)
        q = Ntext()
        for x in self.rep_keys:
            base = "q.{attr} = self.rep['{attr}']".format(attr=x)
            exec(base)
            q.sentence_cn = self.rep['text_value3']
        q.save()
        if q.text_value2.strip()=='$':
            the_answer = q['choose_value' + q.right_answer]
            sentence_text = q.text_value1.replace('$',the_answer)
        else:
            sentence_text = q.text_value1.replace('$',q.text_value2)
        q.sentence_text = sentence_text
        q.save()
        self.q = q
        return self.q

    def save_all(self):
        q = self.save_from_rep()
        f = Flow.objects(name = "能力考N3")[0]
        deal_with_sentence(q,f)
        deal_with_word(q)

if __name__=="__main__":
    pass
    # 1.
    # print(NewNtext('d').show_all())
    # 2.
    # for x in Ntext.objects.all():
    #
    #     f = Flow.objects(name = "能力考N3")[0]
    #     # deal_with_sentence(x,f)
    #     deal_with_word(x)
    # for x in _Db['ntext'].find({},{"_id":0}):
    #     x['text_value3'] = x['sentence_cn']
    #     NewNtext(x).save_all()
