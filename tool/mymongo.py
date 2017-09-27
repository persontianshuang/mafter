import pymongo

from bson.objectid import ObjectId

import bson
def pymg(highest,collections):
    client = pymongo.MongoClient('localhost', 27017)
    zhihu = client[highest]
    collections = zhihu[collections]
    return collections


def ssh(highest,collections):
    client = pymongo.MongoClient('123.206.220.149', 27017)
    zhihu = client[highest]
    collections = zhihu[collections]
    return collections

# ssh('mecab','words').insert({'a':1})
# 速度挺快的
def backup_db(olddb,oldcolllection,newdb,newcolllection,find_condition={}):
    sgk_list = list(pymg(olddb,oldcolllection).find(find_condition))
    pymg(newdb,newcolllection).insert_many(sgk_list)

def backup_ssh_db(olddb,oldcolllection,newdb,newcolllection,find_condition={}):
    # [57099:] [58210:] yuanlai
    sgk_list = list(pymg(olddb,oldcolllection).find(find_condition))[58220:]
    print(len(sgk_list))
    ssh(newdb,newcolllection).insert_many(sgk_list)

# 1.
# backup_db('mynihongo1','words_backup_02','mynihongo1','words')
# sentences
# flow
# words
# backup_ssh_db('mynihongo2','sentences','mynihongo2','sentences',find_condition={'flow_name':'半泽直树1'})
# backup_ssh_db('mynihongo2','sentences','mynihongo2','sentences',find_condition={'belongsto_flow':ObjectId("59acce4fd9f092070ff09f6b")})
# backup_ssh_db('mynihongo2','flow','mynihongo2','flow',find_condition={'name':'半泽直树1'})
# backup_ssh_db('mynihongo2','words','mynihongo2','words')
# backup_ssh_db('mynihongo2','ntext','mynihongo2','ntext')
# backup_ssh_db('mynihongo2','choose_sentences','mynihongo2','choose_sentences')
# 2.
# todo
# def search(w):
#     pymg('mecab','words').find({'word_itself.raw': w})

# 3. song
# c= list(pymg('mecab','sentences').find({'song_id':'2'},{'_id':0}))
# def sa():
#     for inex,i in enumerate(c):
#         if inex<len(c)-1:
#             ss={}
#             ss['sentence_jp']=i['sentence_jp']
#             ss['sentence_cn']=i['sentence_cn']
#
#             def dd(wl):
#                 ddwl = {
#                     'word_belongsto_n': 'N2',
#                     'mecab':wl['word_mecab']
#                 }
#                 return ddwl
#             ss['words_list'] = [dd(x) for x in i['words_list']]
#             ss['start']=i['start_song_time']
#             ss['end']=c[inex+1]['start_song_time']
#             yield ss
# print(list(sa()))


# 3. song
# c= list(pymg('mecab','sentences').find({'find_id':'25'},{'_id':0}).limit(29))
# def sa():
#     for inex,i in enumerate(c):
#         # print(i)
#
#         # try:
#         #     s = bson.objectid.ObjectId(i['words_list'][0]['word_db'].id)
#         #     print(s)
#         # except:
#         #     pass
#
#
#         if inex<len(c)-1:
#             ss={}
#             ss['sentence_jp']=i['sentence_jp']
#             ss['sentence_cn']=i['sentence_cn']
#
#             def dd(wl):
#                 ddwl = {
#                     'mecab':wl['word_mecab'],
#                     'meaning':'nil',
#                     'word_belongsto_n':'nil',
#                 }
#
#
#                 if wl['word_db']=='nil':
#                     pass
#                 else:
#                     try:
#                         one = pymg('mecab','words').find_one({'_id': wl['word_db'].id})
#                         if  one['_cls'] == 'Words.Expand':
#                             ddwl['meaning'] = pymg('mecab','words').find_one({'_id': one['expand_by_word'].id})['sgk_meaning']
#                             ddwl['word_belongsto_n'] =  pymg('mecab','words').find_one({'_id': one['expand_by_word'].id})['Nx'],
#                             ddwl['word_belongsto_n'] =  ddwl['word_belongsto_n'][0]
#                         else:
#
#
#                             # one['Nx'] 怎么变成元组了
#                             ddwl['word_belongsto_n'] =  one['Nx'],
#                             ddwl['word_belongsto_n'] = ddwl['word_belongsto_n'][0]
#                             ddwl['meaning'] = one['sgk_meaning']
#                     except:
#                         pass
#
#
#                 return ddwl
#             ss['words_list'] = [dd(x) for x in i['words_list']]
#             ss['start']=i['sss']
#             ss['end']=c[inex+1]['sss']
#             yield ss
# print(list(sa()))
# print(sa())
