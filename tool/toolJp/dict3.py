from tool.toolJp import aboutMecab
from tool import mymongo
from tool.toolJp import kanaTrans
import re


# 1. 平假名转片假名
# for each in mymongo.pymg('mynihongo1','raw_sgk').find():
#     if each['raw'][0] in kanaTrans.pianjiaming and each['raw'][-1] in kanaTrans.pianjiaming:
#         print(each['raw'])
#         read = re.sub(r"・", '', each['raw'])
#         # each['hiragana'] = kanaTrans.trans(read)  不对
#         mymongo.pymg('mynihongo1','raw_sgk').update({'_id': each['_id']},{'$set': {'hiragana':kanaTrans.trans(read)}})
#

# 2. mecab backup dict_backup_03
for each in mymongo.pymg('mynihongo1','raw_sgk').find({'can_mecab':{'$exists':False}}):
    word = aboutMecab.SentenceToMecab(each['raw']).start()
    if len(word) == 1 and word[0][-1]==each['hiragana']:
        if len(word[0])==11:
            mymongo.pymg('mynihongo1','raw_sgk').update({'_id': each['_id']},{'$set': {'mecab': word[0]}})
            mymongo.pymg('mynihongo1','raw_sgk').update({'_id': each['_id']},{'$set': {'can_mecab': 1}})
            print(word)
            print(word[0][-1])
            print(each['hiragana'])
            print('_______')
    else:
        mymongo.pymg('mynihongo1','raw_sgk').update({'_id': each['_id']},{'$set': {'can_mecab': 0}})
