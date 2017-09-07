from flask import Blueprint,jsonify

import bson
from tool.domain import allow_cross_domain

from db.sentences.sentence import Sentences,MgSentence
from db.comments import Comments

sentences = Blueprint('sentences',__name__)

# 创建新的句子
@sentences.route('/', methods=['POST'])
@allow_cross_domain
def create():
    s_d = MgSentence().a_sentence(id)
    return jsonify(s_d)

# 获取某个指定的句子
@sentences.route('/<id>', methods=['GET'])
@allow_cross_domain
def sentence_detail(id):
    s_d = MgSentence().a_sentence(id)
    return jsonify(s_d)


# 获取某个指定的视频流的所有句子
@sentences.route('/<index>/video/<id>', methods=['GET'])
@allow_cross_domain
def video_sentence_one(index,id):
    v_s_o = MgSentence().a_video_sentence_one(id,int(index))
    return jsonify(v_s_o)


# 获取随机一个 N级 的句子
@sentences.route('/random/<nx>', methods=['GET'])
@allow_cross_domain
def sentence_random(nx):
    # print(nx.split('&')[:-1]==[])
    s_d = MgSentence().random(Nx=nx.split('&')[:-1])
    # 队列比较好 redis
    return jsonify(s_d)


# 获取某个句子的全部评论
@sentences.route('/<id>/comments', methods=['GET'])
@allow_cross_domain
def sentence_comments(id):
    s_d = MgSentence().a_sentence_comments(id)
    return jsonify(s_d)

# 添加评论
@sentences.route('/<id>/comments/post/<content>', methods=['GET'])
@allow_cross_domain
def new_comments(id,content):
    # print(Sentences.objects(id=id))
    if len(Comments.objects)<=100:
        new_comment = Comments()
        new_comment.belongsto_sentence = bson.objectid.ObjectId(id)
        new_comment.content = content
        new_comment.save()
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'fail'})
# /598b18a9d9f092140fc8f9de/comments/post/nihaoandsad dsa
