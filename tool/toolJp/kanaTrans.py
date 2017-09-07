kana = {
    'あ': 'ア',
    'い': 'イ',
    'う': 'ウ',
    'え': 'エ',
    'お': 'オ',

    'か': 'カ',
    'き': 'キ',
    'く': 'ク',
    'け': 'ケ',
    'こ': 'コ',
    'が': 'ガ',
    'ぎ': 'ギ',
    'ぐ': 'グ',
    'げ': 'ゲ',
    'ご': 'ゴ',

    'さ': 'サ',
    'し': 'シ',
    'す': 'ス',
    'せ': 'セ',
    'そ': 'ソ',
    'ざ': 'ザ',
    'じ': 'ジ',
    'ず': 'ズ',
    'ぜ': 'ゼ',
    'ぞ': 'ゾ',

    'た': 'タ',
    'ち': 'チ',
    'つ': 'ツ',
    'て': 'テ',
    'と': 'ト',
    'だ': 'ダ',
    'ぢ': 'ヂ',
    'づ': 'ヅ',
    'で': 'デ',
    'ど': 'ド',

    'な': 'ナ',
    'に': 'ニ',
    'ぬ': 'ヌ',
    'ね': 'ネ',
    'の': 'ノ',

    'は': 'ハ',
    'ひ': 'ヒ',
    'ふ': 'フ',
    'へ': 'ヘ',
    'ほ': 'ホ',
    'ぱ': 'パ',
    'ぴ': 'ピ',
    'ぷ': 'プ',
    'ぺ': 'ペ',
    'ぽ': 'ポ',
    'ば': 'バ',
    'び': 'ビ',
    'ぶ': 'ブ',
    'べ': 'ベ',
    'ぼ': 'ボ',

    'ら': 'ラ',
    'り': 'リ',
    'る': 'ル',
    'れ': 'レ',
    'ろ': 'ロ',

    'ま': 'マ',
    'み': 'ミ',
    'む': 'ム',
    'め': 'メ',
    'も': 'モ',

    'わ': 'ワ',
    'を': 'ヲ',
    'や': 'ヤ',
    'よ': 'ヨ',
    'ゆ': 'ユ',

    'ん': 'ン',
    'ぁ': 'ァ',
    'ぃ': 'ィ',
    'ぅ': 'ゥ',
    'ぇ': 'ェ',
    'ぉ': 'ォ',
    'ょ': 'ョ',
    'ゃ': 'ャ',
    'ゅ': 'ュ',
    'っ': 'ッ',

    'ー': 'ー',

}


pianjiaming = ['ギ', 'ャ', 'ユ', 'ミ', 'ロ', 'ヂ', 'ヨ', 'セ', 'ベ', 'ヲ', 'ゾ', 'ジ', 'ス', 'ホ', 'シ', 'ュ', 'コ', 'オ', 'ゴ', 'ブ', 'タ', 'ウ', 'ボ', 'リ', 'ョ', 'レ', 'メ', 'ゲ', 'ル', 'ネ', 'ム', 'ッ', 'フ', 'ア', 'ピ', 'グ', 'ク', 'ノ', 'ハ', 'ダ', 'バ', 'パ', 'ナ', 'ペ', 'ラ', 'ワ', 'ヒ', 'テ', 'ヅ', 'ザ', 'ツ', 'ァ', 'ヤ', 'ヌ', 'チ', 'ォ', 'エ', 'ン', 'カ', 'ィ', 'ズ', 'マ', 'ソ', 'モ', 'ケ', 'ビ', 'プ', 'イ', 'サ', 'ガ', 'ェ', 'ゥ', 'ヘ', 'デ', 'キ', 'ゼ', 'ド', 'ト', 'ポ', 'ニ']
invert_kana = {value:key for key,value in kana.items()}

def trans(words):
    trans_words = words
    try:
        try:
            trans_words = ''.join([invert_kana[x] for x in list(words)])
        except:
            trans_words = ''.join([kana[x] for x in list(words)])
    except:
        trans_words = words
    return trans_words
# print(trans('アーク'))
