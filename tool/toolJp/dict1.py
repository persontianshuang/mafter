# sgk 辞典元数据
import re
import pymongo
def pymg(highest,collections,port='localhost'):
    client = pymongo.MongoClient(port, 27017)
    zhihu = client[highest]
    collections = zhihu[collections]
    return collections

class Sgk():
    def __init__(self,sgk_dict):
        self.sgk_dict = sgk_dict

    def raw_to_dict(self):
        words = self.sgk_dict.split('* * *')
        for each_word in  words:
            final_word = {}
            subed_word = re.sub(r"(\n)+", '\n', each_word)
            if subed_word.strip() != '':
                not_null_word = [x.strip() for x in subed_word.split('\n') if x.strip()!='']
                # print(not_null_word[0])
                final_word['raw'] = self.to_raw_word(not_null_word[0])['raw']
                final_word['hiragana'] = self.to_raw_word(not_null_word[0])['hiragana']
                final_word['import'] = self.to_raw_word(not_null_word[0])['import']

                ex_sentences = []
                meaning = ''
                for items in not_null_word[1:]:

                    if '（例）' in items:
                        ex_sentence = self.to_ex_sentences(final_word['raw'],items)
                        ex_sentences.append(ex_sentence)
                    else:
                        meaning = meaning+'\n'+items
                    final_word['ex_sentences'] = ex_sentences
                    final_word['meaning'] = meaning
                yield final_word


    def to_raw_word(self,raw_data):
        # raw_data.split('【')   ＊へや【部屋】
        splited = raw_data.split('【')
        raw_word = {}

        new_splited0 = re.sub(r'＊','',splited[0])
        # 'あいあいがさ【相合傘】'  ->  ['あいあいがさ', '相合傘】']
        # たえぬく【堪え抜く・耐え抜く】的情况没考虑
        if len(splited)==2 and '】' in splited[1]:
            raw_word = {
                'raw': splited[1][:-1],
                'hiragana': new_splited0
            }
        # 'アイアン'  ->  ['アイアン']
        elif len(splited)==1:
            raw_word = {
                'raw': new_splited0,
                'hiragana': ''
            }

        if splited[0][0]=='＊':
            # 重要
            raw_word['import'] = 1
        else:
            raw_word['import'] = 0
        print(raw_data)
        return raw_word

    def to_ex_sentences(self,word,ex_sentence):
        full_ex_sentence = re.sub(r'～',word,ex_sentence)
        ful_ex_sentence_list = re.sub(r'（例）','',full_ex_sentence).split('／')
        return ful_ex_sentence_list



with open('/Users/user/language/jp/raw1.txt','rt',encoding='utf_8') as text:
    sgk_list = list(Sgk(text.read()).raw_to_dict())
    # print(sgk_list)
    pymg('mynihongo1','raw_sgk').insert_many(sgk_list)


    # cc = re.sub(r'┏','',str(text.read()))
    # file = open('/Users/user/language/jp/raw1.txt','w',encoding='utf_8')
    # file.write(cc)
    # file.close()

for x in pymg('mynihongo1','raw_sgk').find({"raw":{'$regex' : ".+\・.+"}}):
    # print(x['raw'])
    word = x['raw'].split('・')
    kana = ['ヅ', 'ン', 'ハ', 'パ', 'メ', 'ゾ', 'ア', 'プ', 'ワ', 'ス', 'セ', 'ポ', 'ヲ', 'フ', 'ミ', 'ザ', 'エ', 'ィ', 'ェ', 'ナ', 'ロ', 'ベ', 'ジ', 'タ', 'ウ', 'ュ', 'ル', 'ツ', 'モ', 'ヒ', 'ァ', 'ボ', 'ド', 'ゼ', 'ブ', 'ビ', 'ニ', 'ペ', 'ゥ', 'ッ', 'テ', 'ガ', 'ネ', 'ォ', 'シ', 'ヌ', 'サ', 'レ', 'ヂ', 'ノ', 'キ', 'ゲ', 'オ', 'ソ', 'ホ', 'カ', 'ユ', 'ク', 'ト', 'イ', 'ョ', 'マ', 'ダ', 'ケ', 'チ', 'ズ', 'ヨ', 'コ', 'ピ', 'ヘ', 'ゴ', 'ラ', 'リ', 'ヤ', 'ャ', 'グ', 'デ', 'バ', 'ギ', 'ム']
    for w in word:
        if w[0] not in kana and w[-1] not in kana:
            print(w)
            data = {
                'meaning':  x['meaning'],
                'raw':  w,
                'hiragana':  x['hiragana'],
                'ex_sentences':  x['ex_sentences'],
                'import':  x['import']
            }
            pymg('mynihongo1','raw_sgk').insert(data)
            pymg('mynihongo1','raw_sgk').remove({'_id': x['_id']})
        else:
            # print(x['raw'])
            pass
