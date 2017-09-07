from tool import mymongo
from tool import baiduTranslate
from tool.toolJp import aboutMecab
from db.words.expand import ExpandWords
from db.words.meet import MeetWords
from db.words.base import Words
from db.sentences.video import VideoSentences

db_words = mymongo.pymg('mynihongo1','words')
def get_word(each):
    q1 = {'mecab': each}
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
    data = {}
    data['sentence_jp'] = sentence
    data['sentence_cn'] = sentence_cn
    new_words_list = []
    for y in words_list:
        single_word = {}
        single_word['mecab'] = y['mecab']
        single_word['word_belongsto_n'] = y['Nx']
        try:
            single_word['id'] = str(y['_id'])
        except:
            pass
        new_words_list.append(single_word)
    data['words_list'] = new_words_list

    return data

# raw_s = 'それはもう十七年も前のことで、僕たちは小学校の六年生になったばかりだった。'
#
# search_detail = [get_data(x) for x in raw_s.split('。') if x.strip()!='']


def search_api(sentence):
    if len(sentence)<=1500:
        search_detail = [get_data(x) for x in sentence.split('。') if x.strip()!='']
        return search_detail
    else:
        return 'sorry'
