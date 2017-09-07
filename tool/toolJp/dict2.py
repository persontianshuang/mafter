import pymongo
def pymg(highest,collections,port='localhost'):
    client = pymongo.MongoClient(port, 27017)
    zhihu = client[highest]
    collections = zhihu[collections]
    return collections

# 1.
# r = pymg('mecab','raw_sgk').find_one({'raw_word.raw':'dadassa'})
# print(r==None)
#
# for w in pymg('base_nihongo','N_num').find({'log': {'$exists': False}}):
#     if w['sentence_jp'] == '':
#         raw = w['sentence_to_hiragana']
#         hiragana = ''
#     else:
#         raw = w['sentence_jp']
#         hiragana = w['sentence_to_hiragana']
#
#     r = pymg('mynihongo1','raw_sgk').find({'raw': raw,'hiragana':hiragana})
#     count = r.count()
#     try:
#         if count==1:
#             print(r[0]['raw'],r[0]['hiragana'])
#         pymg('mynihongo1','raw_sgk').update({'_id':r[0]['_id']},{'$set': {'Nx': w['word_belongsto_n']}})
#         pymg('mynihongo1','raw_sgk').update({'_id':r[0]['_id']},{'$set': {'en_meaning': w['sentence_en']}})
#         pymg('base_nihongo','N_num').update({'_id':w['_id']},{'$set': {'log': '1'}})
#         print('_______________')
#
#         # todo
#         if count >= 2:
#             #     mean = ''' '''
#             #     ex = []
#             for index,x in enumerate(r):
#                 # ex_sentences
#                 # pymg('mynihongo1','raw_sgk').remove({'_id': x['_id']})
#
#                 pymg('mynihongo1','raw_sgk').update({'_id':x[index]['_id']},{'$set': {'Nx': w['word_belongsto_n']}})
#                 pymg('mynihongo1','raw_sgk').update({'_id':x[index]['_id']},{'$set': {'en_meaning': w['sentence_en']}})
#                 pymg('base_nihongo','N_num').update({'_id':w['_id']},{'$set': {'log': '1'}})
#                 #     print(r['raw'],x['hiragana'])
#                 # print(x['meaning']) meaing+meaning
#
#     except:
#         # print(r[0]['raw'],'__________失败')
#
#         pass

# 2.  找出 raw hiragana 都一样的单词  合并成一个字段

# for each in pymg('mynihongo1','raw_sgk').find({'num': {'$exists': False}}):
#     r = pymg('mynihongo1','raw_sgk').find({'raw': each['raw'],'hiragana':each['hiragana']})
#     count = r.count()
#     if count >= 2:
#         for x in r:
#             pymg('mynihongo1','raw_sgk').update({'_id':each['_id']},{'$set': {'num': 'many'}})
#         print(r)
#     else:
#         pymg('mynihongo1','raw_sgk').update({'_id':each['_id']},{'$set': {'num': 'one'}})

# 3 把整合后的单词 缓冲起来
# for each in pymg('mynihongo1','raw_sgk').find({'num': 'many'}):
#     # print(each['raw'])
#     r = pymg('mynihongo1','raw_sgk').find({'raw': each['raw'],'hiragana':each['hiragana']})
#
#     data = {}
#     data['raw'] = each['raw']
#     data['hiragana'] = each['hiragana']
#     meaning = ''' '''
#     ex_sentences = []
#     for index,x in enumerate(r):
#         # pymg('mynihongo1','raw_sgk').remove({'_id': x['_id']})
#         if meaning.strip()!='':
#             meaning = meaning + '\n|||\n' + x['meaning']
#         else:
#             meaning = meaning +  x['meaning']
#         for ex in x['ex_sentences']:
#             if ex!=[]:
#                 ex_sentences.append(ex)
#         try:
#             if x['Nx']!='':
#                 data['Nx'] = each['Nx']
#             data['en_meaning'] = each['en_meaning']
#         except:
#             pass
#     data['meaning'] = meaning
#     data['ex_sentences'] = ex_sentences
#     if pymg('mynihongo1','ls').find({'raw': data['raw'],'hiragana':data['hiragana']}).count()==0:
#         pymg('mynihongo1','ls').insert(data)
    # try:
    #     print(data['Nx'])
    # except:
    #     pass


# 4. 删除raw_sgk里{'num': 'many'}的文档  插入缓冲的文档
# ls1  = list(pymg('mynihongo1','raw_sgk').find({'num': 'many'}))
# pymg('mynihongo1','ls1').insert_many(ls1)

# for each in pymg('mynihongo1','raw_sgk').find({'num': 'many'}):
#     pymg('mynihongo1','raw_sgk').remove({'_id': each['_id']})


# ls  = list(pymg('mynihongo1','ls').find())
# pymg('mynihongo1','raw_sgk').insert_many(ls)

# backup dict_backup_02
# 5. 加入N1中有的，sgk里没有的单词
# todo
