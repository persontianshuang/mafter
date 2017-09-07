from tool import mymongo
from tool import baiduTranslate
from tool.toolJp import aboutMecab

from db.words.word import Words
from mongoengine import *

from db.config import _MongoengineConnect

connect(_MongoengineConnect)




db_words = mymongo.pymg('mynihongo1','words')
last_mecab = ['raw','sorted1','sorted2','sorted3','sorted4','the_best_shape','flexible_type','original_shape','read','speak','read_hiragana','speak_hiragana']

for x in db_words.find():
    ww = Words()
    ww.Nx = x['Nx']
    ww.tags = x['tags']
    ww.mecab = x['mecab'][:-1]
    ww.meaning = x['meaning']
    for index,a in enumerate(last_mecab[:-1]):
        exec("ww.{}=x['mecab'][{}]".format(a,index))
    ww.save()
    # x['meaning']
    # print(x['Nx'])
    # try:
    #     if x['_cls']!='Words.ExpandWords' and x['_cls']!='Words.MeetWords':
    #         Words(mecab = x['_cls']).save()
    # except:
    #     pass

