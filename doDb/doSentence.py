from tool import mymongo
from tool import baiduTranslate
from tool.toolJp import aboutMecab
from db.words.expand import ExpandWords
from db.words.meet import MeetWords
from db.words.base import Words
from db.sentences.video import VideoSentences

db_words = mymongo.pymg('mynihongo1','words')

def trans_word(to_trans_word):
    to_trans_word.meaning = baiduTranslate.bd_tanslate(to_trans_word.raw)

def trans_sentence(to_trans_sentence):
    to_trans_sentence.sentence_cn = baiduTranslate.bd_tanslate(to_trans_sentence.sentence_jp)

def get_word(each):
    q1 = {'mecab': each}
    finded_word = db_words.find_one(q1)
    # '单词数据库里不存在该单词'
    if finded_word:
        word_cls =finded_word['_cls'].split('.')[-1]
        # Words.objects(mecab = word_mecab) 只能查找Words类
        old_word = eval(word_cls+'''.objects(mecab = each).first()''')
        return old_word
    else:
        # 属于派生
        finded_word = Words.objects(raw= each[7])
        if  str(finded_word) != str([]):
            # 假定 raw 这样就算是派生
            ew = ExpandWords()
            ew.raw = each[0]
            ew.hiragana = each[-1]
            ew.mecab = each
            ew.tags =[x for x in each[1:-4] if x!='*']
            print(ew.raw)
            try:
                ew.meaning = finded_word[0].meaning
                ew.Nx = finded_word[0].Nx
            except:
                pass
            ew.save()
            return ew
        else:
            mt = MeetWords()
            mt.raw = each[0]
            mt.hiragana = each[-1]
            mt.mecab = each
            mt.tags =[x for x in each[1:-4] if x!='*']
            mt.Nx = 'Yours'
            try:
                trans_word(mt)
            except:
                pass
            mt.save()
            return mt

def word_sentence(sentence):
    am = aboutMecab.SentenceToMecab(sentence.sentence_jp).start()
    for each in am:
        print(each)
        if get_word(each):
            word = get_word(each)
            word.in_sentences.append({
                'sentence_db': sentence,
                'sentence_jp': sentence.sentence_jp,
            })
            word.in_sentences_num = word.in_sentences_num+1
            word.save()
            sentence.words_list.append({
                # 'word_db': word,
                'word_Nx': word.Nx,
                'word_id': word.id,
                'word_mecab': word.mecab,
            })
            sentence.save()

        else:
            sentence.words_list.append({
                # 'word_db': 'nil',
                'word_Nx': 'nil',
                'word_mecab': each,
            })
            sentence.save()

# for x in VideoSentences.objects.all():
#     word_sentence(x)

