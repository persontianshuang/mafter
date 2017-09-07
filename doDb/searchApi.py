from tool import mymongo
from tool import baiduTranslate
from tool.toolJp import aboutMecab
from db.words.expand import ExpandWords
from db.words.meet import MeetWords
from db.words.base import Words
from db.sentences.video import VideoSentences

db_words = mymongo.pymg('mynihongo1','words')
def get_word(each):
    q1 = {'mecab': each[7]}
    finded_word = db_words.find_one(q1)
    # '单词数据库里不存在该单词'
    if finded_word:
        return finded_word
    else:
        mt = {}
        mt['raw'] = each[0]
        mt['hiragana'] = each[-1]
        mt['mecab'] = each
        mt['tags'] =[x for x in each[1:-4] if x!='*']
        mt['Nx'] = 'Yours'
        try:
            mt.meaning = baiduTranslate.bd_tanslate(mt['raw'])
        except:
            pass
        return mt


# get_word
def sentence_search(sentence):
    am = aboutMecab.SentenceToMecab(sentence).start()
    for each in am:
        if get_word(each):
            word = get_word(each)
            yield word

def get_data(sentence):
    words_list = list(sentence_search(sentence))
    sentence_cn = baiduTranslate.bd_tanslate(sentence)
    try:
        data = {
            'sentence_jp': sentence,
            'sentence_cn': sentence_cn,
            'words_list': [{'mecab':y['mecab'],'id':str(y['_id']),'word_belongsto_n':y['Nx']} for y in words_list],
        }
    except:
        data = {
            'sentence_jp': sentence,
            'sentence_cn': sentence_cn,
            'words_list': [{'mecab':y['mecab'],'word_belongsto_n':y['Nx']} for y in words_list],
        }

    return data

# raw_s = 'それはもう十七年も前のことで、僕たちは小学校の六年生になったばかりだった。学校からの帰り道で、ランドセルを背負った僕たちは小さな雑木林の脇を歩いていた。季節は春で、雑木林には満開の桜が数えきれないくらい並んでいて、大気には無数の桜の花びらが音もなく舞っていて、足元のアスファルトは花びらに覆われていちめんまっ白に染まっていた。空気はあたたかで、空はまるで青の絵の具をたっぷりの水に溶かしたように淡く澄んでいた。すぐ近くに大きな幹線道路と小お田だ急きゆう線のレールが走っていたはずだけれど、その喧けん騒そうも僕たちのいる場所まではほとんど届かず、あたりは春を祝福するような鳥のさえずりで満ちていた。まわりには僕たちの他に誰もいなかった。'
#
# search_detail = [get_data(x) for x in raw_s.split('。') if x.strip()!='']
# print(search_detail)



