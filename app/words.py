from flask import Blueprint,jsonify

from tool.domain import allow_cross_domain

from db.words.word import Words,MgWord


words = Blueprint('words',__name__)



# 获取某个指定的单词
@words.route('/<id>', methods=['GET'])
@allow_cross_domain
def word_detail(id):
    s_d = MgWord().a_word_meaning(id)
    return jsonify(s_d)

