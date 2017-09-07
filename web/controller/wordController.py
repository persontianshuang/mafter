from tool import mymongo
import bson

db_words = mymongo.pymg('mynihongo1','words')
def get_word(word_id):
    if word_id != 'undefined':
        word_id= bson.objectid.ObjectId(word_id)
        q1 = {'_id': word_id}
        finded_word = db_words.find_one(q1)
        if finded_word:
            return finded_word
