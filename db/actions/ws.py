from tool import mymongo
from tool import baiduTranslate
from tool.toolJp import aboutMecab

from db.words.word import Words
from db.sentences.sentence import Sentences

db_words = mymongo.pymg('mynihongo1','words')
last_mecab = ['raw','sorted1','sorted2','sorted3','sorted4','the_best_shape','flexible_type','original_shape','read','speak','read_hiragana','speak_hiragana']

def trans_word(to_trans_word):
    to_trans_word.meaning = baiduTranslate.bd_tanslate(to_trans_word.raw)

def trans_sentence(to_trans_sentence):
    to_trans_sentence.sentence_cn = baiduTranslate.bd_tanslate(to_trans_sentence.sentence_jp)




def get_word(each):
    finded_word = Words.objects(mecab = each)
    # 单词数据库里存在该单词
    if finded_word:
        return finded_word[0]
    # 单词数据库里不存在该单词
    else:
        # 属于派生
        finded_word = Words.objects(original_shape= each[7])
        if  list(finded_word) != []:
            # 假定 raw 这样就算是派生
            ew = Words()
            ew.mecab = each
            ew.type = 'sub'
            ew.tags =[x for x in each[1:-4] if x!='*']
            print('派生')
            try:
                ew.meaning = finded_word[0].meaning
                ew.Nx = finded_word[0].Nx
            except:
                pass
            ew.save()
            return ew
        else:
            print('yours')
            yours = Words()
            yours.type = 'yours'
            yours.raw = each[0]
            yours.mecab = each
            yours.tags =[x for x in each[1:-4] if x!='*']
            yours.Nx = 'Yours'
            try:
                trans_word(yours)
            except:
                pass
            yours.save()
            return yours


def word_sentence(sentence):
    am = aboutMecab.SentenceToMecab(sentence.jp).start()
    for each in am:
        print(each)
        if get_word(each):
            word = get_word(each)
            word.in_sentences.append({
                'sentence_db': sentence,
                'sentence_jp': sentence.jp,
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

    words_list = sentence.words_list
    w = [word['word_Nx'] for word in words_list if word['word_Nx'][0]=='N']
    if w==[]:
        sentence.NX = 'not in Nx'
    else:
        sentence_Nx = sorted(w)[0]
        sentence.NX = sentence_Nx
    sentence.save()


def word_choose_sentence(sentence):
    am = aboutMecab.SentenceToMecab(sentence.jp).start()
    for each in am:
        print(each)
        if get_word(each):
            word = get_word(each)
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
    sentence.save()
    # words_list = sentence.words_list
    # w = [word['word_Nx'] for word in words_list if word['word_Nx'][0]=='N']
    # if w==[]:
    #     sentence.NX = 'not in Nx'
    # else:
    #     sentence_Nx = sorted(w)[0]
    #     sentence.NX = sentence_Nx
    # sentence.save()
